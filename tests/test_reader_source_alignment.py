"""Reader docs must preserve the real source/release split and usable commands."""
from pathlib import Path
import importlib.util,json,re,unittest
ROOT=Path(__file__).resolve().parents[1]

def current_collection():
    import importlib.util
    spec=importlib.util.spec_from_file_location('current_library_docs', ROOT/'tools/muse_collection.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module.load_collection()

class ReaderSourceAlignmentTests(unittest.TestCase):
 def text(self,path):return (ROOT/path).read_text(encoding='utf-8')
 def test_readme_and_capabilities_include_every_current_role(self):
     roles=json.loads(self.text('presets/catalog.json'))['presets']
     self.assertEqual(len(roles),15)
     readme=self.text('README.md')
     capabilities=self.text('docs/CAPABILITIES.md')
     for role in roles:
         with self.subTest(role=role):
             self.assertIn('presets/'+role+'/INSTALL.md',readme)
             title=self.text('presets/'+role+'/README.md').splitlines()[0].removeprefix('# ').split(' | ')[0]
             self.assertIn(title,capabilities)
 def test_reader_guides_route_to_all_current_downloads(self):
     for page in ['README.md','docs/GITHUB_QUICKSTART.md','docs/CAPABILITIES.md','docs/discovery/AI_AGENT_GUIDE.md','docs/RELEASES.md']:
         body=self.text(page)
         with self.subTest(page=page):
             self.assertIn('15',body)
             self.assertIn('DOWNLOAD_A_SPECIALIST.md',body)
     catalog=json.loads(self.text('hub/site/downloads.json'))
     version=json.loads(self.text('presets/catalog.json'))['release']
     collection=current_collection()
     capabilities=json.loads(self.text('docs/discovery/agent-capabilities.json'))
     tools=json.loads(self.text(capabilities.get('tool_guide_catalog','collections/tool-guides.json')))
     expected={'specialist':15,'skill':len(collection['skills']),'workflow':len(collection['workflows']),
               'tool-guide':len(tools['guides'])}
     self.assertEqual(catalog['version'],version)
     self.assertEqual(catalog['counts'],expected)
     self.assertEqual(len(catalog['items']),sum(expected.values()))
     self.assertEqual(len({(item['kind'],item['id']) for item in catalog['items']}),len(catalog['items']))
     spec=importlib.util.spec_from_file_location('reader_release_layout',ROOT/'scripts/build_release.py')
     builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
     layout=builder.skill_download_layout(collection,version)
     skill_items={item['id']:item for item in catalog['items'] if item['kind']=='skill'}
     self.assertEqual(set(skill_items),set(layout))
     packed={}
     for identity,route in layout.items():
         item=skill_items[identity]
         with self.subTest(skill=identity):
             self.assertEqual({key:item[key] for key in route},route)
             self.assertEqual(item['entry'],'skills/'+identity+'/SKILL.md')
         packed.setdefault(item['asset'],[]).append(item)
     for asset,members in packed.items():
         self.assertTrue(all(item['pack_size']==len(members) for item in members),asset)
         self.assertLessEqual(len(members),builder.SKILLS_PER_PACK,asset)
         self.assertEqual(len({item['entry'] for item in members}),len(members),asset)
     for skill in collection['skills']:
         if skill.get('format')!='portable-skill':
             item=skill_items[skill['id']]
             self.assertEqual(item['asset'],'muse-skill-'+skill['id']+'-'+version+'.zip')
             self.assertEqual(item['pack_kind'],'skill')
             self.assertEqual(item['pack_size'],1)
     individual=[item['asset'] for item in catalog['items'] if item['kind']!='skill']
     self.assertEqual(len(individual),len(set(individual)))
     self.assertFalse(set(individual)&set(packed))
     self.assertEqual(catalog['skill_pack_count'],len(packed))
     self.assertEqual(len({item['asset'] for item in catalog['items']}),len(individual)+len(packed))
     for item in catalog['items']:
         self.assertEqual(item['url'],'https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/'+version+'/'+item['asset'])
 def test_local_entrypoints_survive_reader_rewrite(self):
     for page in ['README.md','docs/GITHUB_QUICKSTART.md']:
         body=self.text(page)
         with self.subTest(page=page):
             self.assertIn('python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"',body)
             self.assertIn('python -B tools/muse_collection.py demo data-engineer',body)
     guide=self.text('docs/GITHUB_QUICKSTART.md')
     self.assertIn('python -B quickstart.py --all',guide)
     self.assertIn('python -B examples/export_portable_skills.py --plan',guide)
     self.assertIn('docs/GITHUB_QUICKSTART.md',self.text('README.md'))
 def test_architecture_explains_shared_vs_role_procedures(self):
  body=self.text('docs/ARCHITECTURE.md')
  for value in ['15','45','five','50','120','role-skills','subchat-scopes','portable_skill_export']:
   self.assertIn(value,body)
 def test_persistence_explains_complete_home_and_preserves_owner_data(self):
     body=self.text('docs/INSTALL_AND_PERSISTENCE.md')
     for value in ['system-profile/profile/','subchat-scopes/subchats/','role-skills/',
                   'memory','preferences','credentials','OWNER_CUSTOMIZED',
                   'database','Back up','same path after restarting']:
         self.assertIn(value,body)
     self.assertIn('refusing to replace',body)
     self.assertIn('original download, your working copy, and the new package',body)
 def test_discovery_metadata_matches_current_setup_and_inventory(self):
     guide=self.text('docs/discovery/AI_AGENT_GUIDE.md')
     self.assertIn('agent-capabilities.json',guide)
     capabilities=json.loads(self.text('docs/discovery/agent-capabilities.json'))
     self.assertEqual(capabilities['homepage'],'https://atlas-origins.github.io/muse-ai-agent-presets/')
     self.assertEqual(capabilities['release'],json.loads(self.text('presets/catalog.json'))['release'])
     self.assertTrue((ROOT/capabilities['tool_guides']).is_file())
     tools=json.loads(self.text(capabilities.get('tool_guide_catalog','collections/tool-guides.json')))
     self.assertEqual(capabilities['tool_guide_count'],len(tools['guides']))
     self.assertEqual(capabilities['tool_workflow_count'],len(tools['workflows']))
     for kit in capabilities['executable_kits']:
         self.assertTrue((ROOT/kit['exporter']).is_file())
         self.assertTrue(kit['download'].endswith('/'+kit['zip']))
     self.assertEqual(set(capabilities['starter_roles']),set(json.loads(self.text('presets/catalog.json'))['presets']))
     counts=json.loads(self.text('collections/muse-starters-v1/COUNTS.json'))
     self.assertEqual(counts['skills'],len(current_collection()['skills']))
     self.assertEqual(counts['workflows'],len(current_collection()['workflows']))
 def test_reader_rewrite_does_not_reintroduce_unsafe_example_destinations(self):
  for p in [ROOT/'README.md',*sorted((ROOT/'docs').rglob('*.md')),*sorted((ROOT/'presets').glob('*/INSTALL.md'))]:
   with self.subTest(path=p.relative_to(ROOT).as_posix()):
    self.assertNotRegex(p.read_text(encoding='utf-8'),r'--to\s+\.\./')

if __name__=='__main__':unittest.main()
