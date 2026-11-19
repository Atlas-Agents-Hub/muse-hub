"""Discovery finds useful resources and exports complete, portable custom kits."""
from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('muse_discover', ROOT / 'tools/discover.py')
discover = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(discover)


class DiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = discover.collection.prepare_collection(discover.collection.load_collection())
        cls.records = discover.load_records(cls.data)

    def cli(self, arguments):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(discover.collection, 'load_collection', return_value=self.data), \
                redirect_stdout(out), redirect_stderr(err):
            code = discover.main(arguments)
        return code, out.getvalue(), err.getvalue()

    def redirected_cli(self, arguments):
        return subprocess.run(
            [sys.executable, '-B', str(ROOT / 'tools/discover.py'), *arguments],
            cwd=ROOT, env={**os.environ, 'PYTHONIOENCODING': 'cp1252'},
            capture_output=True, timeout=120,
        )

    def test_all_catalogs_and_fifteen_specialists_are_searchable(self):
        kinds = {row['kind'] for row in self.records}
        self.assertEqual(kinds, set(discover.KINDS))
        self.assertEqual(sum(row['kind'] == 'skill' for row in self.records), len(self.data['skills']))
        self.assertEqual(sum(row['kind'] == 'workflow' for row in self.records), len(self.data['workflows']))
        self.assertEqual(sum(row['kind'] == 'starter' for row in self.records), len(self.data['starters']))
        roles = {item['id'] for row in self.records for item in row['specialists']}
        self.assertEqual(len(roles), 15)
        for role in roles:
            found = discover.search(self.records, role=role, kinds=['specialist'])
            self.assertEqual(found['total'], 1, role)

    def test_every_search_result_guide_exists(self):
        for row in self.records:
            with self.subTest(kind=row['kind'], identifier=row['id']):
                self.assertTrue((ROOT / row['guide']).is_file(), row['guide'])
                for role in row['specialists']:
                    self.assertTrue((ROOT / role['guide']).is_file(), role['guide'])

    def test_exact_id_is_ranked_first_with_explanation(self):
        result = discover.search(self.records, 'query-plan-review', kinds=['skill'])
        self.assertEqual(result['results'][0]['id'], 'query-plan-review')
        self.assertEqual(result['results'][0]['match_reason'], 'exact title or identifier')
        self.assertEqual(result['results'][0]['matched_terms'], ['query', 'plan', 'review'])

    def test_public_specialist_alias_filters_correctly(self):
        public = discover.search(self.records, 'query', kinds=['skill'], role='data-engineering-architect')
        internal = discover.search(self.records, 'query', kinds=['skill'], role='data-engineer')
        self.assertEqual(public, internal)
        self.assertGreater(public['total'], 0)
        for row in public['results']:
            self.assertIn('data-engineering-architect', [item['id'] for item in row['specialists']])

    def test_all_word_matching_requires_every_meaningful_word(self):
        result = discover.search(self.records, 'help me with sql query', kinds=['skill'], match='all')
        self.assertEqual(result['query_terms'], ['sql', 'query'])
        self.assertGreater(result['total'], 0)
        for row in result['results']:
            self.assertEqual(row['matched_terms'], ['sql', 'query'])

    def test_normalized_unicode_exact_title(self):
        row = {'kind': 'skill', 'id': 'coffee', 'title': 'Café Planning', 'summary': 'Plan a café visit.',
               'category': 'everyday-life', 'specialists': [], 'guide': 'guide.md', 'example': '', 'requirements': []}
        result = discover.search([row], 'CAFE\u0301 PLANNING')
        self.assertEqual(result['results'][0]['match_reason'], 'exact title or identifier')

    def test_pagination_is_stable_and_has_no_repeated_results(self):
        first = discover.search(self.records, 'python', limit=3)
        second = discover.search(self.records, 'python', limit=3, offset=first['next_offset'])
        combined = discover.search(self.records, 'python', limit=6)
        self.assertEqual(first['results'] + second['results'], combined['results'])
        shuffled = self.records.copy()
        random.Random(8).shuffle(shuffled)
        self.assertEqual(discover.search(shuffled, 'python', limit=6), combined)
        self.assertEqual(discover.search(self.records, offset=100_000)['next_offset'], None)

    def test_exact_category_filter_and_no_results(self):
        category = next(row['category'] for row in self.records if row['kind'] == 'skill')
        result = discover.search(self.records, kinds=['skill'], category=category.upper())
        self.assertGreater(result['total'], 0)
        self.assertTrue(all(discover._normalized(row['category']) == discover._normalized(category)
                            for row in result['results']))
        missing = discover.search(self.records, 'qzxvmissingwordnoresults')
        self.assertEqual((missing['total'], missing['results'], missing['next_offset']), (0, [], None))

    def test_invalid_queries_filters_and_page_bounds_are_rejected(self):
        for options in ({'query': 'x' * 257}, {'query': 'sql\nsecret'}, {'query': '\u202ereversed'},
                        {'query': '.*'}, {'kinds': ['unknown']}, {'kinds': 'skill'},
                        {'limit': 0}, {'limit': 101}, {'limit': True}, {'offset': -1},
                        {'offset': 100001}, {'match': 'regex'}, {'role': 'unknown'}, {'category': ''}):
            with self.subTest(options=options), self.assertRaises(discover.collection.CollectionError):
                discover.search(self.records, **options)

    def test_workflow_dependencies_and_script_assets_survive_export(self):
        files = discover.compose_files(self.data, skills=['agent-launcher-orchestrator'], workflows=['pipeline-validation'])
        manifest = json.loads(files['MANIFEST.json'])
        workflow = next(row for row in self.data['workflows'] if row['id'] == 'pipeline-validation')
        self.assertTrue(set(workflow['skills']) <= set(manifest['skills']))
        self.assertIn('tools/run.py', files)
        scripts = [key for key in files if key.startswith('skills/agent-launcher-orchestrator/') and key.endswith('.py')]
        self.assertGreater(len(scripts), 0)
        skill = next(row for row in self.data['skills'] if row['id'] == 'agent-launcher-orchestrator')
        for name, raw in discover.collection.skill_library.package_files(skill).items():
            self.assertEqual(files[name], raw, name)
        with zipfile.ZipFile(io.BytesIO(discover.collection.build_file_map_bytes(files))) as archive:
            self.assertEqual(set(archive.namelist()), set(files))
            for name, digest in manifest['files'].items():
                self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), digest)

    def test_workflow_operation_graph_and_inputs_are_kept(self):
        workflow = next(row for row in self.data['workflows'] if row.get('resources'))
        files = discover.compose_files(self.data, workflows=[workflow['id']])
        for path, raw in discover.collection.workflow_library.package_files(workflow).items():
            self.assertEqual(files[path], raw)
        self.assertIn('tools/workflow_graph.py', files)

    def test_starter_retains_its_prompt_and_adds_its_workflows(self):
        files = discover.compose_files(self.data, starters=['daily-planner'])
        manifest = json.loads(files['MANIFEST.json'])
        starter = next(row for row in self.data['starters'] if row['id'] == 'daily-planner')
        self.assertIn(starter['first_task'], files['starters/daily-planner/STARTER.md'].decode())
        self.assertTrue(set(starter['workflows']) <= set(manifest['workflows']))
        self.assertIn('starters/daily-planner/STARTER.md', files['START_HERE.md'].decode())

    def test_custom_toolkit_is_deterministic_and_deduplicates_selections(self):
        first = discover.compose_files(self.data, skills=['query-plan-review', 'schema-evolution'], workflows=['pipeline-validation'])
        second = discover.compose_files(self.data, skills=['schema-evolution', 'query-plan-review', 'query-plan-review'],
                                        workflows=['pipeline-validation', 'pipeline-validation'])
        self.assertEqual(first, second)
        self.assertEqual(discover.collection.build_file_map_bytes(first), discover.collection.build_file_map_bytes(second))

    def test_plan_is_portable_and_shows_added_dependencies(self):
        files = discover.compose_files(self.data, workflows=['pipeline-validation'])
        plan = discover.plan(files)
        self.assertEqual(plan['added_skills'], plan['skills'])
        self.assertEqual(plan['file_count'], len(files))
        self.assertEqual(plan['uncompressed_bytes'], sum(map(len, files.values())))
        self.assertNotIn(str(ROOT), json.dumps(plan))
        self.assertNotIn(str(ROOT), files['MANIFEST.json'].decode())

    def test_missing_or_invalid_selections_are_rejected(self):
        for options in ({}, {'skills': ['does-not-exist']}, {'skills': ['../escape']},
                        {'workflows': ['does-not-exist']}, {'starters': ['does-not-exist']},
                        {'skills': 'query-plan-review'}, {'skills': ['query-plan-review'] * 65}):
            with self.subTest(options=options), self.assertRaises(discover.collection.CollectionError):
                discover.compose_files(self.data, **options)

    def test_build_cli_writes_new_zip_and_preserves_existing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'custom.zip'
            args = ['build', '--skill', 'query-plan-review', '--to', str(target)]
            code, output, error = self.cli(args)
            self.assertEqual((code, error), (0, ''))
            receipt = json.loads(output)
            original = target.read_bytes()
            self.assertEqual(receipt['sha256'], hashlib.sha256(original).hexdigest())
            code, _, error = self.cli(args)
            self.assertEqual(code, 2)
            self.assertIn('cannot create new output', error)
            self.assertEqual(target.read_bytes(), original)

    def test_invalid_selection_and_output_create_no_archive(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'custom.zip'
            code, _, _ = self.cli(['build', '--skill', 'not-a-skill', '--to', str(target)])
            self.assertEqual(code, 2)
            self.assertFalse(target.exists())
            unsafe = Path(folder) / 'alias' / '..' / 'custom.zip'
            code, _, error = self.cli(['build', '--skill', 'query-plan-review', '--to', str(unsafe)])
            self.assertEqual(code, 2)
            self.assertIn('parent traversal', error)
            self.assertFalse(target.exists())
            code, _, _ = self.cli(['build', '--skill', 'query-plan-review', '--to', str(Path(folder) / 'custom.txt')])
            self.assertEqual(code, 2)
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_json_search_and_public_specialist_show(self):
        code, output, error = self.cli(['search', 'query-plan-review', '--kind', 'skill', '--json'])
        self.assertEqual((code, error), (0, ''))
        self.assertEqual(json.loads(output)['results'][0]['id'], 'query-plan-review')
        code, output, error = self.cli(['show', 'specialist', 'data-engineering-architect'])
        self.assertEqual((code, error), (0, ''))
        self.assertEqual(json.loads(output)['guide'], 'presets/data-engineering-architect/INSTALL.md')

    def test_redirected_show_writes_utf8_in_legacy_locale(self):
        result = self.redirected_cli(['show', 'connector', 'asana'])
        self.assertEqual(result.returncode, 0, result.stderr.decode('utf-8', errors='replace'))
        self.assertEqual(result.stderr, b'')
        expected = next(row for row in self.records if row['kind'] == 'connector' and row['id'] == 'asana')
        actual = json.loads(result.stdout.decode('utf-8'))
        self.assertEqual(actual, expected)
        self.assertIn('\u2192', result.stdout.decode('utf-8'))

    def test_redirected_unicode_build_receipt_and_existing_file_error(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'toolkit-\u6d4b\u8bd5-\u2192.zip'
            args = ['build', '--skill', 'query-plan-review', '--to', str(target)]
            result = self.redirected_cli(args)
            self.assertEqual(result.returncode, 0, result.stderr.decode('utf-8', errors='replace'))
            self.assertEqual(result.stderr, b'')
            receipt = json.loads(result.stdout.decode('utf-8'))
            original = target.read_bytes()
            self.assertEqual(receipt['status'], 'PACKAGE_CREATED')
            self.assertEqual(receipt['path'], str(target.absolute()))
            self.assertEqual(receipt['bytes'], len(original))
            self.assertEqual(receipt['sha256'], hashlib.sha256(original).hexdigest())
            with zipfile.ZipFile(io.BytesIO(original)) as archive:
                self.assertIsNone(archive.testzip())
                self.assertIn('MANIFEST.json', archive.namelist())
            repeated = self.redirected_cli(args)
            self.assertEqual(repeated.returncode, 2)
            self.assertEqual(repeated.stdout, b'')
            error = repeated.stderr.decode('utf-8')
            self.assertIn('cannot create new output', error)
            self.assertIn(target.name, error)
            self.assertEqual(target.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
