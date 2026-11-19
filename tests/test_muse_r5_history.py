"""Task starters retain stable specialist bindings and resolve current methods."""
from pathlib import Path
import json
import importlib.util
import unittest

ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'collections/muse-starters-v1'
BINDINGS={'data-cleaner':'data-engineer','operations-analyst':'reliability-engineer',
          'customer-support-designer':'automation-engineer','frontend-partner':'product-interface-designer'}


def read(name):return json.loads((C/name).read_bytes())


class StarterCompatibilityTests(unittest.TestCase):
    def test_task_specs_and_workflows_reference_current_skills(self):
        skills={row['id'] for row in read('skills.json')}
        cases=read('evaluation_cases.json')
        self.assertEqual(len(cases),len({case['skill_id'] for case in cases}))
        self.assertTrue({case['skill_id'] for case in cases}<=skills)
        for workflow in read('workflows.json'):
            self.assertTrue(workflow['skills'])
            self.assertEqual(len(workflow['skills']),len(set(workflow['skills'])))
            self.assertTrue(set(workflow['skills'])<=skills)

    def test_starter_links_and_specialist_bindings_remain_usable(self):
        starters=read('starters.json')
        self.assertGreater(len(starters),500)
        self.assertEqual(len(starters),len({row['id'] for row in starters}))
        spec=importlib.util.spec_from_file_location('starter_compat_collection',ROOT/'tools/muse_collection.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        collection=module.load_collection(C)
        self.assertEqual({row['id'] for row in starters},{row['id'] for row in collection['starters']})
        skills={row['id'] for row in collection['skills']}
        workflows={row['id'] for row in collection['workflows']}
        roles={row['id'] for row in read('specialists.json')}
        for starter in starters:
            with self.subTest(starter=starter['id']):
                self.assertTrue(set(starter['skills'])<=skills)
                self.assertTrue(set(starter['workflows'])<=workflows)
                self.assertEqual(len(starter['skills']),len(set(starter['skills'])))
                self.assertEqual(len(starter['workflows']),len(set(starter['workflows'])))
                if 'specialist_role' in starter:self.assertIn(starter['specialist_role'],roles)
                if starter['id'] in BINDINGS:self.assertEqual(starter['specialist_role'],BINDINGS[starter['id']])
                self.assertTrue((C/'starters'/starter['id']/'STARTER.md').is_file())


if __name__=='__main__':unittest.main()
