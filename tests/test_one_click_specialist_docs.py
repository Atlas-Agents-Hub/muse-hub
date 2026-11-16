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
    def test_every_specialist_has_one_actual_named_zip_asset_link(self):
        catalog=json.loads((ROOT/"presets/catalog.json").read_text())
        roles=catalog["presets"]
        self.assertEqual(len(roles),15)
        downloads=(ROOT/"docs/DOWNLOAD_A_SPECIALIST.md").read_text()
        self.assertIn("one muse assistant",downloads.lower())
        for role in roles:
            asset="muse-"+ALIAS.get(role,role)+"-v1.1.0.zip"
            link=RELEASE+asset
            with self.subTest(role=role):
                install=(ROOT/"presets"/role/"INSTALL.md").read_text()
                self.assertIn(link,install)
                self.assertIn(link,downloads)
                self.assertIn("No Python",install)
                self.assertIn("three subchats",install)
                self.assertNotIn("This public starter",install)
                self.assertNotIn("The source wrapper delegates",install)
                self.assertLess(len(install.splitlines()),47)
        self.assertEqual(downloads.count("-v1.1.0.zip"),15)

    def test_readme_and_release_make_downloads_primary(self):
        readme=(ROOT/"README.md").read_text()
        self.assertIn("docs/DOWNLOAD_A_SPECIALIST.md",readme[:750])
        release=(ROOT/"docs/RELEASES.md").read_text()
        self.assertIn("## Individual Muse assistants ? v1.1.0",release[:600])
        self.assertIn("v1.0.0",release)
        self.assertIn("v0.4.1-alpha",release)
        self.assertIn("SHA256SUMS.txt",release)

    def test_role_packages_do_not_claim_account_or_tool_activation(self):
        catalog=json.loads((ROOT/"presets/catalog.json").read_text())
        for role in catalog["presets"]:
            text=(ROOT/"presets"/role/"INSTALL.md").read_text().lower()
            with self.subTest(role=role):
                self.assertIn("separate muse assistant",text)
                self.assertIn("not automatically",text)
                self.assertNotIn("download and sign in",text)

    def test_historical_install_archives_are_pinned_and_tampering_refused(self):
        from tempfile import TemporaryDirectory
        from muse_presets.distribution import product_findings
        historical=ROOT/"docs/history/v1-install/adversarial-verifier.md"
        with TemporaryDirectory() as temp:
            r=Path(temp)
            p=r/"docs/history/v1-install/adversarial-verifier.md"
            p.parent.mkdir(parents=True)
            p.write_bytes(historical.read_bytes())
            baseline=r/"collections/muse-starters-v1/PUBLIC_BASELINE.json"
            baseline.parent.mkdir(parents=True)
            baseline.write_bytes((ROOT/"collections/muse-starters-v1/PUBLIC_BASELINE.json").read_bytes())
            self.assertEqual(product_findings(r),[])
            p.write_bytes(p.read_bytes()+b"tampered")
            issues=product_findings(r)
            self.assertTrue(any(x["reason"]=="HISTORICAL_INSTALL_CHANGED" for x in issues))

    def test_direct_download_page_has_no_404_local_links(self):
        page=ROOT/"docs/DOWNLOAD_A_SPECIALIST.md"
        for path in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)",page.read_text()):
            if "://" in path or path.startswith("#"):continue
            self.assertTrue((page.parent/path).exists(),path)
