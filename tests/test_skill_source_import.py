"""Check imported packages using real resources, deduplication, and boundaries."""
from pathlib import Path
import sys
import tempfile
import unittest
import json

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import import_skill_sources as intake
import skill_library


BODY='''# Query Review

## Method

Read the supplied schema and retain the original query plan. Compare the
estimated cardinality with a representative sample from the actual table.
Record the indexed columns, selected predicates, join keys, and sort order.
Use [the checklist](references/checklist.md) to choose an index candidate.
Run `scripts/check.py` with the supplied JSON and compare its row count.

### Validation

1. Check representative inputs and preserve the exact column types.
2. Measure the query plan before and after the change with the same parameters.
3. Verify that duplicate and missing values keep their intended meaning.

## Example

Request: Review the attached orders query and reduce its scan cost while preserving every result row.

The representative sample contains one order without a customer, two repeated
line items, a zero amount, and a timestamp at the end of the reporting period.
For the outer join, keep unmatched orders in the result. The grouped sum must
be based on the same currency and reporting timezone. Treat the sample as
test data and compare the final key set, row order where required, and numeric
precision. Use an explicit transaction when experimenting with indexes and
revert the change if its query plan makes the representative workload slower.
'''


class IntakeTests(unittest.TestCase):
    def source(self,root,name='query-review',body=BODY):
        folder=root/'skills'/name;folder.mkdir(parents=True)
        (root/'LICENSE').write_text('MIT License\nPermission is granted to use, modify, and distribute this test material.\n')
        (folder/'SKILL.md').write_text('---\nname: '+name+'\ndescription: Review SQL queries and preserve the returned rows while improving the query plan.\n---\n'+body)
        (folder/'references').mkdir();(folder/'references/checklist.md').write_text('Check predicate selectivity, join keys, duplicate values, and the final row count.\n')
        (folder/'scripts').mkdir();(folder/'scripts/check.py').write_text('import json\nimport sys\nprint(len(json.load(sys.stdin)))\n')
        spec={'id':'test-source','repository':'example/query-skills','commit':'a'*40,'patterns':['skills/*/SKILL.md']}
        return spec

    def test_converted_package_keeps_executable_and_reference(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'source';root.mkdir()
            spec=self.source(root)
            (root/'skills/query-review/scripts/check.py').write_bytes(b'import json\r\nimport sys\r\nprint(len(json.load(sys.stdin)))\r\n')
            options,rejected=intake.candidates(spec,root)
            self.assertFalse(rejected)
            row,files,_=intake.portable_package(options[0])
            self.assertIn('scripts/check.py',files)
            self.assertNotIn(b'\r\n', files['scripts/check.py'])
            self.assertIn('references/checklist.md',files)
            self.assertEqual(row['roles'],['data-engineer','model-builder'])
            skill_library._check_references(files)
            self.assertIn('Review the attached orders query',row['example'])

    def test_import_deduplicates_same_method_under_two_names(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'source';root.mkdir();out=Path(td)/'library';out.mkdir()
            spec=self.source(root)
            self.source(root,'second-query',BODY.replace('# Query Review','# Another Title'))
            result=intake.import_sources([spec],{'test-source':root},out)
            self.assertEqual(result['added'],1)
            self.assertTrue(any(x['reason']=='duplicate content' for x in result['rejected']))
            rows=skill_library.load_library(out)
            self.assertEqual(len(rows),1)
            skill_library.package_files(rows[0],out)

    def test_short_template_is_excluded(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            spec=self.source(root,body='Provides step-by-step guidance for SQL.\n')
            options,rejected=intake.candidates(spec,root)
            self.assertFalse(options)
            self.assertTrue(rejected)

    def test_catalog_pointer_is_not_imported_as_a_complete_skill(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            spec=self.source(root,body='> **Catalog stub.** The implementation lives in another repository.\n\n'+BODY)
            options,rejected=intake.candidates(spec,root)
            self.assertFalse(options)
            self.assertIn('catalog pointer',rejected[0]['reason'])

    def test_verified_incomplete_source_stays_excluded_on_reimport(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            spec=self.source(root)
            spec['exclude_entries']={'skills/query-review/SKILL.md':'Required query helper is absent.'}
            options,rejected=intake.candidates(spec,root)
            self.assertFalse(options)
            self.assertIn('incomplete source package',rejected[0]['reason'])

    def test_resume_adopts_only_identical_completed_folders(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'source';root.mkdir();out=Path(td)/'library';out.mkdir()
            spec=self.source(root)
            first=intake.import_sources([spec],{'test-source':root},out)
            self.assertEqual(first['added'],1)
            (out/'catalog.json').unlink()
            resumed=intake.import_sources([spec],{'test-source':root},out)
            self.assertEqual(resumed['added'],1)
            (out/'catalog.json').unlink()
            (out/'skills/query-review/scripts/check.py').write_text('print("changed")\n')
            different=intake.import_sources([spec],{'test-source':root},out)
            self.assertEqual(different['added'],0)
            self.assertTrue(any('different files' in x['reason'] for x in different['rejected']))

    def test_shared_reference_is_copied_into_package(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            spec=self.source(root,body=BODY+'\nRead [shared metrics](../../metrics.md).\n')
            (root/'metrics.md').write_text('Compare elapsed time and pages read using the same representative data.\n')
            options,_=intake.candidates(spec,root)
            _,files,_=intake.portable_package(options[0])
            self.assertTrue(any(x.startswith('references/shared/') for x in files))
            skill_library._check_references(files)

    def test_symlink_resource_is_refused(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            spec=self.source(root)
            try:
                (root/'skills/query-review/outside').symlink_to(root/'LICENSE')
            except OSError:
                self.skipTest('This platform requires elevated permission for symlinks')
            options,_=intake.candidates(spec,root)
            with self.assertRaisesRegex(intake.IntakeError,'symbolic link'):
                intake.portable_package(options[0])

    def test_long_methods_keep_distinct_content_identity(self):
        first=BODY+'\n'+('Read the schema and check the plan.\n'*700)
        second=BODY+'\n'+('Use a histogram and compare estimates.\n'*700)
        self.assertNotEqual(intake.content_identity(first),intake.content_identity(second))

    def test_harness_spelling_and_presentation_are_not_new_skills(self):
        a='# Review\nUse Claude Code to compare the JSON rows.\n'
        b='# Another Title\n Use Muse to compare the JSON rows.  \n'
        self.assertEqual(intake.content_identity(a),intake.content_identity(b))

    def test_portable_paths_preserve_actual_api_names(self):
        text='Read ~/.claude/skills/query/SKILL.md. Use AskUserQuestion when the target is missing. Integrate the Claude Messages API.'
        converted=intake.portable_text(text)
        self.assertNotIn('~/.claude',converted)
        self.assertNotIn('AskUserQuestion',converted)
        self.assertIn('Claude Messages API',converted)

    def test_catalog_larger_than_previous_limit_loads(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);rows=[]
            for number in range(1501):
                key=f'query-method-{number}'
                folder=root/'skills'/key;folder.mkdir(parents=True)
                entry=f'---\nname: {key}\ndescription: Review a query plan and preserve the resulting records.\n---\n# Query {number}\nCheck the query plan with actual inputs.\n'.encode()
                license=b'MIT License\n'
                (folder/'SKILL.md').write_bytes(entry)
                (folder/'LICENSE.txt').write_bytes(license)
                rows.append({'id':key,'title':'Query Method','category':'data-engineering',
                    'trigger':'Review a query plan and preserve its resulting records.',
                    'example':'Review the supplied query plan and explain its slowest operation.',
                    'checks':['Check the row count.','Check the column types.','Check the execution plan.'],
                    'roles':['data-engineer'],'path':'skills/'+key,
                    'files':{'SKILL.md':intake.digest(entry),'LICENSE.txt':intake.digest(license)},
                    'license_files':['LICENSE.txt']})
            (root/'catalog.json').write_text(json.dumps({'schema':skill_library.SCHEMA,'skills':rows}))
            self.assertEqual(len(skill_library.load_library(root)),1501)


if __name__=='__main__':unittest.main()
