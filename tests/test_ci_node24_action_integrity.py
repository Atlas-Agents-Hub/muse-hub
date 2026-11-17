"""Pin GitHub-hosted checkout and setup-python by reviewed, Node24-capable commits.

These tests protect the CI trust boundary, not the availability of GitHub
macOS hosted runners, which must be checked against live workflow jobs.
"""
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
WORKFLOW=(ROOT/".github/workflows/checks.yml").read_text(encoding="utf-8")
CHECKOUT="3d3c42e5aac5ba805825da76410c181273ba90b1"
SETUP="6d4fd22b20465ccc0f7354476588e8df7c9ca0e0"


class HostedActionIntegrity(unittest.TestCase):
    def test_every_checkout_and_python_action_is_commit_pinned(self):
        used=re.findall(r"^\s*- uses:\s+(actions/(?:checkout|setup-python))@([^\s#]+)",WORKFLOW,re.M)
        self.assertEqual(len(used),6)
        self.assertEqual(used.count(("actions/checkout",CHECKOUT)),3)
        self.assertEqual(used.count(("actions/setup-python",SETUP)),3)
        self.assertTrue(all(re.fullmatch(r"[0-9a-f]{40}",ref) for _,ref in used))

    def test_still_runs_all_existing_protected_platform_and_privacy_checks(self):
        for required in (
            "permissions:\n  contents: read",
            "matrix:\n        os: [ubuntu-latest, windows-latest, macos-latest]",
            "fail-fast: false",
            "if: ${{ always() }}",
            "needs: [source-tests, public-quality]",
            "run: python -B scripts/check_public.py",
            "run: python -m unittest discover -s tests -v",
            "run: python -m muse_presets.cli audit-neutrality",
            "run: python -B -m muse_presets.cli doctor",
            "run: python -B examples/github_quickstart.py --all",
            "run: python -B scripts/check_ci_results.py",
        ):
            with self.subTest(control=required):
                self.assertIn(required,WORKFLOW)
        self.assertNotIn("continue-on-error: true",WORKFLOW)
        self.assertNotIn("pull_request_target:",WORKFLOW)
        self.assertNotIn("id-token: write",WORKFLOW)


if __name__=="__main__":unittest.main()
