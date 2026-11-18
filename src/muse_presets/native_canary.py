"""Create and verify disposable host-compatibility test packages."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import secrets
from typing import Any

from .catalog import ROOT, load_preset, load_registry
from .native_skill_binding import _unsafe_source_path

HOST_KINDS = frozenset({"personal-hatch", "muse-code"})
CHALLENGE = re.compile(r"^[a-f0-9]{32}$")
SCHEMA = "r32/generic-native-canary-v1"
RECEIPT_SCHEMA = "r32/generic-native-canary-receipt-v1"
FIXTURE_SCHEMA = "r32/native-fixture-events-v1"
POLICY_FILES = frozenset({"GENERIC_CANARY.json", "NATIVE_HANDOFF.md", "SOURCE_RECEIPT.json"})
ROLE_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


class NativeHostUnavailable(RuntimeError):
    """The selected host needs a configured provider connection."""


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _serialized(record: dict) -> bytes:
    return (json.dumps(record, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def _no_duplicate_json(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("DUPLICATE_JSON_KEY")
        out[key] = value
    return out


def _reject_constant(_value):
    raise ValueError("NONSTANDARD_JSON_CONSTANT")


def _role_sources(role_id: str) -> dict[str, bytes]:
    if type(role_id) is not str or ROLE_PATTERN.fullmatch(role_id) is None:
        raise ValueError("INVALID_GENERIC_ROLE")
    if role_id not in load_registry()["presets"]:
        raise ValueError("UNKNOWN_GENERIC_ROLE")
    config = load_preset(role_id)
    if (config.get("id") != role_id or
        config.get("native_muse_status") != "UNBOUND" or
        config.get("maturity") != "PROFILE_TEMPLATE"):
        raise ValueError("GENERIC_SOURCE_NOT_DEFAULT_DENIED")
    files = {}
    for name in ("preset.json", "playbook.json"):
        p = ROOT / "presets" / role_id / name
        if _unsafe_source_path(p) or not p.is_file() or p.stat().st_size > 131072:
            raise ValueError("UNTRUSTED_GENERIC_SOURCE")
        files[name] = p.read_bytes()
        if len(files[name]) > 131072:
            raise ValueError("UNTRUSTED_GENERIC_SOURCE")
    return files


def make_canary(role_id: str, host_kind: str, *, challenge: str | None = None) -> dict:
    """Build a disposable compatibility test with the current profile hashes."""
    if host_kind not in HOST_KINDS:
        raise ValueError("UNKNOWN_HOST_PROFILE")
    sources = _role_sources(role_id)
    if challenge is None:
        challenge = secrets.token_hex(16)
    if type(challenge) is not str or CHALLENGE.fullmatch(challenge) is None:
        raise ValueError("INVALID_DISPOSABLE_CHALLENGE")
    return {
        "schema": SCHEMA,
        "role_id": role_id,
        "host_kind": host_kind,
        "skill_id": "generic_" + role_id.replace("-", "_") + "_canary",
        "skill_id_is_registered": False,
        "disposable_only": True,
        "challenge": challenge,
        "source_pins": {key: _sha(raw) for key, raw in sources.items()},
        "source_grade": "PACKAGE_FILES",
        "native_acceptance": "NOT_RUN",
        "provider_session_id": None,
        "owner_grant_id": None,
        "native_authenticated": False,
        "model_invoked": False,
        "native_effects_enabled": False,
        "native_recipient_readback": False,
        "wrong_owner_provider_denial": False,
    }


def unsupported_native_invoke(canary: dict) -> None:
    """Never fall back to a shell, arbitrary HTTP, personal VM or Muse Code CLI."""
    if type(canary) is not dict or canary.get("schema") != SCHEMA:
        raise ValueError("INVALID_CANARY")
    raise NativeHostUnavailable("PERSONAL_HOST_AUTHENTICATED_PORT_NOT_CONNECTED")


def _handoff(canary: dict) -> bytes:
    role, host = canary["role_id"], canary["host_kind"]
    return (
        "# Host compatibility check\n\n"
        f"Specialist: `{role}`. Host: `{host}`.\n\n"
        f"Use `{canary['skill_id']}` as the test skill identifier.\n"
        "Keep the challenge in GENERIC_CANARY.json with the test results so each\n"
        "invocation can be matched to its response.\n\n"
        "1. Connect the intended account through the host's documented interface.\n"
        "2. Grant the temporary test scope and confirm the available skill.\n"
        "3. Invoke the skill and capture the returned identifiers and result.\n"
        "4. Check access restrictions using a separately authorized test account.\n"
        "5. Read the result from the intended recipient and compare the challenge.\n\n"
        "Use the setup and authentication procedure for the selected host. Keep\n"
        "existing profile, memory, and catalog files intact during the check.\n"
    ).encode("utf-8")


def _admitted_destination(dest: Path) -> None:
    if not dest.is_absolute() or _unsafe_source_path(dest):
        raise ValueError("UNSAFE_DESTINATION_PATH")
    if dest.exists() or dest.is_symlink():
        raise FileExistsError("DESTINATION_EXISTS")
    if not dest.parent.is_dir():
        raise FileNotFoundError("PARENT_DIRECTORY_REQUIRED")


def _expected_bytes(canary: dict) -> dict[str, bytes]:
    policy = {"GENERIC_CANARY.json": _serialized(canary),
              "NATIVE_HANDOFF.md": _handoff(canary)}
    policy["SOURCE_RECEIPT.json"] = _serialized({
        "schema": RECEIPT_SCHEMA,
        "role_id": canary["role_id"],
        "host_kind": canary["host_kind"],
        "policy_sha256": {name: _sha(content) for name, content in sorted(policy.items())},
        "provenance": "LOCAL_TEST_FIXTURE_NOT_NATIVE_AUTHORITY",
        "native_installed": False,
        "provider_authenticated": False,
        "external_effect_authorized": False,
    })
    return policy


def stage_canary(destination: Path, role_id: str, host_kind: str) -> dict:
    """Create a complete host test package in a new directory."""
    canary = make_canary(role_id, host_kind)
    dest = Path(destination)
    _admitted_destination(dest)
    contents = _expected_bytes(canary)
    dest.mkdir(exist_ok=False)
    created: list[Path] = []
    try:
        for name, raw in contents.items():
            path = dest / name
            with path.open("xb") as handle:
                handle.write(raw)
            created.append(path)
    except Exception:
        for path in reversed(created):
            path.unlink(missing_ok=True)
        dest.rmdir()
        raise
    return {
        "status": "HOST_PACKAGE_CREATED",
        "role_id": role_id,
        "host_kind": host_kind,
        "destination": str(dest),
        "native_installed": False,
        "external_effect_authorized": False,
    }


def inspect_canary(destination: Path) -> dict:
    """Read-only, strict closed-tree and current-source comparison."""
    dest = Path(destination)
    rejected = {"status": "REVIEW_REQUIRED", "native_installed": False,
                "external_effect_authorized": False}
    if _unsafe_source_path(dest) or not dest.is_dir():
        return rejected
    try:
        children = list(dest.iterdir())
        if {p.name for p in children} != POLICY_FILES or any(
            p.is_symlink() or not p.is_file() or p.stat().st_size > 131072 for p in children
        ):
            return rejected
        raw = (dest / "GENERIC_CANARY.json").read_bytes()
        data = json.loads(raw, object_pairs_hook=_no_duplicate_json, parse_constant=_reject_constant)
        if type(data) is not dict:
            return rejected
        expected = make_canary(data["role_id"], data["host_kind"], challenge=data["challenge"])
        if data != expected:
            return rejected
        expected_files = _expected_bytes(expected)
        if any((dest / name).read_bytes() != contents for name, contents in expected_files.items()):
            return rejected
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        return rejected
    return {
        "status": "FILES_VERIFIED",
        "role_id": data["role_id"],
        "host_kind": data["host_kind"],
        "native_installed": False,
        "external_effect_authorized": False,
    }


def assess_fixture_transcript(canary: dict, transcript: dict) -> dict:
    """Check correlation of completely UNTRUSTED fixture events.

    Even a perfect transcript can NEVER grant native identity or count as an
    authenticated action. Provider readback must come via a real host channel.
    """
    result = {
        "status": "FIXTURE_REJECTED",
        "evidence_grade": "UNATTESTED_FIXTURE",
        "native_authenticated": False,
        "native_tool_invoked": False,
        "recipient_readback_verified": False,
        "wrong_owner_denied_by_provider": False,
        "external_effect_authorized": False,
    }
    if type(canary) is not dict or type(transcript) is not dict:
        return result
    if (canary.get("schema") != SCHEMA or
        transcript.get("schema") != FIXTURE_SCHEMA or
        transcript.get("host_kind") != canary.get("host_kind") or
        set(transcript) != {"schema", "host_kind", "discovery", "invocation",
                            "recipient_readback", "wrong_owner_refusal"}):
        return result
    expected = {
        "discovery": {"event_id", "owner_principal", "session_id", "skill_id", "status"},
        "invocation": {"event_id", "owner_principal", "session_id",
                       "skill_id", "challenge", "status"},
        "recipient_readback": {"event_id", "invocation_id",
                               "owner_principal", "challenge", "status"},
        "wrong_owner_refusal": {"event_id", "owner_principal", "skill_id", "status"},
    }
    try:
        d, i, b, w = (transcript[name] for name in expected)
        for name, fields in expected.items():
            row = transcript[name]
            if (type(row) is not dict or set(row) != fields or any(
                type(value) is not str or not 1 <= len(value) <= 256
                for value in row.values()
            )):
                return result
        if len({d["event_id"], i["event_id"], b["event_id"], w["event_id"]}) != 4:
            return result
        if not (d["status"] == "found" and i["status"] == "completed" and
                b["status"] == "matched" and w["status"] == "denied"):
            return result
        if not (d["skill_id"] == i["skill_id"] == w["skill_id"] == canary["skill_id"]):
            return result
        if not (d["owner_principal"] == i["owner_principal"] == b["owner_principal"]):
            return result
        if w["owner_principal"] == d["owner_principal"]:
            return result
        if d["session_id"] != i["session_id"]:
            return result
        if b["invocation_id"] != i["event_id"]:
            return result
        if i["challenge"] != b["challenge"] or i["challenge"] != canary["challenge"]:
            return result
    except (KeyError, TypeError):
        return result
    result["status"] = "FIXTURE_CONSISTENT_ONLY"
    return result
