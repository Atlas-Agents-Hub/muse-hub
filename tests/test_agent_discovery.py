"""Human and agent discovery point to the same usable product entry points."""
from __future__ import annotations
import json,re,unittest
from pathlib import Path
from urllib.parse import urlparse
from muse_presets.public_export import PUBLIC_ROOT_FILES,select_public_files
ROOT=Path(__file__).resolve().parents[1]
REPO="atlas-origins/muse-ai-agent-presets"
RELEASE="v0.4.1-alpha"
EIGHT=("coordinator","software-engineer","model-builder","claims-adjudicator","garden-companion","learning-coach","reverse-engineering-researcher","creative-studio")
FROZEN=("research-evaluator","adversarial-verifier","personal-companion")
URL="https://github.com/"+REPO
SITE="https://atlas-origins.github.io/muse-ai-agent-presets/"

class AgentDiscoveryTests(unittest.TestCase):
 def test_llms_index_has_current_releases_roles_and_task_links(self):
  self.assertIn("llms.txt",PUBLIC_ROOT_FILES)
  text=(ROOT/"llms.txt").read_text(encoding="utf-8")
  self.assertTrue(text.startswith("# Muse Hub\n"))
  self.assertIn("15 independent Muse assistants",text)
  self.assertIn(URL+"/releases/tag/v1.4.0",text)
  self.assertIn(SITE,text)
  links=re.findall(r"(?m)^- \[[^\]]+\]\((https://[^)]+)\)",text)
  self.assertGreaterEqual(len(links),30)
  self.assertEqual(len(links),len(set(links)))
  for link in links:
   host=urlparse(link).netloc
   self.assertIn(host,("github.com","raw.githubusercontent.com","atlas-origins.github.io"))
  for role in json.loads((ROOT/"presets/catalog.json").read_text())["presets"]:
   self.assertIn("presets/"+role+"/INSTALL.md",text)
  self.assertIn("llms.txt",select_public_files(ROOT))

 def test_agent_guide_provides_current_package_and_terminal_steps(self):
  text=(ROOT/"docs/discovery/AI_AGENT_GUIDE.md").read_text(encoding="utf-8")
  for target in ("../DOWNLOAD_A_SPECIALIST.md","../GETTING_STARTED.md","../TERMINAL.md","../INSTALL_AND_PERSISTENCE.md"):
   self.assertIn(target,text)
  for step in ("START_HERE.md","three subchat","SHA256SUMS","quickstart.py --all"):
   self.assertIn(step,text)
  self.assertIn("releases/tag/v1.4.0",text)
  self.assertNotIn("source-only",text)

 def test_readme_and_agent_index_agree_on_entrypoints(self):
  readme=(ROOT/"README.md").read_text(encoding="utf-8")
  index=(ROOT/"llms.txt").read_text(encoding="utf-8")
  for path in ("docs/DOWNLOAD_A_SPECIALIST.md","docs/GETTING_STARTED.md","docs/TERMINAL.md","docs/CAPABILITIES.md"):
   self.assertIn(path,readme)
   self.assertIn(path,index)
  self.assertIn("[AI-agent discovery index](llms.txt)",readme)
  self.assertLess(len(readme.encode()),8000)

 def test_discovery_links_do_not_contain_session_material(self):
  for path in ("README.md","llms.txt","docs/discovery/AI_AGENT_GUIDE.md"):
   text=(ROOT/path).read_text(encoding="utf-8").lower()
   self.assertNotIn("token=",text)
   self.assertNotIn("hatch_sess=",text)
   self.assertNotIn("install automatically",text)

 def test_machine_discovery_json_matches_current_packages_and_tools(self):
  doc=json.loads((ROOT/"docs/discovery/agent-capabilities.json").read_text(encoding="utf-8"))
  self.assertEqual(doc["schema"],"specialist-ai-agent-kits/discovery/v1")
  self.assertEqual(doc["repository"],URL)
  self.assertEqual(doc["release"],"v1.4.0")
  self.assertEqual(doc["license"],"MIT")
  roles=json.loads((ROOT/"presets/catalog.json").read_text())["presets"]
  self.assertEqual(set(doc["starter_roles"]),set(roles))
  self.assertEqual(set(doc["specialist_downloads"]),set(roles))
  self.assertEqual(doc["released_starter_zip_count"],15)
  aliases={"data-engineering-architect":"data-engineer","infrastructure-reliability-engineer":"reliability-engineer"}
  for role in roles:
   asset="muse-"+aliases.get(role,role)+"-v1.4.0.zip"
   expected=URL+"/releases/download/v1.4.0/"+asset
   self.assertEqual(doc["specialist_downloads"][role],expected)
  for entry in doc["executable_offline_kits"]:
   self.assertEqual(entry["download"],doc["specialist_downloads"][entry["role"]])
   self.assertTrue((ROOT/entry["exporter"]).is_file())
  self.assertEqual(doc["sha256_index"],URL+"/releases/download/v1.4.0/SHA256SUMS")
  self.assertEqual(doc["homepage"],SITE)
  self.assertEqual(doc["downloads_page"],SITE+"downloads.html")

 def test_agent_boundary_claims_are_fail_closed(self):
  doc=json.loads((ROOT/"docs/discovery/agent-capabilities.json").read_text(encoding="utf-8"))
  claims=doc["boundaries"]
  for key in ("native_muse_agents_installed","hosted_agent_service",
              "autonomous_model_backed_agents_out_of_box","external_connectors_enabled",
              "independent_rights_authentication","large_language_model_training"):
   self.assertIs(claims[key],False,key)
  self.assertEqual(doc["python_minimum"],"3.12")
  self.assertIn("Git requirements vary",doc["dependency_note"])
  self.assertNotIn("password",str(doc).lower())
  self.assertNotIn("token=",str(doc).lower())

if __name__=="__main__":unittest.main()
