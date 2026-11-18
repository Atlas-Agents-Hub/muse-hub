"""Behavioral regressions for the shipped Notebook client state machine.

Node supplies only a minimal DOM and HTTP boundary fixture. Real loopback
HTTP/SQLite and Chromium acceptance are separate tests.
"""
from pathlib import Path
import json
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("node"), "Node is optional for client VM regressions")
class NotebookClientTests(unittest.TestCase):
    def run_case(self, case):
        result = subprocess.run(
            [shutil.which("node"), str(ROOT / "tests/notebook_client_cases.cjs"), case,
             str(ROOT / "src/muse_presets/companion_assets/notebook.js")],
            stdin=subprocess.DEVNULL, capture_output=True, text=True,
            encoding="utf-8", timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout), {"case": case, "status": "PASS"})

    def test_revoked_scope_clears_private_state_and_old_handlers(self):
        self.run_case("revoked_read_403")

    def test_invalid_unauthorized_body_still_clears_session(self):
        self.run_case("revoked_read_401_malformed")

    def test_acknowledged_write_then_denied_read_is_not_refused_write(self):
        self.run_case("committed_write_read_403")

    def test_failed_followup_read_keeps_write_fenced_until_readback(self):
        self.run_case("committed_write_read_400")

    def test_actual_mutation_conflict_keeps_unsaved_draft(self):
        self.run_case("mutation_conflict_preserves_draft")

    def test_supported_unicode_note_remains_readable(self):
        self.run_case("unicode_saved_note_is_readable")

    def test_unicode_limit_matches_server_codepoints(self):
        self.run_case("unicode_limit_save")

    def test_over_limit_unicode_is_preserved_without_write(self):
        self.run_case("unicode_over_limit_refused_locally")


if __name__ == "__main__":
    unittest.main()
