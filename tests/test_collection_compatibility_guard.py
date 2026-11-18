"""Negative controls for inventory reconciliation; local metadata is never authority."""
import copy,hashlib,importlib.util,json,pathlib,tempfile,unittest
R=pathlib.Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('collection_compatibility_guard',R/'tools/collection_compatibility.py')
M=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(M)

class CompatibilityGuards(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.mapping=json.loads((R/'collections/muse-starters-v1/PUBLIC_COMPATIBILITY.json').read_bytes())
  cls.legacy={x['legacy_id'] for x in cls.mapping['procedure_links']}
  cls.skills={x['id'] for x in json.loads((R/'collections/muse-starters-v1/skills.json').read_bytes())}
 def check(self,x):return M.validate_mapping(x,self.legacy,self.skills)
 def test_reviewed_mapping_is_valid(self):self.assertIsNone(self.check(self.mapping))
 def test_library_starts_at_seventy_five(self):
  x=copy.deepcopy(self.mapping);x['collection_skill_count']=125
  with self.assertRaisesRegex(ValueError,'COUNT'):self.check(x)
 def test_no_combined_unique_claim(self):
  x=copy.deepcopy(self.mapping);x['combined_unique_capability_count']=125
  with self.assertRaisesRegex(ValueError,'COUNT'):self.check(x)
 def test_no_native_activation_claim(self):
  x=copy.deepcopy(self.mapping);x['native_installation']='INSTALLED'
  with self.assertRaisesRegex(ValueError,'NATIVE'):self.check(x)
 def test_no_promoted_comparison_claim(self):
  x=copy.deepcopy(self.mapping);x['model_comparisons']='WINNER'
  with self.assertRaisesRegex(ValueError,'NATIVE'):self.check(x)
 def test_missing_legacy_reference_refused(self):
  x=copy.deepcopy(self.mapping);x['procedure_links'].pop()
  with self.assertRaisesRegex(ValueError,'LEGACY'):self.check(x)
 def test_duplicate_legacy_reference_refused(self):
  x=copy.deepcopy(self.mapping);x['procedure_links'][1]=copy.deepcopy(x['procedure_links'][0])
  with self.assertRaisesRegex(ValueError,'LEGACY'):self.check(x)
 def test_unknown_collection_skill_refused(self):
  x=copy.deepcopy(self.mapping);x['procedure_links'][0]['related_collection_skills'].append('imaginary')
  with self.assertRaisesRegex(ValueError,'RELATED'):self.check(x)
 def test_duplicate_related_skill_refused(self):
  x=copy.deepcopy(self.mapping);x['procedure_links'][0]['related_collection_skills']*=2
  with self.assertRaisesRegex(ValueError,'RELATED'):self.check(x)
 def test_false_equivalence_refused(self):
  x=copy.deepcopy(self.mapping);x['procedure_links'][0]['claims_behavioral_equivalence']=True
  with self.assertRaisesRegex(ValueError,'EQUIVALENCE'):self.check(x)
 def test_renamed_role_alias_refused(self):
  x=copy.deepcopy(self.mapping);x['role_aliases']['automation-engineer']='new-agent'
  with self.assertRaisesRegex(ValueError,'ALIAS'):self.check(x)
 def test_destructive_disposition_refused(self):
  x=copy.deepcopy(self.mapping);x['procedure_links'][0]['disposition']='REPLACE_AGENT'
  with self.assertRaisesRegex(ValueError,'DISPOSITION'):self.check(x)
 def test_unknown_acceptance_field_refused(self):
  x=copy.deepcopy(self.mapping);x['approved']=True
  with self.assertRaisesRegex(ValueError,'SCHEMA'):self.check(x)
 def test_semantic_equivalence_not_implied_by_shared_name(self):
  x=copy.deepcopy(self.mapping);x['procedure_links'][0]['reason']=''
  with self.assertRaisesRegex(ValueError,'REASON'):self.check(x)
 def test_duplicate_json_refused(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'data.json';p.write_text('{"count":75,"count":125}',encoding='utf8')
   with self.assertRaises(ValueError):M.read_json(p)
 def test_whole_public_repository_checks(self):
  x=M.check_repository(R)
  self.assertEqual(x['status'],'COLLECTION_COMPATIBILITY_VERIFIED')
  self.assertEqual(x['collection_skills'],75)
  self.assertEqual(x['legacy_procedures'],50)
  self.assertIsNone(x['combined_unique_capabilities'])
  self.assertFalse(x['native_installed'])
 def test_archived_role_and_promotion_tampering_refused(self):
  from unittest.mock import patch
  original=M._bytes
  for target,expected in (
   ('docs/history/v1-install/adversarial-verifier.txt','PUBLIC_SOURCE_DRIFT'),
   ('docs/history/v1-role-readmes/creative-studio.txt','PUBLIC_SOURCE_DRIFT'),
   ('docs/history/promotion-source/SPECIALIST_QUICKSTART.txt','IMPORTED_SOURCE_DRIFT')):
   def reader(root,name,checked=target):
    return b'tampered' if name==checked else original(root,name)
   with self.subTest(archive=target),patch.object(M,'_bytes',side_effect=reader):
    with self.assertRaisesRegex(M.CompatibilityError,expected):
     M.check_repository(R)

 def test_original_history_remains_snapshot_not_catalog_downgrade(self):
  original=json.loads((R/'collections/muse-starters-v1/r5/baseline/legacy_catalog.json').read_bytes())
  current=json.loads((R/'presets/catalog.json').read_bytes())
  self.assertEqual(current['presets'][:11],original['presets'])
  self.assertEqual(len(current['presets']),15)

class ReviewedSourceRevisionGuards(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.baseline=json.loads((R/'collections/muse-starters-v1/PUBLIC_BASELINE.json').read_bytes())
  cls.provenance=json.loads((R/'collections/muse-starters-v1/PROMOTION_PROVENANCE.json').read_bytes())
  cls.revisions=json.loads((R/M.REVISION_MANIFEST).read_bytes())
 def check(self,value):return M.validate_revisions(value,self.baseline,self.provenance)
 def test_historical_ledgers_and_reviewed_manifest_have_independent_literal_pins(self):
  expected={
   'collections/muse-starters-v1/PUBLIC_BASELINE.json':'755ffbbf3bdb8abeb97bd69a6b59f616d4acd535a292b3228afff8e8e7cfe589',
   'collections/muse-starters-v1/PROMOTION_PROVENANCE.json':'f8bde97a22c6002d38efc5d8c5edf96afdf3fa93585333fd1702e8b44e2324b5',
   'collections/muse-starters-v1/R3_BASELINE_ASSETS.json':'3d53f30e013a0d9ff3134b4fb852df059ab26f98a3660ec4b635dd29c134203f',
   'collections/muse-starters-v1/PUBLIC_REVISIONS.json':'f4d647516c63844918ea465d6eb08b3b02a6ca842aa1ad92b154ee25172d9ed7',
   'docs/history/public-revisions-v1.1.0.json.txt':'e9885c818ebc67a54c97b7c1009f0f874745f799ceb0d6e43bf048ef4e30d324',
  }
  for name,digest in expected.items():
   with self.subTest(path=name):self.assertEqual(hashlib.sha256((R/name).read_bytes()).hexdigest(),digest)
  self.assertEqual(M.REVISION_MANIFEST_SHA256,expected[M.REVISION_MANIFEST])
 def test_reviewed_revision_rows_validate(self):
  result=self.check(self.revisions)
  self.assertEqual(sum(len(rows) for rows in result.values()),self.revisions['reviewed_file_count'])
  self.assertIn('presets/catalog.json',result['public'])
  self.assertIn('tools/muse_collection.py',result['promotion'])
 def test_forged_current_hash_cannot_authorize_modified_source(self):
  from unittest.mock import patch
  forged=copy.deepcopy(self.revisions)
  row=next(row for row in forged['entries'] if row['original_path']=='presets/catalog.json')
  row['current_sha256']=hashlib.sha256(b'tampered').hexdigest()
  original=M._bytes
  def reader(root,name):
   if name==M.REVISION_MANIFEST:return (json.dumps(forged,indent=2)+'\n').encode()
   if name=='presets/catalog.json':return b'tampered'
   return original(root,name)
  with patch.object(M,'_bytes',side_effect=reader):
   with self.assertRaisesRegex(M.CompatibilityError,'REVIEWED_REVISIONS_MANIFEST_DRIFT'):
    M.check_repository(R)
 def test_unknown_duplicate_redirected_or_relabelled_revisions_are_refused(self):
  mutations=(
   ('SCHEMA',lambda x:x.update(approved=True)),
   ('LINEAGE',lambda x:x.update(historical_source_commit='0'*40)),
   ('PREVIOUS',lambda x:x.update(previous_revision_sha256='0'*64)),
   ('COUNT',lambda x:x['entries'].pop()),
   ('PATH',lambda x:x['entries'].__setitem__(1,copy.deepcopy(x['entries'][0]))),
   ('HISTORY',lambda x:x['entries'][0].update(original_path='../private.txt')),
   ('HISTORY',lambda x:x['entries'][0].update(historical_sha256='0'*64)),
   ('ARCHIVE',lambda x:x['entries'][0].update(archive_path='../../other.txt')),
   ('HASH',lambda x:x['entries'][0].update(current_sha256=x['entries'][0]['historical_sha256'])),
   ('KIND',lambda x:x['entries'][0].update(change_kind='AUTOMATIC_APPROVAL')),
  )
  for reason,mutate in mutations:
   value=copy.deepcopy(self.revisions);mutate(value)
   with self.subTest(reason=reason),self.assertRaisesRegex(M.CompatibilityError,'REVIEWED_REVISIONS_'+reason):
    self.check(value)
 def test_archived_and_current_tampering_are_separately_refused(self):
  from unittest.mock import patch
  rows={row['original_path']:row for row in self.revisions['entries']}
  names=['presets/catalog.json','tools/muse_collection.py',
         'presets/adversarial-verifier/INSTALL.md','presets/adversarial-verifier/README.md',
         'docs/collection/SPECIALIST_QUICKSTART.md',
         next(name for name in rows if name.endswith('/SKILL.md'))]
  original=M._bytes
  for name in names:
   row=rows[name]
   for target,reason in ((row['archive_path'],'PUBLIC_SOURCE_DRIFT' if row['ledger']=='public' else 'IMPORTED_SOURCE_DRIFT'),
                         (name,'REVIEWED_SOURCE_DRIFT')):
    def reader(root,path,checked=target):return b'tampered' if path==checked else original(root,path)
    with self.subTest(path=target),patch.object(M,'_bytes',side_effect=reader):
     with self.assertRaisesRegex(M.CompatibilityError,reason):M.check_repository(R)
 def test_previous_review_snapshot_tampering_is_refused(self):
  from unittest.mock import patch
  original=M._bytes
  def reader(root,path):return b'changed previous review' if path==M.PREVIOUS_REVISION_PATH else original(root,path)
  with patch.object(M,'_bytes',side_effect=reader):
   with self.assertRaisesRegex(M.CompatibilityError,'REVIEWED_REVISIONS_PREVIOUS_DRIFT'):M.check_repository(R)
 def test_original_ledger_rewrites_are_refused(self):
  from unittest.mock import patch
  original=M._bytes
  for name,reason in (('PUBLIC_BASELINE.json','PUBLIC_BASELINE_LEDGER_DRIFT'),
                      ('PROMOTION_PROVENANCE.json','PROMOTION_PROVENANCE_LEDGER_DRIFT')):
   target='collections/muse-starters-v1/'+name
   def reader(root,path,checked=target):return b'changed ledger' if path==checked else original(root,path)
   with self.subTest(path=target),patch.object(M,'_bytes',side_effect=reader):
    with self.assertRaisesRegex(M.CompatibilityError,reason):M.check_repository(R)


class ExportNamespaceGuards(unittest.TestCase):
 def test_unapproved_tools_path_refused(self):
  from muse_presets.public_export import select_public_files,PublicExportError
  with tempfile.TemporaryDirectory() as d:
   root=pathlib.Path(d);(root/'tools').mkdir();(root/'tools/new_dispatcher.py').write_text('x=1\n')
   with self.assertRaisesRegex(PublicExportError,'UNAPPROVED_COLLECTION_PATH'):select_public_files(root,verify_manifest=False)
 def test_unapproved_collection_path_refused(self):
  from muse_presets.public_export import select_public_files,PublicExportError
  with tempfile.TemporaryDirectory() as d:
   root=pathlib.Path(d);(root/'collections/owner-private').mkdir(parents=True);(root/'collections/owner-private/notes.md').write_text('test')
   with self.assertRaisesRegex(PublicExportError,'UNAPPROVED_COLLECTION_PATH'):select_public_files(root,verify_manifest=False)

if __name__=='__main__':unittest.main(verbosity=2)
