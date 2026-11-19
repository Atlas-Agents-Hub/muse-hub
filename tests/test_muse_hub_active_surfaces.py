"""Muse Hub naming and truthful source-based connector/discovery copy.

Keep historical source schema IDs stable, preserve upstream pinned connector
records and avoid advertising disconnected services as installed capabilities.
"""
from pathlib import Path
import json
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]


class MuseHubActiveSurfaces(unittest.TestCase):
    def test_connector_site_identity_only_muse_hub(self):
        body=(ROOT/'docs/connectors/index.html').read_text(encoding='utf8')
        self.assertIn('<title>Muse Hub | Custom connectors for your apps and services</title>', body)
        self.assertIn('aria-label="Muse Hub home"', body)
        self.assertIn('<span>Muse Hub</span></a>', body)
        self.assertIn('<h1 id="title">Bring your tools into the conversation.</h1>', body)
        self.assertIn('Setup instructions, service actions and task prompts in one place.',body)
        self.assertNotIn('Muse Specialist Toolkit',body)
        self.assertNotIn('150+ Custom Connectors',body)
        self.assertNotIn('Your Muse. More possibilities.',body)
        connectors=json.loads((ROOT/'docs/connectors/catalog.json').read_bytes())['connectors']
        self.assertEqual(body.count('<details class="connector-card"'),len(connectors))
        title=re.search(r'<meta name="description" content="([^"]+)">',body)
        self.assertIsNotNone(title)
        self.assertLessEqual(len(title.group(1)),160)

    def test_connector_source_csp_and_credentials_unchanged(self):
        page=(ROOT/'docs/connectors/index.html').read_text(encoding='utf8')
        js=(ROOT/'docs/connectors/app.js').read_text(encoding='utf8')
        self.assertIn("Content-Security-Policy",page)
        self.assertIn("connect-src 'none'",page)
        for anchor in re.findall(r'<a\b[^>]*>',page):
            if 'target="_blank"' in anchor:
                rel=re.search(r'rel="([^"]+)"',anchor)
                self.assertIsNotNone(rel,anchor)
                self.assertTrue({'noopener','noreferrer'}<=set(rel.group(1).split()),anchor)
        for forbidden in ('fetch(', 'innerHTML', 'eval(', 'localStorage'):
            self.assertNotIn(forbidden, js)
        manifest=json.loads((ROOT/'docs/connectors/catalog.json').read_text(encoding='utf8'))
        self.assertGreater(len(manifest['connectors']),250)
        self.assertEqual(len({row['id'] for row in manifest['connectors']}),len(manifest['connectors']))
        self.assertFalse(any(c.get('installed',False) for c in manifest['connectors']))

    def test_machine_readable_engine_index_product_updated(self):
        j=json.loads((ROOT/'docs/discovery/specialist-engine-index.json').read_text(encoding='utf8'))
        self.assertEqual(j['product'],'Muse Hub')
        self.assertEqual(j['schema'],'muse-specialist-toolkit/specialist-engines-v1')
        self.assertEqual(j['role_count'],15)
        self.assertEqual(j['role_count'], len(j['roles']))
        self.assertEqual(len({role['id'] for role in j['roles']}), j['role_count'])
        self.assertEqual(j['host_integrations'],'SEPARATE_AUTHORIZATION')

    def test_ai_discovery_uses_exact_counts_and_reaches_engine_reference(self):
        s=(ROOT/'docs/discovery/AI_AGENT_GUIDE.md').read_text(encoding='utf8')
        counts=json.loads((ROOT/'hub/site/downloads.json').read_text(encoding='utf8'))['counts']
        starters=json.loads((ROOT/'collections/muse-starters-v1/starters.json').read_bytes())
        connectors=json.loads((ROOT/'docs/connectors/catalog.json').read_bytes())['connectors']
        for term in ('# Muse Hub', f"{counts['specialist']} independent assistants", f"{counts['skill']} skills",
                     f"{counts['workflow']} workflows", f'{len(starters)} task starters', f'{len(connectors)} connectors'):
            self.assertIn(term,s)
        self.assertNotIn('100+ configurations',s)
        self.assertNotIn('Muse Specialist Toolkit',s)
        self.assertIn('../collection/SPECIALIST_SCOPE_AND_ENGINES.md',s)
        methods=(ROOT/'docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md').read_text(encoding='utf8')
        self.assertIn('../discovery/specialist-engine-index.json',methods)
        self.assertTrue((ROOT/'docs/discovery/specialist-engine-index.json').is_file())

    def test_repository_metadata_describes_the_product_and_matches_its_homepage(self):
        j=json.loads((ROOT/'.github/muse-hub-metadata-proposal.json').read_text(encoding='utf8'))
        self.assertEqual(j['product_name'],'Muse Hub')
        self.assertEqual(j['schema'],'muse-hub/github-metadata/v2')
        self.assertEqual(j['repository'],'atlas-origins/muse-ai-agent-presets')
        self.assertEqual(j['homepage'],'https://atlas-origins.github.io/muse-ai-agent-presets/')
        self.assertIn('ai-agent-skills',j['topics'])
        self.assertIn('agent-workflows',j['topics'])
        self.assertNotIn('atlas-origins.github.io/kits',j['homepage'])
        self.assertLessEqual(len(j['description']),160)


if __name__=='__main__':
    unittest.main()
