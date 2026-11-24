"""Website maintenance must be read-only and fail closed on deployed-byte drift."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_website_maintenance.py"
WORKFLOW = ROOT / ".github/workflows/website-maintenance.yml"
REQUIRED = ("index.html", "downloads.html", "downloads.json", "public/catalog.json", "sitemap.xml", "llms.txt")


class MaintenanceTests(unittest.TestCase):
    def load_monitor(self):
        self.assertTrue(SCRIPT.is_file(), "Maintenance monitor is missing")
        spec = importlib.util.spec_from_file_location("maintenance", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_workflow_is_scheduled_and_read_only(self):
        self.assertTrue(WORKFLOW.is_file(), "Maintenance workflow is missing")
        workflow = yaml.load(WORKFLOW.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        self.assertEqual(set(workflow["on"]), {"schedule", "workflow_dispatch"})
        self.assertEqual(len(workflow["on"]["schedule"]), 3)
        self.assertEqual(workflow["permissions"], {
            "contents": "read", "actions": "read", "deployments": "read"
        })
        for job in workflow["jobs"].values():
            self.assertNotIn("environment", job)
            self.assertNotIn("permissions", job)
            self.assertNotIn("continue-on-error", job)
            for step in job["steps"]:
                self.assertNotIn("continue-on-error", step)
                self.assertNotIn("deploy-pages", step.get("uses", ""))
                self.assertNotIn("upload-pages-artifact", step.get("uses", ""))
                if "checkout@" in step.get("uses", ""):
                    self.assertEqual(step["with"]["persist-credentials"], "false")
                for forbidden in ("git push", "gh pr merge", "gh release upload", "gh api --method POST"):
                    self.assertNotIn(forbidden, step.get("run", ""))

    def test_deployed_commit_not_current_worktree_is_oracle(self):
        monitor = self.load_monitor()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def git(*args):
                return subprocess.check_output(["git", "-C", folder, *args], stderr=subprocess.DEVNULL).decode().strip()
            git("init", "-q")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@example.com")
            git("config", "core.autocrlf", "false")
            files = {name: ("accepted:" + name).encode() for name in REQUIRED}
            for name, content in files.items():
                path = root / "hub/site" / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            git("add", ".")
            git("commit", "-qm", "deployed fixture")
            deployed = git("rev-parse", "HEAD")
            (root / "hub/site/index.html").write_bytes(b"unpublished change")
            git("commit", "-qam", "unpublished")
            def fetch(name, limit):
                self.assertEqual(limit, len(files[name]) + 1)
                return files[name]
            self.assertEqual(monitor.verify_site(root, deployed, fetch), (len(files), []))
            def corrupt(name, limit):
                return b"wrong" if name == "downloads.html" else files[name]
            count, failures = monitor.verify_site(root, deployed, corrupt)
            self.assertEqual(count, len(files))
            self.assertEqual(len(failures), 1)
            self.assertIn("downloads.html", failures[0])
            def unavailable(name, limit):
                if name == "llms.txt":
                    raise OSError("fixture network failure")
                return files[name]
            self.assertEqual(len(monitor.verify_site(root, deployed, unavailable)[1]), 1)
            with self.assertRaises(ValueError):
                monitor.verify_site(root, "main", fetch)
            (root / "hub/site/llms.txt").unlink()
            git("commit", "-qam", "missing required file")
            with self.assertRaises(ValueError):
                monitor.verify_site(root, git("rev-parse", "HEAD"), fetch)


if __name__ == "__main__":
    unittest.main()
