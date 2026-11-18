"""Keep current setup guides connected to discoverable, runnable checks."""
import importlib.util
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("hub_journey_mapping", ROOT / "tools/hub_journeys.py")
journeys = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(journeys)

EXPECTED = {
    "specialists": ["test_role_skills.py"],
    "skills-workflows": ["test_muse_collection.py", "test_portable_skill_export.py"],
    "connectors": ["test_portable_connectors.py"],
    "terminal": [],
    "companion-home": ["test_companion_room_http.py", "test_companion_room_client.py"],
    "daily-desk": ["test_daily_desk.py", "test_daily_desk_http.py"],
    "family-link": ["test_family_envelope.py", "test_family_sourcekit.py"],
    "creative-studio": ["test_creative_production.py", "test_creative_sourcekit.py"],
    "resource-library": ["test_hub_site_deeplink.py"],
}


class SetupTestMappingTests(unittest.TestCase):
    def test_all_nine_current_guides_map_to_their_actual_checks(self):
        source = json.loads((ROOT / "docs/discovery/setup-journeys.json").read_text(encoding="utf-8"))
        self.assertEqual(source["schema"], "muse-hub/setup-guides/v1")
        self.assertEqual({item["id"] for item in source["features"]}, set(EXPECTED))
        for feature, filenames in EXPECTED.items():
            with self.subTest(feature=feature):
                result = journeys.build_journeys(ROOT, feature=feature)
                self.assertEqual(len(result["journeys"]), 1)
                row = result["journeys"][0]
                self.assertEqual(row["id"], feature)
                self.assertTrue((ROOT / row["guide"]).is_file())
                expected = ["python -B scripts/run_source_test.py " + name for name in filenames]
                self.assertEqual(row["phases"]["named_test"]["commands"], expected)
                self.assertTrue(row["phases"]["named_test"]["instruction"])
                recorded = next(item for item in source["features"] if item["id"] == feature)
                self.assertEqual(recorded["tests"], ["tests/" + name for name in filenames])
                for filename in filenames:
                    self.assertTrue((ROOT / "tests" / filename).is_file())

    def test_advertised_commands_run_without_installed_package_or_pythonpath(self):
        env = dict(os.environ)
        env.pop("PYTHONPATH", None)
        env["PYTHONNOUSERSITE"] = "1"
        for feature in ("specialists", "companion-home"):
            with self.subTest(feature=feature):
                row = journeys.build_journeys(ROOT, feature=feature)["journeys"][0]
                argv = shlex.split(row["phases"]["named_test"]["commands"][0])
                self.assertEqual(argv.pop(0), "python")
                result = subprocess.run([sys.executable, *argv], cwd=ROOT, env=env,
                                        stdin=subprocess.DEVNULL, capture_output=True,
                                        text=True, encoding="utf-8", timeout=60)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertRegex(result.stderr, r"Ran [1-9][0-9]* tests?")

    def test_terminal_guide_supplies_connection_and_readback_instructions(self):
        row = journeys.build_journeys(ROOT, feature="terminal")["journeys"][0]
        self.assertEqual(row["phases"]["named_test"]["commands"], [])
        self.assertTrue(row["phases"]["health"]["instruction"])
        self.assertTrue((ROOT / row["guide"]).is_file())

    def test_current_journey_schema_contains_all_lifecycle_steps(self):
        result = journeys.build_journeys(ROOT)
        self.assertEqual(result["schema"], "muse-hub/setup-journeys/v2")
        self.assertEqual(result["status"], "SETUP_GUIDES_READY")
        self.assertEqual(len(result["journeys"]), 9)
        self.assertEqual({row["id"] for row in result["journeys"]}, set(EXPECTED))
        for row in result["journeys"]:
            self.assertEqual(set(row["phases"]), {"install", "configure", "health", "named_test", "failure", "stop", "uninstall"})
            self.assertTrue(all(phase["instruction"] for phase in row["phases"].values()))


if __name__ == "__main__":
    unittest.main()
