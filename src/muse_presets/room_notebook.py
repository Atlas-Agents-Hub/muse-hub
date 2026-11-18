"""Store persistent room notes with revision checks and archive recovery."""
from __future__ import annotations

from hashlib import sha256
import json
import re

from .personal_companion import PersonalCompanion

SCHEMA = "muse-hub/room-notebook-snapshot/v1"
ROOMS = ("focus", "notebook", "garden", "arcade", "studio")
_NOTE_ID = re.compile(r"[A-Za-z][A-Za-z0-9-]{0,39}\Z")
_MAX_REV = 1_000_000
_MAX_NOTES = 256


def _digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    return sha256(raw.encode("utf-8")).hexdigest()


def _room(room: str) -> str:
    if type(room) is not str or room not in ROOMS:
        raise ValueError("INVALID_ROOM")
    return room


def _key(room: str, note_id: str) -> str:
    _room(room)
    if type(note_id) is not str or not _NOTE_ID.fullmatch(note_id):
        raise ValueError("INVALID_ROOM_NOTE_ID")
    return room + "__" + note_id


def _split(key: str) -> tuple[str, str]:
    if type(key) is not str:
        raise ValueError("ROOM_NOTE_NOT_SCOPED")
    parts = key.split("__", 1)
    if len(parts) != 2:
        raise ValueError("ROOM_NOTE_NOT_SCOPED")
    if _key(parts[0], parts[1]) != key:
        raise ValueError("ROOM_NOTE_NOT_SCOPED")
    return parts[0], parts[1]


def _scope_hash(scope: object) -> str:
    # This is a scope-binding checksum. A caller-provided scope is not proof
    # of an authenticated host, so it can never establish owner identity.
    return _digest({
        "domain": "muse-hub/room-notebook/scope/v1",
        "owner": scope.owner_id,
        "space": scope.space_id,
    })


class RoomNotebook:
    def __init__(self, store: PersonalCompanion):
        if type(store) is not PersonalCompanion:
            raise ValueError("PERSONAL_COMPANION_REQUIRED")
        self._store = store

    def put(self, room: str, note_id: str, text: str, *, expected_revision: int = 0) -> dict:
        key = _key(room, note_id)
        row = self._store.put_note(key, text, expected_revision=expected_revision)
        return dict(row, room_id=room, note_id=note_id)

    def note(self, room: str, note_id: str) -> dict | None:
        row = self._store.note(_key(room, note_id))
        return dict(row, room_id=room, note_id=note_id) if row else None

    def notes(self, room: str) -> list[dict]:
        prefix = _room(room) + "__"
        return [
            dict(row, room_id=room, note_id=row["note_id"][len(prefix):])
            for row in self._store.notes()
            if row["note_id"].startswith(prefix)
        ]

    def forget(self, room: str, note_id: str, *, expected_revision: int) -> dict:
        row = self._store.forget_note(_key(room, note_id), expected_revision=expected_revision)
        return dict(row, room_id=room, note_id=note_id)

    def snapshot(self) -> dict:
        scope = self._store._scope(True)
        notes = []
        for row in self._store.notes():
            room_id, note_id = _split(row["note_id"])
            notes.append({
                "room_id": room_id,
                "note_id": note_id,
                "text": row["text"],
                "revision": row["revision"],
            })
        notes.sort(key=lambda x: (x["room_id"], x["note_id"]))
        if len(notes) > _MAX_NOTES:
            raise ValueError("NOTE_LIMIT")
        return {
            "schema": SCHEMA,
            "scope_fingerprint": _scope_hash(scope),
            "notes": notes,
            "content_sha256": _digest(notes),
            "provider_authenticated": False,
            "native_muse_installed": False,
            "notification_sent": False,
            "scope": "LOCAL_SQLITE_OWNER_SPACE_ONLY",
        }

    def restore(self, snapshot: dict) -> dict:
        scope = self._store._scope(True)
        if type(snapshot) is not dict or set(snapshot) != {
            "schema", "scope_fingerprint", "notes", "content_sha256",
            "provider_authenticated", "native_muse_installed",
            "notification_sent", "scope",
        }:
            raise ValueError("INVALID_NOTEBOOK_SNAPSHOT")
        if (snapshot["schema"] != SCHEMA or
            snapshot["scope"] != "LOCAL_SQLITE_OWNER_SPACE_ONLY" or
            any(snapshot[key] is not False for key in (
                "provider_authenticated", "native_muse_installed", "notification_sent",
            ))):
            raise ValueError("UNTRUSTED_NOTEBOOK_AUTHORITY")
        if snapshot["scope_fingerprint"] != _scope_hash(scope):
            raise ValueError("SCOPE_MISMATCH")
        rows = snapshot["notes"]
        if type(rows) is not list or len(rows) > _MAX_NOTES:
            raise ValueError("INVALID_NOTEBOOK_ROWS")
        if snapshot["content_sha256"] != _digest(rows):
            raise ValueError("SNAPSHOT_CONTENT_MISMATCH")
        seen = set()
        normalized = []
        for row in rows:
            if type(row) is not dict or set(row) != {"room_id","note_id","text","revision"}:
                raise ValueError("INVALID_NOTEBOOK_RECORD")
            key = _key(row["room_id"], row["note_id"])
            if key in seen:
                raise ValueError("DUPLICATE_NOTE_ID")
            seen.add(key)
            if type(row["revision"]) is not int or not (1 <= row["revision"] <= _MAX_REV):
                raise ValueError("INVALID_NOTE_REVISION")
            normalized.append({
                "note_id": key, "text": row["text"], "revision": row["revision"],
            })
        # Atomic new-store restore delegates write ownership to the existing
        # PersonalCompanion transaction method. It refuses any prior notes,
        # even deleted tombstones, so it never rewrites original user history.
        result = self._store.import_frozen_notes(normalized)
        return {
            "schema": SCHEMA,
            "restored": result["count"],
            "scope": "LOCAL_SQLITE_OWNER_SPACE_ONLY",
            "provider_authenticated": False,
            "native_muse_installed": False,
        }
