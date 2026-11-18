"""Explicit local launcher mode; never start a listener during these tests."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("companion_launcher", ROOT / "examples/space_starter.py")
launcher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(launcher)


class CompanionLauncherTests(unittest.TestCase):
    def test_companion_flag_requires_explicit_serve(self):
        with patch.object(launcher.sys, "argv", ["space_starter.py", "--companion-home"]), patch.object(launcher, "demo") as demo:
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                launcher.main()
            self.assertEqual(exc.exception.code, 2)
            demo.assert_not_called()

    def test_companion_mode_uses_existing_server_and_closes_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            database = Path(tmp).resolve() / "notebook.sqlite3"
            server = Mock(server_address=("127.0.0.1", 12345))
            server.serve_forever.side_effect = KeyboardInterrupt
            with patch.object(launcher.sys, "argv", ["space_starter.py", "--serve", "--companion-home", "--database", str(database)]), patch.object(launcher, "make_server", return_value=server) as make, contextlib.redirect_stdout(io.StringIO()):
                try:
                    launcher.main()
                except SystemExit as exc:
                    self.fail("Companion launch option was refused with exit " + str(exc.code))
            self.assertTrue(make.call_args.kwargs["companion_home"])
            self.assertEqual(make.call_args.args[0], database)
            self.assertTrue(make.call_args.kwargs["authority"]().owner_present)
            server.server_close.assert_called_once()

    def test_default_server_does_not_enable_companion_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = Mock(server_address=("127.0.0.1", 12345))
            server.serve_forever.side_effect = KeyboardInterrupt
            with patch.object(launcher.sys, "argv", ["space_starter.py", "--serve", "--database", str(Path(tmp).resolve() / "default.sqlite3")]), patch.object(launcher, "make_server", return_value=server) as make, contextlib.redirect_stdout(io.StringIO()):
                launcher.main()
            self.assertFalse(make.call_args.kwargs.get("companion_home", False))
            server.server_close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
