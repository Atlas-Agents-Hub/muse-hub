"""Verify complete, source-bound specialist positioning and engine disclosure."""
from pathlib import Path
import json, unittest
ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/discovery/specialist-engine-index.json"
GUIDE = ROOT / "docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md"
README = ROOT / "README.md"

class SpecialistEnginePositioning(unittest.TestCase):
 def load(self):
  document = json.loads(REGISTRY.read_bytes())
  self.assertEqual(document["schema"], "muse-specialist-toolkit/specialist-engines-v1")
  return document

 def test_exact_15_roles_not_more_agents(self):
  from_repo = json.loads((ROOT/"presets/catalog.json").read_bytes())["presets"]
  rows = self.load()["roles"]
  self.assertEqual(len(rows), 15)
  self.assertEqual(set(r["id"] for r in rows), set(from_repo))
  self.assertEqual(len({r["id"] for r in rows}), 15)

 def test_engine_sources_and_commands_are_real(self):
  roles = self.load()["roles"]
  for row in roles:
   with self.subTest(role=row["id"]):
    self.assertTrue((ROOT/row["playbook"]).is_file())
    self.assertGreater(len(row["scope"]), 45)
    self.assertGreater(len(row["real_work"]), 1)
    self.assertIn(row["delivery"], ("runnable-kit","source-methods","local-workbench","runnable-extension"))
    for filepath in row["source_engines"]:
     self.assertTrue((ROOT/filepath).is_file(), (row["id"],filepath))
    for filepath in row["examples"]:
     self.assertTrue((ROOT/filepath).is_file(), (row["id"],filepath))
    if row["delivery"] == "source-methods":
     self.assertEqual(row["source_engines"], [])
    else:
     self.assertTrue(row["source_engines"])

 def test_richer_engine_scope_and_separate_permissions(self):
  doc=self.load()
  rows={r["id"]:r for r in doc["roles"]}
  self.assertIn("claim-gate", " ".join(rows["software-engineer"]["source_engines"]))
  self.assertIn("model_toy", " ".join(rows["model-builder"]["source_engines"]))
  self.assertIn("creative_production", " ".join(rows["creative-studio"]["source_engines"]))
  self.assertIn("specialist_extensions", " ".join(rows["automation-engineer"]["source_engines"]))
  self.assertIn("daily_desk", " ".join(rows["personal-companion"]["source_engines"]))
  self.assertEqual(rows["adversarial-verifier"]["delivery"], "source-methods")
  self.assertFalse(any("security_assistance" in p for row in rows.values() for p in row["source_engines"]))
  self.assertEqual(doc["host_integrations"],"SEPARATE_AUTHORIZATION")

 def test_user_and_machine_entrypoints_reach_exact_engine_inventory(self):
     text=README.read_text(encoding="utf8")
     guide=GUIDE.read_text(encoding="utf8")
     self.assertIn("docs/handbook/specialists-by-task.md",text)
     directory=(ROOT/"docs/handbook/specialists-by-task.md").read_text(encoding="utf8")
     self.assertIn("../collection/SPECIALIST_SCOPE_AND_ENGINES.md",directory)
     self.assertIn("docs/discovery/AI_AGENT_GUIDE.md",(ROOT/"llms.txt").read_text(encoding="utf8"))
     self.assertIn("../collection/SPECIALIST_SCOPE_AND_ENGINES.md",(ROOT/"docs/discovery/AI_AGENT_GUIDE.md").read_text(encoding="utf8"))
     self.assertIn("specialist-engine-index.json",guide)
     for role in self.load()["roles"]:
         self.assertIn(role["id"],guide)
     self.assertIn("separately authorized host tools",guide)
     self.assertIn("tool registrations and approvals",guide)

 def test_source_manifests_not_relabelled_as_native_activation(self):
  doc=self.load()
  self.assertEqual(doc["native_muse_activation"], "NOT_ASSERTED")
  for role in doc["roles"]:
   self.assertNotIn("INSTALLED_NATIVE",str(role))
   self.assertNotIn("BLACK_RAVEN_LIVE",str(role))
  for name in ("iron-ledger","provenance-vault"):
   p=ROOT/f"presets/software-engineer/runtime/{name}/ENGINE.json"
   md=json.loads(p.read_bytes())
   self.assertFalse(md["external_effects_enabled"])
   self.assertFalse(md["redistribution_rights_verified"])

 def test_all_public_engine_guide_links_resolve(self):
  import re
  guide=GUIDE.read_text(encoding="utf8")
  found=0
  for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", guide):
   if link.startswith(("https://","http://","#")):continue
   path=link.split("#",1)[0]
   if not path:continue
   found+=1
   self.assertTrue((GUIDE.parent/path).exists(),link)
  self.assertGreater(found,45)

 def test_canonical_discovery_url_matches_organization(self):
  meta=json.loads((ROOT/"docs/discovery/agent-capabilities.json").read_bytes())
  self.assertEqual(meta["repository"],"https://github.com/atlas-origins/muse-ai-agent-presets")
  self.assertIn("atlas-origins",meta["specialist_engine_index"])
  self.assertIn("atlas-origins",(ROOT/"llms.txt").read_text(encoding="utf8"))

 def test_no_broken_possessives_in_role_discovery(self):
  import re
  for path in (README, ROOT/"docs/CAPABILITIES.md",GUIDE):
   text=path.read_text(encoding="utf8")
   with self.subTest(path=path.name):
    self.assertNotRegex(text,r"\b(?:role|specialist)\?s\b")
    self.assertNotIn(chr(0xfffd),text)

if __name__=="__main__": unittest.main()
