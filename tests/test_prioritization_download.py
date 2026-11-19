"""The prioritization download is complete, executable and narrowly exported."""
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
spec = importlib.util.spec_from_file_location("prioritization_release", ROOT / "scripts/build_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)

from muse_presets.public_export import PublicExportError, _validate_file, select_public_files
from muse_presets.neutrality import audit_public_tree

SKILL = "project-prioritization"
ASSET_DIR = "skills/" + SKILL + "/"
CSV_SOURCE = "collections/muse-starters-v1/" + ASSET_DIR + "backlog.csv"
REQUIRED = {"tools/prioritize.py", *(ASSET_DIR + name for name in
             ("PRIORITIZE.md", "PROVENANCE.md", "backlog.json", "backlog.csv"))}


class PrioritizationDownloadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = release.collection.prepare_collection(release.collection.load_collection())

    def test_every_containing_package_has_the_executable_dependency_closure(self):
        def containing_packages():
            yield "skill", release.skill_files(self.data, SKILL)
            for workflow in self.data["workflows"]:
                if SKILL in workflow["skills"]:
                    yield workflow["id"], release.workflow_files(self.data, workflow["id"])
            for role in release.ROLE_WORKFLOWS:
                files = release.specialist_files(self.data, role)
                if ASSET_DIR + "SKILL.md" in files:
                    yield role, files
            for starter in self.data["starters"]:
                files = release.collection.package_files(self.data, starter["id"])
                if ASSET_DIR + "SKILL.md" in files:
                    yield starter["id"], files
        count = 0
        for name, files in containing_packages():
            count += 1
            with self.subTest(package=name):
                self.assertTrue(REQUIRED <= files.keys(), sorted(REQUIRED - files.keys()))
                self.assertIn(b"PRIORITIZE.md", files[ASSET_DIR + "SKILL.md"])
                manifest = json.loads(files["MANIFEST.json"])
                self.assertTrue(REQUIRED <= manifest["files"].keys())
                self.assertEqual(files["tools/prioritize.py"], (ROOT / "tools/prioritize.py").read_bytes())
        self.assertGreaterEqual(count, 12)

    def test_actual_zip_verifies_and_runs_without_a_checkout(self):
        files = release.skill_files(self.data, SKILL)
        self.assertTrue(REQUIRED <= files.keys(), sorted(REQUIRED - files.keys()))
        raw = release._zip(files)
        with tempfile.TemporaryDirectory(prefix="muse-prioritization-") as temporary:
            folder = Path(temporary)
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                archive.extractall(folder)
            environment = dict(os.environ)
            environment.pop("PYTHONPATH", None)
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            def run(*args):
                result = subprocess.run([sys.executable, "-B", *args], cwd=folder,
                    env=environment, capture_output=True, text=True, encoding="utf-8", timeout=30)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(result.stderr, "")
                return result.stdout
            self.assertEqual(json.loads(run("VERIFY.py"))["status"], "PASS")
            report = json.loads(run("tools/prioritize.py", "--input", ASSET_DIR + "backlog.json"))
            self.assertEqual(report["selected_order"], ["prep-data", "onboarding", "quick-guide"])
            self.assertEqual(report["budgets"]["engineering"],
                             {"capacity": "10", "used": "8", "remaining": "2"})
            self.assertEqual(report["budgets"]["design"],
                             {"capacity": "2", "used": "2", "remaining": "0"})
            self.assertEqual(report["completed_ids"], ["tracking-live"])
            csv_report = json.loads(run("tools/prioritize.py", "--input", ASSET_DIR + "backlog.csv",
                "--reach-period", "customers per quarter", "--effort-unit", "person-days",
                "--capacity", "engineering=10", "--capacity", "design=2"))
            self.assertEqual(csv_report, report)
            run("tools/prioritize.py", "--input", ASSET_DIR + "backlog.json", "--format", "csv",
                "--output", "priorities.csv")
            self.assertIn('"First-run guide, ""quick start"""', (folder / "priorities.csv").read_text())
            for document in (folder / ASSET_DIR).glob("*.md"):
                for link in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", document.read_text(encoding="utf-8")):
                    if ":" not in link and not link.startswith("#"):
                        destination = (document.parent / link.split("#", 1)[0]).resolve()
                        self.assertTrue(destination.is_relative_to(folder.resolve()))
                        self.assertTrue(destination.is_file(), str(destination))

    def test_start_guides_expose_the_included_command(self):
        for files in (release.skill_files(self.data, SKILL),
                      release.workflow_files(self.data, "priority-week"),
                      release.specialist_files(self.data, "coordinator")):
            self.assertIn(b"python -B tools/prioritize.py --input skills/project-prioritization/backlog.json",
                          files["START_HERE.md"])

    def test_unrelated_skills_and_instruction_challenges_do_not_advertise_missing_tools(self):
        files = release.skill_files(self.data, "prose-revision")
        self.assertFalse(REQUIRED & files.keys())
        challenge = release.collection.challenge_files(self.data, "project-prioritization-r3-standard", "candidate")
        self.assertFalse(REQUIRED & challenge.keys())
        self.assertNotIn(b"PRIORITIZE.md", challenge[ASSET_DIR + "SKILL.md"])
        self.assertNotIn(b"backlog.json", b"\n".join(challenge.values()))

    def test_public_export_admits_only_the_reviewed_calculator_and_sample_csv(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / "tools").mkdir()
            (folder / "tools/prioritize.py").write_text("# reviewed executable\n")
            sample = folder / CSV_SOURCE
            sample.parent.mkdir(parents=True)
            sample.write_text("id,name\nexample,Example\n")
            selected = select_public_files(folder)
            self.assertEqual(set(selected), {"tools/prioritize.py", CSV_SOURCE})
            other = folder / "tools/unreviewed.py"
            other.write_text("# not admitted\n")
            with self.assertRaisesRegex(PublicExportError, "UNAPPROVED_COLLECTION_PATH"):
                select_public_files(folder)
            other.unlink()
            other = sample.with_name("private.csv")
            other.write_text("name,email\n")
            with self.assertRaisesRegex(PublicExportError, "UNREVIEWED_NON_TEXT_FILE"):
                select_public_files(folder)

    def test_sample_csv_exception_retains_binary_and_symlink_rejection(self):
        with tempfile.TemporaryDirectory() as temporary:
            sample = Path(temporary) / "backlog.csv"
            sample.write_bytes(b"id,name\x00\n")
            with self.assertRaisesRegex(PublicExportError, "BINARY_OR_OVERSIZED_FILE"):
                _validate_file(sample, Path(CSV_SOURCE))
            target = Path(temporary) / "outside.txt"
            target.write_text("id,name\n")
            sample.unlink()
            try:
                sample.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation denied")
            with self.assertRaisesRegex(PublicExportError, "SYMLINK_REFUSED"):
                _validate_file(sample, Path(CSV_SOURCE))

    def test_reviewed_csv_still_passes_through_privacy_and_binary_checks(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            sample = folder / CSV_SOURCE
            sample.parent.mkdir(parents=True)
            sample.write_text("id,name\nexample,Example\n", encoding="utf-8")
            self.assertEqual(audit_public_tree(folder), [])
            sample.write_text("id,name\nexample,SyntheticPrivateRecipient\n", encoding="utf-8")
            self.assertEqual(audit_public_tree(folder, forbidden_terms=("SyntheticPrivateRecipient",)),
                             [{"path": CSV_SOURCE, "reason": "FORBIDDEN_IDENTITY_LABEL"}])
            sample.write_bytes(b"id,name\x00\n")
            self.assertEqual(audit_public_tree(folder),
                             [{"path": CSV_SOURCE, "reason": "UNREVIEWED_BINARY_ASSET"}])
            sample.write_text("id,name\nexample,Example\n", encoding="utf-8")
            other = sample.with_name("unreviewed.csv")
            other.write_text("id,name\nexample,Example\n", encoding="utf-8")
            self.assertEqual(audit_public_tree(folder), [{"path": other.relative_to(folder).as_posix(),
                                                        "reason": "UNREVIEWED_BINARY_ASSET"}])


if __name__ == "__main__":
    unittest.main()
