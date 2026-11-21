"""Build and verify a two-process Family Link handoff toolkit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

SCHEMA = "muse-hub/family-link-offline-kit/v2"
SOURCE_BASE_COMMIT = "49fb71a162173ac2dfb2c0f805e36109c34ac042"
SCOPE = "TWO_PROCESS_HANDOFF"
MANIFEST = "SOURCEKIT_MANIFEST.json"
MAX_MEMBERS = 40
MAX_FILE = 128_000
MAX_UNPACKED = 1_000_000
MAX_ARCHIVE = 2_000_000
HEX = re.compile(r"[a-f0-9]{64}\Z")
ROLE = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z")

# The base commit identifies the reviewed lineage, not the current file bytes.
# Exact release inputs are pinned below and revised only after review.
SOURCE_PINS = {
    "LICENSE": "af30e586ca6503924d5e4d99894ec6c7ce61ba77a55ba081b7a129d33f43fddf",
    "examples/family_offline_handoff_demo.py": 'a10917b6c541307f5963cf2d09f88db0542d5ea5442f16e9acee23bb553f71b7',
    "presets/catalog.json": 'd671abf91a067bfc22dddf6a294614d371578171a1ec0b6b8657243578415401',
    "src/muse_presets/__init__.py": 'f83f4c4be911f649be5321b16a735953134b869be60b423965554a2d28d5a863',
    "src/muse_presets/catalog.py": '685a1c393f8581a4741e40da47fa31accd3577a94a0185a5ca5008e4b690ca48',
    "src/muse_presets/family.py": "af043cc6edc7e0670d2ec098bdd94f7064f4998d58e784f5669cc740bb23780b",
    "src/muse_presets/family_envelope.py": '02fd3b8d6d811bfa21554b09702807f6cf39ec05ed869bb7f672b6e367e5083b',
    "src/muse_presets/neutrality.py": '6f9463d2334c17ec304473a18febe0329dc23d5045545525077d50bfd69b7326',
    "src/muse_presets/site_social.py": 'c5643da37e770374358e8b20175ff44dd0251c452a39aa1e2a69c808afc97992',
    "src/muse_presets/site_product.py": '63479bfa188e2abdda3cbb935bc754dbfd070757a84c753a01127b6047ccb1ba',
    "src/muse_presets/planner_package.py": 'ae34f9e82aaa373be0130e42e6ced40b59af5f8461b7758e7a7f32496393d0c0',
    "src/muse_presets/source_limits.py": '692b4c92957073e97c28347481730729154970f3dcc5e9dfb2cc9a7e91155f7d',
    "src/muse_presets/playbooks.py": 'c3abac0812efe26fbf34698e24fcdc18ebbd0d756bdc771092353b1859e04774',
}
# Exact accepted role bytes, in addition to disabled-by-default policy shape.
# A silent title/description edit must not alter the kit without a new review.
ROLE_PINS = {
    "coordinator": '2b1ea7c098a64ce1e92e053b68bbb4957571a0e40c1862d6e8d0dcb214e06142',
    "software-engineer": 'c92b781e2456a6ef3366da40217a0860f5cd4a6bbe79e535e110989e1240d5e8',
    "model-builder": 'be0dabaeb45b6914f2019f7e0312fc37e1246d23aa8c056e09bfa53e3285684b',
    "research-evaluator": '938efe7a27d3891f05e063cf4f7c9c132430ac87220308fdd24c9701b2cc6727',
    "creative-studio": '9d40e6e1d997f5d4fafd2fa1ad3924546da9ac2a8fdbdaab74cdb33120bffd04',
    "adversarial-verifier": '462d9de206cd7b8977b09afa6e70dda5ff4b248d08ece862c743f4f0f26d9aa8',
    "personal-companion": '8e2ab02cb1ef038ae43974cb77e1effdd69142a75ed37848735fff68aa7bb568',
    "garden-companion": 'c073dbee4ace0f399f51ef9dfec8c94872e75d1248f602e5a1dfb0ebd2fa67c3',
    "learning-coach": '998490c813a70a28b9bc45ed894f1b73b2ce8e6f3fa6c398cb50347af1178129',
    "claims-adjudicator": 'ea27a5773957a6c21043f20b94de2394183d6fe8a58f6228b256d1cbcae431e1',
    "reverse-engineering-researcher": '88d21bec06900d4f3d8fbdbc0ae10b48f9e2418eb944aa52da830a764fc1005f',
    "data-engineering-architect": '9c7aca8c1babe6a724bb429baa1d8fdd6a29d4b5e608ac338a8ff46d98b66ba1',
    "infrastructure-reliability-engineer": '6622cf789e309d894075a20b51059b58dda43f08d0f943fefa18e475050a6b5f',
    "automation-engineer": 'f992650ccd989b4811d095ecbdab710fbddb927a4d885c5a95ece4423765ae5a',
    "product-interface-designer": '54903de1a68a25506ef0fa3b10a76ff643b94a12f2c0a050f7f02a6fb7618c2c',
}
EXPECTED_ROLES = (
    "coordinator", "software-engineer", "model-builder", "research-evaluator",
    "creative-studio", "adversarial-verifier", "personal-companion",
    "garden-companion", "learning-coach", "claims-adjudicator",
    "reverse-engineering-researcher", "data-engineering-architect",
    "infrastructure-reliability-engineer", "automation-engineer",
    "product-interface-designer",
)
FALSE_FLAGS = (
    "native_installed", "sender_authenticated", "recipient_authenticated",
    "effect_authorized", "transport_bound", "public_release_published",
)
START_HERE = """# Family Link handoff review

