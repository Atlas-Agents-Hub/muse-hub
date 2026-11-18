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
        self.assertIn('<title>Muse Hub | Connector directory</title>', body)
        self.assertIn('aria-label="Muse Hub home"', body)
        self.assertIn('<span>Muse Hub</span></a>', body)
        self.assertIn('<h1 id="title">Browse connector guides.</h1>', body)
        self.assertIn('No service is connected by this directory.',body)
        self.assertNotIn('Muse Specialist Toolkit',body)
        self.assertNotIn('150+ Custom Connectors',body)
        self.assertNotIn('Your Muse. More possibilities.',body)
        self.assertEqual(body.count('<details class="connector-card"'),151)
        title=re.search(r'<meta name="description" content="([^"]+)">',body)
        self.assertIsNotNone(title)
        self.assertLessEqual(len(title.group(1)),160)

    def test_connector_source_csp_and_credentials_unchanged(self):
        page=(ROOT/'docs/connectors/index.html').read_text(encoding='utf8')
        js=(ROOT/'docs/connectors/app.js').read_text(encoding='utf8')
        self.assertIn("Content-Security-Policy",page)
        self.assertIn("connect-src 'none'",page)
        self.assertIn('rel="noopener noreferrer"',page)
        for forbidden in ('fetch(', 'innerHTML', 'eval(', 'localStorage'):
            self.assertNotIn(forbidden, js)
        manifest=json.loads((ROOT/'docs/connectors/catalog.json').read_text(encoding='utf8'))
        self.assertEqual(len(manifest['connectors']),151)
        self.assertFalse(any(c.get('installed',False) for c in manifest['connectors']))

    def test_machine_readable_engine_index_product_updated(self):
        j=json.loads((ROOT/'docs/discovery/specialist-engine-index.json').read_text(encoding='utf8'))
        self.assertEqual(j['product'],'Muse Hub')
        self.assertEqual(j['schema'],'muse-specialist-toolkit/specialist-engines-v1')
        self.assertEqual(j['role_count'],15)
        self.assertEqual(j['native_muse_activation'],'NOT_ASSERTED')
        self.assertEqual(j['host_integrations'],'SEPARATE_AUTHORIZATION')

    def test_ai_discovery_uses_exact_counts_and_reaches_engine_reference(self):
        s=(ROOT/'docs/discovery/AI_AGENT_GUIDE.md').read_text(encoding='utf8')
        for term in ('# Muse Hub', '15 independent assistants', '75 skills',
                     '25 workflows', '100 task starters', '151 connectors'):
            self.assertIn(term,s)
        self.assertNotIn('100+ configurations',s)
        self.assertNotIn('Muse Specialist Toolkit',s)
        self.assertIn('../collection/SPECIALIST_SCOPE_AND_ENGINES.md',s)
        methods=(ROOT/'docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md').read_text(encoding='utf8')
        self.assertIn('../discovery/specialist-engine-index.json',methods)
        self.assertTrue((ROOT/'docs/discovery/specialist-engine-index.json').is_file())

    def test_repository_metadata_is_a_proposal_not_an_applied_claim(self):
        j=json.loads((ROOT/'.github/muse-hub-metadata-proposal.json').read_text(encoding='utf8'))
        self.assertEqual(j['product_name'],'Muse Hub')
        self.assertFalse(j['applied_to_github'])
        self.assertFalse(j['claims_live_hub_runtime'])
        self.assertNotIn('atlas-origins.github.io/kits',j['homepage'])
        self.assertLessEqual(len(j['description']),160)


if __name__=='__main__':
    unittest.main()
