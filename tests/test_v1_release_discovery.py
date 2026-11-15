"""V1 release links must remain useful after publication, without stale candidate claims."""
from pathlib import Path
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
REPO="https://github.com/atlas-origins/muse-ai-agent-presets"
TAG="v1.0.0"
class ReleaseDiscovery(unittest.TestCase):
 def test_v1_public_link_targets_and_legacy_release_separated(self):
  d=json.loads((ROOT/"docs/discovery/agent-capabilities.json").read_bytes())
  self.assertEqual(d["release"],TAG)
  self.assertEqual(d["release_publication"],"VERIFY_AT_GITHUB_RELEASES")
  self.assertEqual(d["release_page"],REPO+"/releases/tag/"+TAG)
  self.assertNotIn("sethburkhardt21-dev/muse-ai-agent-presets",d["release_page"])
  self.assertEqual(d["v1_sha256_index"],REPO+"/releases/download/"+TAG+"/SHA256SUMS.txt")
  expected={"source":"muse-specialist-toolkit-v1.0.0.zip",
            "connectors":"muse-custom-connectors-v1.0.0.zip",
            "collection":"muse-specialist-collection-v1.0.0.zip"}
  self.assertEqual(d["v1_assets"],{k:REPO+"/releases/download/"+TAG+"/"+v for k,v in expected.items()})
  self.assertIn("v0.4.1-alpha",d["sha256_index"])
 def test_release_guide_links_to_verified_page_and_no_future_tense(self):
  s=(ROOT/"docs/RELEASES.md").read_text(encoding="utf8")
  self.assertIn("releases/tag/v1.0.0",s)
  self.assertIn("muse-specialist-toolkit-v1.0.0.zip",s)
  self.assertIn("muse-custom-connectors-v1.0.0.zip",s)
  self.assertIn("muse-specialist-collection-v1.0.0.zip",s)
  self.assertNotIn("version is the target",s.lower())
  self.assertIn("v0.4.1-alpha",s)
if __name__=="__main__":unittest.main()
