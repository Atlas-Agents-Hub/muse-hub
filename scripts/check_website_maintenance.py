"""Read-only byte verification of the published website against its deployment commit."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import subprocess
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://atlas-agents-hub.github.io/muse-hub/"
PREFIX = "hub/site/"
REQUIRED = frozenset({
    "index.html", "downloads.html", "downloads.json", "public/catalog.json",
    "sitemap.xml", "llms.txt",
})


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(root), *args], timeout=60
    )


def fetch_live(name: str, limit: int) -> bytes:
    request = Request(
        BASE_URL + quote(name, safe="/"),
        headers={"Cache-Control": "no-cache", "User-Agent": "MuseHub-maintenance/1"},
    )
    with urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise OSError("Unexpected HTTP status")
        return response.read(limit)


def verify_site(root: Path, commit: str, fetch=fetch_live) -> tuple[int, list[str]]:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Full deployment commit identity required")
    paths = [
        path.decode("utf-8").removeprefix(PREFIX)
        for path in git(root, "ls-tree", "-r", "--name-only", "-z", commit, "--", "hub/site").split(b"\0")
        if path
    ]
    if not REQUIRED.issubset(paths):
        raise ValueError("Deployment commit is missing required website files")

    def compare(name: str) -> str | None:
        expected = git(root, "show", commit + ":" + PREFIX + name)
        try:
            actual = fetch(name, len(expected) + 1)
        except OSError as exc:
            return f"{name}: {type(exc).__name__}"
        return None if actual == expected else f"{name}: bytes differ"

    with ThreadPoolExecutor(max_workers=4) as pool:
        failures = [result for result in pool.map(compare, paths) if result]
    return len(paths), failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deployment-commit", required=True)
    args = parser.parse_args()
    try:
        count, failures = verify_site(ROOT, args.deployment_commit)
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(f"Website verification refused: {type(exc).__name__}: {exc}")
        return 1
    print(f"Deployment {args.deployment_commit}: {count - len(failures)}/{count} exact website files.")
    for failure in failures:
        print(failure)
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
