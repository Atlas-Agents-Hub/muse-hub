"""Editorial regressions for the source-facing GitHub landing and setup guides."""
from pathlib import Path
import re
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
        for expected in (
            "15 AI Specialists","100+ Configurations","150+ Custom Connectors",
            "tools/muse_collection.py demo data-engineer",
            "examples/daily_desk.py",
            "151 custom connectors",
            "docs/connectors/README.md",
            "docs/v1/START_HERE.md",
            "not installed native Muse agents",
            "v0.4.1-alpha",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected.lower(),body.lower())
        self.assertLess(len(body.encode("utf-8")),8000)

    def test_hero_and_headings_do_not_use_empty_marketing_slogans(self):
        body=README.read_text(encoding="utf-8")
        self.assertNotIn("## See it work",body)
        self.assertNotIn("## Get started",body)
        self.assertNotIn("## Explore custom connectors",body)
        self.assertNotRegex(body,r"(?im)^These are more than\b|^Want to learn\b")
        self.assertIn("## For developers",body)

    def test_connector_guide_opens_with_concrete_navigation(self):
        text=CONNECTORS.read_text(encoding="utf-8")
        self.assertNotIn("Make your Muse more useful",text)
        self.assertIn("Browse by category",text)
        self.assertIn("151 connectors",text)
        self.assertIn("CATALOG.md",text)

    def test_first_use_leads_with_a_clear_task_not_a_sales_transition(self):
        text=START.read_text(encoding="utf-8")
        self.assertNotIn("Pick your goal.",text)
        self.assertIn("## 1. Use with Muse",text)
        self.assertIn("## 3. Open Personal Companion",text)
        self.assertIn("DAILY_DESK_VERTICAL_SLICE_PASS",text)

    def test_links_and_specialist_inventory_remain_complete(self):
        import json
        body=README.read_text(encoding="utf-8")
        roles=json.loads((ROOT/"presets"/"catalog.json").read_text(encoding="utf-8"))["presets"]
        self.assertEqual(len(roles),15)
        for role in roles:
            with self.subTest(role=role):
                self.assertEqual(body.count("presets/"+role+"/"),1)
        for page in [README,CONNECTORS,START]:
            for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)",page.read_text(encoding="utf-8")):
                if link.startswith(("https://","http://","mailto:","#")):
                    continue
                target=link.split("#",1)[0]
                if target:
                    self.assertTrue((page.parent/target).exists(),(page.name,link))

if __name__=="__main__":
    unittest.main()
