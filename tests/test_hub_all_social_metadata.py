"""Every indexable Muse Hub landing page has coherent, reusable share metadata."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "hub/site"
BASE = "https://atlas-agents-hub.github.io/muse-hub/"
IMAGE = BASE + "social-card.png"


class Head(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.prop = {}
        self.name = {}
        self.link = {}
        self.title = ""
        self.ldjson = []
        self.in_title = False
        self.in_schema = False
        self.schema_text = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta":
            key = a.get("property")
            if key:
                self.prop.setdefault(key, []).append(a.get("content", ""))
            key = a.get("name")
            if key:
                self.name.setdefault(key, []).append(a.get("content", ""))
        elif tag == "link":
            if a.get("rel"):
                self.link.setdefault(a["rel"], []).append(a.get("href", ""))
        elif tag == "title":
            self.in_title = True
        elif tag == "script" and a.get("type") == "application/ld+json":
            self.in_schema = True
            self.schema_text = ""

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_schema:
            self.schema_text += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_schema:
            self.ldjson.append(json.loads(self.schema_text))
            self.in_schema = False


def pages_from_sitemap():
    root = ET.parse(SITE / "sitemap.xml").getroot()
    urls = [element.text for element in root.findall(".//{*}loc")]
    return [(url, SITE / (url.removeprefix(BASE) or "index.html")) for url in urls]


class SocialLandingPageTests(unittest.TestCase):
    def test_all_sitemap_entries_advertise_valid_social_previews(self):
        pages = pages_from_sitemap()
        self.assertGreaterEqual(len(pages), 35)
        self.assertTrue((SITE / "social-card.png").is_file())
        for url, filename in pages:
            with self.subTest(url=url):
                self.assertTrue(url.startswith(BASE))
                self.assertTrue(filename.is_file(), filename)
                metadata = Head()
                metadata.feed(filename.read_text(encoding="utf-8"))
                self.assertEqual(metadata.link.get("canonical"), [url])
                self.assertEqual(metadata.prop.get("og:url"), [url])
                self.assertEqual(metadata.prop.get("og:image"), [IMAGE])
                self.assertEqual(metadata.prop.get("og:image:secure_url"), [IMAGE])
                self.assertEqual(metadata.prop.get("og:image:type"), ["image/png"])
                self.assertEqual(metadata.prop.get("og:image:width"), ["1200"])
                self.assertEqual(metadata.prop.get("og:image:height"), ["630"])
                self.assertEqual(metadata.name.get("twitter:card"), ["summary_large_image"])
                self.assertEqual(metadata.name.get("twitter:image"), [IMAGE])
                self.assertEqual(metadata.name.get("twitter:title"), metadata.prop.get("og:title"))
                self.assertEqual(len(metadata.prop.get("og:image:alt", [])), 1)
                self.assertIn("Muse Hub", metadata.prop["og:image:alt"][0])
                self.assertEqual(len(metadata.prop.get("og:description", [])), 1)
                self.assertTrue(metadata.prop["og:description"][0].strip())

    def test_downloads_and_subject_pages_have_structured_preview_images(self):
        urls = pages_from_sitemap()
        selected = [(url, p) for url, p in urls if url.endswith("downloads.html") or "/library/" in url]
        self.assertGreaterEqual(len(selected), 35)
        for url, path in selected:
            with self.subTest(url=url):
                head = Head()
                head.feed(path.read_text(encoding="utf-8"))
                self.assertEqual(len(head.ldjson), 1)
                self.assertEqual(head.ldjson[0].get("image"), IMAGE)

    def test_paginated_subjects_have_unique_share_titles(self):
        titles = {}
        for url, path in pages_from_sitemap():
            if "/library/" not in url:
                continue
            head = Head()
            head.feed(path.read_text(encoding="utf-8"))
            title = head.prop["og:title"][0]
            self.assertIn("Muse", title)
            self.assertNotIn(title, titles, f"Duplicate share title in {url} and {titles.get(title)}")
            titles[title] = url


if __name__ == "__main__":
    unittest.main()
