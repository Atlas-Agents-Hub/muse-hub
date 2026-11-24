"""Permit website-only updates against an independently verified package release."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"[0-9a-f]{40}\Z")
# Source changes outside this reviewed web surface require a new package release.
WEB_FILES = frozenset({
    "PUBLIC_SOURCE_MANIFEST.json",
    "docs/design/WEB_VISUAL_CONTRACT.md",
    "scripts/render_downloads.py",
    "scripts/check_website_release_scope.py",
    ".github/workflows/pages.yml",
    ".github/workflows/website-maintenance.yml",
    "docs/WEBSITE_MAINTENANCE.md",
    "scripts/check_website_maintenance.py",
    "tests/test_website_maintenance.py",
    "tests/hub_experience_browser.cjs",
    "tests/test_hub_authentic_showcase.py",
    "tests/test_hub_experience_home.py",
    "tests/test_hub_home_product_journey.py",
    "tests/test_hub_site_public_scope.py",
    "tests/test_hub_sitewide_experience.py",
    "tests/test_muse_hub_brand_launch.py",
    "tests/test_public_release_site.py",
    "tests/test_r18_curated_copy_and_setup.py",
    "tests/test_r19_curated_subject_starts.py",
    "tests/test_r20_english_discovery.py",
    "tests/test_website_release_scope.py",
})
EXPORT = "src/muse_presets/public_export.py"
EXPORT_ADDITIONS = (
    b'    "hub/site/experience.css",\n',
    b'    "hub/site/llms.txt",\n',
)
DISPLAY_FIELDS = frozenset({"title", "description", "category", "keywords", "guide_url"})


def git(root: Path, *args: str) -> bytes:
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, timeout=120)
    if result.returncode:
        raise ValueError("Git verification failed: " + " ".join(args[:2]))
    return result.stdout


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def projection(directory: dict) -> dict:
    result = {key: value for key, value in directory.items() if key not in ("items", "bundles")}
    for group in ("items", "bundles"):
        rows = {}
        for row in directory[group]:
            key = (row.get("kind", "bundle"), row["id"])
            if key in rows:
                raise ValueError("Duplicate directory identity: " + str(key))
            rows[key] = {k: v for k, v in row.items() if k not in DISPLAY_FIELDS}
        result[group] = rows
    return result


def check_scope(root: Path, release_head: str, website_head: str) -> int:
    if not SHA.fullmatch(release_head) or not SHA.fullmatch(website_head):
        raise ValueError("Full commit identities required.")
    if git(root, "rev-parse", "HEAD").decode().strip() != website_head:
        raise ValueError("Website checkout differs from expected commit.")
    if git(root, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("Dirty website checkout.")
    git(root, "merge-base", "--is-ancestor", release_head, website_head)
    changes = git(root, "diff", "--raw", "-z", "--no-renames", release_head, website_head).split(b"\0")
    if changes[-1] != b"" or (len(changes)-1) % 2:
        raise ValueError("Unexpected Git diff format.")
    for meta, path_raw in zip(changes[0:-1:2], changes[1:-1:2]):
        name = path_raw.decode("utf-8")
        old_mode, new_mode = meta[1:].split()[:2]
        if not {old_mode, new_mode} <= {b"100644", b"100755", b"000000"}:
            raise ValueError("Non-regular file in website change: " + name)
        if name == EXPORT:
            before = git(root, "show", release_head + ":" + name)
            after = git(root, "show", website_head + ":" + name)
            # Only the two reviewed static-asset inventory additions are authorized.
            for line in EXPORT_ADDITIONS:
                if line not in before:
                    if after.count(line) > 1:
                        raise ValueError("Duplicate export entry.")
                    after = after.replace(line, b"", 1)
            if after != before:
                raise ValueError("Public export implementation changed.")
        elif name not in WEB_FILES and not name.startswith("hub/site/"):
            raise ValueError("Non-website source changed: " + name)
    name = "hub/site/downloads.json"
    original = json.loads(git(root, "show", release_head + ":" + name), object_pairs_hook=unique)
    candidate = json.loads(git(root, "show", website_head + ":" + name), object_pairs_hook=unique)
    if projection(original) != projection(candidate):
        raise ValueError("Package identity, destination, entry or other non-display metadata changed.")
    return len(changes[:-1]) // 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-head", required=True)
    parser.add_argument("--website-head", required=True)
    args = parser.parse_args()
    try:
        count = check_scope(ROOT, args.release_head, args.website_head)
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print("Website compatibility refused:", exc)
        return 1
    print(f"Verified website scope ({count} changed paths); website {args.website_head}, packages {args.release_head}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
