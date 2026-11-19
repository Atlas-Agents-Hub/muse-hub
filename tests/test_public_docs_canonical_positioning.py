"""Reader-facing V1 metadata and canonical-link acceptance."""
import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CURRENT=["CHANGELOG.md","docs/GITHUB_QUICKSTART.md","docs/v1/START_HERE.md"]
SLUGS=json.loads((ROOT/"presets/catalog.json").read_bytes())["presets"]

def current_collection():
    import importlib.util
    spec=importlib.util.spec_from_file_location('current_library_docs', ROOT/'tools/muse_collection.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module.load_collection()

class PublicDocsCanonicalPositioning(unittest.TestCase):
 def test_current_docs_reference_organization_owner(self):
     repository_links=[]
     for path in CURRENT:
         with self.subTest(path=path):
             text=(ROOT/path).read_text("utf8")
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
     connectors=json.loads((ROOT/"docs/connectors/catalog.json").read_bytes())["connectors"]
     self.assertEqual(cap["custom_connector_count"],len(connectors))
 def test_architecture_describes_both_procedure_layers(self):
  page=(ROOT/"docs/ARCHITECTURE.md").read_text("utf8")
  for item in ("skill","workflow","task starter","50 unique","SPECIALIST_SCOPE_AND_ENGINES.md"):
   with self.subTest(value=item):self.assertIn(item,page)
 def test_installation_guide_starts_with_current_package_setup(self):
     page=(ROOT/"docs/INSTALL_AND_PERSISTENCE.md").read_text("utf8")
     for term in ("DOWNLOAD_A_SPECIALIST.md", "START_HERE.md", "three focused subchats",
                  "Windows", "macOS", "Linux", "Python 3.12+"):
         self.assertIn(term,page)
     downloads=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text("utf8")
     release=json.loads((ROOT/"presets/catalog.json").read_bytes())["release"]
     self.assertIn("releases/download/"+release+"/",downloads)
     self.assertIn("releases/download/"+release+"/SHA256SUMS",downloads)
 def test_skills_guide_reaches_current_methods_and_tools(self):
     page=(ROOT/"docs/SKILLS.md").read_text("utf8")
     self.assertIn("handbook/specialists-by-task.md",page)
     collection=current_collection()
     self.assertIn(str(len(collection['skills']))+" skills",page)
     self.assertIn(str(len(collection['workflows']))+" workflows",page)
     self.assertIn("WORKFLOWS.md",page)
     self.assertIn("SKILL_INDEX.md",page)
 def test_current_role_guides_preserve_the_catalog_setup_paths(self):
     roles=json.loads((ROOT/'presets/catalog.json').read_bytes())['presets']
     for role in roles:
         with self.subTest(role=role):
             install=ROOT/'presets'/role/'INSTALL.md'
             overview=ROOT/'presets'/role/'README.md'
             self.assertTrue(install.is_file())
             self.assertTrue(overview.is_file())
             self.assertIn('START_HERE.md',install.read_text())
             self.assertIn('INSTALL.md',overview.read_text())
if __name__=="__main__":unittest.main()
