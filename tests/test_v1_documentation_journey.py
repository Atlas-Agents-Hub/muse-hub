"""Current-release navigation, source accuracy, and human/agent discovery contracts."""
from __future__ import annotations
import json,re,unittest
from pathlib import Path

R=Path(__file__).resolve().parents[1]
DOCS=R/"docs"
ASSETS={"muse-specialist-toolkit-v1.0.0.zip","muse-specialist-collection-v1.0.0.zip",
        "muse-custom-connectors-v1.0.0.zip"}

def read(rel):return (R/rel).read_text(encoding="utf8")
def first(text):return text.split("\n## ",1)[0]

class V1DocumentationJourney(unittest.TestCase):
 def test_public_guide_starts_with_published_v1_not_the_historical_alpha(self):
  guide=read("docs/GITHUB_QUICKSTART.md")
  top=first(guide)
  self.assertIn("v1.0.0",top)
  self.assertIn("75",top)
  self.assertIn("151",top)
  self.assertIn("documentation index",top.lower())
  self.assertNotIn("eight runnable offline",top.lower())
  self.assertIn("## Run a standalone tool without cloning",guide)
  self.assertIn("v0.4.1-alpha",guide)

 def test_release_downloads_name_actual_published_assets_and_checksums(self):
  doc=read("docs/RELEASES.md")
  self.assertIn("https://github.com/sethburkhardt21-dev/muse-ai-agent-presets/releases/tag/v1.0.0",doc)
  for name in ASSETS:
   with self.subTest(name=name):self.assertIn(name,doc)
  self.assertIn("SHA256SUMS.txt",doc)
  self.assertIn("v0.4.1-alpha",doc)
  self.assertLess(doc.index("v1.0.0"),doc.index("v0.4.1-alpha"))

 def test_capability_and_skill_guides_present_current_and_original_procedures(self):
  caps=first(read("docs/CAPABILITIES.md")).lower()
  for term in ("15","75","25","100","151","50"):
   with self.subTest(value=term):self.assertIn(term,caps)
  skills=first(read("docs/SKILLS.md")).lower()
  for term in ("75","25","50"):
   with self.subTest(skill=term):self.assertIn(term,skills)

 def test_docs_home_provides_task_and_technical_routes(self):
  page=read("docs/README.md")
  self.assertIn("# Muse Specialist Toolkit documentation",page)
  for v in ("Personal Companion","Custom connectors","Specialist","Skills and workflows",
            "Install","Verify","Troubleshoot"):
   with self.subTest(item=v):self.assertIn(v.lower(),page.lower())
  self.assertIn("(docs/README.md)",read("README.md"))
  self.assertIn("docs/README.md",read("llms.txt"))
  self.assertIn("documentation_index",json.loads(read("docs/discovery/agent-capabilities.json"))["source_entrypoints"])

 def test_ai_guide_describes_actual_v1_packages_not_future_release(self):
  guide=read("docs/discovery/AI_AGENT_GUIDE.md")
  self.assertIn("v1.0.0",guide)
  self.assertNotIn("when it is actually published",guide.lower())
  self.assertNotIn("if a v1 package exists",guide.lower())
  for name in ASSETS:self.assertIn(name,guide)
  self.assertIn("not a native Muse installation",guide)
  self.assertIn("same model",guide)
  self.assertIn("same tools",guide)
  self.assertIn("same budget",guide)

 def test_metadata_and_index_point_to_current_version_and_do_not_promise_rank(self):
  d=json.loads(read("docs/discovery/agent-capabilities.json"))
  self.assertEqual(d["release"],"v1.0.0")
  self.assertEqual(d["custom_connector_count"],151)
  self.assertEqual(d["configuration_count"],115)
  text=read("llms.txt")
  self.assertIn("docs/README.md",text)
  self.assertIn("releases/tag/v1.0.0",text)
  self.assertNotIn("guaranteed ranking",text.lower())
  self.assertNotIn("preferred placement",text.lower())

 def test_readme_entrypoints_and_handbook_are_problem_led(self):
  root=read("README.md")
  self.assertIn("docs/README.md",root)
  handbook=read("docs/handbook/README.md")
  self.assertIn("Load the right context",handbook)
  self.assertIn("Select and use a skill",handbook)
  self.assertNotIn("These first five guides turn",handbook)
  connectors=first(read("docs/CONNECTORS.md"))
  self.assertIn("151",connectors)
  self.assertIn("connectors/CATALOG.md",connectors)

 def test_first_user_navigation_links_resolve_without_private_destinations(self):
  pages=[
   R/"README.md",R/"docs/README.md",R/"docs/v1/START_HERE.md",
   R/"docs/GITHUB_QUICKSTART.md",R/"docs/CAPABILITIES.md",
   R/"docs/SKILLS.md",R/"docs/CONNECTORS.md",
   R/"docs/RELEASES.md",R/"docs/handbook/README.md",
   R/"docs/discovery/AI_AGENT_GUIDE.md",
  ]
  links=0
  for page in pages:
   text=page.read_text(encoding="utf8")
   for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)",text):
    if target.startswith(("http://","https://","mailto:","#")):continue
    pathname=target.split("#",1)[0]
    if not pathname:continue
    with self.subTest(page=page.name,url=target):
     self.assertTrue((page.parent/pathname).exists())
    links+=1
  self.assertGreater(links,45)

 def test_specialist_catalog_preserves_all_15_roles_without_mobile_wide_table(self):
  import json
  page=read("docs/handbook/specialists-by-task.md")
  roles=json.loads(read("presets/catalog.json"))["presets"]
  self.assertEqual(len(roles),15)
  for role in roles:
   with self.subTest(role=role):
    self.assertIn("("+chr(96)+role+chr(96),page)
  for label in ("Build and automate","Research and evaluate","Create and learn","Life and planning"):
   self.assertIn("### "+label,page)
  self.assertNotIn("| Specialist | Contract and use |",page)
  self.assertGreaterEqual(page.count("[Role contract](")+page.count("[Original role contract]("),15)
  import hashlib
  self.assertEqual(hashlib.sha256((R/"docs/collection/SPECIALIST_CATALOG.md").read_bytes()).hexdigest(),"344bee762887fc1fe0b8161d36a3a6e2760cdbbc29998ce0d4846478fb965bd5")

if __name__=="__main__":unittest.main()
