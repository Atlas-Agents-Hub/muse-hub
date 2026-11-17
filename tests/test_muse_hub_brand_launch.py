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
                      "25 workflows","100 task starters","151 connector records"):
            self.assertIn(label,hero)
        for action in ("Choose an assistant","Get the current published release",
                       "Browse tools","Explore connector records"):
            self.assertIn(action,hero)
        self.assertEqual(text.count("<details>"),4)
        self.assertEqual(text.count("</details>"),4)
        self.assertNotIn("community-built",text.lower())
        self.assertNotIn("community source",text.lower())
        self.assertNotIn("Atlas Origins",text)
        self.assertLess(len(text.encode("utf-8")),8000)

    def test_recent_source_work_is_discoverable_without_native_claims(self):
        text=README.read_text(encoding="utf-8")
        for path in ("kits/engineering-doors/README.md",
                     "kits/family-handoff/README.md",
                     "docs/discovery/ROUTE_COMPATIBILITY.md",
                     "docs/HUB_FEATURE_READINESS.md",
                     "docs/handbook/specialists-by-task.md",
                     "docs/discovery/agent-capabilities.json",
                     "docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md"):
            self.assertIn(path,text)
        self.assertIn("H11",text)
        self.assertIn("H12",text)
        self.assertIn("v1.1.0",text)
        self.assertIn("draft",text.lower())
        self.assertIn("v1.0.0",text)
        self.assertIn("source-only",text.lower())
        self.assertIn("not installed native Muse agents",text)
        self.assertIn("not deployed",text.lower())
        self.assertIn("quickstart.py --role personal-companion --to",text)

    def test_site_uses_distinct_muse_identity_and_newer_features(self):
        html=(SITE/"index.html").read_text(encoding="utf-8")
        self.assertIn("<title>Muse Hub",html)
        self.assertIn('class="brand-symbol"',html)
        self.assertIn("INDEPENDENTLY BUILT FOR MUSE",html)
        self.assertIn("H11 / SOURCE-TESTED",html)
        self.assertIn("H12 / SOURCE-TESTED",html)
        self.assertIn("H00–H21 / OPEN GATES",html)
        for path in ("kits/engineering-doors/README.md",
                     "kits/family-handoff/README.md",
                     "docs/HUB_FEATURE_READINESS.md"):
            self.assertIn(path,html)
        self.assertNotIn("COMMUNITY SOURCE PROJECT",html)
        self.assertNotIn("community-built",html.lower())
        self.assertNotIn("atlas-origins.github.io/kits",html)
        self.assertIn("connect-src 'none'",html)

    def test_site_integrity_matches_exact_static_assets(self):
        meta=json.loads((SITE/"INTEGRITY.json").read_text(encoding="utf-8"))
        self.assertEqual(meta["schema"],"muse-hub/public-website-overlay/v1")
        self.assertEqual(len(meta["files"]),9)
        self.assertIn("index.html",meta["files"])
        self.assertIn("public/catalog.json",meta["files"])
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
