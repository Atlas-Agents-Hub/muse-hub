"""Public entry points describe tasks, packages, and the next action."""
from pathlib import Path
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]

class ProductPositioningTests(unittest.TestCase):
    def test_readme_leads_with_product_and_usable_entrypoints(self):
        text=(ROOT/"README.md").read_text(encoding="utf-8")
        hero=text.split("\n## ",1)[0]
        for term in ("Muse Hub","15 independent assistants","75 skills","25 workflows","100 task starters","151 connectors"):
            self.assertIn(term,hero)
        for path in ("docs/DOWNLOAD_A_SPECIALIST.md","docs/GETTING_STARTED.md","docs/TERMINAL.md"):
            self.assertIn(path,text)
        self.assertIn("releases/tag/v1.2.0",text)
        self.assertIn("https://atlas-origins.github.io/muse-ai-agent-presets/",text)
        prose=re.sub(r"\]\([^)]+\)","]()",text)
        self.assertNotRegex(prose,r"\b(?:H\d{2}|S[1-5])\b")
        for old in ("source-only","not installed native","not deployed","remain a draft","not additional agents"):
            self.assertNotIn(old,prose.lower())
