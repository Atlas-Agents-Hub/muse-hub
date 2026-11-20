"""Social sharing must render a compelling, stable preview from the published site."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import struct
import unittest
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "hub" / "site"
BASE = "https://atlas-agents-hub.github.io/muse-hub/"
IMAGE = BASE + "social-card.png"


class HeadMetadata(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.properties = {}
        self.names = {}
        self.in_head = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "head":
            self.in_head = True
        if not self.in_head or tag != "meta":
            return
        if "property" in attrs:
            self.properties.setdefault(attrs["property"], []).append(attrs.get("content", ""))
        if "name" in attrs:
            self.names.setdefault(attrs["name"], []).append(attrs.get("content", ""))

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False


class MuseHubSocialPreview(unittest.TestCase):
    def test_homepage_and_resource_directory_share_a_stable_image(self):
        for relative in ("index.html", "public/index.html"):
            with self.subTest(page=relative):
                metadata = HeadMetadata()
                metadata.feed((SITE / relative).read_text(encoding="utf-8"))
                for key, expected in (
                    ("og:image", IMAGE),
                    ("og:image:secure_url", IMAGE),
                    ("og:image:type", "image/png"),
                    ("og:image:width", "1200"),
                    ("og:image:height", "630"),
                ):
                    self.assertEqual(metadata.properties.get(key), [expected], (relative, key))
                self.assertEqual(metadata.names.get("twitter:card"), ["summary_large_image"])
                self.assertEqual(metadata.names.get("twitter:image"), [IMAGE])
                alt = metadata.properties.get("og:image:alt")
                self.assertEqual(len(alt or []), 1)
                self.assertIn("Muse Hub", alt[0])
                self.assertTrue(alt[0].strip())
                self.assertNotIn("localhost", metadata.properties["og:image"][0])

    def test_social_image_is_valid_1200_by_630_png(self):
        asset = SITE / "social-card.png"
        data = asset.read_bytes()
        self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"))
        self.assertEqual(data[12:16], b"IHDR")
        self.assertEqual(struct.unpack(">II", data[16:24]), (1200, 630))
        self.assertLess(len(data), 1000000)
        self.assertGreater(len(data), 15000)
        self.assertEqual(urlparse(IMAGE).path, "/muse-hub/social-card.png")

    def test_homepage_structured_data_advertises_image(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertIn('"image": "' + IMAGE + '"', html)


    def test_social_image_rejects_changed_bytes_even_with_new_digest(self):
        import hashlib
        from muse_presets.site_social import valid_social_card
        data = (SITE / "social-card.png").read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        self.assertTrue(valid_social_card(data, digest))
        tampered = bytearray(data)
        tampered[-32] ^= 0x01
        modified = bytes(tampered)
        self.assertFalse(valid_social_card(modified, hashlib.sha256(modified).hexdigest()))
        self.assertFalse(valid_social_card(data + b"unwanted tail", hashlib.sha256(data + b"unwanted tail").hexdigest()))
        self.assertFalse(valid_social_card(data, "0" * 64))



if __name__ == "__main__":
    unittest.main()
