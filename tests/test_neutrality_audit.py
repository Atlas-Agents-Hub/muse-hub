"""The public preset intake must reject host-specific configuration and secrets."""
import tempfile
import hashlib
import json
from unittest.mock import patch
import unittest
from pathlib import Path

from muse_presets.neutrality import audit_public_tree
from muse_presets.catalog import ROOT


class NeutralityAuditTests(unittest.TestCase):
    def reviewed_manifest(self, root, name, raw, reasons):
        from muse_presets import neutrality
        path = root / neutrality.SOURCE_EXAMPLE_MANIFEST
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps({'schema': 'muse-public-source-examples/v1', 'files': {
            name: {'sha256': hashlib.sha256(raw).hexdigest(), 'reasons': reasons,
                   'examples': ['Public documentation example']}}}).encode()
        path.write_bytes(payload)
        return patch.object(neutrality, 'SOURCE_EXAMPLE_MANIFEST_SHA256',
                            hashlib.sha256(payload).hexdigest())

    def test_reviewed_source_examples_require_exact_content_and_reason(self):
        name = 'collections/library/skills/example/SKILL.md'
        raw = ('Contact the public support address: public' + '@vendor.test').encode()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); path = root / name
            path.parent.mkdir(parents=True); path.write_bytes(raw)
            with self.reviewed_manifest(root, name, raw, ['PERSONAL_EMAIL_REVIEW_REQUIRED']):
                self.assertEqual(audit_public_tree(root), [])
                path.write_bytes(raw + b'\nUpdated instructions.')
                self.assertIn('PERSONAL_EMAIL_REVIEW_REQUIRED',
                              {row['reason'] for row in audit_public_tree(root)})

    def test_source_example_acknowledgment_cannot_hide_other_findings(self):
        name = 'collections/library/skills/example/SKILL.md'
        raw = ('public' + '@vendor.test\n' + 'sk-proj-' + 'Z' * 32).encode()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); path = root / name
            path.parent.mkdir(parents=True); path.write_bytes(raw)
            with self.reviewed_manifest(root, name, raw, ['PERSONAL_EMAIL_REVIEW_REQUIRED']):
                self.assertEqual({row['reason'] for row in audit_public_tree(root)}, {'POSSIBLE_SECRET'})

    def test_source_example_manifest_edits_are_not_self_authorizing(self):
        from muse_presets import neutrality
        name = 'collections/library/skills/example/SKILL.md'
        raw = ('public' + '@vendor.test').encode()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); path = root / name
            path.parent.mkdir(parents=True); path.write_bytes(raw)
            with self.reviewed_manifest(root, name, raw, ['PERSONAL_EMAIL_REVIEW_REQUIRED']):
                manifest = root / neutrality.SOURCE_EXAMPLE_MANIFEST
                manifest.write_bytes(manifest.read_bytes() + b'\n')
                reasons = {row['reason'] for row in audit_public_tree(root)}
                self.assertIn('INVALID_SOURCE_EXAMPLE_MANIFEST', reasons)
                self.assertIn('PERSONAL_EMAIL_REVIEW_REQUIRED', reasons)

    def test_reviewed_api_example_is_bound_to_its_exact_bytes(self):
        from muse_presets import neutrality
        name='collections/library/skills/example/references/paths.md'
        raw=('Example: /'+'Users/example/workspace/').encode()
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);path=root/name;path.parent.mkdir(parents=True)
            path.write_bytes(raw)
            reviewed={name:{'sha256':hashlib.sha256(raw).hexdigest(),'reason':'PRIVATE_HOST_PATH'}}
            with patch.object(neutrality,'REVIEWED_EXAMPLE_TEXT',reviewed):
                self.assertEqual(audit_public_tree(root),[])
                path.write_bytes(raw+b'\nChanged example.\n')
                self.assertIn('PRIVATE_HOST_PATH',{row['reason'] for row in audit_public_tree(root)})

    def test_reviewed_api_path_does_not_exempt_credential_checks(self):
        from muse_presets import neutrality
        name='collections/library/skills/example/references/paths.md'
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);path=root/name;path.parent.mkdir(parents=True)
            raw=('Example: /'+'Users/example/workspace/\n'+'sk-proj-'+('Z'*32)).encode()
            path.write_bytes(raw)
            reviewed={name:{'sha256':hashlib.sha256(raw).hexdigest(),'reason':'PRIVATE_HOST_PATH'}}
            with patch.object(neutrality,'REVIEWED_EXAMPLE_TEXT',reviewed):
                self.assertIn('POSSIBLE_SECRET',{row['reason'] for row in audit_public_tree(root)})

    def test_api_routes_and_blank_environment_templates_are_portable_source(self):
        from muse_presets import source_limits
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            package=root/'collections/library/skills/example'
            package.mkdir(parents=True)
            (package/'SKILL.md').write_text('Use GET /api/users/:id/ and /api/home/settings/.')
            raw=b'API_KEY=\nSERVICE_URL=https://example.com\n'
            (package/'.env.example').write_bytes(raw)
            catalog=json.dumps({'schema':'muse-skill-library/v1','skills':[{
                'id':'example','path':'skills/example',
                'files':{'.env.example':hashlib.sha256(raw).hexdigest()}}]}).encode()
            (root/source_limits.LIBRARY_ASSET_CATALOG).write_bytes(catalog)
            with patch.object(source_limits,'LIBRARY_ASSET_CATALOG_SHA256',
                              hashlib.sha256(catalog).hexdigest()):
                self.assertEqual(audit_public_tree(root),[])
                (package/'.env.example').write_text('API_KEY=sk-proj-'+('Z'*32))
                self.assertIn('UNREVIEWED_BINARY_ASSET',
                              {row['reason'] for row in audit_public_tree(root)})

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

    def test_colon_prefixed_paths_and_file_uris_are_refused(self):
        home = '/' + 'home/alice/private.txt'
        mac = '/' + 'Users/alice/private.txt'
        windows = 'C:' + '\\' + 'Users' + '\\' + 'alice' + '\\' + 'private.txt'
        for value in ('path:' + home, 'file://' + home,
                      'file://' + mac, 'path:' + windows):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                (root / 'example.md').write_text(value, encoding='utf-8')
                self.assertEqual(audit_public_tree(root),
                                 [{'path': 'example.md', 'reason': 'PRIVATE_HOST_PATH'}])

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
