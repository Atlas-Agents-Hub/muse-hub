"""Current setup guides, safe source references, and read-only command output."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "tools/hub_journeys.py"
SPEC = importlib.util.spec_from_file_location("muse_hub_journeys", MODULE)
J = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(J)


class HubJourneysTest(unittest.TestCase):
    def feature_fixture(self, root):
        data = (ROOT / J.FEATURE_REGISTER).read_bytes()
        catalog = root / J.FEATURE_REGISTER
        catalog.parent.mkdir(parents=True)
        catalog.write_bytes(data)
        features = json.loads(data)["features"]
        for item in features:
            for name in [item["guide"], *item["source_paths"], *item["tests"]]:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Current guide fixture\n", encoding="utf-8")
        return features

    def test_current_catalog_loads_and_missing_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            features = self.feature_fixture(root)
            self.assertEqual(J.load_features(root), features)
            (root / features[0]["guide"]).unlink()
            with self.assertRaisesRegex(ValueError, "SOURCE_PATH_MISSING"):
                J.load_features(root)

    def test_missing_catalog_does_not_fall_back_to_another_document(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            navigation = root / "docs/discovery/hub-feature-status.json"
            navigation.parent.mkdir(parents=True)
            navigation.write_bytes((ROOT / J.FEATURE_REGISTER).read_bytes())
            with self.assertRaisesRegex(ValueError, "SOURCE_PATH_MISSING"):
                J.load_features(root)

    def test_inventory_matches_current_feature_and_role_catalogs(self):
        result = J.verify_inventory(ROOT)
        self.assertEqual(result["status"], "SETUP_GUIDES_VALID")
        self.assertEqual(result["features"], len(J.load_features(ROOT)))
        self.assertEqual(result["roles"], len(J.load_roles(ROOT)))
        self.assertEqual(result["roles"], 15)

    def test_every_feature_has_actionable_setup_and_recovery_steps(self):
        output = J.build_journeys(ROOT)
        expected = {item["id"] for item in J.load_features(ROOT)}
        self.assertEqual({item["id"] for item in output["journeys"]}, expected)
        self.assertTrue({"daily-desk", "companion-home", "terminal", "family-link", "creative-studio"} <= expected)
        for item in output["journeys"]:
            with self.subTest(feature=item["id"]):
                self.assertEqual(set(item["phases"]), set(J.PHASES))
                self.assertTrue(all(step["instruction"] for step in item["phases"].values()))
                self.assertTrue((ROOT / item["guide"]).is_file())
                for command in item["phases"]["named_test"]["commands"]:
                    self.assertRegex(command, r"^python -B scripts/run_source_test.py test_[a-z0-9_]+\.py$")
                    self.assertTrue((ROOT / "tests" / command.split()[-1]).is_file())

    def test_all_roles_have_a_resolvable_setup_guide(self):
        for role in J.load_roles(ROOT):
            with self.subTest(role=role["id"]):
                result = J.build_journeys(ROOT, feature="specialists", role=role["id"])
                self.assertEqual(result["role"]["id"], role["id"])
                self.assertTrue((ROOT / result["role"]["guide"]).is_file())
                self.assertEqual(len(result["journeys"]), 1)

    def test_traversal_aliases_and_symlinks_are_refused(self):
        features = copy.deepcopy(J.load_features(ROOT))
        for unsafe in ("../private", "/etc/passwd", "docs/../README.md", "docs//README.md", "./README.md", "C:\\private\\key"):
            features[0]["source_paths"] = [unsafe]
            with self.subTest(path=unsafe), self.assertRaisesRegex(ValueError, "SOURCE_PATH_UNSAFE"):
                J.validate_features(features, ROOT)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "target.md").write_text("Fixture\n")
            try:
                (root / "link.md").symlink_to(root / "target.md")
            except (OSError, NotImplementedError):
                self.skipTest("Symlinks unavailable on this host")
            with self.assertRaisesRegex(ValueError, "SOURCE_PATH_UNSAFE"):
                J._safe_file(root, "link.md")

    def test_duplicate_ids_extra_fields_and_incomplete_steps_are_refused(self):
        mutations = (
            ("FEATURE_ID", lambda x: x[1].update(id=x[0]["id"])),
            ("FEATURE_SCHEMA", lambda x: x[0].update(extra=True)),
            ("INSTRUCTION_SHAPE", lambda x: x[0]["instructions"].pop("failure")),
            ("SOURCE_PATH_SHAPE", lambda x: x[0].update(source_paths=[{}])),
            ("TEST_PATH_SHAPE", lambda x: x[0].update(tests=["tests/test_a.py;touch bad"])),
        )
        for reason, mutate in mutations:
            value = copy.deepcopy(J.load_features(ROOT))
            mutate(value)
            with self.subTest(reason=reason), self.assertRaisesRegex(ValueError, reason):
                J.validate_features(value, ROOT)

    def test_duplicate_json_keys_constants_and_oversized_input_are_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "input.json"
            for raw, reason in ((b'{"features":[],"features":[]}', "DUPLICATE_JSON_KEY"),
                                (b'{"value":NaN}', "INVALID_JSON_CONSTANT"),
                                (b" " * (J.MAX_DOCUMENT_BYTES + 1), "SOURCE_DOCUMENT_SIZE")):
                path.write_bytes(raw)
                with self.subTest(reason=reason), self.assertRaisesRegex(ValueError, reason):
                    J._read_json(path)

    def test_unknown_role_or_feature_is_refused(self):
        with self.assertRaisesRegex(ValueError, "ROLE_UNKNOWN"):
            J.build_journeys(ROOT, role="unknown-role")
        with self.assertRaisesRegex(ValueError, "FEATURE_UNKNOWN"):
            J.build_journeys(ROOT, feature="missing-feature")

    def test_cli_json_markdown_and_errors_preserve_inputs(self):
        features = J.load_features(ROOT)
        paths = {J.FEATURE_REGISTER, "hub/site/roles.json"}
        paths.update(name for item in features for name in [item["guide"], *item["source_paths"], *item["tests"]])
        before = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in paths}
        for args in (["--verify"], ["--feature", "daily-desk", "--role", "learning-coach"], ["--all"]):
            result = subprocess.run([sys.executable, "-B", str(MODULE), *args], cwd=ROOT, capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(json.loads(result.stdout)["status"], {"SETUP_GUIDES_VALID", "SETUP_GUIDES_READY"})
        result = subprocess.run([sys.executable, "-B", str(MODULE), "--feature", "daily-desk", "--format", "markdown"], cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        for phrase in ("Daily Desk", "Check saved receipt", "Get started", "Recover"):
            self.assertIn(phrase, result.stdout)
        invalid = subprocess.run([sys.executable, "-B", str(MODULE), "--feature", "missing-feature"], cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(invalid.returncode, 2)
        self.assertEqual(json.loads(invalid.stdout)["reason"], "FEATURE_UNKNOWN")
        self.assertEqual(before, {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in paths})

    def test_documented_entrypoints_remain_discoverable(self):
        doc = (ROOT / "docs/handbook/hub-setup-journeys.md").read_text()
        for term in ("START_HERE.md", "tools/hub_journeys.py", "--feature daily-desk", "same database path", "newly printed token", "Back up local databases"):
            self.assertIn(term, doc)
        self.assertIn("hub-setup-journeys.md", (ROOT / "docs/handbook/README.md").read_text())


if __name__ == "__main__":
    unittest.main()
