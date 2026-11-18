"""Reader-facing V1 metadata and canonical-link acceptance."""
import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OLD="sethburkhardt21-dev/muse-ai-agent-presets"
CURRENT=["CHANGELOG.md","docs/GITHUB_QUICKSTART.md","docs/v1/START_HERE.md"]
SLUGS=json.loads((ROOT/"presets/catalog.json").read_bytes())["presets"]

class PublicDocsCanonicalPositioning(unittest.TestCase):
 def test_current_docs_reference_organization_owner(self):
     repository_links=[]
     for path in CURRENT:
         with self.subTest(path=path):
             text=(ROOT/path).read_text("utf8")
             self.assertNotIn(OLD,text)
             repository_links.extend(re.findall(r'https://github[.]com/[^/]+/muse-ai-agent-presets',text))
     self.assertTrue(repository_links)
     self.assertEqual(set(repository_links),{"https://github.com/atlas-origins/muse-ai-agent-presets"})
 def test_readme_has_clear_specialist_directory_and_setup_routes(self):
     text=(ROOT/"README.md").read_text("utf8")
     self.assertLess(len(text.encode()),8000)
     self.assertIn("docs/handbook/specialists-by-task.md",text)
     self.assertIn("docs/DOWNLOAD_A_SPECIALIST.md",text)
     self.assertNotIn("or the [full specialist catalog]",text)
     directory=(ROOT/"docs/handbook/specialists-by-task.md").read_text("utf8")
     self.assertIn("../collection/SPECIALIST_SCOPE_AND_ENGINES.md",directory)
     for slug in SLUGS:self.assertIn("presets/"+slug+"/INSTALL.md",text)
 def test_ai_guide_reaches_every_specialist_and_engine_reference(self):
     text=(ROOT/"docs/discovery/AI_AGENT_GUIDE.md").read_text("utf8")
     self.assertIn("../DOWNLOAD_A_SPECIALIST.md",text)
     downloads=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text("utf8")
     for slug in SLUGS:
         with self.subTest(slug=slug):
             self.assertIn("presets/"+slug+"/INSTALL.md",downloads)
     self.assertIn("../collection/SPECIALIST_SCOPE_AND_ENGINES.md",text)
     methods=(ROOT/"docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md").read_text("utf8")
     self.assertIn("specialist-engine-index.json",methods)
     self.assertNotIn("security_assistance.py",text)
 def test_first_use_routes_to_current_setup_and_tool_guides(self):
     text=(ROOT/"docs/v1/START_HERE.md").read_text("utf8")
     for target in ("../DOWNLOAD_A_SPECIALIST.md", "../GETTING_STARTED.md",
                    "../TERMINAL.md", "../SKILLS.md", "../GITHUB_QUICKSTART.md"):
         self.assertIn(target,text)
         self.assertTrue((ROOT/"docs/v1"/target).is_file())
     skills=(ROOT/"docs/SKILLS.md").read_text("utf8")
     self.assertIn("handbook/specialists-by-task.md",skills)
 def test_discovery_index_contains_canonical_website(self):
     text=(ROOT/"llms.txt").read_text("utf8")
     site="https://atlas-origins.github.io/muse-ai-agent-presets/"
     self.assertIn(site,text)
     self.assertIn(site+"downloads.html",text)
     cap=json.loads((ROOT/"docs/discovery/agent-capabilities.json").read_bytes())
     self.assertEqual(cap["homepage"],site)
     self.assertIn("specialist_engine_index",cap)
     self.assertEqual(cap["custom_connector_count"],151)
 def test_architecture_describes_both_procedure_layers(self):
  page=(ROOT/"docs/ARCHITECTURE.md").read_text("utf8")
  for item in ("75 developed","25 workflows","100 task","50 unique","SPECIALIST_SCOPE_AND_ENGINES.md"):
   with self.subTest(value=item):self.assertIn(item,page)
 def test_installation_guide_starts_with_current_package_setup(self):
     page=(ROOT/"docs/INSTALL_AND_PERSISTENCE.md").read_text("utf8")
     for term in ("DOWNLOAD_A_SPECIALIST.md", "START_HERE.md", "three focused subchats",
                  "Windows", "macOS", "Linux", "Python 3.12+"):
         self.assertIn(term,page)
     downloads=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text("utf8")
     self.assertIn("releases/download/v1.1.1/",downloads)
     self.assertIn("releases/download/v1.1.1/SHA256SUMS",downloads)
 def test_skills_guide_reaches_current_methods_and_tools(self):
     page=(ROOT/"docs/SKILLS.md").read_text("utf8")
     self.assertIn("handbook/specialists-by-task.md",page)
     self.assertIn("75 skills",page)
     self.assertIn("25 workflows",page)
     self.assertIn("WORKFLOWS.md",page)
     self.assertIn("SKILL_INDEX.md",page)
 def test_historical_frozen_source_is_still_byte_identical(self):
     import hashlib
     baseline=json.loads((ROOT/"collections/muse-starters-v1/PUBLIC_BASELINE.json").read_bytes())
     revisions=json.loads((ROOT/"collections/muse-starters-v1/PUBLIC_REVISIONS.json").read_bytes())
     self.assertEqual(revisions["schema"],"muse-collection-reviewed-source-revisions/v1")
     revised={row["original_path"]:row for row in revisions["entries"] if row["ledger"]=="public"}
     self.assertEqual(len(baseline["files"]),198)
     preserved_roles=0
     for name,digest in baseline["files"].items():
         with self.subTest(path=name):
             if name in revised:
                 revision=revised[name]
                 self.assertEqual(revision["historical_sha256"],digest)
                 self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),revision["current_sha256"])
                 path=ROOT/revision["archive_path"]
             elif name.startswith("presets/") and name.endswith("/INSTALL.md"):
                 path=ROOT/"docs/history/v1-install"/(Path(name).parent.name+".txt")
                 preserved_roles+=1
             elif name.startswith("presets/") and name.endswith("/README.md"):
                 path=ROOT/"docs/history/v1-role-readmes"/(Path(name).parent.name+".txt")
                 preserved_roles+=1
             else:
                 path=ROOT/name
             self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),digest)
     self.assertEqual(preserved_roles,30)
     for archive in ("v1-install","v1-role-readmes"):
         history=json.loads((ROOT/"docs/history"/archive/"MIGRATION_MANIFEST.json").read_text())
         self.assertEqual(len(history["entries"]),15)
         for entry in history["entries"]:
             self.assertEqual(hashlib.sha256((ROOT/entry["archive_path"]).read_bytes()).hexdigest(),entry["sha256"])
if __name__=="__main__":unittest.main()
