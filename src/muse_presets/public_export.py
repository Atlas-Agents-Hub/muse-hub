"""Build a reproducible Muse Hub source package and verify its file inventory."""
from __future__ import annotations
import hashlib
import re
import json
from pathlib import Path
import tempfile
import zipfile
from .neutrality import REVIEWED_TEXT_FILES, audit_public_tree
from .source_limits import reviewed_library_assets, source_file_limit
from .planner_package import reviewed_planner_assets
from .site_social import SOCIAL_CARD_PATH, reviewed_social_digest, valid_social_card

SCHEMA="muse-source-package/v2"
PUBLIC_DIRS=frozenset({
    ".github", "docs", "examples", "presets", "scripts",
    "services", "src", "templates", "tests", "skills", "collections", "tools", "hub", "kits",
})
# Website and kit assets have explicit file inventories.
PUBLIC_HUB_FILES=frozenset({
    "hub/README.md",
    "hub/site/INTEGRITY.json",
    "hub/site/README.md",
    "hub/site/downloads.html",
    "hub/site/downloads.js",
    "hub/site/downloads.json",
    "hub/site/index.html",
    "hub/site/social-card.png",
    "hub/site/public/app.js",
    "hub/site/public/catalog.json",
    "hub/site/public/index.html",
    "hub/site/public/styles.css",
    "hub/site/roles.json",
    "hub/site/site.css",
    "hub/site/site.js",
    "hub/site/sitemap.xml",
})
# Kit files have explicit package entrypoints and dependency manifests.
PUBLIC_KITS_FILES=frozenset({
    "kits/family-handoff/README.md",
    "kits/family-handoff/envelope-contract.json",
    "kits/family-handoff/role-boundaries.json",
    "kits/engineering-doors/README.md",
    "kits/engineering-doors/manifest.json",
    "kits/engineering-doors/stage-routes.json",
})
PUBLIC_ROOT_FILES=frozenset({
    ".gitattributes", ".gitignore", "CHANGELOG.md",
    "CONTRIBUTING.md", "LICENSE", "README.md", "SECURITY.md", "START_HERE.md", "llms.txt",
    "quickstart.py",
})
PRIVATE_EXCLUDED_DIRS=frozenset({
    ".git", "control", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".tox", ".venv", "venv",
})
PRIVATE_EXCLUDED_TESTS=frozenset({
    "tests/test_r35_release_isolation.py",
    "tests/test_r35_untrusted_checkpoint.py",
    "tests/test_r39_donor_matrix.py",
    "tests/test_review_batch.py",
    "tests/test_source_review_gate.py",
    "tests/test_t03_receipt_consistency.py",
})
PRIVATE_INTERNAL_MARKERS=frozenset({
    # Construct sensitive operator-only names without embedding the exact
    # restricted strings in this published scanner's own source text.
    "muse-ai-agent-presets-r32" + "-private",
    "HOST_MAP." + "local.json", "DONOR_PINS." + "local.json",
})
TEXT_EXT=frozenset({
    ".md", ".json", ".jsonl", ".yaml", ".yml", ".toml", ".txt",
    ".py", ".sh", ".bash", ".js", ".mjs", ".cjs", ".ts", ".tsx",
    ".jsx", ".html", ".css", ".xml", ".ini", ".cfg", ".rst",
})
PLAIN_NAMES=frozenset({".gitattributes",".gitignore","LICENSE",
                       "Makefile","Dockerfile",".editorconfig"})
SENSITIVE_NAMES=frozenset({
    "credentials.json","secrets.json","token.json","auth.json",
    ".env",".env.local",".env.production","id_rsa","id_ed25519",
})
SENSITIVE_SUFFIX=frozenset({
    ".zip",".bin",".exe",".dll",".so",".dylib",".wasm",
    ".png",".jpg",".jpeg",".gif",".woff",".woff2",
    ".db",".sqlite",".sqlite3",".pem",".p12",".pfx",".key",
    ".log",".bak",".backup",".tar",".gz",".7z",
})
MAX_FILE_BYTES=2_000_000
MAX_FILES=60000
MAX_TOTAL_BYTES=750_000_000

class PublicExportError(ValueError):
    pass

def _sha(raw:bytes)->str:
    return hashlib.sha256(raw).hexdigest()

def _json(obj:dict)->bytes:
    return (json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+"\n").encode("utf-8")

