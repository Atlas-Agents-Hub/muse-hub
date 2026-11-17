"""Public copy must distinguish running offline tools from installing native agents."""
from __future__ import annotations
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
README=(ROOT/"README.md")
QUICK=(ROOT/"docs/GITHUB_QUICKSTART.md")
RELEASES=(ROOT/"docs/RELEASES.md")

class ProductPositioningTests(unittest.TestCase):
    def test_readme_leads_with_runnable_tools(self):
        value=README.read_text(encoding="utf-8")
        hero=value.split("## Start with an assistant",1)[0].lower()
        for term in ("muse hub","15 independent assistants","75 skills","25 workflows",
                     "100 task starters","151 connector records"):
            self.assertIn(term,hero)
        self.assertNotIn("muse specialist toolkit",hero)
        self.assertIn("v0.4.1-alpha",value.lower())
        self.assertIn("v1.1.0",value.lower())
        self.assertIn("draft",value.lower())
        self.assertIn("not installed native muse agents",value.lower())

if __name__=="__main__":
    unittest.main()
