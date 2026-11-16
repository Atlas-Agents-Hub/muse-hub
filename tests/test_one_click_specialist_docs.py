"""Every current Muse role must have a mobile-readable direct ZIP path."""
from pathlib import Path
import json
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]
RELEASE="https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/"
ALIAS={"data-engineering-architect":"data-engineer",
       "infrastructure-reliability-engineer":"reliability-engineer"}

class OneClickDocs(unittest.TestCase):
    def test_every_specialist_has_one_staged_filename_without_dead_link(self):
        catalog=json.loads((ROOT/"presets/catalog.json").read_text(encoding="utf-8"))
        roles=catalog["presets"]
        self.assertEqual(len(roles),15)
        downloads=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text(encoding="utf-8")
        self.assertIn("one muse assistant",downloads.lower())
        for role in roles:
            asset="muse-"+ALIAS.get(role,role)+"-v1.1.0.zip"
            link=RELEASE+asset
            with self.subTest(role=role):
                install=(ROOT/"presets"/role/"INSTALL.md").read_text(encoding="utf-8")
                self.assertIn(chr(96)+asset+chr(96),install)
                self.assertIn(chr(96)+asset+chr(96),downloads)
                self.assertNotIn(link,install)
                self.assertNotIn(link,downloads)
                self.assertIn("No Python",install)
                self.assertIn("three subchats",install)
                self.assertNotIn("This public starter",install)
                self.assertNotIn("The source wrapper delegates",install)
                self.assertIn("draft",install.lower())
                self.assertLess(len(install.splitlines()),47)
        self.assertEqual(downloads.count("-v1.1.0.zip"+chr(96)),15)

    def test_readme_and_release_make_downloads_primary(self):
        readme=(ROOT/"README.md").read_text(encoding="utf-8")
        self.assertIn("docs/DOWNLOAD_A_SPECIALIST.md",readme[:750])
        release=(ROOT/"docs/RELEASES.md").read_text(encoding="utf-8")
        self.assertIn("## v1.1.0 — pending publication",release)
        self.assertIn("v1.0.0",release)
        self.assertIn("v0.4.1-alpha",release)
        self.assertIn("SHA256SUMS.txt",release)

    def test_role_packages_do_not_claim_account_or_tool_activation(self):
        catalog=json.loads((ROOT/"presets/catalog.json").read_text(encoding="utf-8"))
        for role in catalog["presets"]:
            text=(ROOT/"presets"/role/"INSTALL.md").read_text(encoding="utf-8").lower()
            with self.subTest(role=role):
                self.assertIn("separate muse assistant",text)
                self.assertIn("not automatically",text)
                self.assertNotIn("download and sign in",text)

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

    def test_draft_release_has_no_dead_public_download_links(self):
        # GitHub draft assets are not publicly downloadable. Until v1.1.0
        # publishes, show exact filenames as plain text, not broken links.
        docs=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text(encoding="utf-8")
        self.assertNotIn("releases/download/v1.1.0/", docs)
        self.assertNotIn("releases/tag/v1.1.0", docs)
        for role in json.loads((ROOT/"presets/catalog.json").read_text(encoding="utf-8"))["presets"]:
            with self.subTest(role=role):
                guide=(ROOT/"presets"/role/"INSTALL.md").read_text(encoding="utf-8")
                self.assertNotIn("releases/download/v1.1.0/", guide)
                self.assertIn("v1.1.0", guide)
        llms=(ROOT/"llms.txt").read_text(encoding="utf-8")
        self.assertNotIn("releases/tag/v1.1.0", llms)

    def test_direct_download_page_has_no_404_local_links(self):
        page=ROOT/"docs/DOWNLOAD_A_SPECIALIST.md"
        for path in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)",page.read_text(encoding="utf-8")):
            if "://" in path or path.startswith("#"):continue
            self.assertTrue((page.parent/path).exists(),path)
