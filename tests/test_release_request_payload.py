"""Draft edits and publication retain the tag even after GitHub assigns a placeholder."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
HEAD='1234567890abcdef1234567890abcdef12345678'


class ReleaseRequestPayload(unittest.TestCase):
    def call(self,*args):
        return subprocess.run([sys.executable,'-B',str(ROOT/'scripts/release_payload.py'),
                               '--version','v1.1.1','--expected-head',HEAD,*args],
                              capture_output=True,text=True,encoding='utf-8')

    def test_draft_and_publish_requests_both_retain_tag_and_exact_commit(self):
        with tempfile.TemporaryDirectory() as directory:
            body=Path(directory)/'notes.md'
            notes='# Improvements\n\nKeep `START_HERE.md` beside your extracted files.\n'
            body.write_text(notes,encoding='utf-8')
            for phase,args in [('draft',['--body-file',str(body)]),('publish',[])]:
                result=self.call('--phase',phase,*args)
                self.assertEqual(result.returncode,0,result.stderr)
                request=json.loads(result.stdout)
                self.assertEqual(request['tag_name'],'v1.1.1')
                self.assertEqual(request['target_commitish'],HEAD)
                self.assertFalse(request['prerelease'])
                self.assertEqual(request['draft'],phase=='draft')
                if phase=='draft':self.assertEqual(request['body'],notes)
                else:
                    self.assertEqual(request['make_latest'],'true')
                    self.assertNotIn('body',request)

    def test_incomplete_and_ambiguous_requests_produce_no_payload(self):
        for args in (['--phase','draft'],['--phase','publish','--expected-head','main'],
                     ['--phase','publish','--version','untagged-123'],
                     ['--phase','publish','--version','v1.1.1-beta']):
            with self.subTest(args=args):
                result=self.call(*args)
                self.assertNotEqual(result.returncode,0)
                self.assertEqual(result.stdout,'')


if __name__=='__main__':unittest.main()
