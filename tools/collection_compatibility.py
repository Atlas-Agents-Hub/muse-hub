"""Validate specialist procedure IDs, role aliases, and links to the skill library."""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("collection_source_reader", ROOT / "tools/muse_collection.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("COLLECTION_READER_UNAVAILABLE")
_collection = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(_collection)
read_json = _collection.read_json
ALIASES = {"data-engineer": "data-engineering-architect", "reliability-engineer": "infrastructure-reliability-engineer"}
SHARED = {"evidence_audit", "safe_resume", "research_verification", "consent_and_effects", "quality_handoff"}
SCHEMA = "muse-collection-public-compatibility/v2"


class CompatibilityError(ValueError):
    pass


def require(condition: bool, reason: str) -> None:
    if not condition:
        raise CompatibilityError(reason)


def validate_mapping(value: dict, procedure_ids: set[str], skill_ids: set[str]) -> None:
    require(type(value) is dict and set(value) == {"schema", "role_aliases", "procedure_links"}, "SCHEMA")
    require(value["schema"] == SCHEMA, "SCHEMA")
    require(value["role_aliases"] == ALIASES, "ALIAS")
    links = value["procedure_links"]
    require(type(links) is list and len(links) == len(procedure_ids), "PROCEDURE_COUNT")
    seen = set()
    for row in links:
        require(type(row) is dict and set(row) == {"procedure_id", "role", "method", "related_collection_skills"}, "SCHEMA")
        identifier = row["procedure_id"]
        require(type(identifier) is str and identifier in procedure_ids and identifier not in seen, "PROCEDURE_ID")
        seen.add(identifier)
        require(type(row["role"]) is str and bool(row["role"]) and type(row["method"]) is str and bool(row["method"]), "PROCEDURE_FIELDS")
        related = row["related_collection_skills"]
        require(type(related) is list and 1 <= len(related) <= 64 and all(type(x) is str for x in related), "RELATED")
        require(len(related) == len(set(related)) and set(related) <= skill_ids, "RELATED")
    require(seen == procedure_ids, "PROCEDURE_ID")


def _relative(root: Path, name: str) -> Path:
    require(type(name) is str and bool(name) and not name.startswith("/") and "\\" not in name and ":" not in name and all(x not in ("", ".", "..") for x in name.split("/")), "UNSAFE_PATH")
    path = root / name
    _collection._safe_path(path)
    require(path.resolve().is_relative_to(root.resolve()), "UNSAFE_PATH")
    return path


def verify_current_manifest(root: Path) -> int:
    """Check the current distribution after its manifest has been refreshed."""
    source = str(ROOT / "src")
    if source not in sys.path:
        sys.path.insert(0, source)
    from muse_presets.public_export import select_public_files
    _relative(root, "PUBLIC_SOURCE_MANIFEST.json")
    require((root / "PUBLIC_SOURCE_MANIFEST.json").is_file(), "PUBLIC_MANIFEST_MISSING")
    return len(select_public_files(root))


def current_inventory(data: dict) -> dict:
    """Count the collection entries and worked practice artifacts actually present."""
    cases = data.get("depth_cases", [])
    specialists = data.get("specialists", [])
    return {
        "schema": "muse-hub/library-inventory/v1",
        "skills": len(data["skills"]),
        "workflows": len(data["workflows"]),
        "task_starters": len(data["starters"]),
        "specialists": len(specialists),
        "skills_with_practice_cases": len({case["skill_id"] for case in cases}),
        "practice_cases": len(cases),
        "positive_practice_examples": sum("reference_output" in case for case in cases),
        "negative_practice_examples": sum("wrong_output" in case for case in cases),
        "task_evaluation_specs": len(data.get("evaluation_cases", [])),
        "executable_specialist_extensions": sum(role.get("kind") == "executable-extension" for role in specialists),
    }


def check_repository(root: Path = ROOT, *, verify_manifest: bool = False) -> dict:
    root = Path(root)
    require(root.resolve() == ROOT.resolve(), "SOURCE_ROOT_MISMATCH")
    prefix = "collections/muse-starters-v1/"
    data = _collection.load_collection(root / prefix)
    mapping = read_json(root / (prefix + "PUBLIC_COMPATIBILITY.json"))
    registry = read_json(root / "presets/catalog.json")
    roles = registry["presets"]
    require(type(roles) is list and all(type(x) is str for x in roles) and len(roles) == len(set(roles)) == 15, "ROLE_COUNT")
    source = str(root / "src")
    if source not in sys.path:
        sys.path.insert(0, source)
    from muse_presets.role_skills import skill_id, SHARED_SKILLS
    require(set(SHARED_SKILLS) == SHARED, "SHARED_IDS_CHANGED")
    expected = {identifier: ("shared", identifier) for identifier in SHARED_SKILLS}
    for role in roles:
        book = read_json(_relative(root, "presets/" + role + "/playbook.json"))
        methods = book.get("methods")
        require(book.get("role_id") == role and type(methods) is list and len(methods) == 3, "ROLE_METHOD_COUNT")
        for method in methods:
            require(type(method) is dict and type(method.get("id")) is str, "ROLE_METHOD_ID")
            identifier = skill_id(role, method["id"])
            require(identifier not in expected, "DUPLICATE_PROCEDURE")
            expected[identifier] = (role, method["id"])
    skills = {item["id"] for item in data["skills"]}
    validate_mapping(mapping, set(expected), skills)
    for row in mapping["procedure_links"]:
        require((row["role"], row["method"]) == expected[row["procedure_id"]], "PROCEDURE_SOURCE_JOIN")
    result = {"status": "COLLECTION_COMPATIBILITY_VERIFIED", "roles": len(roles),
              "collection_skills": len(skills), "procedures": len(expected),
              "starters": len(data["starters"]), "workflows": len(data["workflows"])}
    if verify_manifest:
        result["verified_source_files"] = verify_current_manifest(root)
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--verify-manifest", action="store_true", help="Also verify current public file hashes after refreshing the release manifest")
    mode.add_argument("--inventory", action="store_true", help="Print the current library and practice counts")
    args = parser.parse_args(argv)
    try:
        result = current_inventory(_collection.load_collection()) if args.inventory else check_repository(verify_manifest=args.verify_manifest)
        print(json.dumps(result, sort_keys=True, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError, UnicodeError) as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
