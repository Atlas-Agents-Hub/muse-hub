"""Component catalog and fixture command-line behavior."""
from contextlib import redirect_stdout,redirect_stderr
import io,json,unittest
from muse_presets.cli import main

class ComponentCliTests(unittest.TestCase):
    def call(self,args):
        out=io.StringIO();err=io.StringIO()
        try:
            with redirect_stdout(out),redirect_stderr(err):code=main(args)
        except SystemExit as exc:
            self.fail('CLI feature not available: '+err.getvalue()[-200:])
        return code,json.loads(out.getvalue())

    def test_catalog_lists_six_actual_statuses(self):
        rc,result=self.call(['component-list'])
        self.assertEqual(rc,0)
        self.assertEqual(len(result['capabilities']),6)
        self.assertFalse(result['capabilities']['animation']['executable'])

    def test_inspection_does_not_execute(self):
        rc,result=self.call(['component-inspect','--capability','garden'])
        self.assertEqual(rc,0)
        self.assertEqual(result['status'],'FILES_VERIFIED')

    def test_fixture_without_optin_is_refused(self):
        rc,result=self.call(['component-fixture','--capability','claims'])
        self.assertEqual(rc,2)
        self.assertEqual(result['status'],'REFUSED')
        self.assertIn('OPTIN_REQUIRED',result['reason'])

    def test_optin_runs_real_local_claims(self):
        rc,result=self.call(['component-fixture','--capability','claims','--allow-reviewed-fixture'])
        self.assertEqual(rc,0)
        self.assertEqual(result['fixture_result']['disposition'],'OVERCLAIM')
        self.assertFalse(result['external_effect_authorized'])

    def test_unavailable_animation_stays_refused(self):
        rc,result=self.call(['component-fixture','--capability','animation','--allow-reviewed-fixture'])
        self.assertEqual(rc,2)
        self.assertIn('COMPONENT_REQUIRES_RENDERER',result['reason'])

if __name__=='__main__':unittest.main()
