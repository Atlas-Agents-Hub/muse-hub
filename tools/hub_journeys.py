#!/usr/bin/env python3
"""H19: read-only Muse Hub installation/recovery journeys.

Reuses the public H00-H21 readiness register and existing role install guides.
It never stages files, authenticates providers, installs agents or invokes effects.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "muse-hub/h19-source-journeys/v1"
PHASES = ("install", "configure", "health", "named_test", "failure", "stop", "uninstall")
IDS = tuple(f"H{i:02d}" for i in range(22))
ROLE_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
TESTS = {
    "H02": "tests/test_hub_site_overlay.py",
    "H03": "tests/test_muse_route_compat_h03.py",
    "H11": "tests/test_h11_engineering_doors.py",
    "H12": "tests/test_family_sourcekit.py",
    "H14": "tests/test_companion_home_h14_h17.py",
    "H15": "tests/test_companion_home_h14_h17.py",
    "H16": "tests/test_companion_home_h14_h17.py",
    "H17": "tests/test_companion_home_h14_h17.py",
    "H19": "tests/test_hub_journeys.py",
}


def _pairs(items: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _read_json(path: Path) -> dict:
    if path.is_symlink() or not path.is_file():
        raise ValueError("SOURCE_DOCUMENT_MISSING")
    result = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs)
    if not isinstance(result, dict):
        raise ValueError("SOURCE_DOCUMENT_SHAPE")
    return result


def _safe_file(root: Path, name: str) -> Path:
    if (not isinstance(name, str) or not name
            or "\\" in name or ":" in name or name.startswith("/")
            or name.startswith("//")):
        raise ValueError("SOURCE_PATH_UNSAFE")
    relative = Path(name)
    if relative.is_absolute() or any(part in ("", ".", "..") for part in relative.parts):
        raise ValueError("SOURCE_PATH_UNSAFE")
    target = root
    for part in relative.parts:
        target = target / part
        if target.is_symlink() or (hasattr(target, "is_junction") and target.is_junction()):
            raise ValueError("SOURCE_PATH_UNSAFE")
    if not target.is_file():
        raise ValueError("SOURCE_PATH_MISSING")
    return target


def validate_features(tasks: list[dict], root: Path = ROOT) -> None:
    if not isinstance(tasks, list) or len(tasks) != len(IDS):
        raise ValueError("FEATURE_IDS")
    names = [x.get("id") if isinstance(x, dict) else None for x in tasks]
    if names != list(IDS):
        raise ValueError("FEATURE_IDS")
    known = set(names)
    graph = {}
    for task in tasks:
        ident = task["id"]
        deps = task.get("dependencies")
        if not isinstance(deps, list) or len(deps) != len(set(deps)):
            raise ValueError("DEPENDENCY_SHAPE")
        if any(x not in known for x in deps):
            raise ValueError("DEPENDENCY_UNKNOWN")
        graph[ident] = deps
        if (not isinstance(task.get("title"), str) or not task["title"]
                or not isinstance(task.get("status"), str)
                or not isinstance(task.get("next_verification"), str)
                or not task["next_verification"]):
            raise ValueError("FEATURE_METADATA_MISSING")
        if task.get("native_runtime_verified") is not False or task.get("site_deployed") is not False:
            raise ValueError("UNVERIFIED_RUNTIME_CLAIM_REFUSED")
        paths = task.get("source_paths")
        if not isinstance(paths, list) or len(paths) != len(set(paths)):
            raise ValueError("SOURCE_PATH_SHAPE")
        for path in paths:
            _safe_file(root, path)
    visiting, visited = set(), set()

    def visit(node: str) -> None:
        if node in visiting:
            raise ValueError("DEPENDENCY_CYCLE")
        if node in visited:
            return
        visiting.add(node)
        for parent in graph[node]:
            visit(parent)
        visiting.remove(node)
        visited.add(node)

    for node in names:
        visit(node)


def load_features(root: Path = ROOT) -> list[dict]:
    doc = _read_json(root / "docs/discovery/hub-feature-status.json")
    if doc.get("schema") != "muse-hub/h00-h21-feature-readiness/v1":
        raise ValueError("FEATURE_SCHEMA")
    tasks = doc.get("tasks")
    validate_features(tasks, root)
    return tasks


def load_roles(root: Path = ROOT) -> list[dict]:
    doc = _read_json(root / "hub/site/roles.json")
    if doc.get("schema") != "muse-hub-site/role-directory/v1":
        raise ValueError("ROLE_SCHEMA")
    roles = doc.get("roles")
    if not isinstance(roles, list) or len(roles) != 15:
        raise ValueError("ROLE_COUNT")
    ids = []
    for item in roles:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise ValueError("ROLE_SHAPE")
        slug = item["id"]
        if not ROLE_RE.fullmatch(slug):
            raise ValueError("ROLE_SLUG")
        ids.append(slug)
        _safe_file(root, "presets/" + slug + "/INSTALL.md")
    if len(ids) != len(set(ids)):
        raise ValueError("ROLE_DUPLICATE")
    return roles


def verify_inventory(root: Path = ROOT) -> dict:
    tasks = load_features(root)
    roles = load_roles(root)
    return {
        "schema": SCHEMA,
        "status": "SOURCE_INVENTORY_VALID_NOT_RUNTIME_VERIFIED",
        "features": len(tasks),
        "roles": len(roles),
        "native_installed": False,
        "external_effect_authorized": False,
        "site_deployed": False,
        "source_verification_only": True,
    }


def _phase(status: str, instruction: str, **extra: object) -> dict:
    return {"status": status, "instruction": instruction, **extra}


def build_journeys(root: Path = ROOT, *, feature: str | None = None,
                   role: str | None = None) -> dict:
    tasks = load_features(root)
    roles = load_roles(root)
    by_role = {item["id"]: item for item in roles}
    if feature is not None and feature not in IDS:
        raise ValueError("FEATURE_UNKNOWN")
    if role is not None and role not in by_role:
        raise ValueError("ROLE_UNKNOWN")
    chosen = [x for x in tasks if feature is None or x["id"] == feature]
    guide = "presets/" + role + "/INSTALL.md" if role else None
    result = []
    for item in chosen:
        paths = item["source_paths"]
        test_path = TESTS.get(item["id"])
        if test_path is not None:
            _safe_file(root, test_path)
        name = test_path or item["id"] + "_HOST_ACCEPTANCE_NOT_VERIFIED"
        phases = {
            "install": _phase(
                "SOURCE_GUIDE_ONLY" if paths else "BLOCKED_NO_PUBLIC_SOURCE",
                "Read reviewed source files; do not treat them as installed agents."
                if paths else "No reviewed standalone source installer for this feature.",
                source_paths=paths),
            "configure": _phase(
                "OWNER_ACTION_REQUIRED" if guide else "NO_ROLE_SELECTED",
                "Review " + guide + " and the host compatibility guide; no automatic account registration."
                if guide else "Choose a specialist and consult its INSTALL.md; host registration is separate.",
                role_guide=guide),
            "health": _phase(
                "READ_ONLY_SOURCE_PATHS_PRESENT" if paths else "NO_PUBLIC_SOURCE",
                "Verified paths exist locally; provider, device and native execution remain unverified.",
                checked_paths=paths),
            "named_test": _phase(
                "SOURCE_TEST_AVAILABLE_NOT_RUN" if test_path else "NOT_VERIFIED",
                "Run the named local source test independently; it cannot prove native host behavior."
                if test_path else "No qualified host test exists; do not claim operational acceptance.",
                name=name,
                command=("python -B scripts/run_source_test.py " +
                         Path(test_path).name) if test_path else None),
            "failure": _phase(
                "HOLD_UNKNOWN",
                "Do not retry an ambiguous external action. Next required evidence: " +
                item["next_verification"]),
            "stop": _phase(
                "NO_EXTERNAL_EFFECT",
                "This tool starts no process or connection; stop only an owned local run, never a third-party worker."),
            "uninstall": _phase(
                "MANUAL_OWNER_VERIFICATION",
                "Remove only verified disposable output you own; native revocation and remote jobs require original host authorization."),
        }
        result.append({
            "id": item["id"], "title": item["title"], "priority": item["priority"],
            "dependencies": item["dependencies"], "readiness_status": item["status"],
            "source_paths": paths, "next_verification": item["next_verification"],
            "phases": phases, "native_runtime_verified": False, "site_deployed": False,
        })
    return {
        "schema": SCHEMA,
        "status": "SOURCE_JOURNEY_PLAN_NOT_INSTALLATION",
        "role": {"id": role, "guide": guide} if role else None,
        "journeys": result,
        "native_installed": False,
        "external_effect_authorized": False,
        "site_deployed": False,
    }


def _markdown(result: dict) -> str:
    if "journeys" not in result:
        return ("# Muse Hub source inventory\n\n"
                "Source checked: " + str(result["features"]) + " features, " +
                str(result["roles"]) + " roles. Native Muse: NOT VERIFIED.\n")
    lines = [
        "# Muse Hub installation and recovery journeys",
        "",
        "SOURCE ONLY — native Muse, recipient effects and hosted site: NOT VERIFIED.",
        "",
        "| Feature | Source status | Named source test | Native |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["journeys"]:
        lines.append("| " + item["id"] + " — " + item["title"].replace("|", "/") +
                     " | " + item["readiness_status"] + " | " +
                     item["phases"]["named_test"]["name"] + " | NOT VERIFIED |")
    lines.extend(["", "Each journey has install, configure, health, named_test, failure, stop and uninstall phases.",
                  "No host action, deployment or release is performed."])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Read-only H00-H21 source journeys; not a native installer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--feature")
    group.add_argument("--all", action="store_true")
    group.add_argument("--verify", action="store_true")
    parser.add_argument("--role", help="one of the 15 public specialist slugs")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args(argv)
    try:
        if args.verify:
            result = verify_inventory()
        else:
            result = build_journeys(feature=args.feature, role=args.role)
        print(json.dumps(result, indent=2, sort_keys=True) if args.format == "json"
              else _markdown(result))
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "REFUSED", "reason": str(exc),
                          "native_installed": False,
                          "external_effect_authorized": False}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
