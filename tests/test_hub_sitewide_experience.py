"""Cross-page R8 contracts for the published static Muse Hub site."""
import json
import re
import unittest
from html import escape
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
                self.assertIn('class="site-header r7-header muse-header"', source)
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
                if 'class="subject-source"' in source:
                    self.assertIn('<summary>Included pack path</summary>', source)
                    self.assertIn('class="subject-card-actions"', source)
                self.assertIn('href="../downloads.html"', source)
                self.assertIn('src="../muse-mark.png"', source)

    def test_guides_have_progressive_mobile_navigation(self):
        source = (SITE / "public/index.html").read_text(encoding="utf-8")
        self.assertIn('class="site-header r7-header muse-header"', source)
        self.assertIn('class="mobile-navigation"', source)
        self.assertIn('aria-label="Mobile navigation"', source)
        self.assertIn('href="../downloads.html"', source)
        self.assertIn('href="../experience.css"', source)
        styles = (SITE / "experience.css").read_text(encoding="utf-8")
        self.assertIn(".muse-header .mobile-navigation > summary", styles)
        self.assertIn(".muse-header .mobile-navigation nav a", styles)

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

    def test_same_site_header_and_spacing_tokens_on_every_page_family(self):
        pages = [SITE / "index.html", SITE / "downloads.html",
                 *self.subjects, SITE / "public/index.html"]
        for page in pages:
            with self.subTest(page=page.name):
                content = page.read_text(encoding="utf-8")
                self.assertIn('class="site-header r7-header muse-header"', content)
                self.assertIn('class="mobile-navigation"', content)
                self.assertIn('experience.css', content)
        css = self.css
        self.assertIn('.subject-pagination a:not([rel]):not([aria-current])', css)
        for token in ("--muse-gutter", "--muse-panel", "--muse-border",
                      "--muse-gap", "--muse-sans", "--muse-serif"):
            self.assertIn(token, css)
        guide = (SITE / "public/index.html").read_text("utf-8")
        self.assertNotIn("guide-mobile-nav", guide)
        self.assertNotIn("wordmark-symbol", guide)

    def test_subject_pack_paths_are_accessible_and_not_primary_card_copy(self):
        pages = self.subjects
        disclosed = 0
        for page in pages:
            source = page.read_text("utf-8")
            disclosed += source.count('<details class="subject-source">')
            self.assertNotIn('class="download-entry">Inside this collection:', source)
        catalog = json.loads((SITE / 'downloads.json').read_text('utf-8'))
        packed = sum(row.get('pack_kind') == 'skill-pack' for row in catalog['items'])
        self.assertEqual(disclosed, packed, 'Every skill-pack resource must retain its source-path disclosure')

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

    def test_specialist_setup_links_match_installed_kit_guides(self):
        catalog = json.loads((SITE / "downloads.json").read_text("utf-8"))
        roles = json.loads((SITE / "roles.json").read_text("utf-8"))["roles"]
        specialists = {row["id"]: row for row in catalog["items"] if row["kind"] == "specialist"}
        self.assertEqual(set(specialists), {role["id"] for role in roles})
        self.assertEqual(len(specialists), 15)
        home = (SITE / "index.html").read_text("utf-8")
        library = (SITE / "downloads.html").read_text("utf-8")
        subject_pages = "\n".join(page.read_text("utf-8") for page in self.subjects)
        for role_id, entry in specialists.items():
            with self.subTest(role=role_id):
                setup_link = f"index.html?role={role_id}#setup"
                self.assertEqual(entry["guide_url"], setup_link)
                self.assertTrue((ROOT / "presets" / role_id / "INSTALL.md").is_file())
                self.assertIn(f'<option value="{role_id}"', home)
                self.assertIn(f'href="{setup_link}"', library)
                self.assertIn(f'href="../{setup_link}"', subject_pages)

    def test_public_inventory_counts_match_catalog(self):
        data = json.loads((SITE / "downloads.json").read_text("utf-8"))
        home = (SITE / "index.html").read_text("utf-8")
        downloads = (SITE / "downloads.html").read_text("utf-8")
        for kind, count in data["counts"].items():
            with self.subTest(kind=kind):
                self.assertIn(f'<dd data-library-count="{kind}">{count:,}</dd>', home)
        self.assertIn(
            f'Search {data["counts"]["skill"]:,} skills, '
            f'{data["counts"]["workflow"]:,} workflows, and '
            f'{data["counts"]["tool-guide"]:,} tool guides.',
            downloads,
        )

    def test_subject_structured_breadcrumbs_match_visible_pages(self):
        site_base = "https://atlas-agents-hub.github.io/muse-hub/"
        for page in self.subjects:
            with self.subTest(page=page.name):
                source = page.read_text("utf-8")
                match = re.search(
                    r'<script type="application/ld\+json">(.*?)</script>', source, re.S
                )
                self.assertIsNotNone(match, "Subject page requires JSON-LD")
                schema = json.loads(match.group(1))
                self.assertEqual(schema["@type"], "CollectionPage")
                elements = schema["breadcrumb"]["itemListElement"]
                self.assertEqual(len(elements), 3)
                self.assertEqual([row["position"] for row in elements], [1, 2, 3])
                self.assertEqual(
                    [row["name"] for row in elements[:2]], ["Muse Hub", "Library"]
                )
                self.assertEqual(elements[0]["item"], site_base)
                self.assertEqual(elements[1]["item"], site_base + "downloads.html")
                self.assertEqual(elements[2]["item"], site_base + "library/" + page.name)
                self.assertIn(
                    f'<span>{escape(elements[2]["name"])}</span></nav>',
                    source,
                )

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
