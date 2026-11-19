"""Editorial regressions for the source-facing GitHub landing and setup guides."""
from pathlib import Path
import re
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
README=ROOT/"README.md"
CONNECTORS=ROOT/"docs"/"connectors"/"README.md"
START=ROOT/"docs"/"v1"/"START_HERE.md"

class EditorialClarity(unittest.TestCase):
    def test_generic_marketing_contrasts_are_absent_from_landing(self):
        body=README.read_text(encoding="utf-8")
        disallowed=(
            "These are more than instruction files",
            "Bring the services you already use into Muse",
            "not a long alphabetical table",
            "four practical paths",
            "Want to learn the system in depth?",
            "Make more of your Muse",
            "organized around what you want to accomplish",
        )
        for phrase in disallowed:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase.lower(),body.lower())

    def test_actions_identify_real_operation_and_expected_result(self):
        body=README.read_text(encoding="utf-8")
        inventory=json.loads((ROOT/"hub/site/downloads.json").read_text(encoding="utf-8"))["counts"]
        starters=json.loads((ROOT/"collections/muse-starters-v1/starters.json").read_bytes())
        connectors=json.loads((ROOT/"docs/connectors/catalog.json").read_bytes())["connectors"]
        release=json.loads((ROOT/"presets/catalog.json").read_bytes())["release"]
        for expected in ("Muse Hub","15 independent assistants",str(inventory["skill"])+" skills",str(inventory["workflow"])+" workflows",
                         f"{len(starters)} task starters",f"{len(connectors)} connectors","START_HERE.md",
                         "tools/muse_collection.py demo data-engineer",
                         "docs/connectors/README.md","docs/GETTING_STARTED.md", "docs/TERMINAL.md",
                         f"releases/tag/{release}", "https://atlas-agents-hub.github.io/muse-ai-agent-presets/downloads.html"):
            with self.subTest(expected=expected):
                self.assertIn(expected.lower(),body.lower())
        self.assertLess(len(body.encode("utf-8")),8000)

if __name__=="__main__":
    unittest.main()
