"""Deterministic, source-pinned Family Link OFFLINE handoff kit (H12).

Bundles the existing local envelope/role-policy implementation verbatim,
not a replacement transport or actor. No credentials, native permissions,
background workers or cross-account execution.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

SCHEMA = "muse-hub/family-link-offline-kit/v1"
SOURCE_BASE_COMMIT = "7069f0621da0d0ca7f87b1661872e4dbfa805d37"
SCOPE = "SOURCE_ONLY_OFFLINE_TWO_PROCESS_NOT_DELIVERED"
MANIFEST = "SOURCEKIT_MANIFEST.json"
MAX_MEMBERS = 40
MAX_FILE = 128_000
MAX_UNPACKED = 1_000_000
MAX_ARCHIVE = 2_000_000
HEX = re.compile(r"[a-f0-9]{64}\Z")
ROLE = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z")

# Frozen original modules and catalog from the accepted post-PR23 source.
# An authorized future update must review and revise the pins deliberately.
SOURCE_PINS = {
    "LICENSE": "af30e586ca6503924d5e4d99894ec6c7ce61ba77a55ba081b7a129d33f43fddf",
    "examples/family_offline_handoff_demo.py": "cd830ada0c87a72586ce5265b52e748bee89c14916bb3f224a4b6e8805f30a43",
    "presets/catalog.json": "f3c186454e722099255bdfc4ef08fceb5756b418a45599f8ba5e3b5e341e8cc1",
    "src/muse_presets/__init__.py": "40efad1b553ff0ef0c8f27b3d91ae97e6a933693040cdc9bbc648f100719c3bb",
    "src/muse_presets/catalog.py": "8d2f49924dbdf538c61c5b3fc25d588812309ec4901d3f289ae0f387ca76c445",
    "src/muse_presets/family.py": "af043cc6edc7e0670d2ec098bdd94f7064f4998d58e784f5669cc740bb23780b",
    "src/muse_presets/family_envelope.py": "ac0aaa563db8e26ebf0fe023970130fba491872984ec3a6bdd2e168f3f901efb",
    "src/muse_presets/neutrality.py": "c22e459f40662c35998a203750e0991f7505c4c908f6c138d1cd76cfae97a60c",
    "src/muse_presets/playbooks.py": "cc368d9a6f9edd9a7893dd1f4a9493d5e2285f5977a6023be5a4daaadc81ce09",
}
# Exact accepted role bytes, in addition to disabled-by-default policy shape.
# A silent title/description edit must not alter the kit without a new review.
ROLE_PINS = {
    "coordinator": "8ccb1cfb93d1c96241380d986d98bdf3c78cb48c5fcc789a38bb8d2e99e1edca",
    "software-engineer": "ec17acb58001b70a1ba3a0e7bedf66dc98a53a53fab923712a83d66c67cd17db",
    "model-builder": "2633fa6710c913af8a6d3d1314aa087f12774bf86d407d15a24ab52cccfd32cd",
    "research-evaluator": "418b0ba914eba8adaa05379124e73e692b786ba6c27fd63bd4e4effc3387e6de",
    "creative-studio": "d6b89a7f0851258af12afcbc224f822e4b0ec76e26e58ee993c789ee4b4ccd48",
    "adversarial-verifier": "319d0dcd9651c8735bc98d4309371a91dd70da2ed539ad3e9075f617f6f71fbe",
    "personal-companion": "c6ffcc014a50319e16ccef442b389d1feeffdfefed25a19e3dc11a0b4b1a317f",
    "garden-companion": "8fa1478f149bc1a7a9cd7690d370266f245f982aeff5fd9c4bd018718784c7fe",
    "learning-coach": "11ac7532685fdf00e037f69401bf9b5e72a87aec16b31b557335e9313b1a0c84",
    "claims-adjudicator": "0d9205ec0e107baf4600106d8b0815a9e2ab8ce1923cf869408ada75ececaca7",
    "reverse-engineering-researcher": "a8d0933de95103e512339aefed4a1fc4f18c1c73a4d0d49c7c14ba00759ebdf1",
    "data-engineering-architect": "309a87c089f7df118e67f5534c7f4d836d7aa2cae1deb2529a4503eb839f408b",
    "infrastructure-reliability-engineer": "5f90c6933687e4fdc40544a45c2946dded8caad6588308a9377e121eab2ff3b6",
    "automation-engineer": "af24ba98e7a99b41dad430273bed1f87b575319590aa88fab06a8d1ec0e6b1af",
    "product-interface-designer": "45127a557bcd56d2a6856a37bf043cfcb0e9e49947913b6b0507cc3de9db3622",
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
START_HERE = """# Family Link — tested offline source handoff (H12)

This archive contains the ORIGINAL source-only Family Link role policy and
bounded metadata envelope, plus the existing two-process fictional demo.
It cannot connect Muse assistants, discover accounts, grant permissions,
send messages, install a native agent, or provide a durable replay ledger.

Requires Python 3.12+ with no dependencies or paid APIs. Verify the archive
SHA-256 from a trusted external source before extracting, then inspect the
included source. The embedded manifest is a tamper check, not a signature.

On macOS/Linux, from the extracted root:

  PYTHONPATH=src python -B examples/family_offline_handoff_demo.py

On Windows PowerShell, from the extracted root:

  $env:PYTHONPATH="src"
  python -B examples/family_offline_handoff_demo.py

Expected: LOCAL_HANDOFF_REVIEW_ONLY_NOT_DELIVERED, separate_process_verified
and replayed_id_refused true, effect_authorized and recipient_authenticated
false. The demo writes only temporary fictional records and cleans them up.

The 15 included profiles have Family Link disabled, transport unbound,
no trusted signer and no native recipient. The source modules are preserved
byte-for-byte from pinned Muse Hub commit 7069f062. Nothing here represents
cross-account acceptance or authorizes a live action. The private donor
TaskGuard/retention P1 remains an independent production hold.
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
        or profile.get("maturity") != "SOURCE_TEMPLATE_ONLY"
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
        "source_commit": SOURCE_BASE_COMMIT,
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
                or manifest.get("source_commit") != SOURCE_BASE_COMMIT
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
        "source_commit": SOURCE_BASE_COMMIT,
        "native_installed": False,
        "effect_authorized": False,
        "public_release_published": False,
    }
