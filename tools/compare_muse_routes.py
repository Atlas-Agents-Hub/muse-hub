#!/usr/bin/env python3
"""Offline comparison of pinned Muse CLI method projections; never contacts Muse.

Only eight methods carry detailed HTTP/path records; the rest are
name-only observations, not an inventory of callable provider permissions.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/discovery/route-compat"
OLD = DATA / "old-258.json"
NEW = DATA / "new-402.json"
PINS = {
    "old": {
        "sha256": "c800ba8833e0dff6cb3da868b1f9f3404f2a2e36bea42f8c359f634d084633cd",
        "bytes": 23500,
        "commit": "dbc7624368fd3aec20258c545f50654dbc92cc5f",
        "git_blob_sha1": "bfdb6b492290c1dd8827087f2f49ab8046f56664",
    },
    "new": {
        "sha256": "4eaf51c921920665b7e512a3c3a9b486aabe7b9f95630961b989cecaa4b1a336",
        "bytes": 36999,
        "commit": "b62adbabb77abf688d26a74f93d405b6667dbc9f",
        "git_blob_sha1": "6634f1b09d7e98b235bd24bdf3397391689cf981",
    },
}
SOURCE_REPO = "nikships/muse-cli"
SOURCE_PATH = "src/muse_cli/routes.json"
METHOD = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*\Z")
PLACEHOLDER = re.compile(r"\{[A-Za-z_][A-Za-z0-9_]*\}")
FIELDS = frozenset({
    "method", "projection", "http", "path", "aliases", "service",
    "streamMode", "noiseOnly", "requestTimeoutMs",
})
HTTP = frozenset({"GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"})
MAX_BYTES = 2_000_000
PROJECTION = "NAME_ONLY_NOT_FULL_ROUTE"


def _pairs_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _nonempty(value: object) -> bool:
    return (
        isinstance(value, str) and bool(value) and len(value) <= 2048
        and value == value.strip() and not any(ord(ch) < 32 for ch in value)
    )


def _validate_aliases(value: object, method: str) -> None:
    # The historical source uses a serialized JSON array for some aliases.
    # Validate its contents without normalizing the source-level diff away.
    if isinstance(value, str):
        try:
            value = json.loads(value, object_pairs_hook=_pairs_no_duplicates)
        except (ValueError, TypeError) as exc:
            raise ValueError(f"{method}: invalid serialized aliases") from exc
    if not isinstance(value, list) or not all(_nonempty(alias) for alias in value):
        raise ValueError(f"{method}: aliases must be nonempty strings")
    if len(value) > 32 or len(set(value)) != len(value):
        raise ValueError(f"{method}: repeated or excessive aliases")
    for alias in value:
        if alias.startswith("/"):
            if (
                alias.startswith("//") or "?" in alias or "#" in alias
                or "%" in alias or "\\" in alias
                or any(segment in (".", "..") for segment in alias.split("/"))
            ):
                raise ValueError(f"{method}: unsafe route alias")
        elif METHOD.fullmatch(alias) is None:
            raise ValueError(f"{method}: unsafe method alias")


def _validate_row(row: object, index: int) -> dict:
    if not isinstance(row, dict):
        raise ValueError(f"route {index}: not a JSON object")
    method = row.get("method")
    if not isinstance(method, str) or METHOD.fullmatch(method) is None:
        raise ValueError(f"route {index}: invalid method")
    extra = set(row) - FIELDS
    if extra:
        raise ValueError(f"{method}: unsupported fields {sorted(extra)}")
    if "projection" in row:
        if set(row) != {"method", "projection"} or row["projection"] != PROJECTION:
            raise ValueError(f"{method}: invalid name-only projection")
        return row
    if row.get("http") not in HTTP or not _nonempty(row.get("path")):
        raise ValueError(f"{method}: full route must provide HTTP verb and relative path")
    path = row["path"]
    route_path = path.split("?", 1)[0]
    if (
        not path.startswith("/") or path.startswith("//")
        or "\\" in path or "#" in path or "://" in path
        or "%" in route_path
        or any(segment in (".", "..") for segment in route_path.split("/"))
        or any("{" in s or "}" in s for s in PLACEHOLDER.sub("", path).split("/"))
    ):
        raise ValueError(f"{method}: unsafe relative route")
    if "aliases" in row:
        _validate_aliases(row["aliases"], method)
    for field in ("service", "streamMode"):
        if field in row and not _nonempty(row[field]):
            raise ValueError(f"{method}: invalid {field}")
    if "noiseOnly" in row and type(row["noiseOnly"]) is not bool:
        raise ValueError(f"{method}: invalid noiseOnly")
    if "requestTimeoutMs" in row and (
        type(row["requestTimeoutMs"]) is not int
        or not 0 < row["requestTimeoutMs"] <= 3_600_000
    ):
        raise ValueError(f"{method}: invalid requestTimeoutMs")
    return row


def load_routes(path: Path) -> dict[str, dict]:
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError("UNSAFE_OR_MISSING_INPUT")
    if path.stat().st_size > MAX_BYTES:
        raise ValueError("PROJECTION_TOO_LARGE")
    try:
        data = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs_no_duplicates,
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("INVALID_UTF8_JSON") from exc
    if not isinstance(data, list) or len(data) > 5000:
        raise ValueError("INVALID_ROUTE_TABLE")
    routes: dict[str, dict] = {}
    for i, item in enumerate(data):
        row = _validate_row(item, i)
        method = row["method"]
        if method in routes:
            raise ValueError(f"DUPLICATE_METHOD: {method}")
        routes[method] = row
    return routes


def verify_pinned_fixture(path: Path, which: str) -> str:
    if which not in PINS:
        raise ValueError("UNRECOGNIZED_PIN")
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError("SOURCE_PIN_MISMATCH")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    pin = PINS[which]
    if len(raw) != pin["bytes"] or digest != pin["sha256"]:
        raise ValueError(f"SOURCE_PIN_MISMATCH: {which}")
    return digest


def _source(path: Path, which: str, pinned: bool) -> dict:
    source = {
        "fixture_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "manifest_verified": pinned,
        "source_only": True,
    }
    if pinned:
        pin = PINS[which]
        source.update({
            "upstream_repo": SOURCE_REPO,
            "upstream_path": SOURCE_PATH,
            "upstream_commit": pin["commit"],
            "recorded_upstream_blob_sha1": pin["git_blob_sha1"],
            "observation": "PINNED_SOURCE_REFERENCE_ONLY",
        })
    return source


def build_report(old_path: Path = OLD, new_path: Path = NEW) -> dict:
    old_path, new_path = Path(old_path), Path(new_path)
    pinned_old = old_path.resolve() == OLD.resolve()
    pinned_new = new_path.resolve() == NEW.resolve()
    if pinned_old:
        verify_pinned_fixture(old_path, "old")
    if pinned_new:
        verify_pinned_fixture(new_path, "new")
    old, new = load_routes(old_path), load_routes(new_path)
    added = sorted(new.keys() - old.keys())
    removed = sorted(old.keys() - new.keys())
    changed = sorted(m for m in old.keys() & new.keys() if old[m] != new[m])
    changed_definitions = []
    matrix = {}
    for method in sorted(old.keys() | new.keys()):
        prior, after = old.get(method), new.get(method)
        old_full = bool(prior and "path" in prior)
        new_full = bool(after and "path" in after)
        definition = (
            "FULL_ROUTE_IN_BOTH" if old_full and new_full else
            "FULL_ROUTE_IN_OLD_ONLY" if old_full else
            "FULL_ROUTE_IN_NEW_ONLY" if new_full else "NAME_ONLY"
        )
        matrix_row = {
            "observed_in": [
                name for name, row in (("old", prior), ("new", after)) if row is not None
            ],
            "definition": definition,
            "live_availability": "NOT_TESTED",
        }
        if old_full:
            matrix_row["old"] = prior
        if new_full:
            matrix_row["new"] = after
        matrix[method] = matrix_row
        if method in changed:
            fields = sorted((set(prior) | set(after)) - {"method"})
            differences = {
                field: {
                    "old": prior.get(field), "new": after.get(field),
                    "old_type": type(prior[field]).__name__ if field in prior else "missing",
                    "new_type": type(after[field]).__name__ if field in after else "missing",
                }
                for field in fields
                if (field in prior) != (field in after) or prior.get(field) != after.get(field)
            }
            changed_definitions.append({
                "method": method,
                "changed_fields": sorted(differences),
                "field_changes": differences,
            })
    namespaces = Counter(name.split(".", 1)[0] for name in added)
    return {
        "schema": "muse-hub/route-compat/v1",
        "scope": (
            "PINNED_OFFLINE_SOURCE_PROJECTION_NOT_LIVE_PROVIDER"
            if pinned_old and pinned_new else "UNVERIFIED_CUSTOM_INPUT_NOT_LIVE_PROVIDER"
        ),
        "live_provider_tested": False,
        "authorization_established": False,
        "old_count": len(old), "new_count": len(new),
        "added_count": len(added), "removed_count": len(removed),
        "changed_count": len(changed),
        "added": added, "removed": removed, "changed": changed,
        "changed_definitions": changed_definitions,
        "added_by_namespace": dict(sorted(namespaces.items(), key=lambda x: (-x[1], x[0]))),
        "matrix": matrix,
        "source": {
            "old": _source(old_path, "old", pinned_old),
            "new": _source(new_path, "new", pinned_new),
        },
        "limitations": [
            "Name-only entries do not expose callable HTTP paths, services or schemas.",
            "Eight source definition differences do not prove breaking live API behavior.",
            "No Muse account, provider, permission or transport was tested.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", type=Path, default=OLD, help="prior pinned projection")
    parser.add_argument("--new", type=Path, default=NEW, help="newer pinned projection")
    parser.add_argument("--expect", help="expected old,new,added,removed,changed counts")
    parser.add_argument("--out", type=Path, help="create-only JSON report path")
    args = parser.parse_args(argv)
    try:
        report = build_report(args.old, args.new)
        if args.expect:
            try:
                expected = [int(x.strip()) for x in args.expect.split(",")]
            except ValueError as exc:
                raise ValueError("INVALID_EXPECT_COUNTS") from exc
            actual = [
                report[k] for k in (
                    "old_count", "new_count", "added_count",
                    "removed_count", "changed_count",
                )
            ]
            if len(expected) != 5 or expected != actual:
                raise ValueError(f"EXPECTED_COUNTS_MISMATCH: {expected} vs {actual}")
        output = json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if args.out:
            try:
                with args.out.open("x", encoding="utf-8", newline="\n") as target:
                    target.write(output)
            except FileExistsError as exc:
                raise ValueError("OUTPUT_EXISTS") from exc
            print(f"CREATED {args.out}: {report['old_count']} to {report['new_count']}")
        else:
            print(output)
    except (ValueError, OSError) as exc:
        print(f"ROUTE_COMPARISON_REFUSED: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
