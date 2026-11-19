"""The public exporter admits only the exact sealed Muse Hub website subtree."""
import tempfile
import json
import unittest
from pathlib import Path
from muse_presets.public_export import select_public_files, PublicExportError

SITE_FILES = (
    "README.md", "index.html", "site.css", "site.js", "roles.json",
    "downloads.html", "downloads.js", "downloads.json", "sitemap.xml",
    "public/index.html", "public/styles.css", "public/app.js",
    "public/catalog.json", "INTEGRITY.json"
)
SITE_URL = "https://atlas-origins.github.io/muse-ai-agent-presets/"
RELEASE = json.loads((Path(__file__).resolve().parents[1]/"presets/catalog.json").read_bytes())["release"]
RELEASE_URL = "https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/" + RELEASE

class HubSitePublicAdmission(unittest.TestCase):
    def setUp(self):
        self._scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self._scratch.cleanup)
        self.root = Path(self._scratch.name)
        (self.root/"hub/site").mkdir(parents=True)
        (self.root/"hub/README.md").write_text("# Muse Hub\n", encoding="utf-8")

    def create_site(self):
        for filename in SITE_FILES:
            file = self.root/"hub/site"/filename
            file.parent.mkdir(parents=True,exist_ok=True)
            file.write_text("{}\n" if file.suffix==".json" else "reviewed Muse Hub source\n",encoding="utf-8")

    def test_only_exact_reviewed_website_files_are_exportable(self):
        self.create_site()
        values=select_public_files(self.root,verify_manifest=False)
        expected={"hub/README.md"}|{"hub/site/"+filename for filename in SITE_FILES}
        self.assertEqual(set(values),expected)

    def test_unknown_hub_subtrees_remain_excluded(self):
        self.create_site()
        for name in ("hub/private.html","hub/site/scratch.html","hub/site/extra/tools.py","hub/site/release.zip"):
            file=self.root/name
            file.parent.mkdir(parents=True,exist_ok=True)
            file.write_bytes(b"unreviewed")
            with self.subTest(name=name):
                with self.assertRaises(PublicExportError):
                    select_public_files(self.root,verify_manifest=False)
            file.unlink()

    def test_site_symlinks_remain_excluded(self):
        self.create_site()
        (self.root/"hub/site/extra.html").symlink_to(self.root/"hub/site/index.html")
        with self.assertRaisesRegex(PublicExportError,"SYMLINK_REFUSED"):
            select_public_files(self.root,verify_manifest=False)

    def test_original_root_hub_scope_remains_strict(self):
        values=select_public_files(self.root,verify_manifest=False)
        self.assertEqual(set(values),{"hub/README.md"})
        (self.root/"hub/private.txt").write_text("private source",encoding="utf-8")
        with self.assertRaisesRegex(PublicExportError,"UNAPPROVED_COLLECTION_PATH"):
            select_public_files(self.root,verify_manifest=False)


    def test_public_site_is_findable_from_root_and_documentation(self):
        project = Path(__file__).resolve().parents[1]
        readme = (project/"README.md").read_text(encoding="utf-8")
        docs = (project/"docs/README.md").read_text(encoding="utf-8")
        for text in (readme, docs):
            self.assertIn("](" + SITE_URL + ")", text)
            self.assertIn("DOWNLOAD_A_SPECIALIST.md", text)
        self.assertLess(len(readme.encode("utf-8")), 8000)

    def test_hub_links_to_the_current_release_and_reviewable_website(self):
        project = Path(__file__).resolve().parents[1]
        readme = (project/"README.md").read_text(encoding="utf-8")
        hub = (project/"hub/README.md").read_text(encoding="utf-8")
        for text in (readme, hub):
            self.assertIn(SITE_URL, text)
            self.assertIn(RELEASE_URL, text)
        self.assertIn("](site/index.html)", hub)
        self.assertIn("](site/downloads.html)", hub)
        self.assertIn("](site/public/index.html)", hub)

    def test_ai_discovery_routes_to_the_canonical_public_website(self):
        project = Path(__file__).resolve().parents[1]
        index = (project/"llms.txt").read_text(encoding="utf-8")
        self.assertIn(SITE_URL, index)
        self.assertIn(RELEASE_URL, index)
        self.assertNotIn("atlas-origins.github.io/kits/", index)

if __name__=="__main__":unittest.main()
