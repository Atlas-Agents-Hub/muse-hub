"""The public exporter admits only the exact sealed Muse Hub website subtree."""
import tempfile
import unittest
from pathlib import Path
from muse_presets.public_export import select_public_files, PublicExportError

SITE_FILES = (
    "README.md", "index.html", "site.css", "site.js", "roles.json",
    "public/index.html", "public/styles.css", "public/app.js",
    "public/catalog.json", "INTEGRITY.json"
)

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

    def test_only_exact_ten_website_files_are_exportable(self):
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


    def test_source_site_is_findable_from_root_and_documentation(self):
        project = Path(__file__).resolve().parents[1]
        readme = (project/"README.md").read_text(encoding="utf-8")
        docs = (project/"docs/README.md").read_text(encoding="utf-8")
        self.assertIn("](hub/site/index.html)", readme)
        self.assertIn("](hub/site/public/index.html)", readme)
        self.assertIn("](../hub/site/index.html)", docs)
        self.assertIn("](../hub/site/public/index.html)", docs)
        self.assertLess(len(readme.encode("utf-8")), 8000)

    def test_hub_status_explicitly_separates_local_source_from_deployment(self):
        project = Path(__file__).resolve().parents[1]
        readme = (project/"README.md").read_text(encoding="utf-8").lower()
        hub = (project/"hub/README.md").read_text(encoding="utf-8").lower()
        self.assertIn("not deployed", readme)
        self.assertIn("not deployed", hub)
        self.assertIn("source-only", readme)
        self.assertIn("](site/index.html)", hub)
        self.assertIn("](site/public/index.html)", hub)
        self.assertIn("v1.1.0", hub)
        self.assertIn("draft", hub)

    def test_ai_discovery_routes_to_site_source_not_an_unrelated_website(self):
        project = Path(__file__).resolve().parents[1]
        index = (project/"llms.txt").read_text(encoding="utf-8")
        host = "https://raw.githubusercontent.com/atlas-origins/muse-ai-agent-presets/main/"
        self.assertIn(host+"hub/site/index.html", index)
        self.assertIn(host+"hub/site/public/index.html", index)
        self.assertNotIn("atlas-origins.github.io/kits/", index)

if __name__=="__main__":unittest.main()
