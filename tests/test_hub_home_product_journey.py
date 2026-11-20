"""Task-first Muse Hub home: compact, useful, accessible mobile journeys."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/"hub/site/index.html"
CSS=ROOT/"hub/site/site.css"

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.main=False;self.sections=[];self.anchor=set();self.nav=[];self.links=[];self.headings=[];self.details=[];self.summaries=0
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if a.get("id"):self.anchor.add(a["id"])
        if t=="main":self.main=True
        if t=="section" and self.main and a.get("id"):self.sections.append(a["id"])
        if t=="a" and a.get("href"):self.links.append((a["href"],a.get("class","")))
        if t=="details":self.details.append(a.get("class",""))
        if t=="summary":self.summaries+=1
        if t in ("h1","h2"):self.headings.append(t)
    def handle_endtag(self,t):
        if t=="main":self.main=False

class HomeJourneys(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html=HTML.read_text(encoding="utf-8")
        cls.css=CSS.read_text(encoding="utf-8")
        cls.page=Page();cls.page.feed(cls.html)

    def test_compact_user_journey_and_clear_navigation(self):
        self.assertIn('class="muse-premium"',self.html)
        self.assertIn('id="companion-spaces"',self.html)
        self.assertIn('id="specialists"',self.html)
        self.assertIn('id="toolkit"',self.html)
        self.assertLessEqual(len(self.page.sections),6)
        self.assertLessEqual(len(self.html),48000)  # Full specialist dataset remains in a closed, user-opened directory.
        self.assertLessEqual(len(re.findall(r"<h2\b",self.html)),9)
        self.assertNotIn("Inside Muse",self.html)
        self.assertNotIn("Included with Muse Hub",self.html)
        self.assertNotIn("independently built for",self.html.casefold())
        self.assertIn("Build on a <span>working app.</span>",self.html)
        self.assertIn('class="mobile-navigation"',self.html)
        self.assertIn('class="premium-space-grid"',self.html)
        self.assertIn('class="premium-path-grid"',self.html)
        self.assertIn('class="specialist-directory"',self.html)

    def test_routes_and_downloads_have_real_targets(self):
        self.assertEqual(self.html.count('class="role-card"'),15)
        self.assertEqual(set(re.findall(r'data-release-caption="([^"]+)"',self.html)),{"packages","specialist","footer"})
        self.assertEqual(len(re.findall('href="https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/[^"]+"',self.html)),18)
        for anchor in ("main","companion-spaces","specialists","setup","toolkit","explore","roadmap"):
            self.assertIn(anchor,self.page.anchor)
        for href,cls in self.page.links:
            if href.startswith("#"):
                self.assertIn(href[1:],self.page.anchor,href)
            if href in ("", "#"):
                self.fail("Missing destination")
        for target in ("docs/spaces/MUSE_PLANNER.md","docs/spaces/TASK_BOARD.md","docs/spaces/DAILY_DESK.md"):
            self.assertTrue((ROOT/target).is_file())

    def test_search_and_onboarding_controls_survive(self):
        for key in ("role-search","role-category","role-reset","role-empty","role-empty-clear",
                    "role-count","role-grid","setup-role-select","setup-role-result","setup-role-empty",
                    "setup-role-download","setup-role-install","setup-role-profile"):
            self.assertIn('id="'+key+'"',self.html)
        self.assertGreaterEqual(self.page.summaries,2)

    def test_mobile_ui_and_motion_have_defined_styles(self):
        self.assertIn(".muse-premium .mobile-navigation",self.css)
        self.assertIn(".muse-premium .premium-path-grid",self.css)
        self.assertIn("@media (max-width: 690px)",self.css)
        self.assertIn("prefers-reduced-motion",self.css)
        self.assertIn("overflow-wrap:anywhere",self.css)

if __name__=="__main__":
    unittest.main()
