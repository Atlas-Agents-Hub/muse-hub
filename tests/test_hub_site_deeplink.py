"""Shareable, fail-closed onboarding URLs for the 15 reviewed Muse Hub roles."""
from __future__ import annotations
import re
import json
import unittest
from pathlib import Path
from urllib.parse import urlsplit, parse_qs
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "hub" / "site"
RELEASE = json.loads((ROOT / "presets/catalog.json").read_bytes())["release"]

class MuseHubDeepLinkTests(unittest.TestCase):
    def test_every_role_card_uses_its_own_same_page_setup_link(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        matches = re.findall(
            r'class="role-card-setup" href="([^"]+)" data-select-role="([a-z][a-z0-9-]+)"',
            html,
        )
        self.assertEqual(len(matches), 15)
        self.assertEqual(len({role for _, role in matches}), 15)
        for url, role in matches:
            with self.subTest(role=role):
                query = urlsplit(url)
                self.assertEqual(query.path, "")
                self.assertEqual(query.fragment, "setup")
                self.assertEqual(parse_qs(query.query), {"role": [role]})
        self.assertEqual(html.count('class="role-card-download"'), 15)
        downloads = re.findall(r'class="role-card-download" href="([^"]+)"', html)
        for url in downloads:
            self.assertTrue(url.startswith(f"https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/{RELEASE}/muse-"),url)
            self.assertTrue(url.endswith(f"-{RELEASE}.zip"),url)
        self.assertIn('id="setup-role-download"', html)

    def test_local_javascript_reads_only_approved_role_ids_and_rewrites_url(self):
        script = (SITE / "site.js").read_text(encoding="utf-8")
        for token in (
            "new URL(window.location.href)",
            "knownRoles.has(incomingRole)",
            "url.searchParams.set('role', slug)",
            "url.searchParams.delete('role')",
            "history.replaceState",
            "event.preventDefault()",
            "selectSetupRole()",
            "roleAssets.get(slug)",
            "setupDownload.href =",
            "card.querySelector('.role-card-download')?.href",
            "roleDownloads.get(slug)",
            "download.startsWith('https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/')",
        ):
            self.assertIn(token, script)
        self.assertIn("if (!knownRoles.has(slug)) return", script)
        for forbidden in ("innerHTML", "fetch(", "XMLHttpRequest", "eval(",
                          "localStorage", "document.write", "new Function("):
            self.assertNotIn(forbidden, script)

    def test_website_exposes_downloads_and_setup_without_internal_gate_labels(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="downloads.html"', html)
        self.assertIn("docs/TERMINAL.md", html)
        self.assertIn("docs/spaces/MUSE_PLANNER.md", html)
        self.assertNotIn("community-built", html.lower())
        self.assertIn("connect-src 'none'", html)
        self.assertNotRegex(html, r"\b[HS]\d{2}\b")
        for stale in ("SOURCE-TESTED", "OPEN GATES", "source-only", "not deployed"):
            self.assertNotIn(stale, html)

if __name__ == "__main__":
    unittest.main()
