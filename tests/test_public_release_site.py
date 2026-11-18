"""Public downloads and deployment must agree with the actual release."""
from __future__ import annotations
import copy
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest import mock

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
        version=self.renderer.release_version()
        self.assertTrue(urls['data-engineering-architect'].endswith('/muse-data-engineer-'+version+'.zip'))
        self.assertTrue(urls['infrastructure-reliability-engineer'].endswith('/muse-reliability-engineer-'+version+'.zip'))

    def release_fixture(self):
        rows=self.directory['items']+self.directory['bundles']
        assets=[{'name':row['asset'],'state':'uploaded','size':123,'browser_download_url':row['url']} for row in rows]
        base='https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/'+self.directory['version']+'/'
        names=('SHA256SUMS','SPECIALIST_DOWNLOADS.json','SKILL_DOWNLOADS.json',
               'WORKFLOW_DOWNLOADS.json','RELEASE_MANIFEST.json','DOWNLOADS.md',
               'muse-role-procedures-50-'+self.directory['version']+'.zip')
        assets.extend({'name':name,'state':'uploaded','size':123,'browser_download_url':base+name} for name in names)
        for asset in assets:asset['digest']='sha256:'+'a'*64
        return {'tag_name':self.directory['version'],'draft':False,'prerelease':False,'assets':assets}

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

    def test_missing_unadvertised_library_and_release_indexes_are_refused(self):
        names=('muse-role-procedures-50-'+self.directory['version']+'.zip',
               'WORKFLOW_DOWNLOADS.json','SKILL_DOWNLOADS.json',
               'RELEASE_MANIFEST.json','DOWNLOADS.md')
        for name in names:
            with self.subTest(missing=name):
                release=self.release_fixture()
                release['assets']=[row for row in release['assets'] if row['name']!=name]
                with self.assertRaises(ValueError):self.checker.check(release,self.directory)

    def test_unexpected_files_and_missing_provider_digest_are_refused(self):
        for change in ('extra_asset','missing_digest'):
            with self.subTest(change=change):
                release=self.release_fixture()
                if change=='extra_asset':
                    extra=copy.deepcopy(release['assets'][0]);extra['name']='BUILD_RECEIPT.json'
                    release['assets'].append(extra)
                else:release['assets'][0].pop('digest')
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




