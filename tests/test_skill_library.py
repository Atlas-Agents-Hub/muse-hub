"""Exercise the library's file closure and portable package boundaries."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('skill_library', ROOT / 'tools/skill_library.py')
library = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(library)


class LibraryTests(unittest.TestCase):
    def fixture(self, root):
        folder = root / 'skills/example-method'
        folder.mkdir(parents=True)
        bodies = {
            'SKILL.md': b'---\nname: example-method\ndescription: Use when comparing a proposed change with its requirements.\n---\n# Compare a change\nRead [the checklist](references/checklist.md).\n',
            'references/checklist.md': b'# Checklist\nCheck inputs, expected results, and the observed result.\n',
            'LICENSE': b'MIT License\nCopyright Example\nPermission notice for this test fixture.\n',
        }
        for name, raw in bodies.items():
            p = folder / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
        row = dict(id='example-method', title='Compare a change', category='Engineering',
                   trigger='Use when comparing a proposed change with its requirements.',
                   roles=['software-engineer'], path='skills/example-method',
                   files={n: hashlib.sha256(b).hexdigest() for n, b in bodies.items()},
                   license_files=['LICENSE'], example='Compare the checkout flow with these acceptance criteria.',
                   checks=['Every criterion has a result.', 'Examples use supplied inputs.', 'Failures include a reproduction.'])
        (root / 'catalog.json').write_text(json.dumps({'schema': 'muse-skill-library/v1', 'skills': [row]}))
        return row

    def test_load_and_package_complete_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); row = self.fixture(root)
            self.assertEqual(library.load_library(root)[0]['id'], row['id'])
            files = library.package_files(row, root)
            self.assertEqual(set(files), {'skills/example-method/' + n for n in row['files']})
            self.assertIn(b'Checklist', files['skills/example-method/references/checklist.md'])

    def test_changed_member_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); row = self.fixture(root)
            (root / row['path'] / 'references/checklist.md').write_text('changed')
            with self.assertRaisesRegex(ValueError, 'DIGEST'):
                library.package_files(row, root)

    def test_extra_unlisted_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); row = self.fixture(root)
            (root / row['path'] / 'unexpected.py').write_text('print(1)')
            with self.assertRaisesRegex(ValueError, 'ROSTER'):
                library.load_library(root)

    def test_traversal_case_collision_and_missing_license_are_rejected(self):
        for mutation in ('traversal', 'collision', 'license', 'role'):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); row = self.fixture(root)
                if mutation == 'traversal': row['path'] = '../elsewhere'
                elif mutation == 'collision': row['files']['skill.md'] = row['files']['SKILL.md']
                elif mutation == 'license': row['license_files'] = []
                else: row['roles'] = ['unknown-specialist']
                with self.assertRaises(ValueError): library.validate_entry(row)

    def test_missing_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); row = self.fixture(root)
            raw = (root / row['path'] / 'SKILL.md').read_bytes().replace(b'references/checklist.md', b'references/missing.md')
            (root / row['path'] / 'SKILL.md').write_bytes(raw)
            row['files']['SKILL.md'] = hashlib.sha256(raw).hexdigest()
            with self.assertRaisesRegex(ValueError, 'REFERENCE'):
                library.package_files(row, root)

    def test_symlink_member_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); row = self.fixture(root)
            p = root / row['path'] / 'references/checklist.md'
            p.unlink()
            try: p.symlink_to(root / row['path'] / 'LICENSE')
            except OSError: self.skipTest('symlink creation is unavailable')
            with self.assertRaisesRegex(ValueError, 'LINK'):
                library.package_files(row, root)


if __name__ == '__main__': unittest.main()
