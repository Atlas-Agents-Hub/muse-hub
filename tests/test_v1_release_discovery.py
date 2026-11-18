"""V1 release links must remain useful after publication, without stale candidate claims."""
from pathlib import Path
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
REPO="https://github.com/atlas-origins/muse-ai-agent-presets"
TAG="v1.1.0"
LEGACY_TAG="v1.0.0"
class ReleaseDiscovery(unittest.TestCase):
 def test_current_public_link_targets_and_specialist_downloads(self):
  d=json.loads((ROOT/"docs/discovery/agent-capabilities.json").read_bytes())
  self.assertEqual(d["release"],TAG)
  self.assertEqual(d["release_publication"],"VERIFY_AT_GITHUB_RELEASES")
  self.assertEqual(d["release_page"],REPO+"/releases/tag/"+TAG)
  self.assertNotIn("sethburkhardt21-dev/muse-ai-agent-presets",d["release_page"])
  self.assertEqual(d["v1_sha256_index"],REPO+"/releases/download/"+TAG+"/SHA256SUMS")
  self.assertEqual(d["sha256_index"],d["v1_sha256_index"])
  expected={"source":"muse-specialist-toolkit-v1.1.0.zip",
            "specialists":"muse-specialists-v1.1.0.zip",
            "skills":"muse-skills-v1.1.0.zip",
            "workflows":"muse-workflows-v1.1.0.zip",
            "starters":"muse-starters-v1.1.0.zip"}
  self.assertEqual(d["v1_assets"],{k:REPO+"/releases/download/"+TAG+"/"+v for k,v in expected.items()})
  self.assertEqual(d["complete_toolkit"],d["v1_assets"]["source"])
  self.assertEqual(d["historical_release"],"v0.4.1-alpha")
  self.assertEqual(d["homepage"],"https://atlas-origins.github.io/muse-ai-agent-presets/")
  self.assertEqual(d["downloads_page"],d["homepage"]+"downloads.html")
  roles=json.loads((ROOT/"presets/catalog.json").read_bytes())["presets"]
  aliases={"data-engineering-architect":"data-engineer",
           "infrastructure-reliability-engineer":"reliability-engineer"}
  self.assertEqual(len(roles),15)
  self.assertEqual(d["specialist_downloads"],{
   role:REPO+"/releases/download/"+TAG+"/muse-"+aliases.get(role,role)+"-"+TAG+".zip"
   for role in roles})
 def test_release_guide_links_to_verified_page_and_no_future_tense(self):
  s=(ROOT/"docs/RELEASES.md").read_text(encoding="utf8")
  self.assertIn(REPO+"/releases/tag/"+TAG,s)
  self.assertIn(REPO+"/releases/download/"+TAG+"/SHA256SUMS",s)
  self.assertIn("releases/tag/"+LEGACY_TAG,s)
  self.assertIn("muse-specialist-toolkit-v1.0.0.zip",s)
  self.assertIn("muse-custom-connectors-v1.0.0.zip",s)
  self.assertIn("muse-specialist-collection-v1.0.0.zip",s)
  self.assertNotIn("version is the target",s.lower())
  self.assertIn("v0.4.1-alpha",s)
if __name__=="__main__":unittest.main()
