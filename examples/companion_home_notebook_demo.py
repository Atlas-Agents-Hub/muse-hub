"""Save room notes, reopen the database, and restore a notebook backup."""
from __future__ import annotations
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from muse_presets.personal_companion import CompanionScope, PersonalCompanion
from muse_presets.room_notebook import RoomNotebook


def check(ok: bool, reason: str) -> None:
    if not ok: raise ValueError(reason)


def main() -> int:
    original = CompanionScope("fictional-owner", "fictional-home", "fictional-owner", True)
    current = [original]
    with TemporaryDirectory(prefix="muse-room-notebook-") as folder:
        home = Path(folder).resolve()
        src = home / "original.sqlite3"
        restored = home / "new-store.sqlite3"
        with PersonalCompanion(src, authority=lambda:current[0]) as store:
            book = RoomNotebook(store)
            check(book.notes("garden")==[], "GARDEN_NOT_EMPTY")
            one = book.put("garden", "idea", "A quiet walk in the afternoon.")
            two = book.put("garden", "idea", "A quiet walk before dinner.",
                           expected_revision=one["revision"])
            book.put("focus","today","Review the next step.")
            check(two["revision"]==2, "REVISION_DID_NOT_INCREMENT")
            check(book.notes("studio")==[], "ROOM_ISOLATION_FAILED")
            snapshot = book.snapshot()
            check(len(snapshot["notes"])==2, "SNAPSHOT_COUNT")
        with PersonalCompanion(src, authority=lambda:current[0]) as reopened:
            check(RoomNotebook(reopened).notes("garden")[0]["revision"]==2,
                  "ORIGINAL_REOPEN_FAILED")
        with PersonalCompanion(restored, authority=lambda:current[0]) as dest:
            result = RoomNotebook(dest).restore(snapshot)
            check(result["restored"]==2, "RESTORE_COUNT")
            check(RoomNotebook(dest).notes("garden")[0]["revision"]==2,
                  "RESTORE_REVISION_LOST")
            try: RoomNotebook(dest).restore(snapshot)
            except ValueError as exc: check("RESTORE_TARGET_NOT_EMPTY" in str(exc),
                                          "WRONG_REPEAT_REFUSAL")
            else: raise ValueError("REPEATED_RESTORE_OVERWROTE_DATA")
            current[0] = CompanionScope("different-owner","fictional-home","different-owner",True)
            check(dest.notes()==[], "OWNER_SPACE_LEAK")
            try: RoomNotebook(dest).restore(snapshot)
            except ValueError as exc: check("SCOPE_MISMATCH" in str(exc), "WRONG_SCOPE_REFUSAL")
            else: raise ValueError("WRONG_SCOPE_RESTORE_ACCEPTED")
    print(json.dumps({
        "status": "ROOM_NOTEBOOK_RESTORE_PASSED",
        "rooms": 5,
        "notes_restored": 2,
        "revision_preserved": True,
        "reopen_verified": True,
        "duplicate_restore_refused": True,
        "cross_owner_scope_refused": True,
    },sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
