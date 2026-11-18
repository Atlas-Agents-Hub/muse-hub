"""H14-H17 neutral Companion Home source, native-safety, and recovery gates."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from muse_presets.personal_companion import CompanionScope, PersonalCompanion
from muse_presets.public_export import select_public_files

ROOT=Path(__file__).resolve().parents[1]
HOME=ROOT/"examples/companion_home"
IDS=("focus","notebook","garden","arcade","studio")


class CompanionHomeContractTests(unittest.TestCase):
    def test_five_configurable_rooms_and_no_room_chat_transport(self):
        data=json.loads((HOME/"rooms.json").read_text(encoding="utf-8"))
        self.assertEqual(data["schema"],"muse-hub/neutral-companion-home/v1")
        rooms=data["rooms"]
        self.assertEqual(tuple(x["id"] for x in rooms),IDS)
        self.assertEqual(len({x["label"] for x in rooms}),5)
        for row in rooms:
            self.assertIn(row["theme"],("signal","ivory","mint","lavender","coral"))
            self.assertTrue(row["feature_ids"])
            self.assertTrue(row["description"])
        self.assertFalse(data["native_muse_installed"])
        self.assertFalse(data["room_local_chat"])
        self.assertTrue(data["global_assistant_external"])
        js=(HOME/"rooms.js").read_text(encoding="utf-8")
        prefix="window.MUSE_HOME_CONFIG = Object.freeze("
        self.assertTrue(js.startswith(prefix))
        self.assertTrue(js.endswith(");\n"))
        self.assertEqual(json.loads(js[len(prefix):-3]),data)

    def test_html_csp_and_five_real_room_surfaces(self):
        text=(HOME/"index.html").read_text(encoding="utf-8")
        for token in ("Content-Security-Policy","connect-src 'none'","script-src 'self'",
                      "style-src 'self'","aria-label=\"Room navigation\"","id=\"room-nav\"",
                      "id=\"room-panel\"","id=\"arcade\"","id=\"studio\"",
                      "id=\"notebook\"","data-action=\"motion\""):
            self.assertIn(token,text)
        for path in ("style.css","rooms.js","home.js"):
            self.assertTrue((HOME/path).is_file(),path)
            self.assertIn(path,text)
        self.assertNotIn("<iframe",text)
        self.assertNotIn("RoomChatWelcome",text)
        self.assertNotIn("ConversationTransport",text)

    def test_animation_director_accessibility_and_original_arcade(self):
        code=(HOME/"home.js").read_text(encoding="utf-8")
        for token in ("prefers-reduced-motion","visibilitychange","aria-pressed",
                      "requestAnimationFrame","cancelAnimationFrame",
                      "setRoom(","textContent","localStorage",
                      "aria-live","keydown","focus","arcade","studio"):
            self.assertIn(token,code)
        self.assertIn("if (selectedRoom === 'studio' && id !== 'studio')",code)
        self.assertIn("roomNav.scrollLeft",code)
        css=(HOME/"style.css").read_text(encoding="utf-8")
        self.assertIn("white-space:nowrap",css)
        for bad in ("fetch(", "XMLHttpRequest", "new WebSocket", "innerHTML",
                    "eval(", "new Function(", "document.write("):
            self.assertNotIn(bad,code)
        rights=json.loads((HOME/"arcade-rights.json").read_text(encoding="utf-8"))
        self.assertEqual(rights["schema"],"muse-hub/arcade-rights/v1")
        self.assertEqual(len(rights["games"]),1)
        self.assertEqual(rights["games"][0]["rights"],"ORIGINAL_MIT_SOURCE")
        self.assertEqual(rights["games"][0]["external_assets"],[])
        self.assertEqual(rights["games"][0]["roms"],[])
        self.assertFalse(rights["third_party_gameplay_assets_included"])

    def test_companion_files_and_working_notebook_setup_are_discoverable(self):
        names=select_public_files(ROOT,verify_manifest=False)
        for name in ("examples/companion_home/index.html",
                     "examples/companion_home/home.js",
                     "examples/companion_home/style.css",
                     "examples/companion_home/rooms.json",
                     "examples/companion_home/rooms.js",
                     "examples/companion_home/arcade-rights.json",
                     "docs/COMPANION_HOME.md"):
            self.assertIn(name,names)
        doc=(ROOT/"docs/COMPANION_HOME.md").read_text(encoding="utf-8")
        self.assertIn("examples/space_starter.py --serve --companion-home --database",doc)
        self.assertIn("127.0.0.1",doc)
        self.assertIn("SQLite",doc)
        self.assertIn("session token",doc)
        self.assertIn("same database path",doc)
        self.assertIn("revision",doc)
        self.assertIn("Refresh saved notes",doc)
        self.assertIn("PersonalCompanion",doc)
        self.assertIn("examples/companion_home/",doc)
        self.assertIn('href="../../docs/COMPANION_HOME.md"',(HOME/"index.html").read_text(encoding="utf-8"))


class RoomNotebookTests(unittest.TestCase):
    def setUp(self):
        from muse_presets.room_notebook import RoomNotebook
        self.Notebook=RoomNotebook
        self.tmp=tempfile.TemporaryDirectory(prefix="h17-room-notes-")
        self.addCleanup(self.tmp.cleanup)
        self.folder=Path(self.tmp.name).resolve()
        self.user=CompanionScope("owner-a","space-a","owner-a",True)
        self.auth=lambda: self.user
        self.first=PersonalCompanion(self.folder/"current.sqlite3",authority=self.auth)
        self.addCleanup(self.first.close)

    def test_room_id_namespace_and_revision_and_reopen(self):
        book=self.Notebook(self.first)
        a=book.put("garden","plant","Water on Friday")
        self.assertEqual(a["revision"],1)
        self.assertEqual(book.notes("garden")[0]["note_id"],"plant")
        self.assertEqual(book.notes("focus"),[])
        b=book.put("garden","plant","Wait for rain",expected_revision=1)
        self.assertEqual(b["revision"],2)
        self.first.close()
        with PersonalCompanion(self.folder/"current.sqlite3",authority=self.auth) as again:
            self.assertEqual(self.Notebook(again).notes("garden")[0]["text"],"Wait for rain")
            with self.assertRaisesRegex(ValueError,"STALE_REVISION"):
                self.Notebook(again).put("garden","plant","stale",expected_revision=1)

    def test_room_snapshot_restore_new_store_preserves_revision(self):
        book=self.Notebook(self.first)
        book.put("garden","plant","Water on Friday")
        book.put("garden","plant","Wait for rain",expected_revision=1)
        book.put("focus","today","Check tasks")
        snap=book.snapshot()
        self.assertEqual(snap["schema"],"muse-hub/room-notebook-snapshot/v1")
        self.assertEqual(len(snap["notes"]),2)
        self.assertIs(snap["provider_authenticated"],False)
        self.assertIs(snap["native_muse_installed"],False)
        with PersonalCompanion(self.folder/"restored.sqlite3",authority=self.auth) as second:
            imported=self.Notebook(second).restore(snap)
            self.assertEqual(imported["restored"],2)
            self.assertEqual(self.Notebook(second).notes("garden")[0]["revision"],2)
            self.assertEqual(self.Notebook(second).notes("focus")[0]["text"],"Check tasks")
            with self.assertRaisesRegex(ValueError,"RESTORE_TARGET_NOT_EMPTY"):
                self.Notebook(second).restore(snap)

    def test_wrong_owner_or_space_cannot_restore_snapshot(self):
        b=self.Notebook(self.first)
        b.put("studio","sketch","Try three frames")
        snap=b.snapshot()
        self.user=CompanionScope("owner-b","space-a","owner-b",True)
        with PersonalCompanion(self.folder/"other.sqlite3",authority=self.auth) as wrong:
            with self.assertRaisesRegex(ValueError,"SCOPE_MISMATCH"):
                self.Notebook(wrong).restore(snap)
            self.assertEqual(wrong.notes(),[])
        self.user=CompanionScope("owner-a","space-b","owner-a",True)
        with PersonalCompanion(self.folder/"other.sqlite3",authority=self.auth) as wrong_space:
            with self.assertRaisesRegex(ValueError,"SCOPE_MISMATCH"):
                self.Notebook(wrong_space).restore(snap)

    def test_untrusted_duplicate_invalid_room_and_partial_restores_refused(self):
        b=self.Notebook(self.first)
        b.put("focus","id1","Good text")
        snap=b.snapshot()
        with PersonalCompanion(self.folder/"dest.sqlite3",authority=self.auth) as new:
            for mutation in (
                lambda d: d["notes"].append(dict(d["notes"][0])),
                lambda d: d["notes"][0].update(text=""),
                lambda d: d["notes"][0].update(note_id="../escape"),
                lambda d: d["notes"][0].update(room_id="unknown"),
                lambda d: d.update(scope_fingerprint="0"*64),
                lambda d: d["notes"][0].update(revision=0),
            ):
                altered=json.loads(json.dumps(snap))
                mutation(altered)
                with self.subTest(altered=altered),self.assertRaises(ValueError):
                    self.Notebook(new).restore(altered)
                self.assertEqual(new.notes(),[])

    def test_mutations_still_require_injected_owner_authority(self):
        book=self.Notebook(self.first)
        self.user=CompanionScope("owner-a","space-a","helper",False)
        with self.assertRaisesRegex(ValueError,"OWNER_APPROVAL_REQUIRED"):
            book.put("focus","task","Do one thing")
        self.assertEqual(book.notes("focus"),[])


if __name__=="__main__":
    unittest.main()
