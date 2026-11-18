"""Every current specialist has a usable package and setup path."""
from pathlib import Path
import json
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]
RELEASE="https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.2/"
ALIAS={"data-engineering-architect":"data-engineer","infrastructure-reliability-engineer":"reliability-engineer"}

class OneClickDocs(unittest.TestCase):
    def test_all_15_specialists_have_current_direct_downloads_and_setup(self):
        roles=json.loads((ROOT/"presets/catalog.json").read_text(encoding="utf-8"))["presets"]
        self.assertEqual(len(roles),15)
        downloads=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text(encoding="utf-8")
        self.assertIn("one Muse assistant",downloads)
        for role in roles:
            asset="muse-"+ALIAS.get(role,role)+"-v1.1.2.zip"
            link=RELEASE+asset
            with self.subTest(role=role):
                install=(ROOT/"presets"/role/"INSTALL.md").read_text(encoding="utf-8")
                self.assertIn(link,install)
                self.assertEqual(downloads.count(link),1)
                for step in ("START_HERE.md","Main","three subchats","First task to try","No Python"):
                    self.assertIn(step,install)
                self.assertIn("separate Muse assistant",install)
                self.assertIn("account and permissions",install)
                self.assertLess(len(install.splitlines()),47)
        self.assertNotIn("draft",downloads.lower())

    def test_readme_and_release_make_current_downloads_primary(self):
        readme=(ROOT/"README.md").read_text(encoding="utf-8")
        self.assertIn("docs/DOWNLOAD_A_SPECIALIST.md",readme[:750])
        release=(ROOT/"docs/RELEASES.md").read_text(encoding="utf-8")
        self.assertIn("releases/tag/v1.1.2",release)
        self.assertLess(release.index("v1.1.2"),release.index("## Earlier releases"))
        self.assertIn("v1.0.0",release)
        self.assertIn("v0.4.1-alpha",release)
        self.assertIn(RELEASE+"SHA256SUMS",release)

    def test_current_guides_link_the_same_release(self):
        for path in ("README.md","docs/DOWNLOAD_A_SPECIALIST.md","docs/RELEASES.md","llms.txt"):
            with self.subTest(path=path):
                text=(ROOT/path).read_text(encoding="utf-8")
                self.assertIn("releases/tag/v1.1.2",text)
                self.assertNotIn("not publicly downloadable",text)
                self.assertNotIn("still a draft",text)

    def test_original_install_text_archives_remain_byte_identical(self):
        import hashlib
        historical=ROOT/"docs/history/v1-install"
        baseline=json.loads((ROOT/"collections/muse-starters-v1/PUBLIC_BASELINE.json").read_text(encoding="utf-8"))
        manifest=json.loads((historical/"MIGRATION_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["entries"]),15)
        for entry in manifest["entries"]:
            with self.subTest(role=entry["original_path"]):
                target=ROOT/entry["archive_path"]
                self.assertEqual(target.suffix,".txt")
                self.assertTrue(target.is_file())
                self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(),
                                 baseline["files"][entry["original_path"]])
        from muse_presets.distribution import product_findings
        self.assertFalse(any(x["reason"]=="HISTORICAL_INSTALL_CHANGED"
                             for x in product_findings(ROOT)))

    def test_direct_download_page_has_no_404_local_links(self):
        page=ROOT/"docs/DOWNLOAD_A_SPECIALIST.md"
        for path in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)",page.read_text(encoding="utf-8")):
            if "://" in path or path.startswith("#"):continue
            self.assertTrue((page.parent/path).exists(),path)
