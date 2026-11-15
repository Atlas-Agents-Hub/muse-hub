"""Public role-directory depth, engine provenance and accurate source scope."""
import json,re,unittest,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
PAGE=R/"docs/handbook/specialists-by-task.md"
INDEX=R/"docs/discovery/specialist-engine-index.json"
FROZEN=R/"docs/collection/SPECIALIST_CATALOG.md"

class RoleDirectoryDepth(unittest.TestCase):
 def test_15_unique_specialists_and_engine_disclosure(self):
  doc=PAGE.read_text(encoding="utf8")
  roles=json.loads(INDEX.read_bytes())["roles"]
  self.assertEqual(len(roles),15)
  for role in roles:
   rid=role["id"]
   with self.subTest(role=rid):
    self.assertEqual(doc.count("("+chr(96)+rid+chr(96)),1)
    self.assertIn(role["playbook"],doc)
    self.assertGreater(len(role["scope"]),65)
    if role["source_engines"]:
     self.assertIn(role["source_engines"][0],doc)
    else:
     self.assertIn("No standalone security-testing engine",doc)
  self.assertIn("production planner, not an image or video renderer",doc)
  self.assertIn("Claim Gate",doc)
  self.assertIn("Daily Desk",doc)
  self.assertIn("bounded local model training",doc)
  self.assertIn("privacy",doc.lower())
 def test_reader_navigation_uses_engine_aware_directory(self):
  readme=(R/"README.md").read_text(encoding="utf8")
  self.assertIn("docs/handbook/specialists-by-task.md",readme)
  guide=(R/"docs/discovery/AI_AGENT_GUIDE.md").read_text(encoding="utf8")
  self.assertIn("specialists-by-task.md",guide)
 def test_generated_directory_matches_registry(self):
  import subprocess,sys
  proc=subprocess.run([sys.executable,"-B","scripts/render_specialist_directory.py","--check"],
                      cwd=R,capture_output=True,timeout=30)
  self.assertEqual(proc.returncode,0,proc.stderr.decode("utf8","replace"))
  self.assertIn(b"DIRECTORY_CURRENT_15_ROLES",proc.stdout)
 def test_original_legacy_catalog_remains_byte_identical(self):
  self.assertEqual(hashlib.sha256(FROZEN.read_bytes()).hexdigest(),
      "344bee762887fc1fe0b8161d36a3a6e2760cdbbc29998ce0d4846478fb965bd5")
 def test_unpublished_security_engine_not_advertised_as_released(self):
  text=PAGE.read_text("utf8")
  self.assertNotIn("security_assistance.py",text)
  self.assertNotIn("muse_security.py",text)
  data=json.loads(INDEX.read_bytes())
  self.assertEqual(data["native_muse_activation"],"NOT_ASSERTED")
  self.assertEqual(next(x for x in data["roles"] if x["id"]=="adversarial-verifier")["source_engines"],[])
if __name__=="__main__":unittest.main()