class GeneratedReleasePresentation(unittest.TestCase):
    """The catalog drives static release captions as well as download links."""

    @classmethod
    def setUpClass(cls):
        cls.renderer=load_script('render_downloads')
        cls.collection=cls.renderer.load_collection(ROOT/'collections/muse-starters-v1')

    def fixture(self,root,version='v9.8.7'):
        (root/'presets').mkdir()
        (root/'presets/catalog.json').write_text(json.dumps({'release':version}),encoding='utf-8')
        site=root/'hub/site'
        site.mkdir(parents=True)
        for name in ('index.html','roles.json'):
            (site/name).write_bytes((ROOT/'hub/site'/name).read_bytes())
        return site

    def run_renderer(self,root,check=False):
        outputs=self.renderer.outputs
        stream=io.StringIO()
        with mock.patch.object(self.renderer,'outputs',side_effect=lambda:outputs(root)), \
             mock.patch.object(self.renderer,'SITE',root/'hub/site'), \
             mock.patch.object(sys,'argv',['render_downloads.py']+(['--check'] if check else [])), \
             redirect_stdout(stream),redirect_stderr(stream):
            result=self.renderer.main()
        return result,stream.getvalue()

    def test_check_rejects_stale_homepage_caption_with_or_without_v_prefix(self):
        with tempfile.TemporaryDirectory() as directory, \
             mock.patch.object(self.renderer,'load_collection',return_value=self.collection):
            root=Path(directory)
            site=self.fixture(root)
            for name,content in self.renderer.outputs(root).items():
                (site/name).write_bytes(content)
            current=(site/'index.html').read_text(encoding='utf-8')
            for caption in ('Version 0.1.0','Version v0.1.0'):
                with self.subTest(caption=caption):
                    stale,count=re.subn(r'Version v?[0-9]+\.[0-9]+\.[0-9]+',caption,current,count=1)
                    self.assertEqual(count,1)
                    (site/'index.html').write_text(stale,encoding='utf-8')
                    result,message=self.run_renderer(root,check=True)
                    self.assertEqual(result,1,message)
                    self.assertIn('index.html',message)
                    self.assertEqual((site/'index.html').read_text(encoding='utf-8'),stale)

    def test_each_homepage_caption_and_downloads_footer_is_checked(self):
        with tempfile.TemporaryDirectory() as directory, \
             mock.patch.object(self.renderer,'load_collection',return_value=self.collection):
            root=Path(directory)
            site=self.fixture(root)
            expected=self.renderer.outputs(root)
            for name,key in (('index.html','packages'),('index.html','specialist'),
                             ('index.html','footer'),('downloads.html','footer')):
                with self.subTest(page=name,caption=key):
                    for output,content in expected.items():(site/output).write_bytes(content)
                    page=expected[name].decode('utf-8')
                    stale,count=re.subn(r'(data-release-caption="'+key+r'"[^>]*>)([^<]+)',
                                        lambda match:match[1]+match[2].replace('9.8.7','0.1.0'),page)
                    self.assertEqual(count,1)
                    (site/name).write_text(stale,encoding='utf-8')
                    result,message=self.run_renderer(root,check=True)
                    self.assertEqual(result,1,message)
                    self.assertIn(name,message)
                    self.assertEqual((site/name).read_text(encoding='utf-8'),stale)

    def test_catalog_upgrade_updates_static_labels_links_and_inherited_footer_in_one_pass(self):
        from html.parser import HTMLParser
        class Page(HTMLParser):
            def __init__(self):super().__init__();self.text=[];self.links=[]
            def handle_starttag(self,tag,attrs):
                if tag=='a' and 'href' in dict(attrs):self.links.append(dict(attrs)['href'])
            def handle_data(self,value):self.text.append(value)

        with tempfile.TemporaryDirectory() as directory, \
             mock.patch.object(self.renderer,'load_collection',return_value=self.collection):
            root=Path(directory)
            site=self.fixture(root)
            for version in ('v9.8.7','v10.4.2'):
                with self.subTest(version=version):
                    (root/'presets/catalog.json').write_text(json.dumps({'release':version}),encoding='utf-8')
                    self.assertEqual(self.run_renderer(root,check=True)[0],1)
                    self.assertEqual(self.run_renderer(root)[0],0)
                    data=json.loads((site/'downloads.json').read_text(encoding='utf-8'))
                    self.assertEqual(data['version'],version)
                    expected_urls={row['url'] for row in data['items']+data['bundles']}
                    for name,label_count in (('index.html',3),('downloads.html',2)):
                        page=Page();page.feed((site/name).read_text(encoding='utf-8'))
                        labels=re.findall(r'\bversion\s+v?([0-9]+\.[0-9]+\.[0-9]+)\b',' '.join(page.text),re.IGNORECASE)
                        self.assertEqual(labels,[version.removeprefix('v')]*label_count,name)
                        downloads={url for url in page.links if '/releases/download/' in url}
                        self.assertEqual(len(downloads),17 if name=='index.html' else 120,name)
                        self.assertTrue(downloads<=expected_urls,(name,downloads-expected_urls))
                        releases=[url for url in page.links if '/releases/tag/' in url]
                        self.assertTrue(all(url==self.renderer.REPO+'/releases/tag/'+version for url in releases))
                    self.assertEqual(self.run_renderer(root,check=True)[0],0)
                    before={name:(site/name).read_bytes() for name in self.renderer.outputs(root)}
                    self.assertEqual(self.run_renderer(root)[0],0)
                    self.assertEqual(before,{name:(site/name).read_bytes() for name in before})

    def test_missing_duplicate_unknown_or_unmarked_homepage_caption_is_refused(self):
        with tempfile.TemporaryDirectory() as directory, \
             mock.patch.object(self.renderer,'load_collection',return_value=self.collection):
            root=Path(directory)
            site=self.fixture(root)
            home=(site/'index.html').read_text(encoding='utf-8')
            mutations={
                'missing':home.replace(' data-release-caption="packages"',''),
                'duplicate':home+'<span data-release-caption="footer">VERSION 1.0.0</span>',
                'unknown':home.replace('data-release-caption="packages"','data-release-caption="extra"'),
                'unmarked':home+'<p>Version 0.1.0</p>',
            }
            for change,content in mutations.items():
                with self.subTest(change=change):
                    (site/'index.html').write_text(content,encoding='utf-8')
                    with self.assertRaisesRegex(ValueError,'[Hh]omepage'):
                        self.renderer.outputs(root)

    def test_unknown_homepage_release_download_is_refused(self):
        with tempfile.TemporaryDirectory() as directory, \
             mock.patch.object(self.renderer,'load_collection',return_value=self.collection):
            root=Path(directory)
            site=self.fixture(root)
            home=(site/'index.html').read_text(encoding='utf-8')
            (site/'index.html').write_text(home.replace('/muse-software-engineer-v','/muse-unknown-v'),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'catalog download'):
                self.renderer.outputs(root)


