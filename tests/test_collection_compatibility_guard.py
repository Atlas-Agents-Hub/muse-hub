"""Procedure mapping and current public-manifest integrity regressions."""
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("collection_compatibility_guard", ROOT / "tools/collection_compatibility.py")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class CompatibilityGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mapping = json.loads((ROOT / "collections/muse-starters-v1/PUBLIC_COMPATIBILITY.json").read_bytes())
        cls.procedures = {row["procedure_id"] for row in cls.mapping["procedure_links"]}
        cls.skills = {row["id"] for row in json.loads((ROOT / "collections/muse-starters-v1/skills.json").read_bytes())}

    def check(self, value):
        return M.validate_mapping(value, self.procedures, self.skills)

    def test_current_mapping_has_all_procedure_ids(self):
        self.assertIsNone(self.check(self.mapping))
        self.assertEqual(len(self.procedures), 50)

    def test_incomplete_duplicate_unknown_or_empty_links_are_refused(self):
        mutations = (
            ("PROCEDURE_COUNT", lambda x: x["procedure_links"].pop()),
            ("PROCEDURE_ID", lambda x: x["procedure_links"][1].update(procedure_id=x["procedure_links"][0]["procedure_id"])),
            ("PROCEDURE_ID", lambda x: x["procedure_links"][0].update(procedure_id="missing_procedure")),
            ("PROCEDURE_FIELDS", lambda x: x["procedure_links"][0].update(role="")),
            ("RELATED", lambda x: x["procedure_links"][0].update(related_collection_skills=[])),
            ("RELATED", lambda x: x["procedure_links"][0]["related_collection_skills"].append("missing-skill")),
            ("RELATED", lambda x: x["procedure_links"][0]["related_collection_skills"].append(x["procedure_links"][0]["related_collection_skills"][0])),
            ("SCHEMA", lambda x: x.update(unknown=True)),
            ("SCHEMA", lambda x: x["procedure_links"][0].update(unknown=True)),
            ("ALIAS", lambda x: x["role_aliases"].update({"another-role": "coordinator"})),
        )
        for reason, mutate in mutations:
            value = copy.deepcopy(self.mapping)
            mutate(value)
            with self.subTest(reason=reason), self.assertRaisesRegex(ValueError, reason):
                self.check(value)

    def test_adding_library_skills_preserves_existing_procedure_links(self):
        self.assertIsNone(M.validate_mapping(self.mapping, self.procedures, self.skills | {"new-compatible-skill"}))

    def test_duplicate_json_keys_are_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "input.json"
            path.write_text('{"schema":1,"schema":2}')
            with self.assertRaises(ValueError):
                M.read_json(path)

    def test_repository_joins_actual_role_methods_to_current_library(self):
        result = M.check_repository(ROOT)
        collection = M._collection.load_collection()
        self.assertEqual(result["status"], "COLLECTION_COMPATIBILITY_VERIFIED")
        self.assertEqual(result["collection_skills"], len(collection["skills"]))
        self.assertEqual(result["workflows"], len(collection["workflows"]))
        self.assertEqual(result["starters"], len(collection["starters"]))
        self.assertEqual(result["procedures"], 50)
        self.assertEqual(result["roles"], 15)
        self.assertNotIn("verified_source_files", result)

    def test_another_checkout_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaisesRegex(ValueError, "SOURCE_ROOT_MISMATCH"):
                M.check_repository(Path(folder))


class CurrentManifestGuards(unittest.TestCase):
    def fixture(self, folder):
        from muse_presets.public_export import export_public_snapshot
        root = Path(folder) / "source"
        root.mkdir()
        (root / "README.md").write_text("# Example package\n\nA portable example.\n")
        target = Path(folder) / "package.zip"
        export_public_snapshot(root, target)
        with zipfile.ZipFile(target) as package:
            (root / "PUBLIC_SOURCE_MANIFEST.json").write_bytes(package.read("PUBLIC_SOURCE_MANIFEST.json"))
        return root

    def test_current_manifest_accepts_exact_bytes_and_refuses_changed_content(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.fixture(folder)
            self.assertEqual(M.verify_current_manifest(root), 1)
            (root / "README.md").write_text("# Changed package\n")
            with self.assertRaisesRegex(ValueError, "STALE_OR_FORGED_PUBLIC_MANIFEST"):
                M.verify_current_manifest(root)

    def test_manifest_must_include_every_current_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.fixture(folder)
            (root / "LICENSE").write_text("Example license\n")
            with self.assertRaisesRegex(ValueError, "STALE_OR_FORGED_PUBLIC_MANIFEST"):
                M.verify_current_manifest(root)

    def test_missing_or_duplicate_key_manifest_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.fixture(folder)
            manifest = root / "PUBLIC_SOURCE_MANIFEST.json"
            manifest.unlink()
            with self.assertRaises(ValueError):
                M.verify_current_manifest(root)
            manifest.write_text('{"files":{},"files":{}}')
            with self.assertRaises(ValueError):
                M.verify_current_manifest(root)


class ExportNamespaceGuards(unittest.TestCase):
    def test_unapproved_tool_and_collection_paths_are_refused(self):
        from muse_presets.public_export import select_public_files, PublicExportError
        for name in ("tools/new_dispatcher.py", "collections/private-notes/notes.md"):
            with self.subTest(path=name), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                path = root / name
                path.parent.mkdir(parents=True)
                path.write_text("Example\n")
                with self.assertRaisesRegex(PublicExportError, "UNAPPROVED_COLLECTION_PATH"):
                    select_public_files(root, verify_manifest=False)


if __name__ == "__main__":
    unittest.main()
