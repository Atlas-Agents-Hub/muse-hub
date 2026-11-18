#!/usr/bin/env python3
"""Find Muse Hub setup, testing, recovery, and update instructions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "muse-hub/setup-journeys/v2"
FEATURE_REGISTER = "docs/discovery/setup-journeys.json"
PHASES = ("install", "configure", "health", "named_test", "failure", "stop", "uninstall")
INSTRUCTIONS = set(PHASES) - {"named_test"}
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
TEST_PATH = re.compile(r"tests/test_[a-z0-9_]+\.py\Z")
MAX_DOCUMENT_BYTES = 1_000_000


def _pairs(items: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _constant(value: str) -> None:
    raise ValueError("INVALID_JSON_CONSTANT:" + value)


def _read_json(path: Path) -> dict:
    if path.is_symlink() or not path.is_file():
        raise ValueError("SOURCE_DOCUMENT_MISSING")
    if path.stat().st_size > MAX_DOCUMENT_BYTES:
        raise ValueError("SOURCE_DOCUMENT_SIZE")
    data = path.read_bytes()
    if len(data) > MAX_DOCUMENT_BYTES:
        raise ValueError("SOURCE_DOCUMENT_SIZE")
    result = json.loads(data.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=_constant)
    if type(result) is not dict:
        raise ValueError("SOURCE_DOCUMENT_SHAPE")
    return result


def _safe_file(root: Path, name: str) -> Path:
    if (type(name) is not str or not name or "\\" in name or ":" in name
            or any(part in ("", ".", "..") for part in name.split("/"))):
        raise ValueError("SOURCE_PATH_UNSAFE")
    if root.is_symlink() or (hasattr(root, "is_junction") and root.is_junction()):
        raise ValueError("SOURCE_PATH_UNSAFE")
    target = root
    for part in name.split("/"):
        target = target / part
        if target.is_symlink() or (hasattr(target, "is_junction") and target.is_junction()):
            raise ValueError("SOURCE_PATH_UNSAFE")
    if not target.is_file():
        raise ValueError("SOURCE_PATH_MISSING")
    return target


def validate_features(features: list[dict], root: Path = ROOT) -> None:
    if type(features) is not list or not 1 <= len(features) <= 128:
        raise ValueError("FEATURE_COUNT")
    seen = set()
    fields = {"id", "title", "summary", "guide", "source_paths", "tests", "instructions"}
    for feature in features:
        if type(feature) is not dict or set(feature) != fields:
            raise ValueError("FEATURE_SCHEMA")
        identifier = feature["id"]
        if type(identifier) is not str or not SLUG.fullmatch(identifier) or identifier in seen:
            raise ValueError("FEATURE_ID")
        seen.add(identifier)
        for key in ("title", "summary"):
            if type(feature[key]) is not str or not 1 <= len(feature[key]) <= 500:
                raise ValueError("FEATURE_METADATA")
        _safe_file(root, feature["guide"])
        paths = feature["source_paths"]
        if (type(paths) is not list or not 1 <= len(paths) <= 32
                or not all(type(path) is str for path in paths)
                or len(paths) != len(set(paths))):
            raise ValueError("SOURCE_PATH_SHAPE")
        for path in paths:
            _safe_file(root, path)
        tests = feature["tests"]
        if (type(tests) is not list or len(tests) > 16
                or not all(type(path) is str and TEST_PATH.fullmatch(path) for path in tests)
                or len(tests) != len(set(tests))):
            raise ValueError("TEST_PATH_SHAPE")
        for path in tests:
            _safe_file(root, path)
        instructions = feature["instructions"]
        if (type(instructions) is not dict or set(instructions) != INSTRUCTIONS
                or not all(type(text) is str and 1 <= len(text) <= 1200 for text in instructions.values())):
            raise ValueError("INSTRUCTION_SHAPE")


def load_features(root: Path = ROOT) -> list[dict]:
    doc = _read_json(_safe_file(root, FEATURE_REGISTER))
    if set(doc) != {"schema", "features"} or doc["schema"] != "muse-hub/setup-guides/v1":
        raise ValueError("FEATURE_SCHEMA")
    validate_features(doc["features"], root)
    return doc["features"]


def load_roles(root: Path = ROOT) -> list[dict]:
    doc = _read_json(_safe_file(root, "hub/site/roles.json"))
    if doc.get("schema") != "muse-hub-site/role-directory/v1":
        raise ValueError("ROLE_SCHEMA")
    roles = doc.get("roles")
    if type(roles) is not list or len(roles) != 15:
        raise ValueError("ROLE_COUNT")
    seen = set()
    for item in roles:
        if type(item) is not dict or type(item.get("id")) is not str or not SLUG.fullmatch(item["id"]):
            raise ValueError("ROLE_SHAPE")
        if item["id"] in seen:
            raise ValueError("ROLE_DUPLICATE")
        seen.add(item["id"])
        _safe_file(root, "presets/" + item["id"] + "/INSTALL.md")
    return roles


def verify_inventory(root: Path = ROOT) -> dict:
    features = load_features(root)
    roles = load_roles(root)
    return {"schema": SCHEMA, "status": "SETUP_GUIDES_VALID", "features": len(features), "roles": len(roles)}


def build_journeys(root: Path = ROOT, *, feature: str | None = None, role: str | None = None) -> dict:
    features = load_features(root)
    roles = {item["id"]: item for item in load_roles(root)}
    if feature is not None and feature not in {item["id"] for item in features}:
        raise ValueError("FEATURE_UNKNOWN")
    if role is not None and role not in roles:
        raise ValueError("ROLE_UNKNOWN")
    selected = [item for item in features if feature is None or item["id"] == feature]
    role_guide = "presets/" + role + "/INSTALL.md" if role else None
    journeys = []
    for item in selected:
        commands = ["python -B scripts/run_source_test.py " + Path(path).name for path in item["tests"]]
        phases = {key: {"instruction": item["instructions"][key]} for key in PHASES if key != "named_test"}
        phases["named_test"] = {"instruction": "Run the listed checks, then try the guide's example." if commands else "Follow the guide's connection and readback steps.", "commands": commands}
        journeys.append({"id": item["id"], "title": item["title"], "summary": item["summary"],
                         "guide": item["guide"], "source_paths": item["source_paths"], "phases": phases})
    return {"schema": SCHEMA, "status": "SETUP_GUIDES_READY", "role": {"id": role, "guide": role_guide} if role else None, "journeys": journeys}


def _markdown(result: dict) -> str:
    if "journeys" not in result:
        return "# Muse Hub setup guides\n\nChecked " + str(result["features"]) + " feature guides and " + str(result["roles"]) + " specialist setup paths.\n"
    lines = ["# Muse Hub setup and recovery", ""]
    if result["role"]:
        lines.extend(["Specialist guide: `" + result["role"]["guide"] + "`", ""])
    headings = {"install": "Get started", "configure": "Configure", "health": "Try it", "named_test": "Check it", "failure": "Recover", "stop": "Stop", "uninstall": "Remove or update"}
    for item in result["journeys"]:
        lines.extend(["## " + item["title"], "", item["summary"], "", "Guide: `" + item["guide"] + "`", ""])
        for phase in PHASES:
            block = item["phases"][phase]
            lines.extend(["### " + headings[phase], "", block["instruction"], ""])
            if block.get("commands"):
                lines.extend(["```sh", *block["commands"], "```", ""])
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--feature", help="feature ID such as daily-desk or companion-home")
    group.add_argument("--all", action="store_true")
    group.add_argument("--verify", action="store_true")
    parser.add_argument("--role", help="specialist ID such as learning-coach")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args(argv)
    try:
        result = verify_inventory() if args.verify else build_journeys(feature=args.feature, role=args.role)
        print(json.dumps(result, indent=2, sort_keys=True) if args.format == "json" else _markdown(result))
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
