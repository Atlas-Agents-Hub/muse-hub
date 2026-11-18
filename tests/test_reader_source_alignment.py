"""Reader docs must preserve the real source/release split and usable commands."""
from pathlib import Path
import json,re,unittest
ROOT=Path(__file__).resolve().parents[1]

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
     self.assertEqual(catalog['version'],'v1.1.2')
     self.assertEqual(catalog['counts'],{'specialist':15,'skill':75,'workflow':25})
     self.assertEqual(len(catalog['items']),115)
     self.assertEqual(len({item['asset'] for item in catalog['items']}),115)
     for item in catalog['items']:
         self.assertEqual(item['url'],'https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.2/'+item['asset'])
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
 def test_runtime_and_comparative_claims_remain_in_scoped_technical_records(self):
     guide=self.text('docs/discovery/AI_AGENT_GUIDE.md')
     self.assertIn('agent-capabilities.json',guide)
     self.assertIn('Describe the result of the command actually used',guide)
     capabilities=json.loads(self.text('docs/discovery/agent-capabilities.json'))
     for field in ('native_muse_agents_installed','hosted_agent_service',
                   'autonomous_model_backed_agents_out_of_box','external_connectors_enabled'):
         self.assertIs(capabilities['boundaries'][field],False)
     counts=json.loads(self.text('collections/muse-starters-v1/COUNTS.json'))
     self.assertEqual(counts['paired_muse_comparisons_executed'],0)
     self.assertEqual(counts['independent_upstream_reviews'],0)
 def test_reader_rewrite_does_not_reintroduce_unsafe_example_destinations(self):
  for p in [ROOT/'README.md',*sorted((ROOT/'docs').rglob('*.md')),*sorted((ROOT/'presets').glob('*/INSTALL.md'))]:
   with self.subTest(path=p.relative_to(ROOT).as_posix()):
    self.assertNotRegex(p.read_text(encoding='utf-8'),r'--to\s+\.\./')

if __name__=='__main__':unittest.main()
