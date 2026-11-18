"""Muse Hub README and standalone website copy/authority regression checks."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from muse_presets.public_export import PublicExportError, select_public_files
from muse_presets.neutrality import audit_public_tree

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"hub/site"
README=ROOT/"README.md"


class MuseHubBrandLaunch(unittest.TestCase):
    def test_readme_is_owner_accurate_and_front_door_is_compact(self):
        text=README.read_text(encoding="utf-8")
        hero=text.split("\n## ",1)[0]
        self.assertLess(len(hero.encode("utf-8")),1100)
        self.assertTrue(text.startswith("# Muse Hub\n"))
        self.assertIn("Independently developed",hero)
        for label in ("15 independent assistants","three subchats","75 skills",
                      "25 workflows","100 task starters","151 connectors"):
            self.assertIn(label,hero)
        for action in ("Choose an assistant","Download v1.2.0",
                       "Visit Muse Hub","Get started"):
            self.assertIn(action,hero)
        self.assertEqual(text.count("<details>"),4)
        self.assertEqual(text.count("</details>"),4)
        self.assertNotIn("community-built",text.lower())
        self.assertNotIn("community source",text.lower())
        self.assertNotIn("Atlas Origins",text)
        self.assertLess(len(text.encode("utf-8")),8000)

    def test_download_and_setup_guides_are_discoverable(self):
        text=README.read_text(encoding="utf-8")
        for path in ("docs/DOWNLOAD_A_SPECIALIST.md",
                     "docs/GETTING_STARTED.md",
                     "docs/TERMINAL.md",
                     "docs/COMPANION_HOME.md",
                     "docs/handbook/specialists-by-task.md",
                     "https://atlas-origins.github.io/muse-ai-agent-presets/",
                     "https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.2.0"):
            self.assertIn(path,text)
        self.assertNotRegex(text, r"\b[HS]\d{2}\b")
        for stale in ("v1.2.0 draft", "source-only", "not deployed"):
            self.assertNotIn(stale,text.lower())
        self.assertIn("quickstart.py --role personal-companion --to",text)

    def test_site_uses_distinct_muse_identity_and_newer_features(self):
        html=(SITE/"index.html").read_text(encoding="utf-8")
        self.assertIn("<title>Muse Hub",html)
        self.assertIn('class="brand-symbol"',html)
        self.assertIn("INDEPENDENTLY BUILT FOR MUSE",html)
        for path in ('href="downloads.html"',
                     "docs/GETTING_STARTED.md",
                     "docs/TERMINAL.md",
                     "docs/COMPANION_HOME.md",
                     "releases/download/v1.2.0/"):
            self.assertIn(path,html)
        self.assertNotRegex(html, r"\b[HS]\d{2}\b")
        self.assertNotIn("COMMUNITY SOURCE PROJECT",html)
        self.assertNotIn("community-built",html.lower())
        self.assertNotIn("atlas-origins.github.io/kits",html)
        self.assertIn("connect-src 'none'",html)

    def test_site_integrity_matches_exact_static_assets(self):
        meta=json.loads((SITE/"INTEGRITY.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["schema"],"muse-hub/public-website-overlay/v1")
        self.assertEqual(meta["source_kind"],"STATIC_WEBSITE")
        self.assertEqual(set(meta["files"]),{
            "README.md", "index.html", "site.css", "site.js", "roles.json",
            "downloads.html", "downloads.js", "downloads.json",
            "public/index.html", "public/styles.css", "public/app.js",
            "public/catalog.json",
        })
        selected=select_public_files(ROOT,verify_manifest=False)
        for path,row in meta["files"].items():
            content=(SITE/path).read_bytes()
            self.assertEqual(row["bytes"],len(content),path)
            self.assertEqual(row["sha256"],hashlib.sha256(content).hexdigest(),path)
            self.assertEqual(selected["hub/site/"+path],content,path)

    def test_unreviewed_svg_never_becomes_public_or_safe_by_name(self):
        # The original byte-pinned privacy policy must remain unchanged;
        # do not expand it to admit a cosmetic vector illustration.
        with tempfile.TemporaryDirectory(prefix="muse-svg-privacy-") as d:
            root=Path(d)
            docs=root/"docs"
            docs.mkdir()
            svg=docs/"unreviewed.svg"
            svg.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg">'
                '<script>alert("bad")</script></svg>',
                encoding="utf-8",
            )
            with self.assertRaises(PublicExportError):
                select_public_files(root,verify_manifest=False)
            self.assertIn(
                {"path":"docs/unreviewed.svg","reason":"UNREVIEWED_BINARY_ASSET"},
                audit_public_tree(root),
            )
            svg.unlink()
            site=root/"hub/site"
            site.mkdir(parents=True)
            (site/"brand.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg"/>',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(PublicExportError,"UNAPPROVED_COLLECTION_PATH"):
                select_public_files(root,verify_manifest=False)


if __name__=="__main__":
    unittest.main()
