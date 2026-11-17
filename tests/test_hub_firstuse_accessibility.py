"""Regression checks for source-only Muse Hub specialist navigation.

Interactive keyboard behavior is separately exercised in the local Chrome QA.
"""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "hub/site/index.html").read_text(encoding="utf-8")
JS = (ROOT / "hub/site/site.js").read_text(encoding="utf-8")
CSS = (ROOT / "hub/site/site.css").read_text(encoding="utf-8")


class SiteFirstUseA11y(unittest.TestCase):
    def test_selected_setup_heading_is_programmatically_focusable(self):
        self.assertIn('<h4 id="setup-role-title" tabindex="-1"></h4>', HTML)
        self.assertRegex(JS, r"setupTitle\.focus\(\{\s*preventScroll:\s*true\s*\}\)")
        self.assertRegex(JS, r"setupTitle\.scrollIntoView\(")
        self.assertIn("#setup-role-title:focus-visible", CSS)

    def test_role_card_links_keep_shareable_setup_fragment(self):
        cards = re.findall(
            r'class="role-card-setup" href="\?role=([a-z0-9-]+)#setup"',
            HTML,
        )
        self.assertEqual(len(cards), 15)
        self.assertEqual(len(set(cards)), 15)
        self.assertIn("url.hash = '#setup'", JS)
        self.assertIn("history.replaceState", JS)

    def test_card_links_have_touch_accessible_targets(self):
        self.assertRegex(
            CSS,
            r"\.role-card-actions a\s*\{[^}]*min-height:\s*44px\s*;",
        )

    def test_both_public_pages_share_an_original_local_only_favicon(self):
        public = (ROOT / 'hub/site/public/index.html').read_text(encoding='utf-8')
        links = []
        for page in (HTML, public):
            matches = re.findall(
                r'<link rel="icon" type="image/svg\+xml" href="(data:image/svg\+xml,[^\"]+)">',
                page,
            )
            self.assertEqual(len(matches), 1)
            links.append(matches[0])
        self.assertEqual(*links)
        svg = unquote(links[0].split(',', 1)[1])
        self.assertLess(len(svg), 800)
        node = ET.fromstring(svg)
        self.assertEqual(node.attrib.get('viewBox'), '0 0 44 44')
        self.assertEqual(
            [el.tag.rsplit('}', 1)[-1] for el in node.iter()],
            ['svg', 'rect', 'path', 'path'],
        )
        original = re.findall(r'<path fill="currentColor" d="([^"]+)"', HTML)
        self.assertGreaterEqual(len(original), 2)
        self.assertEqual([el.attrib['d'] for el in node if el.tag.endswith('path')], original[:2])
        self.assertNotIn('http:', svg.replace('http://www.w3.org/2000/svg', ''))
        self.assertNotIn('<script', svg)
        self.assertIn("img-src 'self' data:", HTML)



if __name__ == "__main__":
    unittest.main()
