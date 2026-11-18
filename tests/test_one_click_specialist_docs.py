"""Every current specialist has a usable package and setup path."""
from pathlib import Path
import json
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]
VERSION=json.loads((ROOT/"presets/catalog.json").read_bytes())["release"]
RELEASE="https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/"+VERSION+"/"
ALIAS={"data-engineering-architect":"data-engineer","infrastructure-reliability-engineer":"reliability-engineer"}

class OneClickDocs(unittest.TestCase):
    def test_all_15_specialists_have_current_direct_downloads_and_setup(self):
        roles=json.loads((ROOT/"presets/catalog.json").read_text(encoding="utf-8"))["presets"]
        self.assertEqual(len(roles),15)
        downloads=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text(encoding="utf-8")
        self.assertIn("one Muse assistant",downloads)
        for role in roles:
            asset="muse-"+ALIAS.get(role,role)+"-"+VERSION+".zip"
            link=RELEASE+asset
            with self.subTest(role=role):
                install=(ROOT/"presets"/role/"INSTALL.md").read_text(encoding="utf-8")
                self.assertIn(link,install)
                self.assertEqual(downloads.count(link),1)
                for step in ("START_HERE.md","Main","three subchats","First task to try"):
                    self.assertIn(step,install)
                self.assertIn("separate Muse assistant",install)
                self.assertIn("account and permissions",install)
                self.assertLess(len(install.splitlines()),47)
        self.assertNotIn("draft",downloads.lower())

    def test_readme_and_release_make_current_downloads_primary(self):
        readme=(ROOT/"README.md").read_text(encoding="utf-8")
        self.assertIn("docs/DOWNLOAD_A_SPECIALIST.md",readme[:750])
        release=(ROOT/"docs/RELEASES.md").read_text(encoding="utf-8")
        self.assertIn("releases/tag/"+VERSION,release)
        self.assertLess(release.index(VERSION),release.index("## Earlier releases"))
        self.assertIn("v1.0.0",release)
        self.assertIn("v0.4.1-alpha",release)
        self.assertIn(RELEASE+"SHA256SUMS",release)

    def test_current_guides_link_the_same_release(self):
        for path in ("README.md","docs/DOWNLOAD_A_SPECIALIST.md","docs/RELEASES.md","llms.txt"):
            with self.subTest(path=path):
                text=(ROOT/path).read_text(encoding="utf-8")
                self.assertIn("releases/tag/"+VERSION,text)
                self.assertNotIn("not publicly downloadable",text)
                self.assertNotIn("still a draft",text)

    def test_current_install_guides_preserve_customization_and_recovery_paths(self):
        roles=json.loads((ROOT/'presets/catalog.json').read_bytes())['presets']
        for role in roles:
            with self.subTest(role=role):
                body=(ROOT/'presets'/role/'INSTALL.md').read_text()
                self.assertIn('START_HERE.md',body)
                self.assertIn('Main',body)
                self.assertIn('three subchats',body)
        guide=(ROOT/'docs/INSTALL_AND_PERSISTENCE.md').read_text().lower()
        for term in ('backup','update','memory'):
            self.assertIn(term,guide)

    def test_direct_download_page_has_no_404_local_links(self):
        page=ROOT/"docs/DOWNLOAD_A_SPECIALIST.md"
        for path in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)",page.read_text(encoding="utf-8")):
            if "://" in path or path.startswith("#"):continue
            self.assertTrue((page.parent/path).exists(),path)
