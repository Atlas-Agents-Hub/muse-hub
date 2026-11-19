"""Exercise the homepage's user routes, origins and preserved setup contract."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import parse_qs, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "hub" / "site"
DOCS = "https://github.com/Atlas-Agents-Hub/muse-ai-agent-presets/blob/main/docs/"
ROLES = {
    "software-engineer", "data-engineering-architect", "automation-engineer",
    "infrastructure-reliability-engineer", "research-evaluator", "claims-adjudicator",
    "adversarial-verifier", "reverse-engineering-researcher", "creative-studio",
    "product-interface-designer", "model-builder", "learning-coach",
    "personal-companion", "garden-companion", "coordinator",
}
ORIGINS = {
    "Inside Muse", "Included with Muse Hub", "Community project", "Official Muse resource",
}
ASSET_NAMES = {
    "data-engineering-architect": "data-engineer",
    "infrastructure-reliability-engineer": "reliability-engineer",
}


class Element:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag = tag
        self.attrs = dict(attrs)
        self.parent = parent
        self.children = []

    def descendants(self):
        for child in self.children:
            if isinstance(child, Element):
                yield child
                yield from child.descendants()

    def text(self):
        return " ".join(
            child.text() if isinstance(child, Element) else child
            for child in self.children
        ).strip()


class Page(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.root = Element("document")
        self.current = self.root
        self.feed(path.read_text(encoding="utf-8"))
        self.nodes = list(self.root.descendants())
        self.ids = {node.attrs["id"]: node for node in self.nodes if "id" in node.attrs}
        self.links = [node for node in self.nodes if node.tag == "a" and "href" in node.attrs]

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in self.VOID:
            self.current = node

    def handle_endtag(self, tag):
        node = self.current
        while node.parent is not None:
            if node.tag == tag:
                self.current = node.parent
                return
            node = node.parent

    def handle_data(self, data):
        self.current.children.append(data)


class HubExperienceHomeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page(SITE / "index.html")

    def test_six_entry_paths_reach_sections_with_usable_actions(self):
        """A visitor can reach every product area without traversing 15 roles."""
        paths = [node for node in self.page.nodes if node.tag == "nav" and node.attrs.get("aria-label") == "Explore Muse Hub"]
        self.assertEqual(len(paths), 1, "The hero needs one accessible six-path navigation.")
        links = [node for node in paths[0].descendants() if node.tag == "a"]
        destinations = {urlsplit(node.attrs["href"]).fragment for node in links}
        self.assertEqual(destinations, {"explore-muse", "specialists", "connect-automate", "companion-spaces", "computer-devices", "explore"})
        self.assertEqual(len(links), 6)
        for link in links:
            with self.subTest(path=link.attrs["href"]):
                self.assertTrue(link.text(), "Every path needs an accessible name.")
                section = self.page.ids[urlsplit(link.attrs["href"]).fragment]
                actions = [node for node in section.descendants() if node.tag == "a" and node.attrs.get("href") and not node.attrs["href"].startswith("#")]
                self.assertTrue(actions, "A product area must lead to a guide, download or service.")

    def test_journeys_reach_the_three_complete_guides(self):
        """Life, development and creative users have a path through the Hub."""
        roadmap = self.page.ids["roadmap"]
        targets = {node.attrs.get("href") for node in roadmap.descendants() if node.tag == "a"}
        self.assertTrue({DOCS + "journeys/" + name for name in (
            "ORGANIZE_YOUR_DAY.md", "BUILD_AND_AUTOMATE.md", "CREATE_SOMETHING.md",
        )}.issubset(targets), "All three journeys need their own working guide destination.")

    def test_feature_actions_explain_origin_and_reach_the_right_source(self):
        """Native features, Hub tools and community integrations remain distinct."""
        destinations = {
            "https://muse.ai/": "Inside Muse",
            "https://www.meta.com/help/superintelligence/1484325780075655/": "Inside Muse",
            "https://apps.apple.com/us/app/muse-from-meta/id6760173601": "Inside Muse",
            "https://platform.muse.ai/docs": "Inside Muse",
            DOCS + "COMPANION_HOME.md": "Included with Muse Hub",
            DOCS + "spaces/DAILY_DESK.md": "Included with Muse Hub",
            DOCS + "FAMILY_LINK.md": "Included with Muse Hub",
            DOCS + "connectors/README.md": "Included with Muse Hub",
            DOCS + "TERMINAL.md": "Community project",
            "https://gadgets.muse.ai/": "Official Muse resource",
        }
        for href, expected in destinations.items():
            with self.subTest(destination=href):
                links = [node for node in self.page.links if node.attrs["href"] == href]
                self.assertTrue(links, f"Missing discovery route: {href}")
                has_context = False
                for link in links:
                    context = link.parent
                    while context and context.tag not in {"article", "section"}:
                        context = context.parent
                    if context:
                        labels = {" ".join(node.text().split()) for node in context.descendants() if "origin-label" in node.attrs.get("class", "").split()}
                        if expected in labels:
                            has_context = True
                self.assertTrue(has_context, "The action needs an origin label in its feature context.")
        labels = [node for node in self.page.nodes if "origin-label" in node.attrs.get("class", "").split()]
        self.assertTrue(all(" ".join(node.text().split()) in ORIGINS for node in labels))

    def test_local_navigation_and_reused_header_footer_resolve(self):
        """In-page and downloads-page navigation cannot silently become dead links."""
        counts = Counter(node.attrs["id"] for node in self.page.nodes if "id" in node.attrs)
        self.assertEqual({key: value for key, value in counts.items() if value != 1}, {})
        for legacy in ("specialists", "toolkit", "explore", "roadmap", "setup"):
            self.assertIn(legacy, counts)
        pages = {"index.html": self.page}
        for link in self.page.links:
            href = link.attrs["href"]
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            with self.subTest(href=href):
                target = parsed.path or "index.html"
                local = SITE / unquote(target)
                self.assertTrue(local.is_file(), f"Local link is missing: {target}")
                if parsed.fragment and local.suffix == ".html":
                    if target not in pages:
                        pages[target] = Page(local)
                    self.assertIn(unquote(parsed.fragment), pages[target].ids)
                if target == "public/index.html" and parsed.query:
                    self.assertIn(parse_qs(parsed.query).get("route", [None])[0], {"cli", "desktop", "watch", "family", "doors", "companion"})
                ancestor = link.parent
                while ancestor:
                    if ancestor.tag in {"header", "footer"} and parsed.fragment:
                        self.assertEqual(parsed.path, "index.html", "Shared navigation must also work on downloads.html.")
                    ancestor = ancestor.parent

    def test_specialist_download_search_and_setup_contract_is_preserved(self):
        """The broader homepage must retain every existing specialist entry point."""
        cards = [node for node in self.page.nodes if "data-role" in node.attrs]
        self.assertEqual({node.attrs["data-role"] for node in cards}, ROLES)
        self.assertEqual(len(cards), len(ROLES))
        options = {node.attrs.get("value") for node in self.page.ids["setup-role-select"].descendants() if node.tag == "option" and node.attrs.get("value")}
        self.assertEqual(options, ROLES)
        for card in cards:
            role = card.attrs["data-role"]
            asset = ASSET_NAMES.get(role, role)
            with self.subTest(role=role):
                self.assertTrue(card.attrs.get("data-category"))
                self.assertTrue(card.attrs.get("data-search"))
                self.assertEqual(card.attrs.get("data-asset"), asset)
                links = [node for node in card.descendants() if node.tag == "a"]
                self.assertTrue(any(node.attrs.get("data-select-role") == role and parse_qs(urlsplit(node.attrs["href"]).query).get("role") == [role] and urlsplit(node.attrs["href"]).fragment == "setup" for node in links))
                self.assertTrue(any("/releases/download/" in node.attrs.get("href", "") and f"/muse-{asset}-v" in node.attrs["href"] and node.attrs["href"].endswith(".zip") for node in links))
        for control in ("role-search", "role-category", "role-reset", "role-empty-clear", "role-count", "role-grid", "setup-role-result", "setup-role-title", "setup-role-download", "setup-role-install", "setup-role-profile"):
            self.assertIn(control, self.page.ids)
        captions = Counter(node.attrs["data-release-caption"] for node in self.page.nodes if "data-release-caption" in node.attrs)
        self.assertEqual(captions, {"packages": 1, "specialist": 1, "footer": 1})


if __name__ == "__main__":
    unittest.main()
