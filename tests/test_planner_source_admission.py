"""Preserve the complete Planner app through the public source boundary."""
from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from muse_presets.neutrality import audit_public_tree
from muse_presets.planner_package import (
    INVENTORY_PATH, SOURCE_PATH, reviewed_planner_assets, source_files,
)
from muse_presets.public_export import PublicExportError, select_public_files

ROOT = Path(__file__).resolve().parents[1]


class PlannerSourceAdmissionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="muse-planner-source-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        inventory = self.root / INVENTORY_PATH
        inventory.parent.mkdir(parents=True)
        inventory.write_bytes((ROOT / INVENTORY_PATH).read_bytes())
        for name, raw in source_files(ROOT).items():
            target = self.root / SOURCE_PATH / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)

    def test_complete_app_and_lockfile_survive_source_selection(self):
        selected = select_public_files(self.root)
        expected = {SOURCE_PATH + '/' + name for name in source_files(ROOT)}
        self.assertEqual(set(selected), expected | {INVENTORY_PATH})
        self.assertEqual(len([name for name in selected if name.endswith('.sql')]), 21)
        self.assertEqual(selected[SOURCE_PATH + '/bun.lock'],
                         (ROOT / SOURCE_PATH / 'bun.lock').read_bytes())
        self.assertEqual(audit_public_tree(self.root), [])

    def test_changed_migration_or_client_source_is_rejected(self):
        for name in ('schema.sql', 'client/src/App.tsx'):
            with self.subTest(name=name):
                path = self.root / SOURCE_PATH / name
                original = path.read_bytes()
                path.write_bytes(original + b'\n// changed after review\n')
                with self.assertRaisesRegex(PublicExportError, 'INVALID_PLANNER_ASSET_INVENTORY'):
                    select_public_files(self.root)
                reasons = {row['reason'] for row in audit_public_tree(self.root)}
                self.assertIn('INVALID_PLANNER_ASSET_INVENTORY', reasons)
                path.write_bytes(original)

    def test_unreviewed_extra_app_file_is_rejected(self):
        (self.root / SOURCE_PATH / 'drizzle' / '9999_extra.sql').write_text('SELECT 1;', encoding='utf-8')
        with self.assertRaisesRegex(PublicExportError, 'INVALID_PLANNER_ASSET_INVENTORY'):
            select_public_files(self.root)

    def test_missing_inventory_cannot_silently_drop_support_files(self):
        (self.root / INVENTORY_PATH).unlink()
        with self.assertRaisesRegex(PublicExportError, 'INVALID_PLANNER_ASSET_INVENTORY'):
            select_public_files(self.root)

    def test_unrelated_sql_is_not_admitted_by_planner_review(self):
        (self.root / 'examples' / 'unreviewed.sql').write_text('SELECT 1;', encoding='utf-8')
        with self.assertRaisesRegex(PublicExportError, 'UNREVIEWED_NON_TEXT_FILE'):
            select_public_files(self.root)

    def test_portable_kit_without_planner_needs_no_app_inventory(self):
        with tempfile.TemporaryDirectory(prefix='muse-planner-absent-') as directory:
            self.assertEqual(reviewed_planner_assets(Path(directory)), {})


if __name__ == '__main__':
    unittest.main()