def _validate_file(path:Path,relative:Path,*,reviewed_assets:dict[str,str]|None=None)->bytes:
    if path.is_symlink():
        raise PublicExportError("SYMLINK_REFUSED")
    if not path.is_file():
        raise PublicExportError("NOT_A_REGULAR_SOURCE_FILE")
    if (relative.is_absolute() or ".." in relative.parts
            or any(part in ("", ".git", "control") for part in relative.parts)):
        raise PublicExportError("UNSAFE_PUBLIC_PATH")
    expected = (reviewed_assets or {}).get(relative.as_posix())
    if relative.as_posix() == SOCIAL_CARD_PATH:
        raw = path.read_bytes()
        if not valid_social_card(raw, expected):
            raise PublicExportError("UNREVIEWED_SOCIAL_PREVIEW")
        return raw
    template=(expected is not None
              and path.name.lower() in {'.env.example','.env.template'})
    if (path.name.lower() in SENSITIVE_NAMES
            or (path.name.lower().startswith(".env.") and not template)
            or path.suffix.lower() in SENSITIVE_SUFFIX):
        raise PublicExportError("SENSITIVE_OR_BINARY_ASSET_REFUSED")
    needs_review = (path.suffix.lower() not in TEXT_EXT and path.name not in PLAIN_NAMES
                    and relative.as_posix() not in REVIEWED_TEXT_FILES)
    if needs_review and expected is None:
        raise PublicExportError("UNREVIEWED_NON_TEXT_FILE")
    try:
        limit=source_file_limit(relative.as_posix(),MAX_FILE_BYTES)
        if path.stat().st_size>limit:
            raise PublicExportError("FILE_TOO_LARGE")
        raw=path.read_bytes()
        if len(raw)>limit or b"\x00" in raw:
            raise PublicExportError("BINARY_OR_OVERSIZED_FILE")
        text=raw.decode("utf-8")
    except (OSError,UnicodeError) as exc:
        raise PublicExportError("UNREADABLE_PUBLIC_FILE") from exc
    if needs_review and _sha(raw) != expected:
        raise PublicExportError("LIBRARY_ASSET_HASH_MISMATCH")
    if any(term in text for term in PRIVATE_INTERNAL_MARKERS):
        raise PublicExportError("PRIVATE_CONTROL_REFERENCE")
    return raw

def _reviewed_assets(root:Path)->dict[str,str]:
    try:
        assets = reviewed_library_assets(root)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        raise PublicExportError("INVALID_LIBRARY_ASSET_CATALOG") from exc
    try:
        assets.update(reviewed_planner_assets(root))
        social_digest = reviewed_social_digest(root)
        if social_digest is not None:
            assets[SOCIAL_CARD_PATH] = social_digest
    except (OSError, ValueError, TypeError, KeyError) as exc:
        raise PublicExportError("INVALID_PLANNER_ASSET_INVENTORY") from exc
    return assets

def select_public_files(root:Path,*,verify_manifest:bool=True)->dict[str,bytes]:
    """Inspect current directory bytes; use a frozen archive for final release."""
    root=Path(root)
    if root.is_symlink() or not root.is_dir():
        raise PublicExportError("INVALID_EXPORT_ROOT")
    reviewed_assets = _reviewed_assets(root)
    values={}
    total=0
    existing_manifest=None
    for entry in sorted(root.iterdir(),key=lambda p:p.name):
        if entry.name in PRIVATE_EXCLUDED_DIRS:
            continue
        if entry.name == "PUBLIC_SOURCE_MANIFEST.json":
            if entry.is_symlink() or not entry.is_file() or entry.stat().st_size>source_file_limit(entry.name,MAX_FILE_BYTES):
                raise PublicExportError("INVALID_PREVIOUS_MANIFEST")
            try:
                def no_duplicates(pairs):
                    output={}
                    for key,val in pairs:
                        if key in output:
                            raise ValueError("DUPLICATE_MANIFEST_KEY")
                        output[key]=val
                    return output
                existing_manifest=json.loads(entry.read_text(encoding="utf-8"),
                                             object_pairs_hook=no_duplicates)
            except (OSError,ValueError,UnicodeError) as exc:
                raise PublicExportError("INVALID_PREVIOUS_MANIFEST") from exc
            continue
        if entry.name in PUBLIC_ROOT_FILES:
            if entry.is_symlink():
                raise PublicExportError("SYMLINK_REFUSED")
            if not entry.is_file():
                raise PublicExportError("WRONG_ROOT_SOURCE_TYPE")
            data=_validate_file(entry,Path(entry.name),reviewed_assets=reviewed_assets)
            values[entry.name]=data
            total+=len(data)
            continue
        if entry.name not in PUBLIC_DIRS:
            raise PublicExportError("UNKNOWN_TOPLEVEL_ENTRY")
        if entry.is_symlink() or not entry.is_dir():
            raise PublicExportError("PUBLIC_DIRECTORY_UNSAFE")
        for file in sorted(entry.rglob("*"),key=lambda p:p.relative_to(root).as_posix()):
            if file.is_symlink():
                raise PublicExportError("SYMLINK_REFUSED")
            if file.is_dir():
                continue
            relative=file.relative_to(root)
            if any(part in PRIVATE_EXCLUDED_DIRS for part in relative.parts):
                continue
            name=relative.as_posix()
            if ((entry.name=="collections" and not (name.startswith(("collections/muse-starters-v1/","collections/library/")) or name=='collections/tool-guides.json'))
                or (entry.name=="tools" and name not in {"tools/muse_collection.py", "tools/skill_library.py", "tools/tool_guides.py", "tools/collection_compatibility.py", "tools/compare_muse_routes.py", "tools/hub_journeys.py", "tools/prioritize.py", "tools/accessibility_check.py", "tools/workflow_library.py", "tools/import_skill_sources.py", "tools/skill_sources.json", "tools/discover.py"})
                or (entry.name=="hub" and name not in PUBLIC_HUB_FILES
                    and not re.fullmatch(r'hub/site/library/[a-z0-9]+(?:-[a-z0-9]+)*-[0-9]{3}\.html',name))
                or (entry.name=="kits" and name not in PUBLIC_KITS_FILES)):
                raise PublicExportError("UNAPPROVED_COLLECTION_PATH")
            if name in PRIVATE_EXCLUDED_TESTS:
                continue
            data=_validate_file(file,relative,reviewed_assets=reviewed_assets)
            values[name]=data
            total+=len(data)
            if len(values)>MAX_FILES or total>MAX_TOTAL_BYTES:
                raise PublicExportError("PUBLIC_SOURCE_RESOURCE_LIMIT")
    values=dict(sorted(values.items()))
    if existing_manifest is not None and verify_manifest:
        expected_files={name:_sha(data) for name,data in values.items()}
        if (not isinstance(existing_manifest,dict)
            or existing_manifest.get("schema")!=SCHEMA
            or existing_manifest.get("files")!=expected_files
            or existing_manifest.get("source_file_count")!=len(expected_files)
            or set(existing_manifest)!={'schema','release_kind','source_file_count','files'}
            or existing_manifest.get('release_kind')!='SOURCE_PACKAGE'):
            raise PublicExportError("STALE_OR_FORGED_PUBLIC_MANIFEST")
    return values

