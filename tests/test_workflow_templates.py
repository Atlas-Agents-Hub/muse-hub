"""Behavior checks for portable workflow graphs and their package resources."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WorkflowTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = load('workflow_library', ROOT / 'tools/workflow_library.py')

    def graph(self):
        return {'schema': 'muse-workflow-graph/v1', 'id': 'example-flow',
                'title': 'Example data flow',
                'nodes': [
                    {'id': 'step-1', 'label': 'Read records', 'operation': 'input',
                     'adapter': 'muse', 'parameters': {}},
                    {'id': 'step-2', 'label': 'Filter rows', 'operation': 'filter',
                     'adapter': 'local', 'parameters': {'field': 'score', 'minimum': 4}},
                    {'id': 'step-3', 'label': 'Return result', 'operation': 'respond',
                     'adapter': 'muse', 'parameters': {}}],
                'edges': [{'from': 'step-1', 'to': 'step-2', 'channel': 'main', 'branch': 0},
                          {'from': 'step-2', 'to': 'step-3', 'channel': 'main', 'branch': 0}],
                'configuration': [], 'entrypoints': ['step-1']}

    def test_plan_preserves_dependency_order_and_branch_labels(self):
        g = self.graph()
        result = self.library.plan(g)
        self.assertEqual(result['waves'], [['step-1'], ['step-2'], ['step-3']])
        self.assertEqual(result['edges'], g['edges'])
        self.assertEqual(result['adapters'], ['local', 'muse'])

    def test_unknown_reference_is_rejected(self):
        g = self.graph(); g['edges'][0]['to'] = 'unknown'
        with self.assertRaisesRegex(ValueError, 'unresolved'):
            self.library.validate_graph(g)

    def test_duplicate_node_is_rejected(self):
        g = self.graph(); g['nodes'].append(copy.deepcopy(g['nodes'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            self.library.validate_graph(g)

    def test_loop_is_reported_instead_of_silently_sorted(self):
        g = self.graph()
        g['edges'].append({'from':'step-3','to':'step-2','channel':'main','branch':1})
        result = self.library.plan(g)
        self.assertEqual(result['waves'], [['step-1']])
        self.assertEqual(result['iterative_nodes'], ['step-2', 'step-3'])

    def test_configuration_placeholder_must_resolve(self):
        g = self.graph();g['nodes'][0]['parameters']={'url':{'configuration_input':'source-url'}}
        with self.assertRaisesRegex(ValueError, 'configuration'):
            self.library.validate_graph(g)
        g['configuration']=[{'id':'source-url','purpose':'URL to the selected public source'}]
        self.library.validate_graph(g)

    def test_nonfinite_parameters_rejected(self):
        g = self.graph();g['nodes'][0]['parameters']={'number':float('nan')}
        with self.assertRaisesRegex(ValueError, 'finite'):
            self.library.validate_graph(g)

    def test_resource_hash_is_verified_before_packaging(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);p=root/'workflow-assets/example-flow';p.mkdir(parents=True)
            raw=(json.dumps(self.graph())+'\n').encode();(p/'WORKFLOW.json').write_bytes(raw)
            row={'id':'example-flow','resources':{'path':'workflow-assets/example-flow',
                 'files':{'WORKFLOW.json':hashlib.sha256(raw).hexdigest()}}}
            out=self.library.package_files(row,root)
            self.assertEqual(out,{'workflows/example-flow/WORKFLOW.json':raw})
            (p/'WORKFLOW.json').write_bytes(raw+b' ')
            with self.assertRaisesRegex(ValueError,'digest'):
                self.library.package_files(row,root)

    def test_traversal_and_symlink_resources_rejected(self):
        row={'id':'example-flow','resources':{'path':'../outside',
             'files':{'WORKFLOW.json':'0'*64}}}
        with self.assertRaisesRegex(ValueError,'path'):
            self.library.validate_resources(row)
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);p=root/'workflow-assets/example-flow';p.mkdir(parents=True)
            target=root/'elsewhere';target.write_text('{}')
            try:(p/'WORKFLOW.json').symlink_to(target)
            except OSError:self.skipTest('symlinks unavailable')
            row['resources']['path']='workflow-assets/example-flow'
            with self.assertRaisesRegex(ValueError,'symlink'):
                self.library.package_files(row,root)

    def test_transformation_reference_is_data(self):
        with tempfile.TemporaryDirectory() as directory:
            marker=Path(directory)/'should-not-exist'
            g=self.graph()
            g['nodes'][1]['parameters']={'reference':f'open({str(marker)!r}, "w").write("bad")'}
            self.library.plan(g)
            self.assertFalse(marker.exists())


class ConversionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.importer=load('workflow_importer',ROOT/'scripts/import_workflow_templates.py')

    def test_credentials_and_account_fields_become_named_inputs(self):
        s=self.importer.Sanitizer({'Read':'step-1'})
        p=s.clean({'chatId':'123456789','headers':{'parameters':[
            {'name':'Authorization','value':'Bearer private-value'}]},
            'url':'https://api.example.test/v1/projects/827110332c21cbe000ab13f6d292d5adb1f1f8db?token=private',
            'model':'vendor-model'},'step-1')
        self.assertIn('configuration_input',p['chatId'])
        self.assertIn('configuration_input',p['model'])
        self.assertNotIn('private',json.dumps(p))
        template=next(x['endpoint_template'] for x in s.configuration if 'endpoint_template' in x)
        self.assertEqual(template,'https://api.example.test/v1/projects/{resource}?token={value}')

    def test_source_reference_becomes_named_step_binding(self):
        s=self.importer.Sanitizer({'Read records':'step-1'})
        value=s.clean("={{ $('Read records').item.json.email }}",'step-2',('text',))
        self.assertIn('steps["step-1"].record.email',value['expression'])
        self.assertNotIn('$(',value['expression'])

    def test_unresolved_source_expression_is_rejected(self):
        s=self.importer.Sanitizer({'Read':'step-1'})
        with self.assertRaisesRegex(ValueError,'unresolved'):
            s.expression("={{ $('Deleted node').item.json.value }}")

    def test_source_blob_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);p=root/'x.json';p.write_text('{"nodes":[]}')
            with self.assertRaisesRegex(ValueError,'blob mismatch'):
                self.importer.convert(p,root,{'x.json':'0'*40},set())

    def test_conversion_preserves_disabled_pass_through_ports_and_empty_branches(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);path=root/'Sample.json'
            source={'nodes':[
                {'name':'Read','type':'n8n-nodes-base.manualTrigger','parameters':{}},
                {'name':'Paused step','type':'n8n-nodes-base.set','disabled':True,
                 'parameters':{'value':'old setting'}},
                {'name':'Join','type':'n8n-nodes-base.merge','parameters':{'mode':'combine'}}],
                'connections':{
                    'Read':{'main':[[{'node':'Paused step','index':0}]]},
                    'Paused step':{'main':[[{'node':'Join','index':1}]]},
                    'Join':{'main':[None]}}}
            raw=json.dumps(source).encode();path.write_bytes(raw)
            digest=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
            result,reason=self.importer.convert(path,root,{'Sample.json':digest},
                {'automation-contract','data-quality-auditor'})
            self.assertIsNone(reason)
            _,graph,_,_=result
            self.assertTrue(graph['nodes'][1]['parameters']['bypass'])
            self.assertEqual(graph['edges'][1]['input'],1)
            self.assertEqual(graph['terminal_branches'],[{'from':'step-3','channel':'main','branch':0}])


class PublishedCollectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0,str(ROOT/'tools'))
        cls.collection=load('workflow_test_collection',ROOT/'tools/muse_collection.py')
        cls.library=load('workflow_test_library',ROOT/'tools/workflow_library.py')
        cls.data=cls.collection.load_collection()
        cls.workflows=[row for row in cls.data['workflows'] if row.get('resources')]

    def test_complete_unique_workflows_and_task_starters(self):
        self.assertGreater(len(self.data['workflows']),250)
        self.assertGreater(len(self.data['starters']),500)
        prompts=[s['first_task'] for s in self.data['starters']]
        self.assertEqual(len(prompts),len(set(prompts)))
        self.assertGreater(len(self.workflows),200)
        for row in self.workflows:
            with self.subTest(workflow=row['id']):
                resources=self.library.package_files(row)
                graph=json.loads(resources['workflows/'+row['id']+'/WORKFLOW.json'])
                self.assertEqual(graph['source']['revision'],'827110332c21cbe000ab13f6d292d5adb1f1f8db')
                self.assertGreaterEqual(len(graph['nodes']),3)
                inputs=json.loads(resources['workflows/'+row['id']+'/INPUTS.json'])
                self.assertEqual(set(inputs['settings']),{x['id'] for x in graph['configuration']})

    def test_downloaded_starter_contains_graph_inputs_and_working_inspector(self):
        p=next(s for s in self.data['starters'] if s.get('workflow_task',{}).get('mode')=='outcome')
        files=self.collection.package_files(self.data,p['id'])
        identity=p['workflows'][0]
        self.assertIn('workflows/'+identity+'/INPUTS.json',files)
        self.assertIn('workflows/'+identity+'/WORKFLOW.json',files)
        self.assertIn('tools/workflow_graph.py',files)
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for name,raw in files.items():
                path=root/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
            run=subprocess.run([sys.executable,'-B','tools/workflow_graph.py',
                'workflows/'+identity+'/WORKFLOW.json'],cwd=root,capture_output=True,text=True,timeout=20)
            self.assertEqual(run.returncode,0,run.stderr)
            result=json.loads(run.stdout)
            self.assertEqual(result['workflow'],identity)
            self.assertTrue(result['waves'] or result['iterative_nodes'])


if __name__ == '__main__':
    unittest.main()
