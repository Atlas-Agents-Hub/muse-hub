"""H12 source-only Family Link kit: deterministic ZIP, isolation, and fail-closed checks."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

from muse_presets.family_sourcekit import (
    FamilySourcekitError, export_family_sourcekit, verify_family_sourcekit,
)

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ROLES = 15


class FamilySourcekitTests(unittest.TestCase):
    def setUp(self):
        self._temp = tempfile.TemporaryDirectory(prefix="muse-family-sourcekit-")
        self.addCleanup(self._temp.cleanup)
        self.base = Path(self._temp.name)

    def export(self, dest=None, root=ROOT):
        dest = dest or self.base / "family-link-offline.zip"
        result = export_family_sourcekit(root, dest)
        self.assertEqual(result["status"], "LOCAL_FAMILY_LINK_KIT_EXPORTED")
        self.assertFalse(result["native_installed"])
        self.assertFalse(result["effect_authorized"])
        self.assertEqual(result["source_roles"], EXPECTED_ROLES)
        self.assertEqual(result["sha256"], hashlib.sha256(dest.read_bytes()).hexdigest())
        self.assertEqual(
            verify_family_sourcekit(dest, result["sha256"])["status"],
            "LOCAL_FAMILY_LINK_KIT_VERIFIED",
        )
        return result

    def test_export_exact_members_and_determinism(self):
        out = self.base / "family-link-offline.zip"
        a = self.export(out)
        another = self.base / "repeat.zip"
        b = self.export(another)
        self.assertEqual(out.read_bytes(), another.read_bytes())
        self.assertEqual(a["sha256"], b["sha256"])
        with zipfile.ZipFile(out) as z:
            names = z.namelist()
            self.assertEqual(names, sorted(names))
            self.assertEqual(len(set(names)), len(names))
            self.assertIn("SOURCEKIT_MANIFEST.json", names)
            self.assertIn("START_HERE.md", names)
            self.assertIn("src/muse_presets/family_envelope.py", names)
            self.assertIn("examples/family_offline_handoff_demo.py", names)
            self.assertIn("presets/catalog.json", names)
            manifest = json.loads(z.read("SOURCEKIT_MANIFEST.json"))
            self.assertEqual(manifest["schema"], "muse-hub/family-link-offline-kit/v1")
            for field in ("native_installed", "sender_authenticated",
                          "recipient_authenticated", "effect_authorized",
                          "transport_bound", "public_release_published"):
                self.assertIs(manifest[field], False)
            self.assertEqual(len(manifest["role_ids"]), EXPECTED_ROLES)
            self.assertEqual(
                set(manifest["files_sha256"]), set(names) - {"SOURCEKIT_MANIFEST.json"},
            )
            for name, digest in manifest["files_sha256"].items():
                self.assertEqual(hashlib.sha256(z.read(name)).hexdigest(), digest, name)
            for name in names:
                self.assertNotIn("..", Path(name).parts)
                self.assertFalse(name.startswith("/"))

    def test_extracted_original_two_process_demo_works_without_provider(self):
        self.export()
        extracted = self.base / "extracted"
        extracted.mkdir()
        with zipfile.ZipFile(self.base / "family-link-offline.zip") as z:
            z.extractall(extracted)
        demo = extracted / "examples" / "family_offline_handoff_demo.py"
        env = dict(os.environ, PYTHONPATH=str(extracted / "src"), PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run(
            [sys.executable, "-B", str(demo)],
            cwd=extracted, env=env, capture_output=True, text=True, timeout=45,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        actual = json.loads(result.stdout)
        self.assertEqual(actual["status"], "LOCAL_HANDOFF_REVIEW_ONLY_NOT_DELIVERED")
        self.assertTrue(actual["separate_process_verified"])
        self.assertTrue(actual["replayed_id_refused"])
        for field in ("recipient_acknowledged", "effect_authorized",
                      "external_effect_authorized", "recipient_authenticated",
                      "durable_replay_fence_verified"):
            self.assertFalse(actual[field], field)

    def test_missing_external_zip_pin_and_tampering_fail_closed(self):
        result = self.export()
        path = self.base / "family-link-offline.zip"
        for pin in ("", "a" * 64, "not-a-hash"):
            with self.subTest(pin=pin), self.assertRaises(FamilySourcekitError):
                verify_family_sourcekit(path, pin)
        original = path.read_bytes()
        path.write_bytes(original + b"!tampered")
        with self.assertRaisesRegex(FamilySourcekitError, "ZIP_SHA256_MISMATCH"):
            verify_family_sourcekit(path, result["sha256"])

    def test_export_no_overwrite_and_no_unreviewed_source(self):
        path = self.base / "occupied.zip"
        path.write_bytes(b"original")
        with self.assertRaises(FileExistsError):
            export_family_sourcekit(ROOT, path)
        self.assertEqual(path.read_bytes(), b"original")
        with self.assertRaises(FileNotFoundError):
            export_family_sourcekit(ROOT, self.base / "missing-dir" / "new.zip")
        self.assertFalse((self.base / "missing-dir").exists())

    def test_modified_policy_or_original_module_refused(self):
        cloned = self.base / "source"
        cloned.mkdir()
        with zipfile.ZipFile(self.export_path_from_original()) as z:
            z.extractall(cloned)
        (cloned / "SOURCEKIT_MANIFEST.json").unlink()
        (cloned / "START_HERE.md").unlink()
        policy = cloned / "presets/model-builder/preset.json"
        document = json.loads(policy.read_text(encoding="utf-8"))
        document["family_link"]["enabled"] = True
        policy.write_text(json.dumps(document), encoding="utf-8")
        with self.assertRaisesRegex(FamilySourcekitError, "FAMILY_DISABLED_POLICY_REQUIRED"):
            export_family_sourcekit(cloned, self.base / "policy.zip")
        document["family_link"]["enabled"] = False
        policy.write_text(json.dumps(document), encoding="utf-8")
        module = cloned / "src/muse_presets/family_envelope.py"
        module.write_bytes(module.read_bytes() + b"\n# review mutation\n")
        with self.assertRaisesRegex(FamilySourcekitError, "SOURCE_PIN_MISMATCH"):
            export_family_sourcekit(cloned, self.base / "module.zip")
        self.assertFalse((self.base / "module.zip").exists())

    def export_path_from_original(self):
        target = self.base / "source-original.zip"
        export_family_sourcekit(ROOT, target)
        return target

    def test_untrusted_archive_member_and_duplicate_rejected_with_matching_hash(self):
        self.export()
        src = self.base / "family-link-offline.zip"
        with zipfile.ZipFile(src) as reader:
            payloads = {name: reader.read(name) for name in reader.namelist()}
        bad = self.base / "unsafe.zip"
        with zipfile.ZipFile(bad, "w") as writer:
            for name, data in payloads.items():
                writer.writestr(name, data)
            writer.writestr("../private.txt", "injected")
        pin = hashlib.sha256(bad.read_bytes()).hexdigest()
        with self.assertRaisesRegex(FamilySourcekitError, "ARCHIVE_MEMBER_UNSAFE"):
            verify_family_sourcekit(bad, pin)
        with zipfile.ZipFile(bad, "a") as writer:
            writer.writestr("START_HERE.md", "duplicate")
        pin = hashlib.sha256(bad.read_bytes()).hexdigest()
        with self.assertRaises(FamilySourcekitError):
            verify_family_sourcekit(bad, pin)

    def test_existing_family_source_remains_the_only_authority(self):
        result = self.export()
        with zipfile.ZipFile(self.base / "family-link-offline.zip") as z:
            manifest = json.loads(z.read("SOURCEKIT_MANIFEST.json"))
            members = set(z.namelist())
            self.assertNotIn("services/family-native/server.py", members)
            self.assertNotIn("credentials.json", members)
            self.assertNotIn(".env", members)
            self.assertEqual(manifest["source_commit"], "befa77356804843ce3a056aed21cb14a9a836b3c")
            self.assertEqual(manifest["scope"], "SOURCE_ONLY_OFFLINE_TWO_PROCESS_NOT_DELIVERED")


    def test_cli_export_verify_and_no_overwrite(self):
        wrapper = ROOT / "examples/export_family_link_sourcekit.py"
        self.assertTrue(wrapper.is_file())
        dest = self.base / "cli-kit.zip"
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-B", str(wrapper)]
        result = subprocess.run(command + ["--to", str(dest)], cwd=ROOT,
                                env=env, text=True, capture_output=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        export = json.loads(result.stdout)
        self.assertEqual(export["status"], "LOCAL_FAMILY_LINK_KIT_EXPORTED")
        prior = dest.read_bytes()
        refused = subprocess.run(command + ["--to", str(dest)], cwd=ROOT,
                                 env=env, text=True, capture_output=True, timeout=30)
        self.assertEqual(refused.returncode, 2)
        self.assertEqual(prior, dest.read_bytes())
        denied = subprocess.run(command + ["--verify", str(dest)], cwd=ROOT,
                                env=env, text=True, capture_output=True, timeout=30)
        self.assertEqual(denied.returncode, 2)
        ok = subprocess.run(command + ["--verify", str(dest), "--sha256", export["sha256"]],
                            cwd=ROOT, env=env, text=True, capture_output=True, timeout=30)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertEqual(json.loads(ok.stdout)["status"], "LOCAL_FAMILY_LINK_KIT_VERIFIED")

    def test_symlinked_module_and_unreviewed_receivers_are_refused(self):
        source = self.base / "source"
        source.mkdir()
        with zipfile.ZipFile(self.export_path_from_original()) as z:
            z.extractall(source)
        (source / "SOURCEKIT_MANIFEST.json").unlink()
        (source / "START_HERE.md").unlink()
        module = source / "src/muse_presets/family.py"
        replacement = module.with_name("family-owned.py")
        module.rename(replacement)
        try:
            module.symlink_to(replacement)
        except (OSError, NotImplementedError):
            self.skipTest("symlink not supported")
        with self.assertRaisesRegex(FamilySourcekitError, "SYMLINK_SOURCE_REFUSED"):
            export_family_sourcekit(source, self.base / "symlink.zip")
        module.unlink()
        replacement.rename(module)
        policy = source / "presets/model-builder/preset.json"
        doc = json.loads(policy.read_text(encoding="utf-8"))
        doc["family_link"]["suggested_receivers"] = ["unreviewed-external-recipient"]
        policy.write_text(json.dumps(doc), encoding="utf-8")
        with self.assertRaisesRegex(FamilySourcekitError, "UNSAFE_FAMILY_RECEIVER_POLICY"):
            export_family_sourcekit(source, self.base / "unreviewed.zip")

    def test_archive_symlinks_rejected_even_with_matching_supplied_zip_hash(self):
        self.export()
        source = self.base / "family-link-offline.zip"
        target = self.base / "linked.zip"
        with zipfile.ZipFile(source) as inp, zipfile.ZipFile(target, "w") as out:
            for info in inp.infolist():
                if info.filename == "START_HERE.md":
                    changed = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                    changed.create_system = 3
                    changed.external_attr = (0o120777 << 16)
                    changed.compress_type = zipfile.ZIP_DEFLATED
                    out.writestr(changed, b"not a text file")
                else:
                    out.writestr(info, inp.read(info))
        changed_digest = hashlib.sha256(target.read_bytes()).hexdigest()
        with self.assertRaisesRegex(FamilySourcekitError, "ARCHIVE_MEMBER_UNSAFE"):
            verify_family_sourcekit(target, changed_digest)

    def test_public_documentation_is_linked_and_not_native_claim(self):
        doc = ROOT / "docs/kits/FAMILY_LINK_SOURCEKIT.md"
        self.assertTrue(doc.is_file())
        text = doc.read_text(encoding="utf-8")
        self.assertIn("examples/export_family_link_sourcekit.py", text)
        self.assertIn("NOT", text)
        self.assertIn("offline", text.lower())
        self.assertIn("FAMILY_LINK.md", (ROOT / "docs/README.md").read_text(encoding="utf-8"))
        self.assertIn("kits/FAMILY_LINK_SOURCEKIT.md", (ROOT / "docs/FAMILY_LINK.md").read_text(encoding="utf-8"))


    def test_nested_unhashable_receiver_policy_refused_without_unhandled_exception(self):
        source = self.base / "source-nested"
        source.mkdir()
        with zipfile.ZipFile(self.export_path_from_original()) as z:
            z.extractall(source)
        policy = source / "presets/model-builder/preset.json"
        doc = json.loads(policy.read_text(encoding="utf-8"))
        doc["family_link"]["suggested_receivers"] = [{"id": "research-evaluator"}]
        policy.write_text(json.dumps(doc), encoding="utf-8")
        with self.assertRaisesRegex(FamilySourcekitError, "UNSAFE_FAMILY_RECEIVER_POLICY"):
            export_family_sourcekit(source, self.base / "bad-policy.zip")
        self.assertFalse((self.base / "bad-policy.zip").exists())



    def test_role_profile_bytes_are_pinned_not_just_policy_flags(self):
        source = self.base / "profile-variant"
        source.mkdir()
        with zipfile.ZipFile(self.export_path_from_original()) as z:
            z.extractall(source)
        policy = source / "presets/model-builder/preset.json"
        document = json.loads(policy.read_text(encoding="utf-8"))
        self.assertFalse(document["family_link"]["enabled"])
        document["title"] = "Silent unrelated edit to policy source"
        policy.write_text(json.dumps(document), encoding="utf-8")
        with self.assertRaisesRegex(FamilySourcekitError, "PROFILE_SOURCE_PIN_MISMATCH"):
            export_family_sourcekit(source, self.base / "changed-profile.zip")
        self.assertFalse((self.base / "changed-profile.zip").exists())

    def test_duplicate_json_manifest_key_fails_even_with_recomputed_zip_hash(self):
        self.export()
        original = self.base / "family-link-offline.zip"
        tampered = self.base / "ambiguous-json.zip"
        with zipfile.ZipFile(original) as src, zipfile.ZipFile(tampered, "w") as out:
            for info in src.infolist():
                raw = src.read(info.filename)
                if info.filename == "SOURCEKIT_MANIFEST.json":
                    text = raw.decode("utf-8")
                    # Duplicate a real key with the same value; ordinary
                    # json.loads accepts this ambiguous source silently.
                    replacement = text.rstrip()
                    self.assertTrue(replacement.endswith("}"))
                    replacement = replacement[:-1] + ', "scope": "SOURCE_ONLY_OFFLINE_TWO_PROCESS_NOT_DELIVERED"}'
                    raw = (replacement + "\n").encode("utf-8")
                out.writestr(info, raw)
        changed_sha = hashlib.sha256(tampered.read_bytes()).hexdigest()
        with self.assertRaisesRegex(FamilySourcekitError, "KIT_ARCHIVE_INVALID"):
            verify_family_sourcekit(tampered, changed_sha)


if __name__ == "__main__":
    unittest.main()
