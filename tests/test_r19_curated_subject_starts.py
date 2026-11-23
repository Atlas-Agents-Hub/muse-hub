"""R19: task-based subject discovery without hiding, duplicating, or inventing resources."""
from __future__ import annotations

import html
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import render_downloads  # noqa: E402

GITHUB_PREFIX = "https://github.com/Atlas-Agents-Hub/muse-hub/blob/main/"


class SubjectStartQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = json.loads((ROOT / "hub/site/downloads.json").read_text("utf-8"))["items"]
        cls.by_id = {row["id"]: row for row in cls.rows}

    def test_misclassified_game_skills_use_game_category(self):
        for identity in ("2d-games", "3d-games"):
            with self.subTest(identity=identity):
                self.assertEqual(self.by_id[identity]["category"], "Creative & games")
                self.assertIn("game", self.by_id[identity]["description"].lower())
                source = ROOT / "collections/library/skills" / identity / "SKILL.md"
                self.assertTrue(source.is_file())
                self.assertIn("game", source.read_text("utf-8").lower())

    def test_starting_tasks_are_real_unique_source_backed_resources(self):
        self.assertEqual(len(render_downloads.SUBJECT_STARTS), 10)
        for label, entries in render_downloads.SUBJECT_STARTS.items():
            with self.subTest(subject=label):
                self.assertEqual(len(entries), 3)
                self.assertEqual(len({resource_id for resource_id, _, _ in entries}), 3)
                self.assertEqual(len({name for _, name, _ in entries}), 3)
                page = ROOT / "hub/site/library" / (render_downloads.subject_slug(label) + "-001.html")
                source = page.read_text("utf-8")
                self.assertEqual(source.count('class="subject-start-link"'), 3)
                self.assertEqual(source.count('class="subject-start"'), 1)
                self.assertIn('aria-label="Task paths in ' + html.escape(label) + '"', source)
                for resource_id, task_name, task_detail in entries:
                    with self.subTest(resource_id=resource_id):
                        row = self.by_id[resource_id]
                        self.assertEqual(row["category"], label)
                        self.assertIn(row["kind"], ("skill", "workflow"))
                        self.assertGreaterEqual(len(task_name), 9)
                        self.assertGreaterEqual(len(task_detail), 28)
                        self.assertLessEqual(len(task_detail), 132)
                        self.assertTrue(row["guide_url"].startswith(GITHUB_PREFIX))
                        relative = row["guide_url"][len(GITHUB_PREFIX):]
                        self.assertTrue((ROOT / relative).is_file(), relative)
                        self.assertIn('data-resource-id="' + resource_id + '"', source)
                        self.assertIn('href="' + html.escape(row["guide_url"], quote=True) + '"', source)
                        self.assertIn(html.escape(task_name), source)
                        self.assertIn(html.escape(task_detail), source)

    def test_curated_panel_only_on_subject_entry_pages_and_all_items_retained(self):
        pages = sorted((ROOT / "hub/site/library").glob("*.html"))
        self.assertEqual(len(pages), 35)
        self.assertEqual(sum(page.read_text("utf-8").count('class="download-card subject-card"')
                             for page in pages), len(self.rows))
        for page in pages:
            if page.stem.endswith("-001"):
                continue
            with self.subTest(page=page.name):
                self.assertNotIn('class="subject-start"', page.read_text("utf-8"))
        self.assertEqual(len(self.rows), 5704)
        self.assertEqual(len({(row["kind"], row["id"]) for row in self.rows}), len(self.rows))

    def test_no_unsafe_curated_links(self):
        for label, entries in render_downloads.SUBJECT_STARTS.items():
            for _, title, detail in entries:
                with self.subTest(subject=label, title=title):
                    self.assertNotIn("<", title + detail)
                    self.assertNotIn(">", title + detail)
                    self.assertNotIn("javascript:", (title + detail).lower())
        css = (ROOT / "hub/site/experience.css").read_text("utf-8")
        for selector in (".subject-start-grid", ".subject-start-link",
                         ".subject-start-link:focus-visible"):
            self.assertIn(selector, css)


if __name__ == "__main__":
    unittest.main()
