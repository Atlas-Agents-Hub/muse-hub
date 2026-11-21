"""H03 regression gates: static method projections, not native Muse authority."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/discovery/route-compat"
OLD = DATA / "old-258.json"
NEW = DATA / "new-402.json"
MODULE = ROOT / "tools/compare_muse_routes.py"
EXPECTED = (
    "c800ba8833e0dff6cb3da868b1f9f3404f2a2e36bea42f8c359f634d084633cd",
    "4eaf51c921920665b7e512a3c3a9b486aabe7b9f95630961b989cecaa4b1a336",
)


def comparator():
    assert MODULE.is_file(), "H03_COMPARATOR_MISSING"
    spec = importlib.util.spec_from_file_location("h03_comparator", MODULE)
    assert spec and spec.loader
    obj = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = obj
    spec.loader.exec_module(obj)
    return obj


class H03Compatibility(unittest.TestCase):
    def test_original_pinned_fixtures_are_byte_exact(self):
        for path, sha in ((OLD, EXPECTED[0]), (NEW, EXPECTED[1])):
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), sha)
        self.assertIn("MIT License", (DATA / "NIKSHIPS-MIT.txt").read_text(encoding="utf-8"))

    def test_exact_method_set_delta_and_negative_live_claims(self):
        report = comparator().build_report()
        self.assertEqual(
            [report[k] for k in ("old_count", "new_count", "added_count", "removed_count", "changed_count")],
            [258, 402, 146, 2, 8],
        )
        self.assertEqual(report["removed"], ["feed.ingest", "feed.unit.share"])
        self.assertEqual(report["scope"], "PINNED_OFFLINE_SOURCE_PROJECTION_NOT_LIVE_PROVIDER")
        self.assertFalse(report["live_provider_tested"])
        self.assertFalse(report["authorization_established"])
        self.assertEqual(report["source"]["old"]["recorded_upstream_blob_sha1"], "bfdb6b492290c1dd8827087f2f49ab8046f56664")
        self.assertEqual(report["source"]["new"]["recorded_upstream_blob_sha1"], "6634f1b09d7e98b235bd24bdf3397391689cf981")

    def test_name_only_cannot_be_misrepresented_as_endpoint(self):
        m = comparator()
        old, new = m.load_routes(OLD), m.load_routes(NEW)
        self.assertEqual(sum("path" in row for row in old.values()), 8)
        self.assertEqual(sum("path" in row for row in new.values()), 8)
        report = m.build_report()
        self.assertEqual(len(report["matrix"]), 404)
        self.assertEqual(sum(x["definition"] == "NAME_ONLY" for x in report["matrix"].values()), 396)
        row = report["matrix"]["ads.details"]
        self.assertEqual(row["observed_in"], ["new"])
        self.assertEqual(row["definition"], "NAME_ONLY")
        self.assertNotIn("path", row)
        self.assertEqual(row["live_availability"], "NOT_TESTED")

    def test_detailed_changed_fields_and_serialization_are_preserved(self):
        report = comparator().build_report()
        self.assertEqual(sorted(report["changed"]), [
            "chat.subscribe", "connectors.accounts_link",
            "custom_connectors.register", "node.disconnect", "node.heartbeat",
            "node.list", "node.register", "node.unpair",
        ])
        changes = {x["method"]: x for x in report["changed_definitions"]}
        self.assertEqual(changes["chat.subscribe"]["changed_fields"], ["requestTimeoutMs"])
        self.assertEqual(changes["connectors.accounts_link"]["changed_fields"], ["path"])
        field = changes["node.list"]["field_changes"]["aliases"]
        self.assertEqual((field["old_type"], field["new_type"]), ("str", "list"))

    def test_malformed_data_is_rejected_before_comparison(self):
        m = comparator()
        invalid = [
            [{"method": "a", "projection": "NAME_ONLY_NOT_FULL_ROUTE"}] * 2,
            [{"method": "../admin", "projection": "NAME_ONLY_NOT_FULL_ROUTE"}],
            [{"method": "a", "http": "POST", "path": "https://evil.invalid"}],
            [{"method": "a", "http": "POST", "path": "/../../private"}],
            [{"method": "a", "http": "POST", "path": "/x/%2e%2e/private"}],
            [{"method": "a", "http": "POST", "path": "/safe", "aliases": ["/../admin"]}],
            [{"method": "a", "http": "POST", "path": "/safe", "aliases": ["x", "x"]}],
            [{"method": "a", "http": "post", "path": "/safe"}],
            [{"method": "a", "projection": "NAME_ONLY_NOT_FULL_ROUTE", "path": "/hidden"}],
            [{"method": "a", "http": "POST", "path": "/safe", "secret": "leak"}],
        ]
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "data.json"
            for rows in invalid:
                path.write_text(json.dumps(rows), encoding="utf-8")
                with self.subTest(rows=rows), self.assertRaises(ValueError):
                    m.load_routes(path)

    def test_source_pin_tampering_fails_closed(self):
        m = comparator()
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / OLD.name
            path.write_bytes(OLD.read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "SOURCE_PIN_MISMATCH"):
                m.verify_pinned_fixture(path, "old")

    def test_custom_input_is_untrusted_and_not_native(self):
        m = comparator()
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / "a.json", Path(d) / "b.json"
            a.write_text('[{"method":"a","projection":"NAME_ONLY_NOT_FULL_ROUTE"}]', encoding="utf-8")
            b.write_text('[{"method":"b","projection":"NAME_ONLY_NOT_FULL_ROUTE"}]', encoding="utf-8")
            report = m.build_report(a, b)
            self.assertEqual((report["added_count"], report["removed_count"], report["changed_count"]), (1, 1, 0))
            self.assertEqual(report["scope"], "UNVERIFIED_CUSTOM_INPUT_NOT_LIVE_PROVIDER")
            self.assertFalse(report["source"]["old"]["manifest_verified"])

    def test_cli_create_only_and_expected_counts(self):
        with tempfile.TemporaryDirectory() as d:
            output = Path(d) / "report.json"
            args = [sys.executable, "-B", str(MODULE), "--expect", "258,402,146,2,8", "--out", str(output)]
            first = subprocess.run(args, capture_output=True, text=True, timeout=20)
            self.assertEqual(first.returncode, 0, first.stderr)
            data = output.read_bytes()
            self.assertEqual(json.loads(data)["changed_count"], 8)
            again = subprocess.run(args, capture_output=True, text=True, timeout=20)
            self.assertEqual(again.returncode, 2)
            self.assertEqual(output.read_bytes(), data)
            self.assertIn("OUTPUT_EXISTS", again.stderr)
            wrong = subprocess.run([sys.executable, "-B", str(MODULE), "--expect", "1,2,3,4,5"], capture_output=True, text=True, timeout=20)
            self.assertEqual(wrong.returncode, 2)
            self.assertIn("EXPECTED_COUNTS_MISMATCH", wrong.stderr)


    def test_public_export_admits_only_reviewed_h03_tool_and_data(self):
        from muse_presets.public_export import PublicExportError, select_public_files
        result = select_public_files(ROOT, verify_manifest=False)
        self.assertIn("tools/compare_muse_routes.py", result)
        self.assertIn("docs/discovery/route-compat/old-258.json", result)
        self.assertIn("docs/discovery/route-compat/new-402.json", result)
        self.assertIn("tests/test_muse_route_compat_h03.py", result)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            tools = root / "tools"
            tools.mkdir()
            (tools / "compare_muse_routes.py").write_text("safe", encoding="utf-8")
            self.assertEqual(
                set(select_public_files(root, verify_manifest=False)),
                {"tools/compare_muse_routes.py"},
            )
            (tools / "unreviewed.py").write_text("do not distribute", encoding="utf-8")
            with self.assertRaisesRegex(PublicExportError, "UNAPPROVED_COLLECTION_PATH"):
                select_public_files(root, verify_manifest=False)


    def test_route_reference_explains_saved_revisions_and_links_terminal(self):
        index = (ROOT / "docs/README.md").read_text(encoding="utf-8")
        self.assertIn("TERMINAL.md", index)
        guide = (ROOT / "docs/discovery/ROUTE_COMPATIBILITY.md").read_text(encoding="utf-8")
        self.assertIn("nikships/muse-cli", guide)
        self.assertIn("Compare two saved revisions of the Muse CLI route table", guide)
        self.assertIn("repeatable JSON report", guide)
        self.assertIn("[terminal guide](../TERMINAL.md)", guide)
        self.assertIn("tools/compare_muse_routes.py --expect 258,402,146,2,8", guide)
        for option in ("--old", "--new", "SHA-256 digests"):
            self.assertIn(option, guide)
        self.assertNotIn(chr(92) + "`", guide)
        terminal = (ROOT / "docs/TERMINAL.md").read_text(encoding="utf-8")
        self.assertIn("quickstart.py --all", terminal)
        self.assertNotIn("nikships/muse-cli", terminal)


if __name__ == "__main__":
    unittest.main()
