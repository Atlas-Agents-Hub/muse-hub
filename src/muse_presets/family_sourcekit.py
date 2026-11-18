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
    "presets/catalog.json": 'd6fc62647cbf08deed286677b4d8b9852001cd2e2fbd9330506f816f7b118bb3',
    "src/muse_presets/__init__.py": '112ef2f80840b5bddecb2e3dec6f6ceca6cc8c3b5862c28e6dad31b4e86d70bd',
    "src/muse_presets/catalog.py": '685a1c393f8581a4741e40da47fa31accd3577a94a0185a5ca5008e4b690ca48',
    "src/muse_presets/family.py": "af043cc6edc7e0670d2ec098bdd94f7064f4998d58e784f5669cc740bb23780b",
    "src/muse_presets/family_envelope.py": '02fd3b8d6d811bfa21554b09702807f6cf39ec05ed869bb7f672b6e367e5083b',
    "src/muse_presets/neutrality.py": '38119ac763825c5c4c3a313b20c8122d787b06d4ebcd30aec015cdcb8bff5e8c',
    "src/muse_presets/playbooks.py": 'c3abac0812efe26fbf34698e24fcdc18ebbd0d756bdc771092353b1859e04774',
}
# Exact accepted role bytes, in addition to disabled-by-default policy shape.
# A silent title/description edit must not alter the kit without a new review.
ROLE_PINS = {
    "coordinator": '8de5decae4de3f106393dae46a447cccbb062ea94a00a20345026eefc285602c',
    "software-engineer": '6d0c183e6a38048feeb195c40efc5a3177b87f07b9e2e78679b99993d49e72c6',
    "model-builder": 'a7282f147723f9d7d92c2161fdb57750b79a16f732f5aefbc6206a1aa36fc9a4',
    "research-evaluator": '44b71797e388adab8dc25ecbddd034a4a6424f901e38a55628db7a22242850fd',
    "creative-studio": 'c88aebc47eb4cdd88622a7335bcefa836a279d4f6928a96e91fc289c65ca16f6',
    "adversarial-verifier": '9d8f6fba05d2398d10b2d09cf47dd8ad06f88168a399ddc5ea0c6711c6cdc732',
    "personal-companion": '0e1c62bd9fdb969040ffed6bdb3919e448eee9335500988dee7b85a04714198d',
    "garden-companion": 'a17cebd32f4b91bf063fd3dee37349da3d1b44f06f9f42f971d26dd108d8ad8a',
    "learning-coach": 'ee6abb91860348085be2def86b224560148b349a804542223998fd9a6299c836',
    "claims-adjudicator": '256b02fa961aa27561fa1a252c36cc023cc297825d65d485fbdb8c1b3bff3a29',
    "reverse-engineering-researcher": 'f4b34287ed03dcfd1a59cdb1caa7ebb98e8ac096efade5d6ef15cca641c0e3ab',
    "data-engineering-architect": '711af6cc6bba03be6891e79af679fda0411fee6d4e84d4cc953afc74b0c7d5e0',
    "infrastructure-reliability-engineer": '2a1ea9f2e4097a27f257fe036c28267623cb8dde63f46b601e0d172d4e3f11e7',
    "automation-engineer": 'dee0d21cc084530b7273505dad496d2fcb2d43b098a0bab6b1770df5a6cfadcc',
    "product-interface-designer": 'eda17bdfc2af0814f86546e11bc62bc1627ca2889ba397fe53d432f3552cc7d4',
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
