"""Adversarial checks of website-only deployment compatibility."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("scope", ROOT / "scripts/check_website_release_scope.py")
scope = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scope)


class WebsiteReleaseScope(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "fixture@example.com")
        self.git("config", "core.autocrlf", "false")
        self.directory = {
            "version": "v1.6.2",
            "items": [{"kind": "skill", "id": "one", "asset": "one.zip",
                       "url": "https://example.invalid/one.zip", "entry": "skills/one/SKILL.md",
                       "description": "Old description"}],
            "bundles": [{"id": "toolkit", "asset": "toolkit.zip", "url": "https://example.invalid/toolkit.zip"}],
        }
        self.write("hub/site/downloads.json", json.dumps(self.directory))
        self.write("hub/site/index.html", "<h1>Old</h1>")
        self.write("src/muse_presets/public_export.py", "PUBLIC_HUB_FILES = {\n    \"hub/site/index.html\",\n}\n")
        self.write("presets/role/INSTALL.md", "Original guide")
        self.base = self.commit()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args]).decode().strip()

    def write(self, name, value):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(value.encode())

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        return self.git("rev-parse", "HEAD")

    def test_unchanged_release_and_descendant_website_are_accepted(self):
        self.assertEqual(scope.check_scope(self.root, self.base, self.base), 0)
        data = copy.deepcopy(self.directory)
        data["items"][0]["description"] = "Clear description"
        self.write("hub/site/downloads.json", json.dumps(data))
        self.write("hub/site/index.html", "<h1>New</h1>")
        self.write("src/muse_presets/public_export.py", "PUBLIC_HUB_FILES = {\n    \"hub/site/index.html\",\n    \"hub/site/llms.txt\",\n}\n")
        self.assertEqual(scope.check_scope(self.root, self.base, self.commit()), 3)

    def test_package_guide_change_requires_new_release(self):
        self.write("presets/role/INSTALL.md", "Altered guide")
        with self.assertRaisesRegex(ValueError, "Non-website source changed"):
            scope.check_scope(self.root, self.base, self.commit())

    def test_non_inventory_export_change_rejected(self):
        self.write("src/muse_presets/public_export.py", "PUBLIC_HUB_FILES = set()\n")
        with self.assertRaisesRegex(ValueError, "Public export implementation changed"):
            scope.check_scope(self.root, self.base, self.commit())

    def test_catalog_tampering_rejected(self):
        for field, value in (("url", "https://example.invalid/evil.zip"),
                             ("entry", "skills/other/SKILL.md"), ("asset", "other.zip"),
                             ("id", "other"), ("roles", ["different"])):
            with self.subTest(field=field):
                data = copy.deepcopy(self.directory)
                data["items"][0][field] = value
                self.write("hub/site/downloads.json", json.dumps(data))
                with self.assertRaisesRegex(ValueError, "Package identity"):
                    scope.check_scope(self.root, self.base, self.commit())
        data = copy.deepcopy(self.directory)
        data["bundles"][0]["asset"] = "wrong.zip"
        self.write("hub/site/downloads.json", json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Package identity"):
            scope.check_scope(self.root, self.base, self.commit())

    def test_dirty_checkout_and_wrong_website_head_rejected(self):
        self.write("hub/site/index.html", "<h1>Dirty</h1>")
        with self.assertRaisesRegex(ValueError, "Dirty website"):
            scope.check_scope(self.root, self.base, self.base)
        current = self.commit()
        with self.assertRaisesRegex(ValueError, "checkout differs"):
            scope.check_scope(self.root, self.base, self.base)
        # A ref name must not be accepted in place of a full SHA.
        with self.assertRaisesRegex(ValueError, "Full commit"):
            scope.check_scope(self.root, "HEAD", current)

    def test_unrelated_release_rejected(self):
        self.write("hub/site/index.html", "Different")
        child = self.commit()
        self.git("checkout", "--detach", self.base)
        with self.assertRaisesRegex(ValueError, "Git verification failed"):
            scope.check_scope(self.root, child, self.base)

    def test_duplicate_id_rejected(self):
        data = copy.deepcopy(self.directory)
        data["items"].append(copy.deepcopy(data["items"][0]))
        self.write("hub/site/downloads.json", json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Duplicate directory identity"):
            scope.check_scope(self.root, self.base, self.commit())
