"""Cross-page R8 contracts for the published static Muse Hub site."""
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "hub/site"


class PageRefs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []
        self.elements = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        for prop in ("href", "src"):
            if prop in attrs:
                self.refs.append((tag, prop, attrs[prop]))


class SitewideExperienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subjects = sorted((SITE / "library").glob("*.html"))
        cls.css = (SITE / "experience.css").read_text(encoding="utf-8")

    def test_every_subject_has_shared_header_footer_and_context(self):
        self.assertGreaterEqual(len(self.subjects), 30)
        categories = {p.name.rsplit("-", 1)[0].rsplit("-", 1)[0] for p in self.subjects}
        self.assertGreaterEqual(len(categories), 12)
        for page in self.subjects:
            with self.subTest(page=page.name):
                source = page.read_text(encoding="utf-8")
                self.assertIn('class="muse-premium subject-index"', source)
                self.assertIn('class="site-header r7-header"', source)
                self.assertIn('class="site-footer premium-footer"', source)
                self.assertIn('class="subject-breadcrumb"', source)
                self.assertIn('class="subject-summary"', source)
                self.assertIn('class="download-card subject-card"', source)
                match = re.search(r'<strong>([\d,]+)</strong> resources', source)
                self.assertIsNotNone(match, "Subject must state resource count")
                count = int(match.group(1).replace(",", ""))
                if count <= 200:
                    self.assertNotIn('class="download-pagination subject-pagination"', source, "Do not render unusable one-page pagination")
                    self.assertIn('<span>All resources</span>', source)
                else:
                    self.assertEqual(source.count('class="download-pagination subject-pagination"'), 2)
                    self.assertEqual(source.count('aria-current="page"'), 2)
                    if page.name.endswith("-001.html"):
                        self.assertIn('rel="next"', source)
                    else:
                        self.assertIn('rel="prev"', source)
                self.assertIn('href="../experience.css"', source)
                self.assertIn('href="../downloads.html"', source)
                self.assertIn('src="../muse-mark.png"', source)

    def test_guides_have_progressive_mobile_navigation(self):
        source = (SITE / "public/index.html").read_text(encoding="utf-8")
        self.assertIn('class="guide-mobile-nav"', source)
        self.assertIn('aria-label="Mobile guide navigation"', source)
        self.assertIn('<summary>Menu ', source)
        self.assertIn('href="../downloads.html"', source)
        styles = (SITE / "public/styles.css").read_text(encoding="utf-8")
        self.assertIn(".guide-mobile-nav > summary:focus-visible", styles)
        self.assertIn(".guide-mobile-nav nav a", styles)

    def test_all_local_page_links_and_assets_resolve(self):
        pages = [SITE / "index.html", SITE / "downloads.html", *self.subjects, SITE / "public/index.html"]
        self.assertEqual(len(pages), len(self.subjects) + 3)
        failures = []
        for page in pages:
            parser = PageRefs()
            parser.feed(page.read_text(encoding="utf-8"))
            for tag, prop, target in parser.refs:
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
                    continue
                local = (page.parent / unquote(parsed.path)).resolve()
                if not local.is_relative_to(SITE.resolve()):
                    failures.append((page.name, target, "escaped website"))
                    continue
                if not local.is_file():
                    failures.append((str(page.relative_to(SITE)), target, "missing target"))
        self.assertEqual(failures, [], f"Local links broke: {failures[:12]}")

    def test_all_38_html_pages_share_brand_and_usable_index(self):
        pages = [SITE / "index.html", SITE / "downloads.html", *self.subjects, SITE / "public/index.html"]
        self.assertGreaterEqual(len(pages), 38)
        for page in pages:
            with self.subTest(page=str(page.relative_to(SITE))):
                parser = PageRefs()
                parser.feed(page.read_text(encoding="utf-8"))
                headings = [attrs for tag, attrs in parser.elements if tag == "h1"]
                self.assertEqual(len(headings), 1, "One clear primary heading on each page")
                landmarks = [tag for tag, _ in parser.elements]
                self.assertIn("main", landmarks)
                self.assertIn("header", landmarks)
                self.assertIn("footer", landmarks)
                self.assertIn("nav", landmarks)

    def test_home_and_main_library_use_shared_spacing_sheet(self):
        for filename in ("index.html", "downloads.html"):
            with self.subTest(page=filename):
                parser = PageRefs()
                parser.feed((SITE / filename).read_text("utf-8"))
                styles = [attrs.get("href") for tag, attrs in parser.elements
                          if tag == "link" and attrs.get("rel") == "stylesheet"]
                self.assertEqual(styles, ["site.css", "experience.css"])

    def test_library_exposes_search_and_advanced_filters_without_js_dependency(self):
        source = (SITE / "downloads.html").read_text("utf-8")
        self.assertIn('<details class="download-advanced">', source)
        self.assertIn('<summary>Refine results</summary>', source)
        self.assertIn('id="download-search"', source)
        self.assertIn('id="download-reset"', source)
        for element in ("download-kind", "download-role", "download-category", "download-sort"):
            self.assertIn('id="' + element + '"', source)
        self.assertIn('class="catalog-subjects"', source)
        self.assertIn('class="download-grid"', source)

    def test_release_guide_matches_released_version(self):
        data = json.loads((SITE / "downloads.json").read_text("utf-8"))
        self.assertEqual(sum(data["counts"].values()), len(data["items"]))
        self.assertEqual(len(data["items"]), 5704)
        planner = next(row for row in data["bundles"] if row["id"] == "space-planner")
        expected = "/blob/" + data["version"] + "/docs/spaces/MUSE_PLANNER.md"
        self.assertIn(expected, planner["guide_url"])
        self.assertIn(expected, (SITE / "index.html").read_text("utf-8"))
        self.assertNotIn("f6b71534070d41806b5eeca5765ad2c3f0dd0ac7", (SITE / "index.html").read_text("utf-8"))


if __name__ == "__main__":
    unittest.main()
