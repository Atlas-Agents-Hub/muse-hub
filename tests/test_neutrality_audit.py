"""The public preset intake must reject host-specific configuration and secrets."""
import tempfile
import hashlib
from unittest.mock import patch
import unittest
from pathlib import Path

from muse_presets.neutrality import audit_public_tree
from muse_presets.catalog import ROOT


class NeutralityAuditTests(unittest.TestCase):
    def test_reviewed_api_example_is_bound_to_its_exact_bytes(self):
        from muse_presets import neutrality
        name=next(name for name,row in neutrality.REVIEWED_EXAMPLE_TEXT.items()
                  if row['reason']=='PRIVATE_HOST_PATH')
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);path=root/name;path.parent.mkdir(parents=True)
            path.write_bytes((ROOT/name).read_bytes())
            self.assertEqual(audit_public_tree(root),[])
            path.write_bytes(path.read_bytes()+b'\nChanged example.\n')
            self.assertIn('PRIVATE_HOST_PATH',{row['reason'] for row in audit_public_tree(root)})

    def test_reviewed_api_path_does_not_exempt_credential_checks(self):
        from muse_presets import neutrality
        name=next(name for name,row in neutrality.REVIEWED_EXAMPLE_TEXT.items()
                  if row['reason']=='PRIVATE_HOST_PATH')
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);path=root/name;path.parent.mkdir(parents=True)
            raw=(ROOT/name).read_bytes()+('\n'+'sk-proj-'+('Z'*32)).encode()
            path.write_bytes(raw)
            reviewed={name:{'sha256':hashlib.sha256(raw).hexdigest(),'reason':'PRIVATE_HOST_PATH'}}
            with patch.object(neutrality,'REVIEWED_EXAMPLE_TEXT',reviewed):
                self.assertIn('POSSIBLE_SECRET',{row['reason'] for row in audit_public_tree(root)})

    def test_current_distributable_assets_are_generic(self):
        self.assertEqual(audit_public_tree(ROOT), [])

    def test_concrete_windows_and_linux_home_paths_are_refused(self):
        for bad in ('C:'+'\\'+'Users'+'\\'+'someone'+'\\'+'AppData'+'\\'+'secret',
                    '/'+'home'+'/'+'jane/workspace/agent'):
            with self.subTest(value=bad), tempfile.TemporaryDirectory() as temp:
                doc = Path(temp)/'templates'/'profile'/'TOOLS.md'
                doc.parent.mkdir(parents=True)
                doc.write_text('path: '+bad, encoding='utf-8')
                results = audit_public_tree(Path(temp))
                self.assertEqual(len(results), 1)
                self.assertEqual(results[0]['reason'], 'PRIVATE_HOST_PATH')
                self.assertNotIn('someone', str(results))
                self.assertNotIn('jane', str(results))

    def test_secrets_and_sensitive_files_are_refused_without_printing_content(self):
        with tempfile.TemporaryDirectory() as temp:
            profile = Path(temp)/'presets'/'safe'
            profile.mkdir(parents=True)
            (profile/'preset.json').write_text('token="sk-proj-'+('Z'*32)+'"')
            (profile/'.env').write_text('SAMPLE_SECRET=sensitive')
            result = audit_public_tree(Path(temp))
            self.assertIn('POSSIBLE_SECRET', [x['reason'] for x in result])
            self.assertIn('SENSITIVE_FILE', [x['reason'] for x in result])
            self.assertNotIn('sensitive', str(result))
            self.assertNotIn('sk-proj-', str(result))

    def test_symlink_to_external_source_is_refused_without_reading_target(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            data = root/'unrelated.txt'
            data.write_text('a private file')
            templ = root/'templates'/'profile'
            templ.mkdir(parents=True)
            try:
                (templ/'AGENTS.md').symlink_to(data)
            except (OSError, NotImplementedError):
                self.skipTest('symlinks unavailable')
            result=audit_public_tree(root)
            self.assertEqual(result[0]['reason'],'SYMLINK_REFUSED')
            self.assertEqual(data.read_text(),'a private file')


if __name__ == '__main__':
    unittest.main()