Inspect a handoff envelope and its role policy, then run the included
two-process example to see validation and replay protection in action.

Use Python 3.12 or newer. Compare the archive's SHA-256 with the release
checksum and extract into a new folder. The example uses temporary sample
records and removes them when it finishes.

On macOS or Linux, run from the extracted folder:

    PYTHONPATH=src python -B examples/family_offline_handoff_demo.py

On Windows PowerShell, run from the extracted folder:

    $env:PYTHONPATH="src"
    python -B examples/family_offline_handoff_demo.py

Expected status: HANDOFF_REVIEW_PASSED. The report sets
separate_process_verified and replayed_id_refused to true.

Read the included role profiles and policy with your Muse task. For a real
handoff, use a connected transport, identify the intended recipient, follow the
user's authorization, and verify the result through the receiving transport.
Keep any failed or ambiguous delivery record for reconciliation before retrying.

The manifest records the reviewed source bytes. Keep it with the example
results and preserve the assistant's existing preferences and private memory.
"""


class FamilySourcekitError(ValueError):
    """Fail-closed source-custody, sourcekit or archive validation."""


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _json(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def _read_reviewed(root: Path, relative: str) -> bytes:
    parts = PurePosixPath(relative).parts
    if not parts or any(part in ("", ".", "..") for part in parts):
        raise FamilySourcekitError("UNSAFE_SOURCE_PATH")
    file = root.joinpath(*parts)
    # Refuse symlinked parents as well as symlinked leaf files.
    current = root
    for part in parts:
        current = current / part
        if current.is_symlink():
            raise FamilySourcekitError("SYMLINK_SOURCE_REFUSED")
    if not file.is_file() or file.stat().st_size > MAX_FILE:
        raise FamilySourcekitError("MISSING_OR_OVERSIZED_SOURCE:" + relative)
    if file.stat().st_nlink != 1:
        raise FamilySourcekitError("HARDLINK_SOURCE_REFUSED")
    data = file.read_bytes()
    if len(data) > MAX_FILE or b"\x00" in data:
        raise FamilySourcekitError("UNSAFE_SOURCE_BYTES")
    try:
        data.decode("utf-8")
    except UnicodeError as exc:
        raise FamilySourcekitError("SOURCE_NOT_UTF8") from exc
    return data


def _validate_catalog(members: dict[str, bytes]) -> tuple[str, ...]:
    catalog = json.loads(members["presets/catalog.json"].decode("utf-8"))
    if (
        type(catalog) is not dict
        or catalog.get("schema") != "muse-presets/catalog-v1"
        or tuple(catalog.get("presets", ())) != EXPECTED_ROLES
        or catalog.get("services") != ["evidence-finder"]
    ):
        raise FamilySourcekitError("ROLE_CATALOG_CHANGED")
    return EXPECTED_ROLES


def _validate_profile(role: str, data: bytes) -> None:
    try:
        profile = json.loads(data.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise FamilySourcekitError("INVALID_ROLE_POLICY") from exc
    if type(profile) is not dict or profile.get("id") != role:
        raise FamilySourcekitError("ROLE_ID_MISMATCH")
    policy = profile.get("family_link")
    if (
        profile.get("schema") != "muse-presets/preset-v1"
        or profile.get("maturity") != "PROFILE_TEMPLATE"
        or profile.get("native_muse_status") != "UNBOUND"
        or profile.get("requirements") != {
            "permissions": [], "external_services": [], "secret_values": [],
        }
        or type(policy) is not dict
        or policy.get("enabled") is not False
        or policy.get("mode") != "proposal-only"
        or policy.get("transport") != "unbound"
        or policy.get("trusted_signer") is not None
        or policy.get("native_recipient") is not None
    ):
        raise FamilySourcekitError("FAMILY_DISABLED_POLICY_REQUIRED")
    receivers = policy.get("suggested_receivers")
    if (
        type(receivers) is not list or not receivers
        or len(receivers) > 16
        or any(type(to) is not str or to == role
               or to not in (*EXPECTED_ROLES, "evidence-finder")
               for to in receivers)
        or len(set(receivers)) != len(receivers)
    ):
        raise FamilySourcekitError("UNSAFE_FAMILY_RECEIVER_POLICY")


def _source_members(root: Path) -> tuple[dict[str, bytes], tuple[str, ...]]:
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise FamilySourcekitError("INVALID_SOURCE_ROOT")
    members = {}
    for name, digest in SOURCE_PINS.items():
        data = _read_reviewed(root, name)
        if _sha(data) != digest:
            raise FamilySourcekitError("SOURCE_PIN_MISMATCH:" + name)
        members[name] = data
    roles = _validate_catalog(members)
    for role in roles:
        name = f"presets/{role}/preset.json"
        data = _read_reviewed(root, name)
        _validate_profile(role, data)
        if _sha(data) != ROLE_PINS[role]:
            raise FamilySourcekitError("PROFILE_SOURCE_PIN_MISMATCH:" + role)
        members[name] = data
    members["START_HERE.md"] = START_HERE.encode("utf-8")
    if len(members) + 1 > MAX_MEMBERS or sum(map(len, members.values())) > MAX_UNPACKED:
        raise FamilySourcekitError("FAMILY_KIT_RESOURCE_LIMIT")
    return members, roles


def _source_manifest(members: dict[str, bytes], roles: tuple[str, ...]) -> dict:
    return {
        "schema": SCHEMA,
        "source_base_commit": SOURCE_BASE_COMMIT,
        "scope": SCOPE,
        "role_ids": list(roles),
        "files_sha256": {name: _sha(raw) for name, raw in sorted(members.items())},
        "source_pins": dict(sorted(SOURCE_PINS.items())),
        "role_profile_pins": dict(sorted(ROLE_PINS.items())),
        **{flag: False for flag in FALSE_FLAGS},
    }


def _validate_member_name(name: str) -> None:
    if (
        type(name) is not str or "\\" in name or not name
        or name.startswith("/") or ":" in name or "\x00" in name
        or any(part in ("", ".", "..") for part in PurePosixPath(name).parts)
        or name != PurePosixPath(name).as_posix()
    ):
        raise FamilySourcekitError("ARCHIVE_MEMBER_UNSAFE")


def verify_family_sourcekit(archive: Path, expected_sha256: str) -> dict:
    """Read-only verification; external ZIP hash mandatory. No extraction."""
    if type(expected_sha256) is not str or HEX.fullmatch(expected_sha256) is None:
        raise FamilySourcekitError("EXTERNAL_ZIP_SHA256_REQUIRED")
    archive = Path(archive)
    if archive.is_symlink() or not archive.is_file() or archive.stat().st_size > MAX_ARCHIVE:
        raise FamilySourcekitError("ARCHIVE_MISSING_UNSAFE_OR_OVERSIZED")
    if _sha(archive.read_bytes()) != expected_sha256:
        raise FamilySourcekitError("ZIP_SHA256_MISMATCH")
    try:
        with zipfile.ZipFile(archive) as reader:
            infos = reader.infolist()
            names = [info.filename for info in infos]
            if len(names) > MAX_MEMBERS or len(names) != len(set(names)):
                raise FamilySourcekitError("ARCHIVE_MEMBERS_DUPLICATED_OR_EXCESSIVE")
            # Refuse traversal or absolute members before classifying an
            # accompanying order drift; path safety is the primary failure.
            for name in names:
                _validate_member_name(name)
            if names != sorted(names):
                raise FamilySourcekitError("ARCHIVE_ORDER_CHANGED")
            total = 0
            contents = {}
            for info in infos:
                _validate_member_name(info.filename)
                mode = (info.external_attr >> 16) & 0o170000
                if (
                    info.is_dir() or mode not in (0, stat.S_IFREG)
                    or info.flag_bits & 1 or info.compress_type != zipfile.ZIP_DEFLATED
                    or info.file_size > MAX_FILE
                ):
                    raise FamilySourcekitError("ARCHIVE_MEMBER_UNSAFE")
                total += info.file_size
                if total > MAX_UNPACKED:
                    raise FamilySourcekitError("ARCHIVE_RESOURCE_LIMIT")
                with reader.open(info) as fh:
                    raw = fh.read(MAX_FILE + 1)
                    if len(raw) != info.file_size or len(raw) > MAX_FILE:
                        raise FamilySourcekitError("ARCHIVE_MEMBER_SIZE_MISMATCH")
                    contents[info.filename] = raw
            if MANIFEST not in contents:
                raise FamilySourcekitError("KIT_MANIFEST_MISSING")
            def no_duplicate_keys(pairs):
                result = {}
                for key, value in pairs:
                    if key in result:
                        raise ValueError("DUPLICATE_JSON_FIELD")
                    result[key] = value
                return result

            def refuse_nonfinite(value):
                raise ValueError("NONFINITE_JSON_VALUE")

            manifest = json.loads(
                contents.pop(MANIFEST).decode("utf-8"),
                object_pairs_hook=no_duplicate_keys,
                parse_constant=refuse_nonfinite,
            )
            if (
                type(manifest) is not dict or manifest.get("schema") != SCHEMA
                or manifest.get("source_base_commit") != SOURCE_BASE_COMMIT
                or "source_commit" in manifest
                or manifest.get("scope") != SCOPE
                or manifest.get("role_ids") != list(EXPECTED_ROLES)
                or manifest.get("source_pins") != SOURCE_PINS
                or manifest.get("role_profile_pins") != ROLE_PINS
                or any(manifest.get(flag) is not False for flag in FALSE_FLAGS)
            ):
                raise FamilySourcekitError("KIT_MANIFEST_INVALID")
            expected_members = set(SOURCE_PINS) | {
                f"presets/{role}/preset.json" for role in EXPECTED_ROLES
            } | {"START_HERE.md"}
            if (
                set(contents) != expected_members
                or manifest.get("files_sha256") != {
                    name: _sha(data) for name, data in sorted(contents.items())
                }
            ):
                raise FamilySourcekitError("KIT_MEMBER_MANIFEST_MISMATCH")
            for name, digest in SOURCE_PINS.items():
                if _sha(contents[name]) != digest:
                    raise FamilySourcekitError("SOURCE_PIN_MISMATCH:" + name)
            _validate_catalog(contents)
            for role in EXPECTED_ROLES:
                data = contents[f"presets/{role}/preset.json"]
                _validate_profile(role, data)
                if _sha(data) != ROLE_PINS[role]:
                    raise FamilySourcekitError("PROFILE_SOURCE_PIN_MISMATCH:" + role)
    except (zipfile.BadZipFile, RuntimeError, OSError, UnicodeError, KeyError, ValueError) as exc:
        if isinstance(exc, FamilySourcekitError):
            raise
        raise FamilySourcekitError("KIT_ARCHIVE_INVALID") from exc
    return {
        "status": "LOCAL_FAMILY_LINK_KIT_VERIFIED",
        "sha256": expected_sha256,
        "members": len(names),
        "source_roles": len(EXPECTED_ROLES),
        "native_installed": False,
        "effect_authorized": False,
        "runtime_verified": False,
    }


def export_family_sourcekit(root: Path, destination: Path) -> dict:
    """Create a deterministic ZIP in an existing external directory. Never overwrite."""
    root = Path(root)
    destination = Path(destination)
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("FAMILY_KIT_DESTINATION_EXISTS")
    if not destination.parent.is_dir() or destination.parent.is_symlink():
        raise FileNotFoundError("FAMILY_KIT_PARENT_REQUIRED")
    if destination.resolve().is_relative_to(root.resolve()):
        raise FamilySourcekitError("KIT_OUTPUT_MUST_BE_OUTSIDE_SOURCE")
    members, roles = _source_members(root)
    members[MANIFEST] = _json(_source_manifest(members, roles))
    if len(members) > MAX_MEMBERS or sum(map(len, members.values())) > MAX_UNPACKED:
        raise FamilySourcekitError("FAMILY_KIT_RESOURCE_LIMIT")
    # Acquire destination exclusively before writing. On failure remove only
    # the newly created output from this call.
    created = False
    try:
        with destination.open("xb") as out:
            created = True
            with zipfile.ZipFile(out, "w") as writer:
                for name, data in sorted(members.items()):
                    _validate_member_name(name)
                    info = zipfile.ZipInfo(name, date_time=(2026, 11, 16, 0, 0, 0))
                    info.create_system = 3
                    info.external_attr = 0o100644 << 16
                    info.compress_type = zipfile.ZIP_DEFLATED
                    writer.writestr(info, data)
        if destination.stat().st_size > MAX_ARCHIVE:
            raise FamilySourcekitError("FAMILY_KIT_ZIP_TOO_LARGE")
        digest = _sha(destination.read_bytes())
        verify_family_sourcekit(destination, digest)
    except Exception:
        if created and destination.is_file() and not destination.is_symlink():
            destination.unlink()
        raise
    return {
        "status": "LOCAL_FAMILY_LINK_KIT_EXPORTED",
        "sha256": digest,
        "bytes": destination.stat().st_size,
        "source_roles": len(roles),
        "members": len(members),
        "source_base_commit": SOURCE_BASE_COMMIT,
        "native_installed": False,
        "effect_authorized": False,
        "public_release_published": False,
    }
