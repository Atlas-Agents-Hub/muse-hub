"""Visual-product acceptance contracts for genuine Planner previews and outcome-led specialist discovery."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import unittest


SITE = Path(__file__).resolve().parents[1] / "hub" / "site"
VALID_SHORTCUTS = {
    "software-engineer",
    "claims-adjudicator",
    "product-interface-designer",
    "coordinator",
}


class _Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class PremiumShowcaseAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (SITE / "index.html").read_text(encoding="utf8")
        cls.css = (SITE / "site.css").read_text(encoding="utf8")
        cls.js = (SITE / "site.js").read_text(encoding="utf8")
        cls.doc = _Markup()
        cls.doc.feed(cls.html)

    def test_real_captures_are_exposed_in_both_device_contexts(self):
        self.assertIn('class="premium-mobile-peek"', self.html)
        images = [attrs for tag, attrs in self.doc.elements if tag == "img"]
        self.assertTrue(any(img.get("src") == "planner-desktop.png" for img in images))
        self.assertTrue(any(img.get("src") == "planner-mobile.png" for img in images))
        self.assertIn('srcset="planner-mobile.png"', self.html)
        self.assertTrue(any(img.get("src") == "planner-mobile.png" and img.get("alt") == "" for img in images))
        self.assertIn('APP SCREENSHOT', self.html)

    def test_full_sized_capture_links_are_accessible_and_honest(self):
        links = [attrs for tag, attrs in self.doc.elements if tag == "a"]
        for name in ("planner-desktop.png", "planner-mobile.png"):
            matches = [link for link in links if link.get("href") == name]
            self.assertEqual(len(matches), 1, name)
            self.assertIn("view", matches[0].get("aria-label", "").lower())
            self.assertEqual(matches[0].get("rel"), "noopener noreferrer")
        self.assertIn("docs/spaces/MUSE_PLANNER.md", self.html)

    def test_shortcuts_map_to_existing_specialist_kit_ids(self):
        shortcuts = [attrs.get("data-suggest-role") for tag, attrs in self.doc.elements
                     if tag == "button" and "data-suggest-role" in attrs]
        self.assertEqual(set(shortcuts), VALID_SHORTCUTS)
        self.assertEqual(len(shortcuts), len(VALID_SHORTCUTS))
        actual_roles = {attrs.get("data-role") for tag, attrs in self.doc.elements
                        if tag == "article" and "data-role" in attrs}
        self.assertTrue(set(shortcuts).issubset(actual_roles))
        self.assertIn("data-suggest-role", self.js)
        self.assertIn("directory.open = true", self.js)

    def test_responsive_preview_keeps_mobile_legibility_and_focus(self):
        self.assertIn(".muse-premium .premium-mobile-peek", self.css)
        self.assertIn(".muse-premium .premium-capture-picture img", self.css)
        self.assertIn("@media(max-width:690px)", self.css)
        self.assertIn(".muse-premium .role-quickpick", self.css)
        self.assertIn(":focus-visible", self.css)

    def test_directory_heading_describes_filtered_results(self):
        self.assertTrue('<span id="role-directory-label">Browse all 15 specialists</span>' in self.html)
        self.assertTrue("directoryLabel.textContent" in self.js)

    def test_specialist_search_remains_real_results_not_a_fake_demo(self):
        self.assertIn('id="role-search"', self.html)
        self.assertIn('id="role-grid"', self.html)
        self.assertIn('id="role-count"', self.html)
        self.assertIn('id="role-empty"', self.html)
        self.assertIn('id="role-reset"', self.html)


if __name__ == "__main__":
    unittest.main()
