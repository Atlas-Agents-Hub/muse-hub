"""Task Board editing, undo and concurrent-save regressions."""
from pathlib import Path
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("node"), "Node unavailable for client regression")
class TaskBoardClientTests(unittest.TestCase):
    def run_case(self, case):
        result = subprocess.run(
            [shutil.which("node"), str(ROOT / "tests/task_board_client_cases.cjs"), case,
             str(ROOT / "examples/task_board/assets/board.js")],
            stdin=subprocess.DEVNULL, capture_output=True, text=True,
            encoding="utf-8", timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout), {"case": case, "status": "PASS"})

    def test_edit_preserves_identity_and_status(self):
        self.run_case("edit_preserves_identity_and_status")

    def test_full_board_can_make_room_for_new_work(self):
        self.run_case("full_board_can_make_room_for_new_work")

    def test_remove_and_undo_preserve_order_and_focus(self):
        self.run_case("removal_undo_restores_order_and_focus")

    def test_new_save_expires_old_undo(self):
        self.run_case("next_mutation_expires_undo")

    def test_conflict_preserves_draft_and_requires_reconciliation(self):
        self.run_case("conflict_preserves_draft_and_fences_writes")

    def test_stale_undo_preserves_other_window_changes(self):
        self.run_case("stale_undo_never_overwrites_new_cards")

    def test_lost_remove_acknowledgement_requires_refresh(self):
        self.run_case("lost_remove_reply_is_reconciled_before_another_write")

    def test_literal_text_and_cancel(self):
        self.run_case("text_is_literal_and_cancel_keeps_saved_card")


class TaskBoardPersistenceTests(unittest.TestCase):
    def setUp(self):
        from muse_presets.personal_companion import CompanionScope
        spec = importlib.util.spec_from_file_location("task_board_example", ROOT / "examples/task_board/board.py")
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "board.sqlite"
        self.scope = CompanionScope("board-owner", "task-board", "board-owner", True)
        self.board = self.module.TaskBoard(self.path, authority=lambda: self.scope)
        self.initial = {"schema": "muse-task-board/v1", "cards": [
            {"id": "one", "title": "Read the brief", "details": "Keep this context", "status": "doing", "priority": "normal"}
        ]}

    def test_edit_remove_undo_persist_across_reopen(self):
        self.board.save(self.initial, expected_revision=0)
        edited = json.loads(json.dumps(self.initial))
        edited["cards"][0].update(title="Read the revised brief", priority="high")
        self.board.save(edited, expected_revision=1)
        self.board.save({"schema": "muse-task-board/v1", "cards": []}, expected_revision=2)
        reopened = self.module.TaskBoard(self.path, authority=lambda: self.scope)
        self.assertEqual(reopened.snapshot()["board"]["cards"], [])
        reopened.save(edited, expected_revision=3)
        self.assertEqual(self.board.snapshot(), {"board": edited, "revision": 4})

    def test_stale_undo_cannot_overwrite_another_window(self):
        self.board.save(self.initial, expected_revision=0)
        self.board.save({"schema": "muse-task-board/v1", "cards": []}, expected_revision=1)
        newer = json.loads(json.dumps(self.initial))
        newer["cards"][0].update(id="new", title="Keep newer work")
        self.board.save(newer, expected_revision=2)
        with self.assertRaisesRegex(ValueError, "STALE_REVISION"):
            self.board.save(self.initial, expected_revision=2)
        self.assertEqual(self.board.snapshot()["board"], newer)


if __name__ == "__main__":
    unittest.main()
