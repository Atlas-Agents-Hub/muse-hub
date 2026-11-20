"""Public entry points describe tasks, packages, and the next action."""
from pathlib import Path
import re
import json
import unittest
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from muse_collection import load_collection
ROOT=Path(__file__).resolve().parents[1]

class ProductPositioningTests(unittest.TestCase):
    def test_readme_leads_with_product_and_usable_entrypoints(self):
        text=(ROOT/"README.md").read_text(encoding="utf-8")
        hero=text.split("\n## ",1)[0]
        data=load_collection()
        connectors=json.loads((ROOT/"docs/connectors/catalog.json").read_bytes())["connectors"]
        guides=json.loads((ROOT/"collections/tool-guides.json").read_bytes())["guides"]
        release=json.loads((ROOT/"presets/catalog.json").read_bytes())["release"]
        for term in ("Muse Hub","15 independent assistants","5,200+ skills","nearly 400 workflows","50+ tool guides","550+ task starters",f"{len(connectors)} connectors"):
            self.assertIn(term,hero)
        for path in ("docs/DOWNLOAD_A_SPECIALIST.md","docs/GETTING_STARTED.md","docs/TERMINAL.md"):
            self.assertIn(path,text)
        self.assertIn(f"releases/tag/{release}",text)
        self.assertIn("https://atlas-agents-hub.github.io/muse-hub/",text)
        prose=re.sub(r"\]\([^)]+\)","]()",text)
        self.assertNotRegex(prose,r"\b(?:H\d{2}|S[1-5])\b")
        for old in ("source-only","not installed native","not deployed","remain a draft","not additional agents"):
            self.assertNotIn(old,prose.lower())