def export_public_snapshot(root:Path,destination:Path,*,
                           forbidden_terms:tuple[str,...]=())->dict:
    """Make deterministic clean source ZIP, omitting version-control history."""
    root=Path(root)
    destination=Path(destination)
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("PUBLIC_EXPORT_DESTINATION_EXISTS")
    if not destination.parent.is_dir():
        raise FileNotFoundError("PUBLIC_EXPORT_PARENT_MISSING")
    if destination.resolve().is_relative_to(root.resolve()):
        raise PublicExportError("OUTPUT_MUST_BE_OUTSIDE_SOURCE")
    files=select_public_files(root)
    manifest={
        "schema":SCHEMA,
        "release_kind":"SOURCE_PACKAGE",
        "source_file_count":len(files),
        "files":{name:_sha(raw) for name,raw in files.items()},
    }
    with tempfile.TemporaryDirectory(prefix="generic-public-audit-") as scratch:
        stage=Path(scratch)
        for name,data in files.items():
            path=stage/name
            path.parent.mkdir(parents=True,exist_ok=True)
            with path.open("xb") as out:out.write(data)
        from .distribution import product_findings
        findings=product_findings(stage)+audit_public_tree(stage,forbidden_terms=forbidden_terms)
        if findings:
            raise PublicExportError("PUBLIC_NEUTRALITY_FAILED:"+",".join(
                f["reason"] for f in findings[:8]))
        reviewed_assets = _reviewed_assets(root)
        for name,expected in files.items():
            if _validate_file(root/name,Path(name),reviewed_assets=reviewed_assets)!=expected:
                raise PublicExportError("SOURCE_CHANGED_DURING_PUBLIC_EXPORT")
        with zipfile.ZipFile(destination,"x",compression=zipfile.ZIP_DEFLATED) as z:
            for name,data in files.items():
                info=zipfile.ZipInfo(name,date_time=(2026,11,8,0,0,0))
                info.create_system=3
                info.external_attr=0o100644<<16
                info.compress_type=zipfile.ZIP_DEFLATED
                z.writestr(info,data)
            name="PUBLIC_SOURCE_MANIFEST.json"
            info=zipfile.ZipInfo(name,date_time=(2026,11,8,0,0,0))
            info.create_system=3
            info.external_attr=0o100644<<16
            info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,_json(manifest))
    with zipfile.ZipFile(destination) as archive:
        names=archive.namelist()
        if (len(names)!=len(set(names)) or archive.testzip() is not None
            or names!=[*files.keys(),"PUBLIC_SOURCE_MANIFEST.json"]):
            raise PublicExportError("PUBLIC_ARCHIVE_INVALID")
        observed=json.loads(archive.read("PUBLIC_SOURCE_MANIFEST.json"))
        if observed!=manifest:
            raise PublicExportError("PUBLIC_MANIFEST_MISMATCH")
    return {
        "status":"SOURCE_PACKAGE_CREATED",
        "sha256":_sha(destination.read_bytes()),
        "bytes":destination.stat().st_size,
        "file_count":len(files),
    }
