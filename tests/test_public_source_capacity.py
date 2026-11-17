"""Public source file-count capacity is bounded without weakening privacy checks."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from muse_presets.public_export import (
    MAX_FILE_BYTES, MAX_FILES, MAX_TOTAL_BYTES,
    PublicExportError, select_public_files,
)


class PublicSourceCapacityTests(unittest.TestCase):
    def test_capacity_extends_future_reviewed_files_with_explicit_hard_limit(self):
        self.assertEqual(MAX_FILES, 2048)
        self.assertEqual(MAX_FILE_BYTES, 2_000_000)
        self.assertEqual(MAX_TOTAL_BYTES, 20_000_000)
        with tempfile.TemporaryDirectory(prefix="muse-public-capacity-") as d:
            root = Path(d)
            docs = root / "docs"
            docs.mkdir()
            (root / "README.md").write_text("# Safe source\n", encoding="utf-8")
            for i in range(2047):
                (docs / f"reviewed-{i:04d}.md").write_text(f"# Reviewed {i}\n", encoding="utf-8")
            files = select_public_files(root, verify_manifest=False)
            self.assertEqual(len(files), 2048)
            self.assertEqual(files["README.md"], b"# Safe source\n")
            (docs / "reviewed-2047.md").write_text("# Excess source\n", encoding="utf-8")
            with self.assertRaisesRegex(PublicExportError, "PUBLIC_SOURCE_RESOURCE_LIMIT"):
                select_public_files(root, verify_manifest=False)

    def test_higher_capacity_never_admits_unreviewed_content(self):
        with tempfile.TemporaryDirectory(prefix="muse-public-privacy-") as d:
            root = Path(d)
            (root / "README.md").write_text("# Reviewed\n", encoding="utf-8")
            docs = root / "docs"
            docs.mkdir()
            for name in ("credentials.json", "local.sqlite", "private-image.png"):
                source = docs / name
                source.write_text("secret", encoding="utf-8")
                with self.subTest(name=name), self.assertRaises(PublicExportError):
                    select_public_files(root, verify_manifest=False)
                source.unlink()
            hub = root / "hub"
            hub.mkdir()
            (hub / "private.md").write_text("private", encoding="utf-8")
            with self.assertRaisesRegex(PublicExportError, "UNAPPROVED_COLLECTION_PATH"):
                select_public_files(root, verify_manifest=False)


if __name__ == "__main__":
    unittest.main()
