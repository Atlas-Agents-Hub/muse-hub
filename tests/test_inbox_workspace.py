"""Inbox helpers preserve coverage, validate preferences and travel in downloads."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / 'collections/muse-starters-v1/skills/inbox-triage'
PACKAGE_ROOT = 'skills/inbox-triage/'
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'tools'), str(ROOT / 'scripts')]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


window = module('inbox_window', SKILL_ROOT / 'scripts/search_window_calculator.py')
reader = module('inbox_reader', SKILL_ROOT / 'scripts/kb_reader.py')
checker = module('inbox_log_check', SKILL_ROOT / 'scripts/draft_safety_validator.py')


class InboxHelperTests(unittest.TestCase):
    def workspace(self, directory):
        target = Path(directory)
        shutil.copytree(SKILL_ROOT / 'examples/Email', target / 'Email')
        return target

    def test_recurring_cadences_cover_a_full_interval_with_overlap(self):
        now = datetime(2026, 11, 19, 18, tzinfo=timezone.utc)
        for cadence, interval, hours in [('once-daily', 24, 26), ('2x-daily', 12, 14), ('3x-daily', 8, 10)]:
            with self.subTest(cadence=cadence):
                result = window.compute(cadence, now)
                self.assertEqual(result['hours_back'], hours)
                self.assertLess(datetime.fromisoformat(result['window_start']), now - timedelta(hours=interval))
                self.assertEqual(result['window_end'], now.isoformat())

    def test_checkpoint_covers_interruptions_and_different_offsets(self):
        now = datetime.fromisoformat('2026-11-19T09:00:00+01:00')
        since = datetime.fromisoformat('2026-11-16T18:00:00-05:00')
        result = window.compute('2x-daily', now, since=since)
        self.assertEqual(result['window_start'], '2026-11-16T22:55:00+00:00')
        self.assertEqual(result['window_end'], '2026-11-19T08:00:00+00:00')
        self.assertEqual(result['coverage_basis'], 'previous-success')
        self.assertEqual(result['run_label'], 'Morning')
        self.assertEqual(result['overlap_minutes'], 5)

    def test_provider_query_bounds_include_fractional_boundary_messages(self):
        now = datetime.fromisoformat('2026-11-19T12:00:00.500000+00:00')
        result = window.compute('on-demand', now, since=now - timedelta(hours=2))
        start = datetime.fromisoformat(result['window_start']).timestamp()
        self.assertLess(result['search_filter_after_unix'], start)
        self.assertGreaterEqual(result['search_filter_before_unix'], now.timestamp())
        self.assertEqual(window.parse_timestamp('2026-11-19T12:00:00Z'), now.replace(microsecond=0))

    def test_invalid_and_ambiguous_windows_are_rejected(self):
        now = datetime(2026, 11, 19, tzinfo=timezone.utc)
        cases = [dict(override_hours=0), dict(override_hours=721), dict(override_hours=True),
                 dict(since=now + timedelta(seconds=1)), dict(since=now, override_hours=1),
                 dict(overlap_minutes=-1), dict(overlap_minutes=121),
                 dict(since=now - timedelta(days=31))]
        for options in cases:
            with self.subTest(options=options), self.assertRaises(ValueError):
                window.compute('2x-daily', now, **options)

    def test_complete_workspace_has_parsed_preferences(self):
        with tempfile.TemporaryDirectory() as folder:
            result = reader.read_kb(self.workspace(folder))
            self.assertEqual(result['verdict'], 'PASS', result)
            self.assertEqual(result['files']['email-patterns.md']['parsed']['voice_register'], 'Casual')
            self.assertEqual(len(result['files']['email-taxonomy.md']['parsed']['categories']), 3)
            self.assertFalse(result['files']['rate-card.md']['present'])

    def test_missing_and_malformed_workspace_files_fail(self):
        for fault in ('missing', 'empty', 'categories', 'rules', 'utf8', 'oversized'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as folder:
                root = self.workspace(folder)
                target = root / 'Email/email-taxonomy.md'
                if fault == 'missing':
                    target.unlink()
                elif fault == 'empty':
                    target.write_text('')
                elif fault == 'categories':
                    target.write_text('# Taxonomy\n\n## Categories\n\n## Report Preferences\nSave a report.\n')
                elif fault == 'rules':
                    (root / 'Email/email-patterns.md').write_text('# Patterns\n\n## Voice Register\nCasual\n')
                elif fault == 'utf8':
                    target.write_bytes(b'\xff')
                else:
                    target.write_bytes(b'a' * (reader.MAX_FILE_BYTES + 1))
                result = reader.read_kb(root)
                self.assertEqual(result['verdict'], 'FAIL', result)
                self.assertTrue(result['issues'])

    def test_linked_workspace_member_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.workspace(folder)
            target = root / 'Email/email-taxonomy.md'
            original = root / 'original.md'
            target.rename(original)
            try:
                target.symlink_to(original)
            except OSError:
                self.skipTest('This platform does not permit symlink creation')
            result = reader.read_kb(root)
            self.assertEqual(result['verdict'], 'FAIL')
            self.assertIn('linked knowledge-base file', json.dumps(result))

    def test_send_checks_cover_draft_send_graph_and_case_variants(self):
        for operation in ('gmail.users.messages.send', 'gmail.users.drafts.send',
                          'users/me/drafts/send', 'me/sendMail', 'users/person/messages/abc/send',
                          'sendmail', 'SEND_EMAIL', 'schedule_send', 'smtp.sendmail',
                          'mcp__gmail__send_email', 'tools.gmail_send_message',
                          'mcp__gmail__drafts_send'):
            with self.subTest(operation=operation):
                result = checker.scan_log(operation + ' -> example-result')
                self.assertEqual(result['verdict'], 'FAIL', result)
                self.assertEqual(result['send_violation_count'], 1)
        clean = checker.scan_log(checker.SAMPLE_PASS_LOG)
        self.assertEqual(clean['verdict'], 'PASS')
        self.assertEqual(clean['draft_indicator_count'], 3)
        self.assertEqual(checker.scan_log('  \n')['verdict'], 'EMPTY')

    def test_action_log_input_is_bounded_and_read_only(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'actions.md'
            raw = checker.SAMPLE_PASS_LOG.encode()
            path.write_bytes(raw)
            self.assertEqual(checker.read_log(path), checker.SAMPLE_PASS_LOG)
            self.assertEqual(path.read_bytes(), raw)
            path.write_bytes(b'x' * (checker.MAX_LOG_BYTES + 1))
            with self.assertRaises(ValueError):
                checker.read_log(path)


class InboxDownloadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import build_release
        cls.release = build_release
        cls.data = build_release.collection.prepare_collection(build_release.collection.load_collection())
        cls.attachments = set(build_release.collection.SKILL_ASSETS['inbox-triage'])
        cls.required = {PACKAGE_ROOT + name for name in cls.attachments}

    def test_existing_skill_and_starter_identity_are_preserved(self):
        self.assertEqual(sum(row['id'] == 'inbox-triage' for row in self.data['skills']), 1)
        starter = next(row for row in self.data['starters'] if row['id'] == 'inbox-assistant')
        self.assertIn('inbox-triage', starter['skills'])
        self.assertEqual(starter['base_role'], 'personal-companion')
        for role_id in ('coordinator', 'personal-companion'):
            role = next(row for row in self.data['specialists'] if row['id'] == role_id)
            self.assertIn('inbox-triage', role['skills'])
            self.assertIn('inbox-setup', role['library_skills'])

    def assert_pack(self, files):
        self.assertTrue(self.required <= files.keys(), sorted(self.required - files.keys()))
        self.assertIn(b'INBOX_WORKSPACE.md', files[PACKAGE_ROOT + 'SKILL.md'])
        self.assertIn(b'kb_reader.py', files['START_HERE.md'])
        manifest = json.loads(files['MANIFEST.json'])
        for name in self.required:
            self.assertEqual(manifest['files'][name], hashlib.sha256(files[name]).hexdigest())

    def test_existing_starters_and_specialists_include_every_helper(self):
        for identifier in ('inbox-assistant', 'admin-catchup', 'customer-support-designer'):
            with self.subTest(starter=identifier):
                self.assert_pack(self.release.collection.package_files(self.data, identifier))
        for role in ('coordinator', 'personal-companion'):
            with self.subTest(role=role):
                files = self.release.specialist_files(self.data, role)
                self.assert_pack(files)
                self.assertIn('skills/inbox-setup/SKILL.md', files)

    def test_unrelated_package_and_instruction_challenge_stay_focused(self):
        unrelated = self.release.skill_files(self.data, 'prose-revision')
        self.assertFalse(self.required & unrelated.keys())
        challenge = self.release.collection.challenge_files(self.data, 'inbox-triage-r3-standard', 'candidate')
        self.assertFalse(self.required & challenge.keys())
        self.assertNotIn(b'INBOX_WORKSPACE.md', challenge[PACKAGE_ROOT + 'SKILL.md'])

    def test_extracted_zip_verifies_and_runs_the_complete_example(self):
        files = self.release.skill_files(self.data, 'inbox-triage')
        self.assert_pack(files)
        with tempfile.TemporaryDirectory(prefix='muse-inbox-') as folder:
            path = Path(folder)
            with zipfile.ZipFile(io.BytesIO(self.release._zip(files))) as archive:
                archive.extractall(path)
            environment = dict(os.environ, PYTHONIOENCODING='cp1252', PYTHONDONTWRITEBYTECODE='1')
            environment.pop('PYTHONPATH', None)
            def run(arguments, code=0):
                result = subprocess.run([sys.executable, '-B', *arguments], cwd=path,
                    env=environment, capture_output=True, timeout=45)
                self.assertEqual(result.returncode, code, result.stderr.decode('utf-8', errors='replace'))
                self.assertEqual(result.stderr, b'')
                return json.loads(result.stdout.decode('utf-8'))
            self.assertEqual(run(['VERIFY.py'])['status'], 'PASS')
            self.assertEqual(run([PACKAGE_ROOT + 'scripts/kb_reader.py', '--workspace',
                                  PACKAGE_ROOT + 'examples', '--output', 'json'])['verdict'], 'PASS')
            interval = run([PACKAGE_ROOT + 'scripts/search_window_calculator.py', '--cadence', '2x-daily',
                            '--since', '2026-11-18T18:00:00Z', '--now', '2026-11-19T09:00:00Z', '--output', 'json'])
            self.assertEqual(interval['window_start'], '2026-11-18T17:55:00+00:00')
            self.assertEqual(run([PACKAGE_ROOT + 'scripts/draft_safety_validator.py', '--action-log',
                PACKAGE_ROOT + 'examples/Email/triage-log/example-run.md', '--output', 'json'])['verdict'], 'PASS')
            self.assertEqual(run([PACKAGE_ROOT + 'scripts/draft_safety_validator.py', '--sample-fail',
                                  '--output', 'json'], code=1)['verdict'], 'FAIL')
            self.assertEqual(run(['VERIFY.py'])['status'], 'PASS')


if __name__ == '__main__':
    unittest.main()
