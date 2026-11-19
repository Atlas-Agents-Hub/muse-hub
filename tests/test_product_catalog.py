"""Specialist docs retain their release links and useful task routing as the catalog grows."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('product_catalog',ROOT/'scripts/render_product_catalog.py')
renderer=importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class ProductCatalogRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=renderer.muse_collection.load_collection(ROOT/'collections/muse-starters-v1')
        cls.guides=renderer.tool_guides.load_guides(ROOT)

    def test_release_change_updates_all_specialist_download_maps(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            names=['presets/catalog.json','docs/connectors/catalog.json',
                   'docs/discovery/agent-capabilities.json','hub/site/roles.json']
            names.extend('presets/'+role+'/preset.json' for role in renderer.ROLE_WORKFLOWS)
            for name in names:
                target=root/name
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes((ROOT/name).read_bytes())
            catalog=json.loads((root/'presets/catalog.json').read_bytes())
            catalog['release']='v9.8.7'
            catalog['downloads']={role:'https://example.test/previous-release.zip' for role in catalog['presets']}
            (root/'presets/catalog.json').write_text(json.dumps(catalog))
            with mock.patch.object(renderer.muse_collection,'load_collection',return_value=self.data), \
                 mock.patch.object(renderer.tool_guides,'load_guides',return_value=self.guides):
                outputs=renderer.outputs(root)
            actual=json.loads(outputs['presets/catalog.json'])
            self.assertEqual(set(actual['downloads']),set(catalog['presets']))
            for role,url in actual['downloads'].items():
                expected=renderer.REPO+'/releases/download/v9.8.7/'+renderer.specialist_asset(role,'v9.8.7')
                self.assertEqual(url,expected)
                self.assertIn(expected,outputs['presets/'+role+'/README.md'].decode())
                self.assertIn(expected,outputs['presets/'+role+'/INSTALL.md'].decode())
                self.assertIn(expected,outputs['presets/'+role+'/LIBRARY.md'].decode())

    def test_explicit_extension_starters_are_discoverable_before_related_tasks(self):
        for role in renderer.muse_collection.EXTENSION_ROLES:
            with self.subTest(role=role):
                explicit=[row for row in self.data['starters'] if row.get('specialist_role')==role]
                self.assertTrue(explicit)
                selected=renderer.suggested_starters(self.data,role,[])
                self.assertEqual([row['id'] for row in selected],[row['id'] for row in explicit])
                workflows={flow for row in self.data['starters'] for flow in row['workflows']}
                expanded=renderer.suggested_starters(self.data,role,workflows)
                self.assertEqual(expanded[:len(explicit)],explicit)
                self.assertEqual(len(expanded),len({row['id'] for row in expanded}))

    def test_unrelated_workflow_does_not_add_a_suggested_starter(self):
        data={'starters':[
            {'id':'direct','base_role':'software-engineer','specialist_role':'data-engineer','workflows':['one']},
            {'id':'related','base_role':'research-evaluator','workflows':['two']},
            {'id':'unrelated','base_role':'creative-studio','workflows':['three']},
        ]}
        actual=renderer.suggested_starters(data,'data-engineer',['two'])
        self.assertEqual([row['id'] for row in actual],['direct','related'])

    def test_every_specialist_has_a_practical_public_first_task(self):
        self.assertEqual(set(renderer.FIRST_TASKS),set(renderer.ROLE_WORKFLOWS))
        for role,text in renderer.FIRST_TASKS.items():
            with self.subTest(role=role):
                self.assertNotRegex(text,r'(?i)\b(?:synthetic|fictional|toy|fixture|canary|seeded)\b')
                self.assertTrue(text.startswith(('Bring ','Describe ')))


if __name__=='__main__':
    unittest.main()
