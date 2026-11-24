"""Public English descriptions must preserve original resource identities."""
import html
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import render_downloads

class EnglishDiscovery(unittest.TestCase):
    def test_all_public_descriptions_have_no_untranslated_scripts(self):
        catalog = render_downloads.catalog()
        rows = catalog["items"]
        self.assertEqual(len(rows), sum(catalog["counts"].values()))
        for row in rows:
            with self.subTest(identity=row["id"]):
                self.assertTrue(row["description"].strip())
                self.assertIsNone(re.search(r"[\u3040-\u30ff\u3400-\u9fff\u0400-\u052f\u0600-\u06ff\uac00-\ud7af]", row["description"]))

    def test_translated_entries_preserve_source_and_reach_static_library(self):
        rows = {r["id"]: r for r in render_downloads.catalog()["items"]}
        published = {r["id"]: r for r in json.loads((ROOT / "hub/site/downloads.json").read_bytes())["items"]}
        pages = "\n".join(p.read_text("utf8") for p in (ROOT / "hub/site/library").glob("*.html"))
        for identity in ['baoyu-comic', 'baoyu-infographic', 'crossframe', 'de-ai-writer', 'emergency-card', 'fact-check-x-unified', 'health-trend-analyzer', 'humanize-chinese', 'liepin-jobs', 'liuguang-banlan-ui', 'makepad-animation', 'makepad-basics', 'makepad-deployment', 'makepad-dsl', 'makepad-event-action', 'makepad-font', 'makepad-layout', 'makepad-platform', 'makepad-shaders', 'makepad-splash', 'monetize', 'pro-launch', 'pro-motion', 'readme-polish', 'robius-app-architecture', 'robius-event-action', 'robius-matrix-integration', 'robius-state-management', 'robius-widget-patterns', 'skill-skill', 'travel-health-analyzer', 'wechat-official-account-strategist', 'xiaohongshu-content-strategist']:
            with self.subTest(identity=identity):
                row = rows[identity]
                source = ROOT / row["guide_url"].split("/blob/main/")[1]
                self.assertRegex(source.read_text("utf8").split("---", 2)[1], r"[\u3400-\u9fff]")
                self.assertEqual(row, published[identity])
                self.assertIn(html.escape(row["description"]), pages)
                self.assertGreaterEqual(len(row["description"].split()), 8)

    def test_dependency_boundary_is_visible(self):
        rows = {r["id"]: r for r in render_downloads.catalog()["items"]}
        self.assertIn("separately installed companion skills", rows["fact-check-x-unified"]["description"])
        self.assertIn("explicit approval", rows["liepin-jobs"]["description"])

if __name__ == "__main__":
    unittest.main()
