"""Public downloads and deployment must agree with the actual release."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]


def load_script(name):
    spec=importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PublicReleaseDownloads(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.renderer=load_script('render_downloads')
        cls.checker=load_script('check_release_links')
        cls.directory=json.loads((ROOT/'hub/site/downloads.json').read_text(encoding='utf-8'))

    def test_rendered_directory_matches_validated_collection(self):
        self.assertEqual(self.directory, self.renderer.catalog())
        for name,expected in self.renderer.outputs().items():
            self.assertEqual((ROOT/'hub/site'/name).read_bytes(),expected,name)
        self.assertEqual(self.directory['counts'],{'specialist':15,'skill':75,'workflow':25})
        self.assertEqual(len({row['asset'] for row in self.directory['items']}),115)

    def test_all_specialist_aliases_agree_between_site_and_discovery(self):
        roles=json.loads((ROOT/'hub/site/roles.json').read_text(encoding='utf-8'))['roles']
        discovery=json.loads((ROOT/'docs/discovery/agent-capabilities.json').read_text(encoding='utf-8'))
        urls={row['id']:row['url'] for row in self.directory['items'] if row['kind']=='specialist'}
        self.assertEqual(urls,{role['id']:role['download_url'] for role in roles})
        self.assertEqual(urls,discovery['specialist_downloads'])
        self.assertTrue(urls['data-engineering-architect'].endswith('/muse-data-engineer-v1.1.0.zip'))
        self.assertTrue(urls['infrastructure-reliability-engineer'].endswith('/muse-reliability-engineer-v1.1.0.zip'))

    def release_fixture(self):
        rows=self.directory['items']+self.directory['bundles']
        assets=[{'name':row['asset'],'state':'uploaded','size':123,'browser_download_url':row['url']} for row in rows]
        assets.extend({'name':name,'state':'uploaded','size':123} for name in ('SHA256SUMS','SPECIALIST_DOWNLOADS.json'))
        return {'tag_name':'v1.1.0','draft':False,'prerelease':False,'assets':assets}

    def test_published_complete_release_is_accepted(self):
        self.checker.check(self.release_fixture(),self.directory)

    def test_missing_or_stale_publication_is_refused(self):
        for change in ('draft','prerelease','wrong_version','missing_package','empty_package','wrong_url','duplicate_asset','missing_checksum'):
            with self.subTest(change=change):
                release=self.release_fixture()
                if change in ('draft','prerelease'):release[change]=True
                elif change=='wrong_version':release['tag_name']='v1.0.0'
                elif change=='missing_package':release['assets'].pop(0)
                elif change=='empty_package':release['assets'][0]['size']=0
                elif change=='wrong_url':release['assets'][0]['browser_download_url']='https://example.com/wrong.zip'
                elif change=='duplicate_asset':release['assets'].append(copy.deepcopy(release['assets'][0]))
                elif change=='missing_checksum':release['assets']=[row for row in release['assets'] if row['name']!='SHA256SUMS']
                with self.assertRaises(ValueError):self.checker.check(release,self.directory)

    def test_site_does_not_display_internal_release_boilerplate(self):
        from html.parser import HTMLParser
        class Visible(HTMLParser):
            def __init__(self):super().__init__();self.skip=0;self.text=[]
            def handle_starttag(self,tag,attrs):
                if tag in ('script','style'):self.skip+=1
            def handle_endtag(self,tag):
                if tag in ('script','style'):self.skip-=1
            def handle_data(self,value):
                if not self.skip:self.text.append(value)
        for name in ('index.html','downloads.html','public/index.html'):
            parser=Visible();parser.feed((ROOT/'hub/site'/name).read_text(encoding='utf-8'))
            text=' '.join(parser.text).casefold()
            for phrase in ('source-only','source only','unpublished draft','not deployed','not additional agents','no authenticated cross-account','not a claim','h11 /','h12 /','h00–h21'):
                self.assertNotIn(phrase,text,(name,phrase))


if __name__=='__main__':unittest.main()
