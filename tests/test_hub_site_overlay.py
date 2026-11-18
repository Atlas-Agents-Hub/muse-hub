"""Standalone test for the canonical hub/site/ GitHub overlay (no dependencies)."""
from __future__ import annotations
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'hub' / 'site'


class MuseHubOverlay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (SITE / 'index.html').read_text('utf8')
        cls.explore = (SITE / 'public' / 'index.html').read_text('utf8')
        cls.catalog = json.loads((SITE / 'public' / 'catalog.json').read_text('utf8'))

    def test_brand_identity_and_local_navigation(self):
        self.assertTrue(self.html.find('<title>Muse Hub') >= 0)
        self.assertEqual(self.html.count('class="role-card"'), 15)
        self.assertIn('href="public/index.html"', self.html)
        self.assertIn('href="../index.html"', self.explore)
        # The old Atlas Origins /kits/ destination must not be linked.
        # New first-party Muse Hub engineering kits are legitimate.
        self.assertNotIn("atlas-origins.github.io/kits/", self.html)
        self.assertNotIn('href="/kits/"', self.html)

    def test_role_specific_setup_from_canonical_fifteen(self):
        roles = json.loads((SITE/'roles.json').read_text('utf8'))['roles']
        slugs = {r['id'] for r in roles}
        choices = re.findall(r'<option value="([a-z][a-z0-9-]+)" data-description=', self.html)
        card_links = re.findall(r'class="role-card-setup" href="\?role=([a-z][a-z0-9-]+)#setup" data-select-role="([a-z][a-z0-9-]+)"', self.html)
        self.assertEqual(len(choices), 15)
        self.assertEqual(len(card_links), 15)
        self.assertEqual(set(choices), slugs)
        self.assertEqual({slug for slug, role in card_links if slug == role}, slugs)
        self.assertTrue(all(slug == role for slug, role in card_links))
        self.assertIn('id="setup-role-result"', self.html)
        self.assertIn('id="setup-role-download"', self.html)
        cards = re.findall(r'<article class="role-card" data-role="([^"]+)" data-asset="([^"]+)"[^>]*>(.*?)</article>', self.html, re.S)
        self.assertEqual(len(cards), 15)
        self.assertEqual({slug for slug, _, _ in cards}, slugs)
        aliases = {"data-engineering-architect": "data-engineer",
                   "infrastructure-reliability-engineer": "reliability-engineer"}
        for slug, asset, body in cards:
            with self.subTest(role=slug):
                self.assertEqual(asset, aliases.get(slug, slug))
                expected = "https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.2/muse-" + asset + "-v1.1.2.zip"
                self.assertIn('class="role-card-download" href="' + expected + '"', body)
        self.assertIn('aria-live="polite"', self.html)

    def test_catalog_is_rights_filtered_without_native_runtime_authority(self):
        self.assertEqual(self.catalog['count'], 63)
        self.assertEqual(len(self.catalog['items']), 63)
        self.assertFalse(self.catalog['native_muse_connected'])
        self.assertEqual(self.catalog['publication'], 'PUBLIC_DIRECTORY')
        self.assertEqual(len(self.catalog['routes']), 6)
        self.assertIn('connect-src \'none\'', self.html)
        self.assertIn('connect-src \'none\'', self.explore)
        self.assertEqual(len({row['id'] for row in self.catalog['items']}), 63)
        self.assertTrue(all(row['url'].startswith('https://') for row in self.catalog['items']))

    def test_no_dead_local_code_assets_and_no_network_scripts(self):
        for file in ('index.html','site.css','site.js','roles.json','downloads.html','downloads.js','downloads.json','public/index.html','public/styles.css','public/app.js','public/catalog.json','README.md'):
            self.assertTrue((SITE/file).is_file(), file)
        for script in ('site.js','downloads.js','public/app.js'):
            text = (SITE/script).read_text('utf8')
            for blocked in ('fetch(', 'XMLHttpRequest', 'localStorage', 'innerHTML'):
                self.assertNotIn(blocked, text)
        downloads = (SITE/'downloads.html').read_text('utf8')
        self.assertIn("connect-src 'none'", downloads)
        for page, dirname in ((self.html,SITE), (self.explore,SITE/'public'), (downloads,SITE)):
            for ref in re.findall(r'(?:src|href)="([^"]+)"', page):
                if ref.startswith(('https://', '#')): continue
                if ref.startswith('data:image/svg+xml,'):
                    # Explicitly scoped to the original self-contained favicon.
                    # No other data: links gain an exception to local path checks.
                    self.assertIn('<link rel="icon" type="image/svg+xml" href="'+ref+'">', page)
                    continue
                if ref.startswith('?role='):
                    self.assertTrue(ref.endswith('#setup'), ref)
                    self.assertTrue(dirname.joinpath('index.html').is_file(), ref)
                    continue
                self.assertNotIn('..', Path(ref).parts[1:], ref)
                self.assertTrue((dirname/ref.split('#', 1)[0]).resolve().exists(), ref)

    def test_all_sealed_bytes_match(self):
        meta = json.loads((SITE/'INTEGRITY.json').read_text('utf8'))
        self.assertEqual(meta['schema'], 'muse-hub/public-website-overlay/v1')
        self.assertEqual(meta['source_kind'], 'STATIC_WEBSITE')
        for rel, row in meta['files'].items():
            file = SITE / rel
            self.assertTrue(file.is_file(), rel)
            raw = file.read_bytes()
            self.assertEqual(len(raw), row['bytes'], rel)
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row['sha256'], rel)


if __name__ == '__main__': unittest.main()
