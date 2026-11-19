"""Current release discovery and setup paths describe shipped resources."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "docs/discovery/hub-feature-status.json"
README = ROOT / "docs/HUB_FEATURE_READINESS.md"


class FeatureDiscoveryContract(unittest.TestCase):
    def test_current_release_and_setup_catalog_are_findable(self):
        current = json.loads(CURRENT.read_bytes())
        release = json.loads((ROOT / "presets/catalog.json").read_bytes())["release"]
        self.assertEqual(current["schema"], "muse-hub/distribution-links/v1")
        self.assertEqual(current["release"], release)
        self.assertEqual(current["release_url"], "https://github.com/Atlas-Agents-Hub/muse-hub/releases/tag/" + release)
        self.assertEqual(current["downloads_url"], "https://atlas-agents-hub.github.io/muse-hub/downloads.html")
        catalog = CURRENT.parent / current["setup_guides"]
        value = json.loads(catalog.read_bytes())
        self.assertEqual(value["schema"], "muse-hub/setup-guides/v1")
        self.assertEqual(len(value["features"]), len({item["id"] for item in value["features"]}))
        for item in value["features"]:
            self.assertTrue((ROOT / item["guide"]).is_file())
            self.assertTrue(item["instructions"]["failure"])
            self.assertTrue(item["instructions"]["uninstall"])

    def test_feature_guide_links_setup_and_current_release(self):
        text = README.read_text()
        for target in ("DOWNLOAD_A_SPECIALIST.md", "GETTING_STARTED.md", "SKILLS.md", "WORKFLOWS.md", "TERMINAL.md", "connectors/README.md", "FAMILY_LINK.md", "COMPANION_HOME.md", "spaces/DAILY_DESK.md", "handbook/hub-setup-journeys.md", "RELEASES.md", "discovery/hub-feature-status.json"):
            with self.subTest(target=target):
                self.assertIn("(" + target + ")", text)
                self.assertTrue((README.parent / target).is_file())
        self.assertIn("https://atlas-agents-hub.github.io/muse-hub/", text)


if __name__ == "__main__":
    unittest.main()
