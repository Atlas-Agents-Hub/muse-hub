"""Tool recommendations stay useful and complete in specialist downloads."""
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('tool_guides_tested',ROOT/'tools/tool_guides.py')
guides=importlib.util.module_from_spec(spec)
spec.loader.exec_module(guides)


class ToolGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=guides.load_guides()

    def test_every_selected_tool_has_a_practical_guide(self):
        self.assertEqual(len(self.data['guides']),51)
        expected={'atlas-continuum','atlas-omnium','superpowers','tinyfish','promptfoo',
            'product-design','keyword-tool','openseo','brand-strategist','aioscan',
            'hugging-face','planetscale','descope','windowisp','pablooo'}
        self.assertTrue(expected<={r['id'] for r in self.data['guides']})
        for row in self.data['guides']:
            with self.subTest(tool=row['id']):
                self.assertGreaterEqual(len(row['steps']),3)
                self.assertGreaterEqual(len(row['checks']),2)
                self.assertTrue(row['supported_functions'])
                body=(ROOT/row['doc_path']).read_text()
                self.assertIn(row['title'],body)
                self.assertIn(row['starter_prompt'],body)
                self.assertIn('## Check the result',body)

    def test_all_specialists_receive_relevant_setup_guides(self):
        for role in guides.ROLES:
            with self.subTest(role=role):
                chosen=guides.selected_ids(self.data,role=role)
                self.assertGreaterEqual(len(chosen),3)
                files=guides.package_files(self.data,role=role)
                self.assertIn('TOOL_GUIDES.md',files)
                for key in chosen:
                    self.assertIn('docs/tools/'+key+'.md',files)

    def test_each_combined_recipe_resolves_inputs_and_checks(self):
        ids={r['id'] for r in self.data['guides']}
        self.assertEqual(len(self.data['workflows']),12)
        for row in self.data['workflows']:
            with self.subTest(workflow=row['id']):
                self.assertGreaterEqual(len(row['guide_ids']),2)
                self.assertTrue(set(row['guide_ids'])<=ids)
                self.assertTrue(row['inputs'])
                self.assertTrue(row['outputs'])
                self.assertGreaterEqual(len(row['checks']),2)
                files=guides.package_files(self.data,ids=row['guide_ids'])
                self.assertIn(row['title'],files['TOOL_GUIDES.md'].decode())

    def test_unknown_guide_does_not_create_an_empty_package(self):
        with self.assertRaisesRegex(ValueError,'UNKNOWN_TOOL_GUIDE'):
            guides.package_files(self.data,ids=['missing-tool'])

    def test_product_classification_matches_actual_tool_purpose(self):
        by_id={r['id']:r for r in self.data['guides']}
        self.assertIn('product screenshots',by_id['pablooo']['summary'].lower())
        self.assertIn('windows desktop pet',by_id['windowisp']['summary'].lower())
        self.assertIn('local',by_id['promptfoo']['cost'].lower())


if __name__=='__main__':unittest.main()
