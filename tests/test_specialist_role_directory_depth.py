"""Public role-directory depth, engine provenance and accurate source scope."""
import json,re,unittest,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
PAGE=R/"docs/handbook/specialists-by-task.md"
INDEX=R/"docs/discovery/specialist-engine-index.json"
FROZEN=R/"docs/collection/SPECIALIST_CATALOG.md"

class RoleDirectoryDepth(unittest.TestCase):
 def test_15_unique_specialists_and_actual_tools_are_described(self):
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
                 self.assertIn("defensive testing playbook",doc)
                 self.assertIn("authorized target",doc)
     for term in ("textual storyboards", "chosen render tools", "Claim Gate", "Daily Desk",
                  "bounded local model training", "privacy"):
         self.assertIn(term,doc)
 def test_reader_navigation_reaches_role_methods_and_setup(self):
     readme=(R/"README.md").read_text(encoding="utf8")
     self.assertIn("docs/handbook/specialists-by-task.md",readme)
     guide=(R/"docs/discovery/AI_AGENT_GUIDE.md").read_text(encoding="utf8")
     self.assertIn("../DOWNLOAD_A_SPECIALIST.md",guide)
     self.assertIn("../collection/SPECIALIST_SCOPE_AND_ENGINES.md",guide)
 def test_generated_directory_matches_registry(self):
  import subprocess,sys
  proc=subprocess.run([sys.executable,"-B","scripts/render_specialist_directory.py","--check"],
                      cwd=R,capture_output=True,timeout=30)
  self.assertEqual(proc.returncode,0,proc.stderr.decode("utf8","replace"))
  self.assertIn(b"DIRECTORY_CURRENT_15_ROLES",proc.stdout)
 def test_current_catalog_lists_all_registered_roles(self):
     current=FROZEN.read_text(encoding='utf8')
     roles=json.loads((R/'collections/muse-starters-v1/specialists.json').read_bytes())
     self.assertEqual(len(roles),15)
     for role in roles:self.assertIn(role['id'],current)
 def test_security_directory_links_existing_methods(self):
  text=PAGE.read_text("utf8")
  self.assertNotIn("security_assistance.py",text)
  self.assertNotIn("muse_security.py",text)
  data=json.loads(INDEX.read_bytes())
  role=next(x for x in data["roles"] if x["id"]=="adversarial-verifier")
  self.assertTrue((R/role["playbook"]).is_file())
  self.assertTrue(role["real_work"])
  for path in role["source_engines"]:
   self.assertTrue((R/path).is_file())
if __name__=="__main__":unittest.main()
