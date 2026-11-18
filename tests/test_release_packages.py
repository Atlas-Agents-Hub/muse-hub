"""Release downloads work after extraction, with no repository import path."""
from __future__ import annotations
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
spec = importlib.util.spec_from_file_location("build_release_tested", ROOT / "scripts/build_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleasePackagesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = release.collection.load_collection()
        cls.archives, cls.records = release.compose_downloads(cls.data)
        cls.temp = tempfile.TemporaryDirectory(prefix="muse-release-extracted-")
        cls.base = Path(cls.temp.name)
        cls.extracted = {}
        for group in ("specialists", "skills", "workflows"):
            for record in cls.records[group]:
                folder = cls.base / record["asset"][:-4]
                with zipfile.ZipFile(io.BytesIO(cls.archives[record["asset"]])) as archive:
                    archive.extractall(folder)
                cls.extracted[record["asset"]] = folder

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def run_python(self, folder, *args):
        env = dict(os.environ)
        env.pop("PYTHONPATH", None)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run([sys.executable, "-B", *args], cwd=folder, env=env,
                              capture_output=True, text=True, encoding="utf-8", timeout=30)

    def test_download_inventory_and_exact_aliases(self):
        self.assertEqual(len(self.archives), 120)
        self.assertEqual([len(self.records[k]) for k in ("specialists", "skills", "workflows")],
                         [15, 75, 25])
        self.assertIn("muse-data-engineer-v1.1.1.zip", self.archives)
        self.assertIn("muse-reliability-engineer-v1.1.1.zip", self.archives)
        for rows in self.records.values():
            self.assertEqual(len(rows), len({r["id"] for r in rows}))
            for row in rows:
                raw = self.archives[row["asset"]]
                self.assertEqual(len(raw), row["bytes"])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"])
                self.assertEqual(row["url"], release.asset_url(row["asset"], "v1.1.1"))

    def test_archive_roster_integrity_and_portable_paths(self):
        for name, raw in self.archives.items():
            with self.subTest(asset=name):
                manifest = release.verify_archive(raw)
                self.assertIn("LICENSE", manifest["files"])
                self.assertIn("START_HERE.md", manifest["files"])
                self.assertIn("VERIFY.py", manifest["files"])
                with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                    for path in archive.namelist():
                        self.assertFalse(PurePosixPath(path).is_absolute())
                        self.assertNotIn("..", path.split("/"))
                        self.assertNotIn("\\", path)
                    self.assertEqual(len(archive.namelist()),
                                     len({p.casefold() for p in archive.namelist()}))

    def test_all_individual_downloads_verify_in_fresh_directories(self):
        self.assertEqual(len(self.extracted), 115)
        for name, folder in self.extracted.items():
            with self.subTest(asset=name):
                result = self.run_python(folder, "VERIFY.py")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(json.loads(result.stdout)["status"], "PASS")

    def test_advertised_local_tools_run_without_checkout(self):
        executed = 0
        for name, folder in self.extracted.items():
            if not (folder / "tools/run.py").is_file():
                continue
            with self.subTest(asset=name):
                result = self.run_python(folder, "tools/run.py", "--demo")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                output = json.loads(result.stdout)
                self.assertTrue(output["results"])
                self.assertFalse(output["external_actions_performed"])
                self.assertFalse(output["model_called"])
                executed += 1
        self.assertGreaterEqual(executed, 20)

    def test_every_skill_practice_command_runs_after_extraction(self):
        for record in self.records["skills"]:
            folder = self.extracted[record["asset"]]
            guide = (folder / "practice/README.md").read_text(encoding="utf-8")
            match = re.search(r"python -B (practice/check_outputs.py check --case [^\n]+)", guide)
            self.assertIsNotNone(match, record["id"])
            with self.subTest(skill=record["id"]):
                result = self.run_python(folder, *match.group(1).split())
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_workflows_include_their_skill_dependencies(self):
        workflows = {w["id"]: w for w in self.data["workflows"]}
        for record in self.records["workflows"]:
            folder = self.extracted[record["asset"]]
            for skill in workflows[record["id"]]["skills"]:
                self.assertTrue((folder / "skills" / skill / "SKILL.md").is_file())
                self.assertTrue((folder / "skills" / skill / "DEPTH.md").is_file())
            text = (folder / "workflows" / (record["id"] + ".md")).read_text(encoding="utf-8")
            self.assertNotIn("tools/muse_collection.py", text)
            self.assertNotIn("muse_presets.specialist_extensions", text)

    def test_relative_markdown_links_resolve_inside_each_package(self):
        for name, folder in self.extracted.items():
            for document in folder.rglob("*.md"):
                for link in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", document.read_text(encoding="utf-8")):
                    if ":" in link or link.startswith("#"):
                        continue
                    destination = (document.parent / link.split("#", 1)[0]).resolve()
                    with self.subTest(asset=name, document=str(document.relative_to(folder)), link=link):
                        self.assertTrue(destination.is_relative_to(folder.resolve()))
                        self.assertTrue(destination.exists())

    def test_skill_agent_entrypoints_name_the_packaged_depth_document(self):
        for record in self.records["skills"]:
            folder = self.extracted[record["asset"]]
            text = (folder / "AGENTS.md").read_text(encoding="utf-8")
            with self.subTest(skill=record["id"]):
                links = re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", text)
                depth = "skills/" + record["id"] + "/DEPTH.md"
                self.assertIn(depth, links)
                self.assertTrue((folder / depth).is_file())

    def test_documented_custom_input_command_runs_with_the_example_shape(self):
        raw = self.archives["muse-skill-schema-evolution-v1.1.1.zip"]
        folder = self.base / "documented-custom-input"
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            archive.extractall(folder)
        guide = (folder / "tools/README.md").read_text(encoding="utf-8")
        command = re.search(r"python -B (tools/run.py --tool ([a-z-]+) --input input.json)", guide)
        self.assertIsNotNone(command, guide)
        examples = json.loads((folder / "tools/EXAMPLES.json").read_bytes())
        inputs = next(j["inputs"] for j in examples["jobs"] if j["skill_id"] == command.group(2))
        (folder / "input.json").write_text(json.dumps(inputs), encoding="utf-8")
        result = self.run_python(folder, *command.group(1).split())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["results"][0]["skill_id"], command.group(2))
        self.assertFalse(report["external_actions_performed"])

    def test_specialists_keep_the_canonical_components_and_policy(self):
        from muse_presets.standalone_pack import inspect_standalone_pack
        for record in self.records["specialists"]:
            folder = self.extracted[record["asset"]]
            report = inspect_standalone_pack(folder / "assistant")
            with self.subTest(role=record["id"]):
                self.assertEqual(report["status"], "LOCAL_STANDALONE_MATCH")
                self.assertEqual(report["subchat_count"], 3)
                self.assertEqual(report["skill_count"], 8)
                self.assertFalse(report["native_installed"])
                self.assertFalse(report["can_apply"])
                for path in ("system-profile/profile", "subchat-scopes/subchats", "role-skills/custom-skills"):
                    self.assertTrue((folder / "assistant" / path).is_dir())
                self.assertTrue((folder / "FIRST_TASK.md").is_file())

    def test_original_fifty_procedures_remain_distinct(self):
        raw = self.archives["muse-role-procedures-50-v1.1.1.zip"]
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            receipt = json.loads(archive.read("PORTABLE_SKILLS_MANIFEST.json"))
            self.assertEqual(receipt["unique_skills"], 50)
            self.assertEqual(receipt["role_methods"], 45)
            self.assertEqual(receipt["shared_skills"], 5)
            self.assertIn("75", archive.read("README.md").decode())

    def test_bundles_preserve_individual_packages(self):
        for kind, count in (("specialists",15),("skills",75),("workflows",25),("starters",100)):
            raw = self.archives["muse-" + kind + "-v1.1.1.zip"]
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                members = json.loads(archive.read("PACKAGES.json"))["packages"]
                self.assertEqual(len(members), count)
                for member in members:
                    nested = archive.read("packages/" + member["asset"])
                    self.assertEqual(hashlib.sha256(nested).hexdigest(), member["sha256"])
                    release.verify_archive(nested)
                    if kind != "starters":
                        self.assertEqual(nested, self.archives[member["asset"]])

    def test_start_instructions_are_current_and_useful(self):
        for name, folder in self.extracted.items():
            text = (folder / "START_HERE.md").read_text(encoding="utf-8")
            with self.subTest(asset=name):
                self.assertIn("existing Muse", text)
                self.assertIn("No Python is required", text)
                self.assertNotRegex(text.lower(), r"source.only|not installed|draft release|draft-only|not additional agents|other 99")
                self.assertIn("VERIFY.py", text)

    def test_build_is_deterministic_and_rejects_bad_selection(self):
        first = release._zip(release.skill_files(self.data, "schema-evolution"))
        self.assertEqual(first, release._zip(release.skill_files(self.data, "schema-evolution")))
        for value in ("../v1.1.1", "v1.1", "v1.1.1/other"):
            with self.assertRaises(ValueError):
                release._version(value)
        with self.assertRaises(ValueError):
            release.skill_files(self.data, "unknown")
        with self.assertRaises(ValueError):
            release.collection.instruction_files(self.data, ["unknown"], [])
        with self.assertRaises(ValueError):
            release.collection.instruction_files(self.data, [], ["unknown"])

    def test_tampered_tool_is_refused_before_import(self):
        raw = self.archives["muse-skill-schema-evolution-v1.1.1.zip"]
        folder = self.base / "tampered"
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            archive.extractall(folder)
        (folder / "tools/specialist_extensions/data.py").write_text(
            "raise RuntimeError('TAMPERED_CODE_EXECUTED')\n", encoding="utf-8")
        for args in (("VERIFY.py",), ("tools/run.py", "--demo")):
            result = self.run_python(folder, *args)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("CHANGED", result.stderr)
            self.assertNotIn("TAMPERED_CODE_EXECUTED", result.stderr)

    def test_verifier_rejects_unsafe_and_colliding_manifest_names(self):
        raw = self.archives["muse-skill-schema-evolution-v1.1.1.zip"]
        folder = self.base / "invalid-manifest"
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            archive.extractall(folder)
        manifest_path = folder / "MANIFEST.json"
        original = json.loads(manifest_path.read_bytes())
        for name in ("../LICENSE", "/LICENSE", "C:LICENSE", "skills\\schema-evolution\\SKILL.md", "skills//SKILL.md", "license"):
            altered = {**original, "files": dict(original["files"])}
            altered["files"][name] = altered["files"]["LICENSE"]
            manifest_path.write_text(json.dumps(altered), encoding="utf-8")
            with self.subTest(path=name):
                result = self.run_python(folder, "VERIFY.py")
                self.assertEqual(result.returncode, 2)
                self.assertRegex(result.stderr, "UNSAFE_MANIFEST_ENTRY|DUPLICATE_PORTABLE_PATH")

    def test_release_refuses_existing_destination_without_changes(self):
        folder = self.base / "existing-output"
        folder.mkdir()
        sentinel = folder / "keep.txt"
        sentinel.write_text("preserve", encoding="utf-8")
        with self.assertRaises(ValueError):
            release.build_release(folder, "0" * 40)
        self.assertEqual(sentinel.read_text(), "preserve")
        self.assertEqual(list(folder.iterdir()), [sentinel])


if __name__ == "__main__":
    unittest.main()
