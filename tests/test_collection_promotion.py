"""Compatibility and source-bound admission of the existing skill collection."""
from __future__ import annotations
import copy,hashlib,importlib.util,json,os,pathlib,subprocess,sys,tempfile,unittest,zipfile,io
R=pathlib.Path(__file__).resolve().parents[1]
C=R/'collections/muse-starters-v1'

def load_tool():
 spec=importlib.util.spec_from_file_location('promoted_collection',R/'tools/muse_collection.py')
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

class CollectionPromotion(unittest.TestCase):
 def test_current_inventory_has_unique_skills_and_workflows(self):
  tool=load_tool();data=tool.load_collection()
  for group in ('skills','workflows','starters'):
   self.assertTrue(data[group])
   self.assertEqual(len(data[group]),len({row['id'] for row in data[group]}))
  report=json.loads((C/'PUBLIC_COMPATIBILITY.json').read_bytes())
  self.assertEqual(report['schema'],'muse-collection-public-compatibility/v2')
  self.assertEqual(len(report['procedure_links']),50)
 def test_all_role_procedures_map_to_current_library_skills(self):
  from muse_presets.catalog import load_registry
  from muse_presets.role_skills import plan_role_skills,SHARED_SKILLS
  expected=set(SHARED_SKILLS)
  for role in load_registry()['presets']:expected.update(plan_role_skills(role)['skill_ids'])
  report=json.loads((C/'PUBLIC_COMPATIBILITY.json').read_bytes())
  self.assertEqual({row['procedure_id'] for row in report['procedure_links']},expected)
  self.assertEqual(len(report['procedure_links']),len(expected))
  skills={s['id'] for s in load_tool().load_collection()['skills']}
  for row in report['procedure_links']:
   self.assertTrue(row['related_collection_skills'])
   self.assertTrue(set(row['related_collection_skills'])<=skills)
  self.assertEqual(len(load_registry()['presets']),15)
 def test_aliases_resolve_existing_specialist_ids(self):
  mapping=json.loads((C/'PUBLIC_COMPATIBILITY.json').read_bytes())
  catalog=json.loads((R/'presets/catalog.json').read_bytes())
  self.assertEqual(mapping['role_aliases'],{'data-engineer':'data-engineering-architect','reliability-engineer':'infrastructure-reliability-engineer'})
  self.assertTrue(set(mapping['role_aliases'].values())<=set(catalog['presets']))
 def test_current_role_profiles_have_matching_setup_and_methods(self):
  roles=json.loads((R/'presets/catalog.json').read_bytes())['presets']
  for role in roles:
   with self.subTest(role=role):
    for leaf in ('README.md','INSTALL.md','playbook.json','preset.json'):
     self.assertTrue((R/'presets'/role/leaf).is_file())
    book=json.loads((R/'presets'/role/'playbook.json').read_bytes())
    self.assertEqual(book['role_id'],role)
    self.assertEqual(len(book['methods']),3)
 def test_collection_documents_and_licenses_are_present(self):
  for path in ('LICENSE','README.md','SKILL_INDEX.md','CATALOG.md','PUBLIC_COMPATIBILITY.json'):
   self.assertTrue((C/path).is_file(),path)
  self.assertTrue((R/'docs/collection/SPECIALIST_QUICKSTART.md').is_file())
 def test_compatibility_check_uses_current_role_and_library_catalogs(self):
  spec=importlib.util.spec_from_file_location('current_compatibility',R/'tools/collection_compatibility.py')
  checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
  report=checker.check_repository()
  data=load_tool().load_collection()
  self.assertEqual(report['collection_skills'],len(data['skills']))
  self.assertEqual(report['workflows'],len(data['workflows']))
  self.assertEqual(report['starters'],len(data['starters']))
 def test_invalid_origin_and_false_native_badges_are_rejected(self):
  tool=load_tool();d=tool.load_collection()
  for change in ['license','invalid-result','duplicate']:
   x=copy.deepcopy(d)
   if change=='license':x['sources'][0]['reuse']='copy';x['sources'][0]['license']='UNKNOWN'
   elif change=='invalid-result':x['skills'][0]['evaluation']='fabricated-result'
   else:x['skills'][1]['steps']=x['skills'][0]['steps']
   with self.subTest(change=change),self.assertRaises(tool.CollectionError):tool.validate(x)
 def test_all_starters_build_and_reopen_with_hashes(self):
  tool=load_tool();d=tool.load_collection()
  for starter in d['starters']:
   with self.subTest(starter=starter['id']):
    raw=tool.build_bytes(d,starter['id'])
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
     self.assertIsNone(z.testzip());m=json.loads(z.read('MANIFEST.json'))
     self.assertEqual(set(z.namelist()),set(m['files'])|{'MANIFEST.json'})
     for n,h in m['files'].items():self.assertEqual(hashlib.sha256(z.read(n)).hexdigest(),h)
     self.assertFalse(any(n.endswith(('IDENTITY.md','SOUL.md','MEMORY.md')) for n in z.namelist()))
 def test_specialist_examples_return_repeatable_computed_results(self):
  tool=load_tool();d=tool.load_collection()
  expected={
   'schema-evolution':{'status':'compatible','added':['note'],'row_count':40},
   'incremental-pipeline':{'status':'applied','stale_events':1,'duplicate_events':1,'applied_keys':['A']},
   'query-plan-review':{'table_scans':['SCAN users'],'searches':['SEARCH orders USING INDEX order_id (id=?)']},
   'service-objectives':{'status':'exhausted','burn_rate':'2','remaining_bad_events':'-1'},
   'capacity-planning':{'required_instances':7,'additional_instances':3},
   'incident-triage':{'status':'resolved','time_to_mitigate_seconds':300.0,'time_to_resolve_seconds':1200.0},
   'automation-contract':{'order':['read','send'],'review':'blocked','blocked_steps':[{'id':'send','reasons':['approval_missing']}]},
   'selector-resilience':{'selected':'semantic','eligible':['semantic']},
   'effect-reconciliation':{'observation':'unknown','receipt_ids':[],'requires_provider_readback':True,'retry_authorized':False},
   'design-token-audit':{'status':'pass','pairs':[{'id':'body','foreground':'ink','background':'paper','ratio':21.0,'minimum_ratio':4.5,'passed':True}]},
   'interaction-state-coverage':{'status':'incomplete','unreachable':['error'],'missing_required':['empty']},
  }
  observed=set()
  for role in tool.EXTENSION_ROLES:
   with self.subTest(role=role):
    out=tool.specialist_demo(d,role)
    self.assertEqual(out['status'],'EXAMPLES_COMPLETED')
    self.assertEqual(out['specialist'],role)
    role_record=next(row for row in d['specialists'] if row['id']==role)
    self.assertEqual({row['skill_id'] for row in out['results']},set(role_record['skills']))
    for row in out['results']:
     observed.add(row['skill_id'])
     self.assertRegex(row['input_sha256'],r'^[a-f0-9]{64}$')
     for key,value in expected[row['skill_id']].items():
      self.assertEqual(row['output'][key],value,(role,row['skill_id'],key))
    self.assertEqual(out,tool.specialist_demo(d,role))
  self.assertEqual(observed,set(expected))
 def test_five_operating_guides_and_daily_desk_contract_exist(self):
  guides={
   'context-loading':['## First useful result','context-demo-v1','## Verify','## Failure and recovery'],
   'skill-setup':['START_HERE.md','examples/export_portable_skills.py --plan','## Check the result','## Update and recover'],
   'subchat-workrooms':['Main','three subchats','quickstart.py --role personal-companion','## Resume after an interruption','INSTALL.md'],
   'durable-documents':['## First useful result','## Verify','## Failure and recovery','restore'],
   'source-and-host-capabilities':['## Try the local tools','workflow-demo pipeline-validation','## Check the intended result','TERMINAL.md'],
  }
  for name,required in guides.items():
   p=R/'docs/handbook'/f'{name}.md';body=p.read_text(encoding='utf8')
   self.assertGreaterEqual(body.count('\n## '),3)
   for token in required:self.assertIn(token,body)
  body=(R/'docs/handbook/daily-desk-design.md').read_text(encoding='utf8')
  for word in ['SpaceCompanion','PersonalCompanion','../spaces/DAILY_DESK.md','stale','restore']:
   self.assertIn(word,body)
  self.assertRegex(body,r'\b(?:3|three) tasks\b')
  self.assertRegex(body,r'\b(?:2|two) notes\b')
 def test_documentation_routes_do_not_silently_replace_profile_install(self):
  body=(R/'docs/collection/MUSE_CURATED_COLLECTION.md').read_text(encoding='utf8')
  for s in ['15','memory','portable','DOWNLOAD_A_SPECIALIST.md','tools/muse_collection.py']:
   self.assertIn(s,body)

if __name__=='__main__':unittest.main(verbosity=2)
