"""Protect Muse Hub's established visual identity across future redesigns."""
from __future__ import annotations

from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
CSS=(ROOT/"hub/site/site.css").read_text(encoding="utf-8")
HTML=(ROOT/"hub/site/index.html").read_text(encoding="utf-8")

class MuseBrandIdentityTests(unittest.TestCase):
    def test_existing_brand_tokens_remain_authoritative(self):
        for token in ("--black:#151515", "--ink:#161616", "--paper:#f8f6e9",
                      "--paper-strong:#fffcf1", "--signal:#f4ff52",
                      '--serif:Georgia,"Iowan Old Style","Baskerville",serif'):
            self.assertIn(token,CSS)

    def test_new_site_uses_exact_brand_and_serif(self):
        section=CSS.split("/* Muse Hub R3: product-first homepage. Scoped to this page only. */",1)[1]
        self.assertIn("--signal:#f4ff52",section)
        self.assertIn("background:var(--black)",section)
        self.assertIn("font-family:var(--serif)",section)
        self.assertIn("var(--serif)",section)
        self.assertIn(".setup .premium-eyebrow{color:var(--signal)}",section)
        self.assertIn('<meta name="theme-color" content="#151515">',HTML)
        self.assertNotIn("#0d1727",section)
        for unbranded in ("#80ecd0","#8ef0d4","#7aebc5","#14263b","#263d50"):
            self.assertNotIn(unbranded,section)

    def test_logo_and_brand_color_survive_in_site(self):
        self.assertIn("brand-symbol",HTML)
        self.assertIn("brand-text",HTML)
        self.assertIn("MUSE <span>HUB</span>",HTML)
        self.assertIn("premium-button-primary",HTML)
        self.assertIn("premium-product-preview",HTML)
        self.assertIn("premium-space-grid",HTML)
        self.assertTrue((ROOT/"hub/site/social-card.png").is_file())

if __name__=="__main__":
    unittest.main()
