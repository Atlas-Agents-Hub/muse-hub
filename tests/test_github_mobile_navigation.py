"""GitHub-native, phone-readable product and connector discovery."""
from pathlib import Path
import json,re,sys,subprocess,unittest
ROOT=Path(__file__).resolve().parents[1]
README=ROOT/"README.md"
CROOT=ROOT/"docs"/"connectors"
GROUPS={
 "work-and-productivity":"Work and productivity",
 "ai-research-and-data":"AI, research and data",
 "development-and-infrastructure":"Development and infrastructure",
 "design-and-creative":"Design and creative",
 "business-and-commerce":"Business and commerce",
 "home-and-devices":"Home and devices",
 "publishing-and-social":"Publishing and social",
 "everyday-and-more":"Everyday and more",
}
def doc(path):return path.read_text(encoding="utf8")
def catalog():return json.loads(doc(CROOT/"catalog.json"))["connectors"]

class GitHubMobileNavigation(unittest.TestCase):
 def test_homepage_is_a_product_story_not_a_scrollable_table_or_warnings(self):
  body=doc(README);hero=body.split("\n## ",1)[0]
  self.assertLess(len(hero.encode("utf8")),1100)
  for claim in ["Muse Specialist Toolkit","Your Muse. Your Specialists. Your Possibilities.",
                "15 AI Specialists","100+ Configurations","150+ Custom Connectors"]:
   self.assertIn(claim,hero)
  for phrase in ["source-only","not installed","offline","75 skills","native enrollment"]:
   self.assertNotIn(phrase,hero.lower())
  self.assertFalse(re.search(r"(?m)^\|\s*---",body))
  self.assertFalse(re.search(r"(?m)^\|.*\|",body))
  self.assertNotIn(" ? ",body)
 def test_homepage_has_four_obvious_actions_before_technical_details(self):
  body=doc(README);first=body.split("## For developers",1)[0]
  for phrase in ["Choose a specialist","Browse task configurations",
                 "Explore custom connectors","Try Daily Desk"]:
   self.assertIn(phrase,first)
  self.assertIn("docs/connectors/README.md",first)
  self.assertIn("docs/v1/START_HERE.md",first)
  self.assertIn("docs/spaces/DAILY_DESK.md",first)
  self.assertIn("tools/muse_collection.py demo data-engineer",body)
  self.assertIn("docs/collection/SPECIALIST_QUICKSTART.md",body)
  self.assertIn("[AI-agent discovery index](llms.txt)",body)
  self.assertIn("not installed native muse agents",body.lower())
 def test_all_specialists_are_visible_in_use_case_groups(self):
  body=doc(README)
  roles=json.loads(doc(ROOT/"presets/catalog.json"))["presets"]
  self.assertEqual(len(roles),15)
  for role in roles:
   with self.subTest(role=role):
    self.assertEqual(body.count("presets/"+role+"/"),1)
  for phrase in ["Build and automate","Research and evaluate",
                 "Create and learn","Life and planning"]:
   self.assertIn(phrase,body)
 def test_connector_landing_has_use_case_navigation_not_an_undifferentiated_list(self):
  body=doc(CROOT/"README.md")
  self.assertFalse(re.search(r"(?m)^\|.*\|",body))
  self.assertIn("150+ Custom Connectors",body)
  self.assertIn("Browse by what you want to do",body)
  for group,title in GROUPS.items():
   with self.subTest(group=group):
    self.assertIn("CATALOG.md#"+group,body)
    self.assertIn(title,body)
  self.assertLess(body.index("Browse by what you want to do"),body.index("Source and attribution"))
  self.assertNotIn("not installed",body[:body.index("Browse by what you want to do")].lower())
 def test_all_151_connectors_are_grouped_with_links_and_short_descriptions(self):
  body=doc(CROOT/"CATALOG.md")
  self.assertNotRegex(body,r"(?m)^\|.*\|")
  self.assertIn("Browse by use case",body)
  self.assertEqual(len(catalog()),151)
  positions=[]
  for group,title in GROUPS.items():
   self.assertIn("## "+title,body)
   positions.append(body.index("## "+title))
  self.assertEqual(positions,sorted(positions))
  for entry in catalog():
   with self.subTest(connector=entry["id"]):
    self.assertEqual(body.count(entry["source_url"]),1)
  # Count only connector links; user-facing GitHub links remain directly browsable.
  links=re.findall(r"\]\((https://github\.com/bluman1/muse-connectors/blob/[a-f0-9]{40}/connectors/[a-z0-9-]+/SKILL\.md)\)",body)
  self.assertEqual(len(links),151);self.assertEqual(len(set(links)),151)
  self.assertIn("As&#97;na",body)
 def test_category_renderer_is_deterministic_and_detects_outdated_docs(self):
  p=ROOT/"scripts/render_github_connector_directory.py"
  self.assertTrue(p.is_file())
  r=subprocess.run([sys.executable,"-B",str(p),"--check"],cwd=ROOT,capture_output=True,timeout=25)
  self.assertEqual(r.returncode,0,r.stdout.decode("utf8","replace")+r.stderr.decode("utf8","replace"))
 def test_markdown_relative_links_exist_and_catalog_is_utf8(self):
  for page in [README,CROOT/"README.md",CROOT/"CATALOG.md"]:
   s=doc(page)
   self.assertNotIn("\ufffd",s)
   for name in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)",s):
    if name.startswith(("https://","http://","mailto:")) or name.startswith("#"):continue
    rel=name.split("#",1)[0]
    if rel:
     self.assertTrue((page.parent/rel).exists(),(page.name,name))

if __name__=="__main__":unittest.main()
