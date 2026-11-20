"""TDD acceptance for authentic responsive Muse Planner showcase and discovery."""
from __future__ import annotations
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import struct
import unittest

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"hub/site"

class _Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_hero=False
        self.images=[]
        self.search_depth=None
        self.details_depth=0
        self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="section" and "premium-hero" in a.get("class","").split():
            self.in_hero=True
        if tag=="img" and self.in_hero:self.images.append(a)
        if tag=="details":self.details_depth+=1
        if a.get("id")=="role-search":self.search_depth=self.details_depth
        if tag=="a":self.links.append(a)
    def handle_endtag(self,tag):
        if tag=="details":self.details_depth-=1
        if tag=="section" and self.in_hero:self.in_hero=False

class AuthenticShowcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.home=(SITE/"index.html").read_text(encoding="utf8")
        cls.css=(SITE/"site.css").read_text(encoding="utf8")
        cls.js=(SITE/"site.js").read_text(encoding="utf8")
        cls.doc=_Page();cls.doc.feed(cls.home)

    def test_hero_uses_authentic_local_planner_screens(self):
        self.assertIn('srcset="planner-mobile.png"',self.home)
        self.assertIn('src="planner-desktop.png"',self.home)
        self.assertTrue(any("Muse Planner" in x.get("alt","") for x in self.doc.images))
        for name,size in (("planner-mobile.png",(390,490)),("planner-desktop.png",(980,745))):
            p=SITE/name
            self.assertTrue(p.is_file(),name)
            data=p.read_bytes()
            self.assertLess(len(data),180000)
            self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertEqual(struct.unpack(">II",data[16:24]),size)

    def test_product_image_visible_on_mobile(self):
        self.assertFalse(re.search(r"\.muse-premium\s+\.premium-product-preview\s*\{\s*display\s*:\s*none",self.css))
        self.assertIn(".muse-premium .premium-product-preview",self.css)

    def test_specialist_search_not_buried_inside_disclosure(self):
        self.assertEqual(self.doc.search_depth,0)
        self.assertIn('id="role-search"',self.home)
        self.assertIn('class="specialist-directory"',self.home)
        self.assertIn("directory.open = true",self.js)

    def test_site_metadata_descriptions_distinct(self):
        seen=set()
        for page in sorted((SITE/"library").glob("*.html")):
            pattern=re.search(r'<meta name="description" content="([^"]+)"',page.read_text(encoding="utf8"))
            self.assertIsNotNone(pattern,str(page))
            self.assertNotIn(pattern.group(1),seen,page.name)
            seen.add(pattern.group(1))

    def test_preview_digests_match_site_integrity(self):
        import json
        manifest=json.loads((SITE/"INTEGRITY.json").read_text(encoding="utf8"))["files"]
        for name in ("planner-desktop.png","planner-mobile.png"):
            data=(SITE/name).read_bytes()
            self.assertEqual(manifest[name]["sha256"],hashlib.sha256(data).hexdigest())
            self.assertEqual(manifest[name]["bytes"],len(data))

    def test_capture_gate_rejects_modified_pixels_and_geometry(self):
        from muse_presets.site_product import valid_product_capture,reviewed_product_capture_digests
        digests=reviewed_product_capture_digests(ROOT)
        self.assertEqual(len(digests),2)
        for relative,digest in digests.items():
            data=(ROOT/relative).read_bytes()
            self.assertTrue(valid_product_capture(relative,data,digest))
            damaged=bytearray(data);damaged[-13] ^= 0x01
            self.assertFalse(valid_product_capture(relative,bytes(damaged),digest))
            self.assertFalse(valid_product_capture(relative,data,"0"*64))
            self.assertFalse(valid_product_capture("hub/site/unreviewed.png",data,digest))

if __name__=="__main__":unittest.main()
