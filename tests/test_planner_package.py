"""Planner downloads preserve the complete app and reject changed source files."""
from __future__ import annotations

from contextlib import contextmanager
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from muse_presets import planner_package as planner

spec = importlib.util.spec_from_file_location('planner_release_tested', ROOT / 'scripts/build_release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class PlannerPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = planner.source_files(ROOT)
        cls.inventory = (ROOT / planner.INVENTORY_PATH).read_bytes()
        cls.archive = release._zip(release.planner_files())

    @contextmanager
    def copied_source(self):
        with tempfile.TemporaryDirectory(prefix='muse-planner-source-') as directory:
            root = Path(directory)
            files = {planner.SOURCE_PATH + '/' + name: raw for name, raw in self.source.items()}
            files[planner.INVENTORY_PATH] = self.inventory
            for name, raw in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
            yield root

    def test_all_app_files_migrations_and_host_build_contract_are_preserved(self):
        self.assertEqual(len(self.source), 64)
        migrations = {name for name in self.source if name.startswith('drizzle/') and name.endswith('.sql')}
        self.assertEqual(len(migrations), 20)
        required = {'bun.lock', 'package.json', 'space.json', 'schema.sql', 'LICENSE',
                    'metadata/SOURCE.json', 'metadata/TEMPLATE.json', 'client/build.mjs',
                    'scripts/prepare-sdk.ts', 'server/.generated/privileged.contract.ts',
                    'drizzle/meta/_journal.json', 'client/tests/mounted-workspace.test.tsx'}
        self.assertTrue(required <= self.source.keys())
        manifest = json.loads(self.inventory)
        self.assertEqual(manifest['files'], {name: hashlib.sha256(raw).hexdigest()
                                            for name, raw in self.source.items()})
        package = json.loads(self.source['package.json'])
        self.assertEqual(package['dependencies']['@hatch/space-sdk'], 'file:./.sdk/space-sdk.tgz')
        self.assertEqual(package['scripts']['build:client'], 'bun ./client/build.mjs')
        journal = json.loads(self.source['drizzle/meta/_journal.json'])
        self.assertEqual({'drizzle/' + row['tag'] + '.sql' for row in journal['entries']}, migrations)

    def test_extracted_download_verifies_without_the_checkout(self):
        manifest = release.verify_archive(self.archive)
        self.assertEqual(manifest['kind'], 'space')
        self.assertEqual(manifest['id'], 'planner')
        self.assertEqual(manifest['source_files'], 64)
        self.assertEqual(manifest['specialists'], ['coordinator', 'personal-companion'])
        self.assertEqual(manifest['entry'], 'spaces/planner/README.md')
        with tempfile.TemporaryDirectory(prefix='muse-planner-extracted-') as directory:
            root = Path(directory)
            with zipfile.ZipFile(io.BytesIO(self.archive)) as archive:
                archive.extractall(root)
            actual = {p.relative_to(root / planner.PACKAGE_PATH).as_posix(): p.read_bytes()
                      for p in (root / planner.PACKAGE_PATH).rglob('*') if p.is_file()}
            self.assertEqual(actual, self.source)
            self.assertEqual((root / 'PLANNER_FILES.json').read_bytes(), self.inventory)
            env = dict(os.environ)
            env.pop('PYTHONPATH', None)
            env['PYTHONDONTWRITEBYTECODE'] = '1'
            verified = subprocess.run([sys.executable, '-B', 'VERIFY.py'], cwd=root, env=env,
                                      capture_output=True, text=True, encoding='utf-8', timeout=20)
            self.assertEqual(verified.returncode, 0, verified.stdout + verified.stderr)
            self.assertEqual(json.loads(verified.stdout)['status'], 'PASS')
            self.assertIn('[the Planner setup guide](spaces/planner/README.md)',
                          (root / 'START_HERE.md').read_text(encoding='utf-8'))
            altered = root / planner.PACKAGE_PATH / 'drizzle/0020_calendar_source_identity.sql'
            altered.write_bytes(altered.read_bytes() + b'\n-- changed after extraction\n')
            refused = subprocess.run([sys.executable, '-B', 'VERIFY.py'], cwd=root, env=env,
                                     capture_output=True, text=True, encoding='utf-8', timeout=20)
            self.assertEqual(refused.returncode, 2)
            self.assertIn('MEMBER_CHANGED:', refused.stderr)

    def test_archive_is_deterministic_and_uses_the_release_version(self):
        self.assertEqual(self.archive, release._zip(release.planner_files()))
        self.assertEqual(release.planner_asset('v9.8.7'), 'muse-space-planner-v9.8.7.zip')
        self.assertEqual(json.loads(release.planner_files('v9.8.7')['MANIFEST.json'])['version'], 'v9.8.7')
        with self.assertRaises(ValueError):
            release.planner_asset('../v1.6.0')

    def test_runtime_sdk_dependencies_builds_and_databases_are_excluded(self):
        with self.copied_source() as root:
            excluded = ['.sdk/space-sdk.tgz', 'node_modules/package/index.js',
                        'client/dist/index.html', 'client/dist-cvm/index.html', 'server/dist/actions.js',
                        '.space-build/bundle.js', '.bun-cache/cache.bin', '__pycache__/helper.pyc',
                        'app.db', 'app.db-wal', 'app.db-shm', 'local.sqlite', 'client/types.tsbuildinfo']
            for name in excluded:
                path = root / planner.SOURCE_PATH / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'private runtime bytes\0')
            self.assertEqual(planner.source_files(root), self.source)
            packaged = planner.package_files(root)
            for name in excluded:
                self.assertNotIn(planner.PACKAGE_PATH + '/' + name, packaged)

    def test_missing_and_unreviewed_support_files_are_refused(self):
        with self.copied_source() as root:
            app = root / planner.SOURCE_PATH
            extra = app / 'server/src/unreviewed-helper.ts'
            extra.write_text('export const unreviewed = true;\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'PLANNER_SOURCE_ROSTER_MISMATCH'):
                planner.source_files(root)
            extra.unlink()
            (app / 'drizzle/0001_initial.sql').unlink()
            with self.assertRaisesRegex(ValueError, 'PLANNER_SOURCE_ROSTER_MISMATCH'):
                planner.source_files(root)

    def test_changed_app_instructions_lockfile_and_migration_are_refused(self):
        with self.copied_source() as root:
            for name in ('README.md', 'bun.lock', 'drizzle/0020_calendar_source_identity.sql',
                         'server/.generated/privileged.contract.ts'):
                path = root / planner.SOURCE_PATH / name
                path.write_bytes(self.source[name] + b'\nchanged\n')
                with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'PLANNER_SOURCE_CHANGED:'):
                    planner.source_files(root)
                path.write_bytes(self.source[name])

    def test_rehashed_local_inventory_is_not_automatically_accepted(self):
        with self.copied_source() as root:
            manifest = json.loads(self.inventory)
            changed = b'# Changed Planner instructions\n'
            (root / planner.SOURCE_PATH / 'README.md').write_bytes(changed)
            manifest['files']['README.md'] = hashlib.sha256(changed).hexdigest()
            (root / planner.INVENTORY_PATH).write_text(json.dumps(manifest), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'PLANNER_INVENTORY_NOT_REVIEWED'):
                planner.source_files(root)

    def test_unsafe_colliding_and_runtime_inventory_paths_are_refused(self):
        with self.copied_source() as root:
            for name in ('../outside.md', '/README.md', 'C:README.md', 'client\\README.md',
                         'client//README.md', 'client/NUL.txt', 'readme.md', 'node_modules/source.js'):
                changed = json.loads(self.inventory)
                digest = changed['files'].pop('schema.sql')
                changed['files'][name] = digest
                raw = (json.dumps(changed) + '\n').encode()
                (root / planner.INVENTORY_PATH).write_bytes(raw)
                with self.subTest(path=name), mock.patch.object(planner, 'INVENTORY_SHA256', hashlib.sha256(raw).hexdigest()):
                    with self.assertRaisesRegex(ValueError, 'PLANNER_UNSAFE_SOURCE_PATH|PLANNER_INVALID_SOURCE_INVENTORY'):
                        planner.source_files(root)

    def test_symlinked_support_file_is_refused(self):
        with self.copied_source() as root:
            target = root / 'outside-readme.md'
            target.write_bytes(self.source['README.md'])
            member = root / planner.SOURCE_PATH / 'README.md'
            member.unlink()
            try:
                member.symlink_to(target)
            except OSError:
                self.skipTest('Symlink creation is unavailable on this host')
            with self.assertRaisesRegex(ValueError, 'PLANNER_LINKED_SOURCE_REFUSED'):
                planner.source_files(root)

    def test_symlinked_support_directory_is_refused(self):
        with self.copied_source() as root:
            member = root / planner.SOURCE_PATH / 'client'
            target = root / 'outside-client'
            member.rename(target)
            try:
                member.symlink_to(target, target_is_directory=True)
            except OSError:
                self.skipTest('Symlink creation is unavailable on this host')
            with self.assertRaisesRegex(ValueError, 'PLANNER_LINKED_SOURCE_REFUSED'):
                planner.source_files(root)

    def test_source_export_hook_only_returns_exact_reviewed_app_paths(self):
        hashes = planner.reviewed_planner_assets(ROOT)
        self.assertEqual(hashes, {planner.SOURCE_PATH + '/' + name: hashlib.sha256(raw).hexdigest()
                                  for name, raw in self.source.items()})
        self.assertEqual(sum(name.endswith('.sql') for name in hashes), 21)
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(planner.reviewed_planner_assets(Path(directory)), {})


if __name__ == '__main__':
    unittest.main()
