"""Exercise the homepage's user routes, origins and preserved setup contract."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import parse_qs, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "hub" / "site"
REPO_BLOB = "https://github.com/Atlas-Agents-Hub/muse-hub/blob/"
SPACE_GUIDE_REF = "f6b71534070d41806b5eeca5765ad2c3f0dd0ac7"
ROLES = {
    "software-engineer", "data-engineering-architect", "automation-engineer",
    "infrastructure-reliability-engineer", "research-evaluator", "claims-adjudicator",
    "adversarial-verifier", "reverse-engineering-researcher", "creative-studio",
    "product-interface-designer", "model-builder", "learning-coach",
    "personal-companion", "garden-companion", "coordinator",
}
ORIGINS = {
    "Included with Muse Hub", "Community project", "Official Muse resource",
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

    def test_four_task_paths_reach_correct_specialist_setup(self):
        """Each R7 task goes to its matching kit; none may resolve to a generic dead end."""
        cards = [node for node in self.page.nodes if "premium-path-card" in node.attrs.get("class", "").split()]
        expected = {
            "Build an app": "software-engineer",
            "Research a question": "research-evaluator",
            "Improve a design": "product-interface-designer",
            "Plan a project": "coordinator",
        }
        self.assertEqual(len(cards), len(expected))
        seen = set()
        for card in cards:
            headings = [node.text() for node in card.descendants() if node.tag == "strong"]
            self.assertEqual(len(headings), 1)
            title = headings[0]
            self.assertIn(title, expected)
            self.assertNotIn(title, seen)
            seen.add(title)
            url = urlsplit(card.attrs["href"])
            self.assertEqual(url.path, "")
            self.assertEqual(url.fragment, "setup")
            self.assertEqual(parse_qs(url.query).get("role"), [expected[title]])
            self.assertIn(expected[title], ROLES)
            self.assertTrue(any(node.tag == "small" and node.text().strip() for node in card.descendants()))
        self.assertEqual(seen, set(expected))

    def test_primary_journey_to_three_working_space_guides(self):
        """Featured apps have direct usable setup destinations."""
        paths={
            "Muse Planner":"spaces/MUSE_PLANNER.md",
            "Task Board":"spaces/TASK_BOARD.md",
            "Daily Desk":"spaces/DAILY_DESK.md",
        }
        cards=[n for n in self.page.nodes if "premium-space-card" in n.attrs.get("class","").split()]
        self.assertEqual(len(cards),3)
        for title,subpath in paths.items():
            with self.subTest(title=title):
                self.assertTrue((ROOT/"docs"/subpath).is_file())
                ref = "main" if title == "Daily Desk" else SPACE_GUIDE_REF
                guide_url = f"{REPO_BLOB}{ref}/docs/{subpath}"
                self.assertTrue(any(title in card.text() and any(
                    a.tag=="a" and a.attrs.get("href") == guide_url
                    for a in card.descendants()) for card in cards))

    def test_site_copy_is_clear_and_product_led(self):
        """Public copy must not bury the value behind confusing origin badges."""
        text=self.page.root.text()
        for unwanted in ("Inside Muse","Included with Muse Hub","independently built for"):
            self.assertNotIn(unwanted,text)
        self.assertIn("Make Muse your own."," ".join(text.split()))
        self.assertIn("Find a specialist",text)
        self.assertIn("Start with a working Space.",text)
        self.assertEqual(len([n for n in self.page.nodes if "origin-label" in n.attrs.get("class","").split()]),0)

    def test_app_entrypoints_support_keyboard_and_progressive_disclosure(self):
        """Menus and specialist/setup directories should not create a long mobile scroll."""
        disclosures=[n for n in self.page.nodes if n.tag=="details"]
        self.assertEqual(len(disclosures),3)
        self.assertTrue(all("open" not in d.attrs for d in disclosures))
        self.assertTrue(all(any(n.tag=="summary" for n in d.children if isinstance(n,Element)) for d in disclosures))
        primary=[n for n in self.page.nodes if n.tag=="nav" and n.attrs.get("aria-label")=="Primary navigation"]
        self.assertEqual(len(primary),1)
        self.assertEqual([a.text() for a in primary[0].descendants() if a.tag == "a"],
                         ["Spaces", "Specialists", "Library", "Tool guides", "Getting started"])
        self.assertEqual([a.attrs["href"] for a in primary[0].descendants() if a.tag == "a"],
                         ["index.html#companion-spaces", "index.html#specialists", "downloads.html",
                          "downloads.html?type=tool-guide", "index.html#setup"])
        self.assertIn("mobile-navigation",(SITE/"index.html").read_text(encoding="utf8"))
        self.assertIn("premium-space-grid",(SITE/"index.html").read_text(encoding="utf8"))

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
