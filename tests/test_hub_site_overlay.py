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
        self.assertNotIn('/kits/', self.html)

    def test_role_specific_setup_from_canonical_fifteen(self):
        roles = json.loads((SITE/'roles.json').read_text('utf8'))['roles']
        slugs = {r['id'] for r in roles}
        choices = re.findall(r'<option value="([a-z][a-z0-9-]+)" data-description=', self.html)
        card_links = re.findall(r'class="role-card-setup" href="#setup" data-select-role="([a-z][a-z0-9-]+)"', self.html)
        self.assertEqual(len(choices), 15)
        self.assertEqual(len(card_links), 15)
        self.assertEqual(set(choices), slugs)
        self.assertEqual(set(card_links), slugs)
        self.assertIn('id="setup-role-result"', self.html)
        self.assertNotIn('/'.join(('releases','download','v1.1.0'))+'/', self.html)
        self.assertIn('aria-live="polite"', self.html)

    def test_catalog_is_rights_filtered_and_source_only(self):
        self.assertEqual(self.catalog['count'], 63)
        self.assertEqual(len(self.catalog['items']), 63)
        self.assertFalse(self.catalog['native_muse_connected'])
        self.assertEqual(len(self.catalog['routes']), 6)
        self.assertIn('connect-src \'none\'', self.html)
        self.assertIn('connect-src \'none\'', self.explore)
        self.assertEqual(len({row['id'] for row in self.catalog['items']}), 63)
        self.assertTrue(all(row['url'].startswith('https://') for row in self.catalog['items']))

    def test_no_dead_local_code_assets_and_no_network_scripts(self):
        for file in ('index.html','site.css','site.js','roles.json','public/index.html','public/styles.css','public/app.js','public/catalog.json','README.md'):
            self.assertTrue((SITE/file).is_file(), file)
        for script in ('site.js','public/app.js'):
            text = (SITE/script).read_text('utf8')
            for blocked in ('fetch(', 'XMLHttpRequest', 'localStorage', 'innerHTML'):
                self.assertNotIn(blocked, text)
        for page, dirname in ((self.html,SITE), (self.explore,SITE/'public')):
            for ref in re.findall(r'(?:src|href)="([^"]+)"', page):
                if ref.startswith(('https://', '#')): continue
                self.assertNotIn('..', Path(ref).parts[1:], ref)
                self.assertTrue((dirname/ref).resolve().exists(), ref)

    def test_all_sealed_bytes_match(self):
        meta = json.loads((SITE/'INTEGRITY.json').read_text('utf8'))
        self.assertEqual(meta['schema'], 'muse-hub/public-website-overlay/v1')
        for rel, row in meta['files'].items():
            file = SITE / rel
            self.assertTrue(file.is_file(), rel)
            raw = file.read_bytes()
            self.assertEqual(len(raw), row['bytes'], rel)
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row['sha256'], rel)


if __name__ == '__main__': unittest.main()
