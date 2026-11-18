"""Current library counts match the shipped catalogs and practice artifacts."""
from pathlib import Path
import importlib.util
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'collections/muse-starters-v1'


class CollectionInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.counts=json.loads((C/'COUNTS.json').read_bytes())
        spec=importlib.util.spec_from_file_location('current_inventory_collection',ROOT/'tools/muse_collection.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        cls.data=module.load_collection()

    def test_inventory_matches_current_files(self):
        expected={
            'schema':'muse-hub/library-inventory/v1',
            'skills':len(self.data['skills']),
            'workflows':len(self.data['workflows']),
            'task_starters':len(self.data['starters']),
            'specialists':len(self.data['specialists']),
            'skills_with_practice_cases':len({case['skill_id'] for case in self.data['depth_cases']}),
            'practice_cases':len(self.data['depth_cases']),
            'positive_practice_examples':sum('reference_output' in case for case in self.data['depth_cases']),
            'negative_practice_examples':sum('wrong_output' in case for case in self.data['depth_cases']),
            'task_evaluation_specs':len(self.data['evaluation_cases']),
            'executable_specialist_extensions':sum(role.get('kind')=='executable-extension' for role in self.data['specialists']),
        }
        self.assertEqual(self.counts,expected)

    def test_ids_are_unique_and_practice_points_to_real_skills(self):
        for group in ('skills','workflows','starters','specialists','depth_cases'):
            records=self.data[group]
            self.assertEqual(len(records),len({row['id'] for row in records}),group)
        skills={row['id'] for row in self.data['skills']}
        for case in self.data['depth_cases']:
            self.assertIn(case['skill_id'],skills)
            self.assertNotEqual(case['reference_output'],case['wrong_output'])

    def test_inventory_command_derives_the_same_values(self):
        spec=importlib.util.spec_from_file_location('inventory_check',ROOT/'tools/collection_compatibility.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        self.assertEqual(module.current_inventory(self.data),self.counts)

    def test_library_guides_link_current_setup_and_practice(self):
        for file in ('CURATION_POLICY.md','EVALUATION.md','ROADMAP.md'):
            text=(C/file).read_text()
            self.assertIn('COUNTS.json',text)
        self.assertIn('SKILL_INDEX.md',(C/'EVALUATION.md').read_text())
        self.assertIn('tools/collection_compatibility.py --inventory',(C/'CURATION_POLICY.md').read_text())


if __name__=='__main__':unittest.main()
