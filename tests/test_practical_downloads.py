"""Practical additions remain complete in the ZIPs people actually download."""
from __future__ import annotations

import importlib.util
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
spec = importlib.util.spec_from_file_location("practical_release", ROOT / "scripts/build_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)

from muse_presets.public_export import PublicExportError, select_public_files

REQUIRED = {
    "daily-briefing": {"skills/daily-briefing/REMINDERS.md", "skills/daily-briefing/CALENDAR_REVIEW.md"},
    "weekly-reset": {"skills/weekly-reset/GOAL_REVIEW.md"},
    "accessible-ui": {"tools/accessibility_check.py", "skills/accessible-ui/SOURCE_CHECK.md",
        "skills/accessible-ui/examples/clean.html", "skills/accessible-ui/examples/review.html"},
}


class PracticalDownloadsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = release.collection.load_collection()

    def assert_complete(self, files):
        manifest = json.loads(files["MANIFEST.json"])
        for skill, required in REQUIRED.items():
            if "skills/" + skill + "/SKILL.md" not in files:
                self.assertFalse(required & files.keys())
                continue
            self.assertTrue(required <= files.keys(), sorted(required - files.keys()))
            self.assertTrue(required <= manifest["files"].keys())
            for name in required:
                source = ROOT / (name if name.startswith("tools/") else "collections/muse-starters-v1/" + name)
                self.assertEqual(files[name], source.read_bytes(), name)
            for name in required:
                if name.endswith(".md"):
                    self.assertIn(Path(name).name.encode(), files["skills/" + skill + "/SKILL.md"])
                    self.assertIn(name.encode(), files["START_HERE.md"])

    def test_dependencies_reach_skills_roles_workflows_and_starters(self):
        packages = [(key, release.skill_files(self.data, key)) for key in REQUIRED]
        packages += [(key, release.specialist_files(self.data, key)) for key in release.ROLE_WORKFLOWS]
        packages += [(row["id"], release.workflow_files(self.data, row["id"])) for row in self.data["workflows"]]
        packages += [(row["id"], release.collection.package_files(self.data, row["id"])) for row in self.data["starters"]]
        for name, files in packages:
            with self.subTest(package=name):
                self.assert_complete(files)

    def test_accessibility_zip_runs_its_examples_without_the_checkout(self):
        files = release.skill_files(self.data, "accessible-ui")
        self.assert_complete(files)
        raw = release._zip(files)
        with tempfile.TemporaryDirectory(prefix="muse-accessibility-download-") as temporary:
            folder = Path(temporary)
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                archive.extractall(folder)
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            env.pop("PYTHONPATH", None)
            def run(*args, expected=0):
                result = subprocess.run([sys.executable, "-B", *args], cwd=folder, env=env,
                    capture_output=True, text=True, encoding="utf-8", timeout=30)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                self.assertEqual(result.stderr, "")
                return json.loads(result.stdout)
            self.assertEqual(run("VERIFY.py")["status"], "PASS")
            clean = run("tools/accessibility_check.py", "--input", "skills/accessible-ui/examples/clean.html")
            self.assertEqual(clean["status"], "checked")
            self.assertEqual(clean["findings"], [])
            review = run("tools/accessibility_check.py", "--input", "skills/accessible-ui/examples/review.html", expected=1)
            self.assertEqual(review["status"], "findings")
            self.assertTrue(review["findings"])
            error = run("tools/accessibility_check.py", "--input", "missing.html", expected=2)
            self.assertEqual(error["status"], "error")
            self.assertFalse((folder / "__pycache__").exists())

    def test_worksheet_packages_resolve_their_local_links(self):
        for key in ("daily-briefing", "weekly-reset"):
            files = release.skill_files(self.data, key)
            self.assert_complete(files)
            with tempfile.TemporaryDirectory() as temporary:
                folder = Path(temporary)
                with zipfile.ZipFile(io.BytesIO(release._zip(files))) as archive:
                    archive.extractall(folder)
                for name in REQUIRED[key]:
                    document = folder / name
                    for link in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", document.read_text(encoding="utf-8")):
                        if ":" not in link and not link.startswith("#"):
                            destination = (document.parent / link.split("#", 1)[0]).resolve()
                            self.assertTrue(destination.is_relative_to(folder.resolve()))
                            self.assertTrue(destination.is_file(), str(destination))

    def test_instruction_challenges_do_not_advertise_missing_attachments(self):
        for key in REQUIRED:
            case = next(row for row in self.data["depth_cases"] if row["skill_id"] == key)
            files = release.collection.challenge_files(self.data, case["id"], "candidate")
            self.assertFalse(REQUIRED[key] & files.keys())
            instruction = files["skills/" + key + "/SKILL.md"]
            for name in REQUIRED[key]:
                self.assertNotIn(Path(name).name.encode(), instruction)

    def test_public_tool_export_remains_an_exact_allowlist(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "tools").mkdir()
            (root / "tools/accessibility_check.py").write_text("# reviewed tool\n", encoding="utf-8")
            self.assertEqual(set(select_public_files(root)), {"tools/accessibility_check.py"})
            (root / "tools/other_checker.py").write_text("# unrelated\n", encoding="utf-8")
            with self.assertRaisesRegex(PublicExportError, "UNAPPROVED_COLLECTION_PATH"):
                select_public_files(root)


if __name__ == "__main__":
    unittest.main()
