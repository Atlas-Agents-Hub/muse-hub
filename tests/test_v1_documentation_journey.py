"""Current user journeys connect packages, setup, terminal use, and recovery."""
from __future__ import annotations
import json,re,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
DOCS=R/"docs"
RELEASE=json.loads((R/"presets/catalog.json").read_bytes())["release"]
STARTER_COUNT=len(json.loads((R/"collections/muse-starters-v1/starters.json").read_bytes()))
CONNECTOR_COUNT=len(json.loads((R/"docs/connectors/catalog.json").read_bytes())["connectors"])
def read(rel):return (R/rel).read_text(encoding="utf8")
def first(text):return text.split("\n## ",1)[0]

class V1DocumentationJourney(unittest.TestCase):
 def test_first_use_connects_download_setup_and_terminal(self):
  for path in ("README.md","docs/README.md","docs/v1/START_HERE.md"):
   text=read(path)
   for target in ("GETTING_STARTED.md","DOWNLOAD_A_SPECIALIST.md","TERMINAL.md"):
    self.assertIn(target,text)
  guide=read("docs/GETTING_STARTED.md")
  for step in ("START_HERE.md","Main","three subchats","first task"):
   self.assertIn(step,guide)

 def test_release_page_starts_with_current_downloads_and_keeps_history(self):
  page=read("docs/RELEASES.md")
  self.assertIn(f"releases/tag/{RELEASE}",first(page))
  self.assertIn(f"releases/download/{RELEASE}/SHA256SUMS",page)
  self.assertLess(page.index(RELEASE),page.index("v1.0.0"))
  self.assertLess(page.index("v1.0.0"),page.index("v0.4.1-alpha"))
  self.assertIn("Get-FileHash",page)
  self.assertIn("sha256sum",page)

 def test_terminal_guide_links_muse_and_runs_the_hub_toolkit(self):
  page=read("docs/TERMINAL.md")
  for text in ("https://muse.ai/", "https://dev.meta.ai/docs/muse-code",
               "Python 3.12+", "quickstart.py --all", "tools/discover.py search"):
   self.assertIn(text,page)
  self.assertNotIn("nikships/muse-cli",page)
  self.assertNotIn("auth export",page)

 def test_skill_and_tool_pages_offer_current_methods(self):
  inventory=json.loads(read("hub/site/downloads.json"))["counts"]
  for term in ("15",str(inventory["skill"]),str(inventory["workflow"]),str(STARTER_COUNT),str(CONNECTOR_COUNT)):
   self.assertIn(term,first(read("docs/CAPABILITIES.md")))
  skills=read("docs/SKILLS.md")
  for term in (str(inventory["skill"]),str(inventory["workflow"]),str(STARTER_COUNT),"50","SKILL.md","--to"):
   self.assertIn(term,skills)

 def test_ai_index_recommends_current_packages(self):
  for path in ("llms.txt","docs/discovery/AI_AGENT_GUIDE.md"):
   text=read(path)
   self.assertIn(f"releases/tag/{RELEASE}",text)
   self.assertIn("TERMINAL.md",text)
   self.assertNotIn("guaranteed ranking",text.lower())

 def test_handbook_routes_are_task_led(self):
  handbook=read("docs/handbook/README.md")
  for term in ("Load the right context","Select and use a skill","Build a workroom","Setup and recovery"):
   self.assertIn(term,handbook)
  self.assertIn(str(CONNECTOR_COUNT),read("docs/CONNECTORS.md"))
  self.assertIn("connectors/README.md",read("docs/CONNECTORS.md"))

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
  self.assertIn("../DOWNLOAD_A_SPECIALIST.md",read("docs/collection/SPECIALIST_CATALOG.md"))

if __name__=="__main__":unittest.main()