class ReleaseContentProof(unittest.TestCase):
    """A complete, consistently named release still must prove its bytes and commit."""
    HEAD='1234567890abcdef1234567890abcdef12345678'
    release_fixture=PublicReleaseDownloads.release_fixture

    @classmethod
    def setUpClass(cls):
        cls.checker=load_script('check_release_links')
        cls.directory=json.loads((ROOT/'hub/site/downloads.json').read_bytes())

    def proof_fixture(self):
        import hashlib
        release=self.release_fixture()
        bodies={row['name']:('content for '+row['name']).encode() for row in release['assets']}
        records={'specialists':[],'skills':[],'workflows':[],'bundles':[]}
        key={'specialist':'specialists','skill':'skills','workflow':'workflows'}
        rows=list(self.directory['items'])+list(self.directory['bundles'])
        name='muse-role-procedures-50-'+self.directory['version']+'.zip'
        rows.append({'id':'role-procedures-50','asset':name,
                     'url':'https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/'+self.directory['version']+'/'+name})
        for row in rows:
            raw=bodies[row['asset']]
            records[key.get(row.get('kind'),'bundles')].append({
                'id':row['id'],'asset':row['asset'],'url':row['url'],
                'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
        packages={row['asset']:{'bytes':row['bytes'],'sha256':row['sha256']}
                  for group in records.values() for row in group}
        manifest={'schema':'muse-release/v2','version':self.directory['version'],
                  'source':{'head':self.HEAD,'tree':'2'*40,'source_files':1207},
                  'assets':packages,'downloads':records}
        bodies['RELEASE_MANIFEST.json']=(json.dumps(manifest)+'\n').encode()
        self.seal_fixture(release,bodies)
        return release,bodies,manifest

    @staticmethod
    def seal_fixture(release,bodies):
        import hashlib
        bodies['SHA256SUMS']=''.join(hashlib.sha256(raw).hexdigest()+'  '+name+'\n'
                                   for name,raw in sorted(bodies.items()) if name!='SHA256SUMS').encode()
        for row in release['assets']:
            raw=bodies[row['name']]
            row.update(size=len(raw),digest='sha256:'+hashlib.sha256(raw).hexdigest())

    def verify(self,release,bodies,tag_head=None):
        self.checker.check_proof(release,self.directory,bodies['RELEASE_MANIFEST.json'],
                                bodies['SHA256SUMS'],self.HEAD,tag_head or self.HEAD)

    def test_complete_content_proof_is_accepted(self):
        release,bodies,_=self.proof_fixture()
        self.verify(release,bodies)

    def test_wrong_tag_or_built_source_is_refused(self):
        release,bodies,manifest=self.proof_fixture()
        with self.assertRaisesRegex(ValueError,'tag'):
            self.verify(release,bodies,'f'*40)
        manifest['source']['head']='f'*40
        bodies['RELEASE_MANIFEST.json']=json.dumps(manifest).encode()
        self.seal_fixture(release,bodies)
        with self.assertRaisesRegex(ValueError,'different commit'):
            self.verify(release,bodies)

    def test_downloaded_metadata_and_provider_digest_disagreements_are_refused(self):
        for change in ('manifest_bytes','checksum_bytes','provider_digest'):
            release,bodies,_=self.proof_fixture()
            if change=='manifest_bytes':bodies['RELEASE_MANIFEST.json']+=b' '
            elif change=='checksum_bytes':bodies['SHA256SUMS']+=b'\n'
            else:release['assets'][0]['digest']='sha256:'+'0'*64
            with self.subTest(change=change),self.assertRaises(ValueError):self.verify(release,bodies)

    def test_resealed_metadata_cannot_redirect_or_omit_a_download(self):
        for change in ('wrong_package_size','missing_package','wrong_index_id','wrong_index_url'):
            release,bodies,manifest=self.proof_fixture()
            name=next(iter(manifest['assets']))
            if change=='wrong_package_size':manifest['assets'][name]['bytes']+=1
            elif change=='missing_package':manifest['assets'].pop(name)
            elif change=='wrong_index_id':manifest['downloads']['specialists'][0]['id']='different-role'
            else:manifest['downloads']['specialists'][0]['url']='https://example.com/wrong.zip'
            bodies['RELEASE_MANIFEST.json']=json.dumps(manifest).encode()
            self.seal_fixture(release,bodies)
            with self.subTest(change=change),self.assertRaises(ValueError):self.verify(release,bodies)

    def test_duplicate_checksum_and_manifest_keys_are_refused(self):
        import hashlib
        release,bodies,_=self.proof_fixture()
        bodies['SHA256SUMS']+=bodies['SHA256SUMS'].splitlines(keepends=True)[0]
        checksum=next(row for row in release['assets'] if row['name']=='SHA256SUMS')
        checksum.update(size=len(bodies['SHA256SUMS']),digest='sha256:'+hashlib.sha256(bodies['SHA256SUMS']).hexdigest())
        with self.assertRaisesRegex(ValueError,'duplicate checksum'):
            self.verify(release,bodies)
        release,bodies,_=self.proof_fixture()
        bodies['RELEASE_MANIFEST.json']=b'{"schema":"muse-release/v2",'+bodies['RELEASE_MANIFEST.json'][1:]
        self.seal_fixture(release,bodies)
        with self.assertRaisesRegex(ValueError,'Duplicate JSON key'):
            self.verify(release,bodies)


if __name__=='__main__':unittest.main()
