"""All 15 specialist descriptions reflect their full role methods, not a tiny demo."""
from pathlib import Path
import re
import unittest
import json

ROOT=Path(__file__).resolve().parents[1]
README=ROOT/"README.md"
CREATIVE=ROOT/"docs"/"collection"/"CREATIVE_STUDIO_SCOPE.md"
FROZEN_CREATIVE=ROOT/"presets"/"creative-studio"/"README.md"

REQUIRED={
 "software-engineer": ("build","debug","regression"),
 "data-engineering-architect": ("data","schema","migration"),
 "automation-engineer": ("workflow","dependencies","retry"),
 "infrastructure-reliability-engineer": ("reliability","incident","recovery"),
 "research-evaluator": ("research","evidence","evaluation"),
 "claims-adjudicator": ("claims","evidence","verdict"),
 "adversarial-verifier": ("security","failures","fixes"),
 "reverse-engineering-researcher": ("software","protocols","observed"),
 "creative-studio": ("visual","animation","interactive","render","continuity"),
 "product-interface-designer": ("product","user journeys","accessibility"),
 "model-builder": ("model","training","evaluate"),
 "learning-coach": ("study","practice","scored"),
 "personal-companion": ("daily","routines","privacy"),
 "garden-companion": ("plants","seasonal","care"),
 "coordinator": ("complex","specialist","handoffs"),
}

class RolePositioningTests(unittest.TestCase):
 def test_exact_role_inventory_and_role_scope(self):
  source=README.read_text(encoding="utf8")
  area=source.split("## Find your specialist",1)[1].split("## Try the tools",1)[0]
  registry=json.loads((ROOT/"presets/catalog.json").read_text(encoding="utf8"))
  self.assertEqual(set(registry["presets"]),set(REQUIRED))
  for role,required in REQUIRED.items():
   with self.subTest(role=role):
    regex=r"(?m)^- \*\*\[[^\]]+\]\(presets/"+re.escape(role)+r"/\)\*\* - (.+)$"
    m=re.search(regex,area)
    self.assertIsNotNone(m,role)
    if not m:continue
    summary=m.group(1).lower()
    for word in required:self.assertIn(word,summary)
    self.assertGreater(len(summary),85)
    self.assertNotRegex(summary,r"[a-z][?][a-z]")
  self.assertEqual(len(re.findall(r"(?m)^- \*\*\[[^\]]+\]\(presets/[^)]+/\)\*\*",area)),15)
  self.assertLess(len(source.encode("utf8")),8000)

 def test_no_more_roles_reduced_to_only_demo_operations(self):
  body=README.read_text(encoding="utf8").lower()
  for phrase in (
   "produce briefs, storyboards and continuity records",
   "review datasets, experiments and evaluation metrics",
   "audit ui states, control labels and user journeys",
   "validate dependencies and review retry rules",
   "map dependencies, decisions and handoffs",
   "record plant observations and track care routines",
  ):
   with self.subTest(phrase=phrase):
    self.assertNotIn(phrase,body)

 def test_creative_studio_scope_distinguishes_role_from_bundled_planner(self):
  import hashlib
  self.assertEqual(hashlib.sha256(FROZEN_CREATIVE.read_bytes()).hexdigest(),
      "27de0639a4a2867c0aa8e2b5d5ca4feadd7fda157e513317195cd12caafab48c")
  body=CREATIVE.read_text(encoding="utf8").lower()
  for phrase in ("visual","animation","interactive","asset","render","continuity","delivery",
                 "production planner","not an image or video renderer","creative_studio_demo.py"):
   with self.subTest(term=phrase):self.assertIn(phrase,body)

 def test_role_intro_links_to_concrete_implemented_capabilities(self):
  body=README.read_text(encoding="utf8")
  self.assertIn("[capability guide](docs/capabilities.md)",body.lower())
  self.assertIn("## Try the tools",body)
  self.assertIn("python -B examples/daily_desk.py",body)

if __name__=="__main__":unittest.main()
