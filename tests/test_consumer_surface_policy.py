"""The distribution gate covers guides inside downloads and rendered app text."""
from pathlib import Path
import tempfile
import unittest

from muse_presets.distribution import product_findings


class ConsumerSurfacePolicy(unittest.TestCase):
    def findings(self,path,text):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);target=root/path
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(text,encoding='utf-8')
            return product_findings(root)

    def test_internal_release_notice_is_refused_in_a_shared_skill_or_collection_guide(self):
        for path in ('skills/shared/example/SKILL.md','collections/muse-starters-v1/README.md',
                     'templates/system-profile/VOICE.md'):
            with self.subTest(path=path):
                found=self.findings(path,'# Getting started\nThese are working source-only capabilities.\n')
                self.assertIn('INTERNAL_RELEASE_LANGUAGE',{row['reason'] for row in found})

    def test_visible_html_notice_is_refused_even_when_split_across_elements(self):
        for path in ('examples/companion_home/index.html','src/muse_presets/desk_assets/index.html'):
            with self.subTest(path=path):
                found=self.findings(path,'<main>These are <b>source-only</b> capabilities.</main>')
                self.assertIn('INTERNAL_RELEASE_LANGUAGE',{row['reason'] for row in found})

    def test_machine_fields_and_code_samples_are_preserved(self):
        fixtures=(
            ('skills/shared/example/SKILL.md','---\nstatus: source-only\n---\n# Check your work\nRun the included example.\n'),
            ('docs/USAGE.md','# Use the verifier\n```json\n{"status":"source-only"}\n```\n'),
            ('examples/companion_home/index.html','<script>const status="source-only";</script><main>Open your notebook.</main>'),
        )
        for path,text in fixtures:
            with self.subTest(path=path):self.assertEqual(self.findings(path,text),[])

    def test_retired_history_is_not_reintroduced_to_the_current_product(self):
        found=self.findings('docs/history/older-guide.txt','Old release notes.\n')
        self.assertIn('INTERNAL_ARTIFACT',{row['reason'] for row in found})

if __name__=='__main__':unittest.main()
