"""Muse Hub reader-level identity, download, and privacy acceptance."""
from pathlib import Path
import hashlib
import json
import re
import unittest
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from muse_collection import load_collection
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
TICK=chr(96)
REPO="https://github.com/atlas-origins/muse-ai-agent-presets"
SITE="https://atlas-origins.github.io/muse-ai-agent-presets/"
VERSION=json.loads((ROOT/"presets/catalog.json").read_bytes())["release"]
RELEASE=REPO+"/releases/tag/"+VERSION
DOWNLOAD=REPO+"/releases/download/"+VERSION+"/"
ALIASES={"data-engineering-architect":"data-engineer",
         "infrastructure-reliability-engineer":"reliability-engineer"}
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

    def test_current_release_is_findable_and_history_is_preserved(self):
        for name in ("README.md","docs/DOWNLOAD_A_SPECIALIST.md","docs/RELEASES.md","hub/README.md"):
            with self.subTest(file=name):
                s=read(name)
                self.assertIn(RELEASE,s)
                for stale in (VERSION+" draft", "not deployed", "source-only"):
                    self.assertNotIn(stale,s.lower())
        self.assertIn("releases/latest", read("README.md"))
        self.assertIn(REPO+"/releases/tag/v1.0.0", read("docs/RELEASES.md"))

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
                self.assertIn(RELEASE,t)
                self.assertIn(DOWNLOAD+"muse-"+ALIASES.get(role,role)+"-"+VERSION+".zip",t)
                self.assertIn("START_HERE.md",t)
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
        self.assertIn(RELEASE, downloads)
        self.assertIn("releases/latest", downloads)
        roles=json.loads(read("presets/catalog.json"))["presets"]
        for role in roles:
            self.assertIn(DOWNLOAD+"muse-"+ALIASES.get(role,role)+"-"+VERSION+".zip",downloads)
        self.assertNotIn(" ? ",downloads)

    def test_active_docs_have_no_escaped_line_breaks(self):
        paths=[ROOT/"README.md",ROOT/"llms.txt",ROOT/"hub/README.md",ROOT/"docs/README.md"]
        paths.extend((ROOT/"presets").glob("*/README.md"))
        paths.extend((ROOT/"presets").glob("*/INSTALL.md"))
        for p in paths:
            text=p.read_text(encoding="utf-8")
            with self.subTest(path=p.relative_to(ROOT).as_posix()):
                self.assertNotIn(chr(92)+"n-",text)
                self.assertNotIn(chr(92)+"n##",text)

    def test_llms_txt_parseable_links_and_source_identity(self):
        t=read("llms.txt")
        self.assertIn("## Start here",t)
        self.assertIn("## Individual specialist homes",t)
        self.assertIn("## Skills, workflows, and tools",t)
        self.assertNotIn("\\n",t)
        links=re.findall(r"(?m)^- \[[^\]]+\]\((https://[^)]+)\)",t)
        self.assertGreaterEqual(len(links),18)
        self.assertEqual(len(links),len(set(links)))
        self.assertIn(SITE,links)
        self.assertIn(RELEASE,links)
        for link in links:
            parsed=urlsplit(link)
            with self.subTest(link=link):
                self.assertIn(parsed.hostname, {"github.com", "raw.githubusercontent.com", "atlas-origins.github.io"})
                self.assertIsNone(parsed.username)
                self.assertIsNone(parsed.password)
                if parsed.hostname=="atlas-origins.github.io":
                    self.assertTrue(parsed.path.startswith("/muse-ai-agent-presets/"))

    def test_repository_metadata_describes_the_product_and_search_topics(self):
        metadata=json.loads(read('.github/muse-hub-metadata-proposal.json'))
        self.assertEqual(metadata['product_name'],'Muse Hub')
        self.assertEqual(metadata['repository'],'atlas-origins/muse-ai-agent-presets')
        self.assertEqual(metadata['homepage'],SITE)
        self.assertEqual(metadata['schema'],'muse-hub/github-metadata/v2')
        self.assertLessEqual(len(metadata['description']),160)
        self.assertIn('muse-ai',metadata['topics'])
        self.assertLessEqual(len(metadata['topics']),20)
        self.assertEqual(len(metadata['topics']),len(set(metadata['topics'])))
        for topic in metadata['topics']:
            self.assertRegex(topic,r'^[a-z0-9-]{1,50}$')

    def test_current_public_setup_files_are_present_for_every_role(self):
        roles=json.loads(read('presets/catalog.json'))['presets']
        for role in roles:
            with self.subTest(role=role):
                self.assertTrue((ROOT/'presets'/role/'INSTALL.md').is_file())
                self.assertTrue((ROOT/'presets'/role/'README.md').is_file())
                self.assertEqual(json.loads(read('presets/'+role+'/playbook.json'))['role_id'],role)

    def test_public_guides_describe_the_current_library(self):
        data=load_collection()
        skills=data['skills'];workflows=data['workflows']
        main=read('README.md')
        connectors=json.loads(read('docs/connectors/catalog.json'))['connectors']
        self.assertIn(str(len(connectors))+' connectors',main)
        self.assertIn(str(len(skills))+' skills',main)
        self.assertIn(str(len(workflows))+' workflows',main)
        for name in ('README.md','hub/README.md','docs/README.md'):
            text=read(name)
            self.assertNotIn('private_repository',text)
            self.assertNotIn('HOST_MAP.'+'local.json',text)
