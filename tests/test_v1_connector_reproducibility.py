"""Connector ZIP bytes must be deterministic across independent builds.

The manifest entry is subject to the same fixed metadata contract as source members.
"""
from pathlib import Path
import importlib.util
import tempfile
import unittest
import zipfile
import hashlib

ROOT = Path(__file__).resolve().parents[1]

def module():
    spec = importlib.util.spec_from_file_location(
        "connector_catalog_repro", ROOT / "scripts" / "connector_catalog.py"
    )
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

class ReproducibleConnectorArchive(unittest.TestCase):
    def test_all_members_include_manifest_with_frozen_zip_metadata(self):
        build = module()
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "catalog.zip"
            receipt = build.export_catalog(path)
            self.assertEqual(receipt["connectors"], len(build.load_catalog()['connectors']))
            with zipfile.ZipFile(path) as archive:
                members = archive.infolist()
                self.assertGreater(len(members), 250)
                self.assertIn("MANIFEST.json", [row.filename for row in members])
                for row in members:
                    self.assertEqual(row.date_time, (2026, 1, 1, 0, 0, 0))
                    self.assertEqual(row.create_system, 3, "ZIP must be platform-neutral")
                    self.assertEqual(row.external_attr >> 16, 0o644)

    def test_two_clean_exports_have_identical_sha256(self):
        build = module()
        with tempfile.TemporaryDirectory() as temp:
            first = Path(temp) / "one.zip"
            second = Path(temp) / "two.zip"
            build.export_catalog(first)
            build.export_catalog(second)
            self.assertEqual(
                hashlib.sha256(first.read_bytes()).hexdigest(),
                hashlib.sha256(second.read_bytes()).hexdigest(),
            )

if __name__ == "__main__":
    unittest.main()
