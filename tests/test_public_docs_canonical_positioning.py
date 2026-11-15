"""Reader-facing V1 metadata and canonical-link acceptance."""
import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OLD="sethburkhardt21-dev/muse-ai-agent-presets"
CURRENT=["CHANGELOG.md","docs/GITHUB_QUICKSTART.md","docs/v1/START_HERE.md"]
SLUGS=json.loads((ROOT/"presets/catalog.json").read_bytes())["presets"]

class PublicDocsCanonicalPositioning(unittest.TestCase):
 def test_current_docs_reference_organization_owner(self):
  for path in CURRENT:
   with self.subTest(path=path):
    text=(ROOT/path).read_text("utf8")
    self.assertNotIn(OLD,text)
    self.assertIn("atlas-origins/muse-ai-agent-presets",text)
 def test_readme_has_single_clear_specialist_directory_route(self):
  text=(ROOT/"README.md").read_text("utf8")
  self.assertLess(len(text.encode()),8000)
  self.assertIn("docs/handbook/specialists-by-task.md",text)
  self.assertIn("docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md",text)
  self.assertNotIn("or the [full specialist catalog]",text)
  for slug in SLUGS:self.assertIn("presets/"+slug+"/",text)
 def test_ai_guide_covers_every_specialist(self):
  text=(ROOT/"docs/discovery/AI_AGENT_GUIDE.md").read_text("utf8")
  for slug in SLUGS:
   with self.subTest(slug=slug):
    self.assertIn("presets/"+slug+"/",text)
  self.assertIn("specialist-engine-index.json",text)
  self.assertIn("SPECIALIST_SCOPE_AND_ENGINES.md",text)
  self.assertNotIn("security_assistance.py",text)
 def test_first_use_routes_to_engine_aware_guide(self):
  text=(ROOT/"docs/v1/START_HERE.md").read_text("utf8")
  self.assertIn("SPECIALIST_SCOPE_AND_ENGINES.md",text)
  self.assertIn("specialists-by-task.md",text)
 def test_discovery_index_contains_canonical_website(self):
  text=(ROOT/"llms.txt").read_text("utf8")
  self.assertIn("https://atlas-origins.github.io/kits/",text)
  cap=json.loads((ROOT/"docs/discovery/agent-capabilities.json").read_bytes())
  self.assertIn("specialist_engine_index",cap)
  self.assertEqual(cap["custom_connector_count"],151)
 def test_architecture_describes_both_procedure_layers(self):
  page=(ROOT/"docs/ARCHITECTURE.md").read_text("utf8")
  for item in ("75 developed","25 workflows","100 task","50 unique","SPECIALIST_SCOPE_AND_ENGINES.md"):
   with self.subTest(value=item):self.assertIn(item,page)
 def test_installation_guide_starts_with_current_v1_package_choices(self):
  page=(ROOT/"docs/INSTALL_AND_PERSISTENCE.md").read_text("utf8")
  self.assertIn("v1.0.0",page)
  self.assertIn("muse-specialist-collection-v1.0.0.zip",page)
  self.assertIn("v0.4.1-alpha",page)
 def test_skills_guide_prefers_engine_aware_directory(self):
  page=(ROOT/"docs/SKILLS.md").read_text("utf8")
  self.assertIn("handbook/specialists-by-task.md",page)
  self.assertIn("75 developed",page)
  self.assertIn("25 workflows",page)
 def test_historical_frozen_source_is_still_byte_identical(self):
  import hashlib
  baseline=json.loads((ROOT/"collections/muse-starters-v1/PUBLIC_BASELINE.json").read_bytes())
  self.assertEqual(len(baseline["files"]),198)
  for name,digest in baseline["files"].items():
   with self.subTest(path=name):
    self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),digest)
if __name__=="__main__":unittest.main()
