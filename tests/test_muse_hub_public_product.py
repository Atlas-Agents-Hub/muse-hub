"""Muse Hub reader-level identity, download, and privacy acceptance."""
from pathlib import Path
import hashlib
import json
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]
TICK=chr(96)
def read(s):return (ROOT/s).read_text(encoding="utf-8")
class MuseHubPublicProduct(unittest.TestCase):
    def test_root_and_core_guides_use_muse_hub_brand_not_old_marketing(self):
        for name in ("README.md","docs/README.md","llms.txt",
                     "docs/discovery/AI_AGENT_GUIDE.md","hub/README.md"):
            with self.subTest(file=name):
                t=read(name)
                self.assertIn("Muse Hub",t)
                self.assertNotIn("Muse Specialist Toolkit",t)
                self.assertNotIn("Atlas Origins",t)
        self.assertTrue(read("README.md").startswith("# Muse Hub\n"))
        self.assertLess(len(read("README.md").encode("utf-8")),8000)

    def test_reality_status_distinguishes_public_and_draft_releases(self):
        for name in ("README.md","docs/DOWNLOAD_A_SPECIALIST.md","docs/RELEASES.md","hub/README.md"):
            with self.subTest(file=name):
                s=read(name).lower()
                self.assertIn("v1.0.0",s)
                self.assertIn("v1.1.0",s)
                self.assertIn("draft",s)
                self.assertIn("not",s)
        self.assertIn("releases/latest", read("README.md"))

    def test_all_15_assistants_stay_separate_and_have_entrypoints(self):
        roles=json.loads(read("presets/catalog.json"))["presets"]
        self.assertEqual(len(roles),15)
        main=read("README.md")
        self.assertIn("three subchats",main)
        self.assertIn("separate",main.lower())
        for role in roles:
            with self.subTest(role=role):
                self.assertEqual(main.count("presets/"+role+"/INSTALL.md"),1)
                t=read("presets/"+role+"/INSTALL.md")
                self.assertIn("Muse Hub",t)
                self.assertIn("Main",t)
                self.assertIn("three subchats",t)
                self.assertIn("current published",t.lower())
                self.assertIn("v1.1.0",t)
                self.assertNotIn(" ? ",t)
                self.assertNotIn("This public starter",t)
                role_readme=read("presets/"+role+"/README.md")
                self.assertIn("Muse Hub",role_readme)
                self.assertIn("INSTALL.md",role_readme)

    def test_key_links_exist_and_public_links_are_not_mislabeled(self):
        for source in ("README.md","docs/README.md","docs/DOWNLOAD_A_SPECIALIST.md","docs/RELEASES.md","hub/README.md"):
            text=read(source)
            for raw in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)",text):
                if raw.startswith(("https://","http://","mailto:","#")):continue
                target=raw.split("#",1)[0]
                if target:
                    self.assertTrue((ROOT/Path(source).parent/target).exists(),(source,raw))
        downloads=read("docs/DOWNLOAD_A_SPECIALIST.md")
        self.assertIn("draft", downloads.lower())
        self.assertIn("releases/latest", downloads)
        self.assertNotIn(" ? ",downloads)

    def test_llms_txt_parseable_links_and_source_identity(self):
        t=read("llms.txt")
        self.assertIn("## Current public release",t)
        self.assertIn("## Individual specialist homes",t)
        self.assertIn("## Hub scope",t)
        self.assertNotIn("\\n",t)
        links=re.findall(r"(?m)^- \[[^\]]+\]\((https://[^)]+)\)",t)
        self.assertGreaterEqual(len(links),18)
        self.assertEqual(len(links),len(set(links)))
        self.assertTrue(all(("github.com" in link or "raw.githubusercontent.com" in link) for link in links))

    def test_metadata_proposal_does_not_claim_live_issuance(self):
        j=json.loads(read(".github/muse-hub-metadata-proposal.json"))
        self.assertEqual(j["product_name"],"Muse Hub")
        self.assertEqual(j["repository"],"atlas-origins/muse-ai-agent-presets")
        self.assertTrue(j["homepage"].startswith("https://github.com/atlas-origins/muse-ai-agent-presets"))
        self.assertNotIn("atlas-origins.github.io/kits",j["homepage"])
        self.assertLessEqual(len(j["description"]),160)
        self.assertEqual(j["applied_to_github"],False)
        self.assertFalse(j["claims_live_hub_runtime"])

    def test_original_public_source_custody_remains_verifiable(self):
        ledger=json.loads(read("collections/muse-starters-v1/PUBLIC_BASELINE.json"))["files"]
        migration=json.loads(read("docs/history/v1-install/MIGRATION_MANIFEST.json"))["entries"]
        self.assertEqual(len(migration),15)
        for row in migration:
            archived=ROOT/row["archive_path"]
            self.assertTrue(archived.is_file())
            self.assertEqual(hashlib.sha256(archived.read_bytes()).hexdigest(),
                             ledger[row["original_path"]])

    def test_no_private_source_ids_or_live_hub_claims(self):
        for name in ("README.md","hub/README.md","docs/README.md"):
            text=read(name)
            self.assertNotIn("GreenBean-Muse-Assistant",text)
            self.assertNotIn("muse-ai-agent-presets-r32" + "-private",text)
            self.assertIn("not",text.lower())
        self.assertIn("151 connector records",read("README.md"))
        self.assertIn("75 skills",read("README.md"))
        self.assertIn("25 workflows",read("README.md"))
