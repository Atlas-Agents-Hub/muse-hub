"""Keep existing source tests discoverable without promoting native acceptance."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("hub_journey_mapping", ROOT / "tools/hub_journeys.py")
journeys = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(journeys)

class SourceTestMappingTests(unittest.TestCase):
    def assert_mapping(self, feature, filename):
        result = journeys.build_journeys(ROOT, feature=feature)
        row = result["journeys"][0]
        test = row["phases"]["named_test"]
        self.assertEqual(test["status"], "SOURCE_TEST_AVAILABLE_NOT_RUN")
        self.assertEqual(test["name"], "tests/" + filename)
        self.assertEqual(test["command"], "python -B -m unittest discover -s tests -p " + filename)
        self.assertTrue((ROOT / test["name"]).is_file())
        self.assertFalse(row["native_runtime_verified"])
        self.assertFalse(row["site_deployed"])
        self.assertFalse(result["external_effect_authorized"])

    def test_h03_route_comparison_test_is_discoverable(self):
        self.assert_mapping("H03", "test_muse_route_compat_h03.py")

    def test_h14_rooms_test_is_discoverable(self):
        self.assert_mapping("H14", "test_companion_home_h14_h17.py")

    def test_h15_motion_contract_test_is_discoverable(self):
        self.assert_mapping("H15", "test_companion_home_h14_h17.py")

    def test_h16_arcade_contract_test_is_discoverable(self):
        self.assert_mapping("H16", "test_companion_home_h14_h17.py")

    def test_h17_sqlite_test_is_discoverable(self):
        self.assert_mapping("H17", "test_companion_home_h14_h17.py")

    def test_unmapped_native_routes_stay_unverified(self):
        for feature in ("H04", "H05", "H06", "H07", "H08", "H09", "H10", "H13", "H18", "H20"):
            with self.subTest(feature=feature):
                row = journeys.build_journeys(ROOT, feature=feature)["journeys"][0]
                self.assertEqual(row["phases"]["named_test"]["status"], "NOT_VERIFIED")
                self.assertIsNone(row["phases"]["named_test"]["command"])
                self.assertFalse(row["native_runtime_verified"])

    def test_all_journeys_preserve_source_only_status(self):
        result = journeys.build_journeys(ROOT)
        self.assertEqual(len(result["journeys"]), 22)
        self.assertEqual(result["status"], "SOURCE_JOURNEY_PLAN_NOT_INSTALLATION")
        self.assertFalse(result["native_installed"])
        self.assertFalse(result["external_effect_authorized"])
        self.assertFalse(result["site_deployed"])

if __name__ == "__main__":
    unittest.main()
