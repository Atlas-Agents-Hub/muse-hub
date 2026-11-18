"""H19 source-only first-use/recovery journey regression and hostile-data tests."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "tools" / "hub_journeys.py"
SPEC = importlib.util.spec_from_file_location("muse_hub_journeys", MODULE)
assert SPEC and SPEC.loader
J = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(J)


class HubJourneysTest(unittest.TestCase):
    def test_all_22_features_and_15_roles_are_source_checked(self):
        result = J.verify_inventory(ROOT)
        self.assertEqual(result["status"], "SOURCE_INVENTORY_VALID_NOT_RUNTIME_VERIFIED")
        self.assertEqual(result["features"], 22)
        self.assertEqual(result["roles"], 15)
        self.assertFalse(result["native_installed"])
        self.assertFalse(result["external_effect_authorized"])
        self.assertFalse(result["site_deployed"])

    def test_h19_source_acceptance_is_recorded_without_native_promotion(self):
        row = next(x for x in J.load_features(ROOT) if x["id"] == "H19")
        self.assertEqual(row["status"], "SOURCE_JOURNEYS_TESTED_HOST_NOT_VERIFIED")
        self.assertIn("tools/hub_journeys.py", row["source_paths"])
        self.assertIn("docs/handbook/hub-setup-journeys.md", row["source_paths"])
        self.assertIs(row["native_runtime_verified"], False)
        self.assertIs(row["site_deployed"], False)
        docs = (ROOT / "docs/HUB_FEATURE_READINESS.md").read_text(encoding="utf-8")
        self.assertIn("(discovery/hub-feature-status.json)", docs)
        self.assertIn("(handbook/hub-setup-journeys.md)", docs)

    def test_every_feature_has_seven_explicit_phases_and_holds(self):
        output = J.build_journeys(ROOT)
        self.assertEqual(len(output["journeys"]), 22)
        self.assertEqual([x["id"] for x in output["journeys"]], [f"H{i:02d}" for i in range(22)])
        for row in output["journeys"]:
            with self.subTest(feature=row["id"]):
                self.assertEqual(set(row["phases"]), set(J.PHASES))
                self.assertEqual(row["phases"]["failure"]["status"], "HOLD_UNKNOWN")
                self.assertEqual(row["phases"]["stop"]["status"], "NO_EXTERNAL_EFFECT")
                self.assertEqual(row["phases"]["uninstall"]["status"], "MANUAL_OWNER_VERIFICATION")
                self.assertFalse(row["native_runtime_verified"])
                self.assertFalse(row["site_deployed"])
                self.assertIn("named_test", row["phases"])
                self.assertTrue(row["phases"]["named_test"]["name"])
                self.assertTrue(row["next_verification"])

    def test_all_roles_have_real_install_guide_without_installed_claim(self):
        for role in J.load_roles(ROOT):
            with self.subTest(role=role["id"]):
                result = J.build_journeys(ROOT, feature="H19", role=role["id"])
                self.assertEqual(result["role"]["id"], role["id"])
                self.assertEqual(result["role"]["guide"], "presets/" + role["id"] + "/INSTALL.md")
                self.assertEqual(len(result["journeys"]), 1)
                self.assertFalse(result["native_installed"])

    def test_missing_source_is_not_promoted_to_installable(self):
        tasks = copy.deepcopy(J.load_features(ROOT))
        target = next(t for t in tasks if t["id"] == "H11")
        target["source_paths"] = ["kits/engineering-doors/not-present.json"]
        with self.assertRaisesRegex(ValueError, "SOURCE_PATH_MISSING"):
            J.validate_features(tasks, ROOT)

    def test_path_traversal_and_symlink_references_refused(self):
        tasks = copy.deepcopy(J.load_features(ROOT))
        target = next(t for t in tasks if t["id"] == "H11")
        for unsafe in ("../private", "/etc/passwd", "kits/../../secrets", "C:\\secrets\\key"):
            with self.subTest(path=unsafe):
                target["source_paths"] = [unsafe]
                with self.assertRaisesRegex(ValueError, "SOURCE_PATH_UNSAFE"):
                    J.validate_features(tasks, ROOT)

    def test_duplicate_unknown_and_cyclic_dependencies_refused(self):
        tasks = copy.deepcopy(J.load_features(ROOT))
        tasks[1]["id"] = tasks[0]["id"]
        with self.assertRaisesRegex(ValueError, "FEATURE_IDS"):
            J.validate_features(tasks, ROOT)
        tasks = copy.deepcopy(J.load_features(ROOT))
        tasks[0]["dependencies"] = ["H99"]
        with self.assertRaisesRegex(ValueError, "DEPENDENCY_UNKNOWN"):
            J.validate_features(tasks, ROOT)
        tasks = copy.deepcopy(J.load_features(ROOT))
        tasks[0]["dependencies"] = ["H01"]
        with self.assertRaisesRegex(ValueError, "DEPENDENCY_CYCLE"):
            J.validate_features(tasks, ROOT)

    def test_unknown_role_or_feature_refused(self):
        with self.assertRaisesRegex(ValueError, "ROLE_UNKNOWN"):
            J.build_journeys(ROOT, role="admin<script>")
        with self.assertRaisesRegex(ValueError, "FEATURE_UNKNOWN"):
            J.build_journeys(ROOT, feature="H99")

    def test_cli_json_and_markdown_are_read_only(self):
        for args in (
            ["--verify"],
            ["--feature", "H19", "--role", "learning-coach"],
            ["--all"],
        ):
            with self.subTest(args=args):
                result = subprocess.run(
                    [sys.executable, "-B", str(MODULE), *args],
                    cwd=ROOT, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                payload = json.loads(result.stdout)
                self.assertFalse(payload["native_installed"])
                self.assertFalse(payload["external_effect_authorized"])
        md = subprocess.run(
            [sys.executable, "-B", str(MODULE), "--all", "--format", "markdown"],
            cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(md.returncode, 0, md.stderr)
        self.assertIn("H19", md.stdout)
        self.assertIn("NOT VERIFIED", md.stdout)
        self.assertNotIn("native Muse installed", md.stdout.lower())
        invalid = subprocess.run(
            [sys.executable, "-B", str(MODULE), "--feature", "H99"],
            cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertNotEqual(invalid.returncode, 0)

    def test_documented_journey_is_discoverable_and_non_destructive(self):
        doc = (ROOT / "docs/handbook/hub-setup-journeys.md").read_text(encoding="utf-8")
        index = (ROOT / "docs/README.md").read_text(encoding="utf-8")
        handbook = (ROOT / "docs/handbook/README.md").read_text(encoding="utf-8")
        self.assertIn("tools/hub_journeys.py", doc)
        self.assertIn("handbook/README.md", index)
        self.assertIn("hub-setup-journeys.md", handbook)
        for entrypoint in ("START_HERE.md", "GETTING_STARTED.md", "TERMINAL.md",
                           "COMPANION_HOME.md#open-companion-home",
                           "scripts/run_source_test.py"):
            self.assertIn(entrypoint, doc)
        for recovery in ("same database path", "newly printed token",
                         "reconcile the original result", "Back up local databases"):
            self.assertIn(recovery, doc)
        self.assertIn("read-only", doc)


if __name__ == "__main__":
    unittest.main()
