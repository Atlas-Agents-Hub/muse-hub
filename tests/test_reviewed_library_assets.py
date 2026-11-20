"""Library support files require their reviewed path and exact catalog bytes."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from muse_presets import source_limits
from muse_presets.neutrality import audit_public_tree
from muse_presets.public_export import PublicExportError, select_public_files


class ReviewedLibraryAssetTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def put(self, name, raw):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def approve(self, files):
        catalog = {'schema': 'muse-skill-library/v1', 'skills': [{
            'id': 'example', 'path': 'skills/example',
            'files': {name: hashlib.sha256(raw).hexdigest()
                      for name, raw in files.items()},
        }]}
        raw = (json.dumps(catalog, sort_keys=True) + '\n').encode()
        self.put(source_limits.LIBRARY_ASSET_CATALOG, raw)
        return patch.object(source_limits, 'LIBRARY_ASSET_CATALOG_SHA256',
                            hashlib.sha256(raw).hexdigest())

    def test_reviewed_support_files_remain_exportable_and_scanned(self):
        examples = {
            'assets/data.csv': b'id,name\nexample,Example\n',
            'assets/icon.svg': b'<svg xmlns="http://www.w3.org/2000/svg"/>\n',
            'assets/schema.sql': b'CREATE TABLE example (id INTEGER);\n',
            'assets/hooks/commit-msg': b'#!/bin/sh\nexit 0\n',
            'scripts/.snyk': b'version: v1.0.0\n',
            '.env.example': b'API_KEY=\nSERVICE_URL=https://example.com\n',
        }
        for name, raw in examples.items():
            self.put('collections/library/skills/example/' + name, raw)
        with self.approve(examples):
            exported = select_public_files(self.root)
            self.assertEqual(audit_public_tree(self.root), [])
            for name, raw in examples.items():
                self.assertEqual(exported['collections/library/skills/example/' + name], raw)
            self.assertIn({'path': 'collections/library/skills/example/assets/data.csv',
                           'reason': 'FORBIDDEN_IDENTITY_LABEL'},
                          audit_public_tree(self.root, forbidden_terms=('Example',)))

    def test_changed_reviewed_asset_is_rejected(self):
        name = 'collections/library/skills/example/assets/data.csv'
        original = b'id,name\nexample,Example\n'
        asset = self.put(name, original)
        with self.approve({'assets/data.csv': original}):
            asset.write_bytes(original + b'new,Unreviewed\n')
            with self.assertRaisesRegex(PublicExportError, 'LIBRARY_ASSET_HASH_MISMATCH'):
                select_public_files(self.root)
            self.assertIn({'path': name, 'reason': 'UNREVIEWED_BINARY_ASSET'},
                          audit_public_tree(self.root))

    def test_unlisted_or_relocated_assets_are_rejected(self):
        raw = b'<svg xmlns="http://www.w3.org/2000/svg"/>\n'
        approved = 'collections/library/skills/example/assets/icon.svg'
        self.put(approved, raw)
        with self.approve({'assets/icon.svg': raw}):
            for name in (
                'collections/library/skills/example/assets/unlisted.svg',
                'collections/library/skills/other/assets/icon.svg',
                'docs/icon.svg', 'docs/private.csv', 'docs/example.template',
                'docs/example.ps1', 'docs/example.go', 'docs/example.tmpl',
                'docs/example.java', 'docs/example.vcf', 'docs/example.example',
                'docs/example.sql', 'docs/example.cpp', 'docs/example.h',
                'docs/example.dot', 'docs/.snyk',
            ):
                with self.subTest(name=name):
                    unlisted = self.put(name, raw)
                    try:
                        with self.assertRaisesRegex(PublicExportError, 'UNREVIEWED_NON_TEXT_FILE'):
                            select_public_files(self.root)
                        self.assertIn({'path': name, 'reason': 'UNREVIEWED_BINARY_ASSET'},
                                      audit_public_tree(self.root))
                    finally:
                        unlisted.unlink()

    def test_catalog_edits_cannot_authorize_new_asset_bytes(self):
        name = 'collections/library/skills/example/assets/data.csv'
        original = b'id,name\nexample,Example\n'
        asset = self.put(name, original)
        with self.approve({'assets/data.csv': original}):
            changed = original + b'new,Unreviewed\n'
            asset.write_bytes(changed)
            catalog_path = self.root / source_limits.LIBRARY_ASSET_CATALOG
            catalog = json.loads(catalog_path.read_bytes())
            catalog['skills'][0]['files']['assets/data.csv'] = hashlib.sha256(changed).hexdigest()
            catalog_path.write_text(json.dumps(catalog))
            with self.assertRaisesRegex(PublicExportError, 'INVALID_LIBRARY_ASSET_CATALOG'):
                select_public_files(self.root)
            self.assertIn('INVALID_LIBRARY_ASSET_CATALOG',
                          {row['reason'] for row in audit_public_tree(self.root)})

    def test_reviewed_inventory_cannot_escape_its_skill_directory(self):
        for name in ('../other/data.csv', '/outside.csv', 'assets/../../outside.csv',
                     'assets\\outside.csv', 'C:/outside.csv'):
            with self.subTest(name=name), self.approve({name: b'id,name\n'}):
                with self.assertRaisesRegex(PublicExportError, 'INVALID_LIBRARY_ASSET_CATALOG'):
                    select_public_files(self.root)

    def test_reviewed_inventory_does_not_override_sensitive_or_binary_rejection(self):
        for name, raw in (
            ('assets/data.csv', b'id,name\x00\n'),
            ('assets/private.key', b'not a permitted file'),
            ('credentials.json', b'{}'),
            ('.env', b'API_KEY=\n'),
        ):
            with self.subTest(name=name):
                asset = self.put('collections/library/skills/example/' + name, raw)
                try:
                    with self.approve({name: raw}):
                        with self.assertRaises(PublicExportError):
                            select_public_files(self.root)
                        self.assertTrue(audit_public_tree(self.root))
                finally:
                    asset.unlink()

    def test_template_review_does_not_bypass_content_checks(self):
        name = 'collections/library/skills/example/.env.example'
        raw = ('API_KEY=sk-proj-' + 'Z' * 32 + '\n').encode()
        self.put(name, raw)
        with self.approve({'.env.example': raw}):
            self.assertIn({'path': name, 'reason': 'POSSIBLE_SECRET'},
                          audit_public_tree(self.root))

    def test_catalog_symlink_is_refused(self):
        path = self.root / source_limits.LIBRARY_ASSET_CATALOG
        path.parent.mkdir(parents=True)
        outside = self.root / 'donor.json'
        outside.write_text('{}')
        try:
            path.symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest('symlink creation unavailable')
        with self.assertRaisesRegex(PublicExportError, 'INVALID_LIBRARY_ASSET_CATALOG'):
            select_public_files(self.root)
        self.assertIn('INVALID_LIBRARY_ASSET_CATALOG',
                      {row['reason'] for row in audit_public_tree(self.root)})


if __name__ == '__main__':
    unittest.main()
