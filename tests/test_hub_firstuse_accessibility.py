"""Regression checks for source-only Muse Hub specialist navigation.

Interactive keyboard behavior is separately exercised in the local Chrome QA.
"""
from pathlib import Path
import re
import unittest

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

    def test_public_pages_share_the_local_muse_hub_mark(self):
        site = ROOT / "hub/site"
        for relative in ("index.html", "downloads.html", "public/index.html"):
            page = site / relative
            body = page.read_text(encoding="utf-8")
            links = re.findall(r'<link rel="icon" type="image/png" href="([.a-z/-]+\.png)">', body)
            self.assertEqual(len(links), 1, relative)
            self.assertEqual((page.parent / links[0]).resolve(), site / "muse-mark.png")
            self.assertIn("img-src 'self' data:", body)
        from muse_presets.site_product import reviewed_product_capture_digests
        self.assertIn("hub/site/muse-mark.png", reviewed_product_capture_digests(ROOT))


if __name__ == "__main__":
    unittest.main()
