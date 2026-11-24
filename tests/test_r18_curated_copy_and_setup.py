"""Independent checks for authored discovery copy and guided package setup."""
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
import build_release  # noqa: E402

SOURCE_MARKERS = {
    "azure-eventhub-dotnet": "eventprocessorclient",
    "cc-skill-project-guidelines-example": "illustrative project template",
    "claude-scientific-skills": "discovery guide",
    "expo-dev-client": "eas build",
    "favicon": "imagemagick",
    "geo-citability": "citability scoring rubric",
    "geo-crawlers": "gptbot",
    "hugging-face-dataset-viewer": "/first-rows",
}

class CuratedCopyAndSetupContracts(unittest.TestCase):
    def test_short_descriptions_are_source_grounded_and_published(self):
        catalog = render_downloads.catalog()
        rows = {row["id"]: row for row in catalog["items"]}
        published = {row["id"]: row for row in json.loads(
            (ROOT / "hub/site/downloads.json").read_text("utf-8"))["items"]}
        subject_html = "\n".join(
            path.read_text("utf-8") for path in (ROOT / "hub/site/library").glob("*.html")
        )
        copies = set()
        for identity, marker in SOURCE_MARKERS.items():
            with self.subTest(identity=identity):
                resource = ROOT / "collections/library/skills" / identity / "SKILL.md"
                self.assertIn(marker, resource.read_text("utf-8").lower())
                description = rows[identity]["description"]
                self.assertGreaterEqual(len(description), 90)
                self.assertLessEqual(len(description), 220)
                self.assertNotEqual(description.lower(), rows[identity]["title"].lower())
                self.assertNotIn(description, copies, "Distinct methods need distinct copy")
                copies.add(description)
                self.assertEqual(description, published[identity]["description"])
                self.assertIn(html.escape(description), subject_html)

    def test_all_15_install_guides_match_release_identity_and_safe_setup(self):
        roles = json.loads((ROOT / "presets/catalog.json").read_text("utf-8"))["presets"]
        version = build_release.DEFAULT_VERSION
        self.assertEqual(len(roles), 15)
        for role in roles:
            with self.subTest(role=role):
                guide = ROOT / "presets" / role / "INSTALL.md"
                body = guide.read_text("utf-8")
                asset_url = build_release.asset_url(
                    build_release.specialist_asset(role, version), version)
                self.assertGreaterEqual(body.count(asset_url), 2)
                self.assertIn("package ID (" + role + ") and version (" + version + ")", body)
                for requirement in ("MANIFEST.json", "skills.yaml",
                                    "assistant/system-profile/profile/",
                                    "assistant/subchat-scopes/subchats/",
                                    "Wait for me to approve the proposed changes.",
                                    "preserve my identity, preferences, memory, credentials",
                                    "If you detect a mismatch, stop"):
                    self.assertIn(requirement, body)
                for relative in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)", body):
                    if "://" not in relative and not relative.startswith("#"):
                        self.assertTrue((guide.parent / relative).exists(), relative)

    def test_two_representative_release_archives_contain_documented_files(self):
        data = build_release.collection.prepare_collection(
            build_release.collection.load_collection(ROOT / "collections/muse-starters-v1"))
        for role in ("garden-companion", "learning-coach"):
            with self.subTest(role=role):
                raw = build_release._zip(build_release.specialist_files(
                    data, role, build_release.DEFAULT_VERSION))
                import io
                import zipfile
                manifest = build_release.verify_archive(raw)
                self.assertEqual(manifest["id"], role)
                self.assertEqual(manifest["version"], build_release.DEFAULT_VERSION)
                with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                    names = set(archive.namelist())
                    for name in ("MANIFEST.json", "START_HERE.md", "INSTALL_IN_MUSE.md",
                                 "skills.yaml", "PROFILE.md", "FIRST_TASK.md",
                                 "CONNECTORS.md",
                                 "assistant/system-profile/profile/IDENTITY.md",
                                 "assistant/role-skills/config/skills.yaml"):
                        self.assertIn(name, names)
                    scoped = [name for name in names
                              if re.fullmatch(r"assistant/subchat-scopes/subchats/[^/]+/SUBCHAT.json", name)]
                    self.assertEqual(len(scoped), 3)
                    self.assertIn("Wait for me to approve", archive.read(
                        "INSTALL_IN_MUSE.md").decode("utf-8"))

if __name__ == "__main__":
    unittest.main()
