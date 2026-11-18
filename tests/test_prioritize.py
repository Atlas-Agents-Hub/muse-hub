"""Behavior tests for exact RICE ranking and a resource-bounded next batch."""
from __future__ import annotations

import contextlib
import copy
import csv
from decimal import localcontext, ROUND_DOWN
import importlib.util
import io
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


TOOL = Path(__file__).resolve().parents[1] / "tools" / "prioritize.py"


def item(ident="alpha", **updates):
    value = {"id": ident, "name": ident.title(), "reach": 100, "impact": 1,
             "confidence_pct": 100, "effort": 1, "resource": "engineering"}
    value.update(updates)
    return value


def document(items=None, **updates):
    value = {"schema": "muse-prioritization/v1", "reach_period": "2026-Q4",
             "effort_unit": "person-days", "capacity": {"engineering": 10},
             "items": [item()] if items is None else items}
    value.update(updates)
    return value


class PrioritizeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        spec = importlib.util.spec_from_file_location("prioritize_under_test", TOOL)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def run_cli(self, value=None, *, raw=None, suffix=".json", args=()):
        source = self.root / ("input" + suffix)
        source.write_text(json.dumps(document() if value is None else value)
                          if raw is None else raw, encoding="utf-8", newline="")
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                code = self.mod.main(["--input", str(source), *args])
            except SystemExit as exc:
                code = exc.code
        return code, stdout.getvalue(), stderr.getvalue()

    def successful(self, value=None, **kwargs):
        code, out, err = self.run_cli(value, **kwargs)
        self.assertEqual((code, err), (0, ""))
        return json.loads(out)

    def rejected(self, value=None, *, message, **kwargs):
        code, out, err = self.run_cli(value, **kwargs)
        self.assertEqual((code, out), (2, ""))
        self.assertIn("prioritize: error:", err)
        self.assertIn(message, err)

    def test_independently_calculated_rice_and_confidence_endpoints(self):
        result = self.successful(document([
            item("launch", reach=120, impact=2, confidence_pct=80, effort=4),
            item("certain", reach=30, impact=3, confidence_pct=100, effort=2),
            item("unknown", reach=999, impact=3, confidence_pct=0, effort=1),
        ]))
        ranked = result["ranked_items"]
        self.assertEqual([(x["id"], x["score_exact"], x["score"]) for x in ranked],
                         [("launch", "48/1", "48"), ("certain", "45/1", "45"),
                          ("unknown", "0/1", "0")])
        self.assertEqual(result["schema"], "muse-prioritization-report/v1")
        self.assertEqual(result["reach_period"], "2026-Q4")
        self.assertEqual(result["effort_unit"], "person-days")

    def test_fractional_scores_sorted_before_display_rounding(self):
        result = self.successful(document([
            item("alpha", reach=1, effort=3),
            item("zulu", reach=1.000000000001, effort=3),
        ]))
        self.assertEqual([x["id"] for x in result["ranked_items"]], ["zulu", "alpha"])
        self.assertEqual(result["ranked_items"][0]["score"], "0.333333")
        self.assertEqual(result["ranked_items"][1]["score_exact"], "1/3")

    def test_permutations_ties_and_repeated_runs_are_byte_deterministic(self):
        items = [item("zulu", dependencies=["base", "addon"]),
                 item("alpha"), item("base", reach=0), item("addon", reach=0)]
        expected = self.run_cli(document(items))[1]
        for permutation in itertools.permutations(items):
            data = document(list(permutation))
            data["items"] = copy.deepcopy(data["items"])
            for entry in data["items"]:
                entry["dependencies"] = list(reversed(entry.get("dependencies", [])))
            self.assertEqual(self.run_cli(data)[1], expected)
        self.assertEqual(self.run_cli(document(items))[1], expected)

    def test_plan_does_not_mutate_input(self):
        original = document([item("zulu", dependencies=["beta", "alpha"]),
                             item("alpha"), item("beta")])
        before = copy.deepcopy(original)
        self.mod.plan(original)
        self.assertEqual(original, before)

    def test_decimal_context_cannot_change_scores_budgets_or_bounds(self):
        data = document([item(reach=1234, effort=0.25)], capacity={"engineering": 0.3})
        expected = self.mod.plan(data)
        with localcontext() as context:
            context.prec = 2
            context.rounding = ROUND_DOWN
            self.rejected(document([item(reach=1000000000001)]), message="number")
            context.Emax = 2
            context.Emin = -2
            self.assertEqual(self.mod.plan(data), expected)

    def test_decimal_efforts_fit_exact_capacity(self):
        result = self.successful(document([item("one", effort=0.1),
                                            item("two", effort=0.2)],
                                           capacity={"engineering": 0.3}))
        self.assertEqual(result["selected_order"], ["one", "two"])
        self.assertEqual(result["budgets"]["engineering"],
                         {"capacity": "0.3", "used": "0.3", "remaining": "0"})

    def test_oversized_item_is_deferred_whole_then_small_item_fits(self):
        result = self.successful(document([
            item("large", reach=1000, effort=11), item("small", reach=1, effort=2),
        ]))
        self.assertEqual(result["selected_order"], ["small"])
        deferred = result["deferred"][0]
        self.assertEqual(deferred["id"], "large")
        self.assertEqual(deferred["bundle"], ["large"])
        self.assertEqual(deferred["shortfalls"]["engineering"],
                         {"required": "11", "remaining": "10", "shortfall": "1"})
        self.assertIn("engineering", deferred["reason"])
        self.assertIn("person-days", deferred["reason"])
        self.assertEqual(result["budgets"]["engineering"]["used"], "2")

    def test_prerequisites_precede_high_ranked_item_across_resources(self):
        result = self.successful(document([
            item("launch", reach=1000, effort=2, dependencies=["design"]),
            item("design", reach=0, effort=3, resource="design"),
        ], capacity={"engineering": 2, "design": 3}))
        self.assertEqual(result["ranked_items"][0]["id"], "launch")
        self.assertEqual(result["selected_order"], ["design", "launch"])
        self.assertEqual(result["ranked_items"][0]["selection_order"], 2)
        self.assertEqual(result["budgets"]["design"]["remaining"], "0")

    def test_infeasible_bundle_commits_no_partial_cost(self):
        result = self.successful(document([
            item("launch", reach=1000, effort=2, dependencies=["design"]),
            item("design", reach=1, effort=2, resource="design"),
            item("other", reach=10, effort=1),
        ], capacity={"engineering": 1, "design": 2}))
        self.assertEqual(result["selected_order"], ["other", "design"])
        self.assertEqual(result["deferred"][0]["bundle"], ["design", "launch"])
        self.assertEqual(result["budgets"]["design"]["used"], "2")

    def test_shared_diamond_dependency_is_charged_once(self):
        result = self.successful(document([
            item("launch", reach=1000, dependencies=["left", "right"]),
            item("left", dependencies=["base"]),
            item("right", dependencies=["base"]), item("base"),
        ], capacity={"engineering": 4}))
        self.assertEqual(result["selected_order"], ["base", "left", "right", "launch"])
        self.assertEqual(result["budgets"]["engineering"]["used"], "4")

    def test_two_candidates_share_already_selected_prerequisite(self):
        result = self.successful(document([
            item("alpha", dependencies=["base"]),
            item("beta", dependencies=["base"]), item("base", reach=0),
        ], capacity={"engineering": 3}))
        self.assertEqual(result["selected_order"], ["base", "alpha", "beta"])
        self.assertEqual(result["deferred"], [])

    def test_done_dependency_costs_zero_and_is_not_selected_again(self):
        result = self.successful(document([
            item("launch", dependencies=["base"]),
            item("base", effort=1000, status="done"),
        ], capacity={"engineering": 1}))
        self.assertEqual(result["selected_order"], ["launch"])
        self.assertEqual(result["completed_ids"], ["base"])
        self.assertEqual(result["budgets"]["engineering"]["used"], "1")
        base = next(x for x in result["ranked_items"] if x["id"] == "base")
        self.assertEqual((base["selection_status"], base["selection_order"]), ("done", None))

    def test_zero_capacity_defers_todo_but_accepts_completed(self):
        result = self.successful(document([item("todo"), item("done", status="done")],
                                           capacity={"engineering": 0}))
        self.assertEqual(result["selected_order"], [])
        self.assertEqual(result["completed_ids"], ["done"])
        self.assertEqual(result["budgets"]["engineering"]["used"], "0")

    def test_all_documented_impact_and_effort_unit_categories(self):
        for impact in (0.25, 0.5, 1, 2, 3):
            for unit in ("person-hours", "person-days", "person-months"):
                with self.subTest(impact=impact, unit=unit):
                    result = self.successful(document([item(impact=impact)], effort_unit=unit))
                    self.assertEqual(result["selected_order"], ["alpha"])

    def test_invalid_numeric_values_and_types_are_rejected(self):
        for field, values in {
            "reach": [-1, True, "100", None, float("nan"), float("inf"), 1e13],
            "effort": [0, -1, True, "1", 1e-13],
            "confidence_pct": [-1, 101, True, "100"],
            "impact": [0, 0.75, 4, True, "1"],
        }.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.rejected(document([item(**{field: value})]), message="")

    def test_extreme_exponents_and_long_number_tokens_are_rejected(self):
        template = json.dumps(document()).replace('"reach": 100', '"reach": TOKEN')
        for token in ("1e999999999", "1e-999999999", "1e13", "1e-13", "9" * 5000):
            with self.subTest(token=token[:20]):
                self.rejected(raw=template.replace("TOKEN", token), message="number")

    def test_bounded_scientific_notation_is_accepted(self):
        raw = json.dumps(document()).replace('"reach": 100', '"reach": 1e2')
        result = self.successful(raw=raw)
        self.assertEqual(result["ranked_items"][0]["score_exact"], "100/1")

    def test_invalid_categories_names_slugs_and_dependencies_are_rejected(self):
        for change in ({"status": "pending"}, {"status": ""}, {"resource": "absent"},
                       {"id": "../alpha"}, {"id": "A"}, {"name": " "},
                       {"name": "bad\x00name"}, {"name": "\ud800"},
                       {"dependencies": "alpha"}, {"dependencies": [3]},
                       {"dependencies": ["x", "x"]}):
            with self.subTest(change=change):
                self.rejected(document([item(**change)]), message="")

    def test_invalid_document_metadata_and_capacity_are_rejected(self):
        for changes in ({"schema": "muse-prioritization/v2"}, {"reach_period": ""},
                        {"effort_unit": "days"}, {"capacity": {"engineering": -1}},
                        {"capacity": {"engineering": True}}, {"capacity": {}},
                        {"capacity": {"Engineering": 10}}, {"items": []},
                        {"items": [item(str(i)) for i in range(1001)]}):
            with self.subTest(changes=str(changes)[:100]):
                self.rejected(document(**changes), message="")

    def test_unknown_and_missing_fields_are_rejected(self):
        for data in (document(unexpected=True), document([item(unexpected=True)])):
            self.rejected(data, message="unknown")
        for field in ("schema", "reach_period", "effort_unit", "capacity", "items"):
            data = document(); del data[field]
            self.rejected(data, message="missing")
        for field in ("id", "name", "reach", "impact", "confidence_pct", "effort", "resource"):
            data = document(); del data["items"][0][field]
            self.rejected(data, message="missing")

    def test_duplicate_json_keys_rejected_at_every_depth(self):
        raw = json.dumps(document())
        for candidate in (raw.replace('"schema":', '"schema": "first", "schema":', 1),
                          raw.replace('"engineering": 10', '"engineering": 9, "engineering": 10'),
                          raw.replace('"reach": 100', '"reach": 5, "reach": 100')):
            self.rejected(raw=candidate, message="duplicate JSON key")

    def test_duplicate_item_ids_rejected(self):
        self.rejected(document([item(), item()]), message="duplicate item id")

    def test_missing_dependencies_rejected_even_for_done_items(self):
        for status in ("todo", "done"):
            self.rejected(document([item(dependencies=["missing"], status=status)]),
                          message="missing dependency")

    def test_cycles_self_cycles_and_done_cycles_rejected(self):
        for items in ([item(dependencies=["alpha"])],
                      [item("alpha", dependencies=["beta"]), item("beta", dependencies=["alpha"])],
                      [item("alpha", dependencies=["beta"], status="done"),
                       item("beta", dependencies=["alpha"], status="done")]):
            self.rejected(document(items), message="cycle")

    def test_thousand_item_chain_does_not_hit_recursion_limit(self):
        items = [item(f"item-{i:04}", reach=i, dependencies=[] if i == 0
                      else [f"item-{i - 1:04}"]) for i in range(1000)]
        result = self.successful(document(items, capacity={"engineering": 1000}))
        self.assertEqual(result["selected_order"], [x["id"] for x in items])
        self.assertEqual(result["budgets"]["engineering"]["remaining"], "0")

    def csv_input(self, rows, fields=None):
        fields = fields or ["id", "name", "reach", "impact", "confidence_pct", "effort",
                            "resource", "dependencies", "status"]
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
        return stream.getvalue()

    def csv_args(self, *extra):
        return ("--reach-period", "2026-Q4", "--effort-unit", "person-days",
                "--capacity", "engineering=10", *extra)

    def test_csv_input_and_quoted_output_preserve_ordinary_text(self):
        name = 'Build, "measure"\nand learn'
        raw = self.csv_input([item(name=name)])
        result = self.successful(raw=raw, suffix=".csv", args=self.csv_args())
        self.assertEqual(result["ranked_items"][0]["name"], name)
        code, out, err = self.run_cli(raw=raw, suffix=".csv",
                                      args=self.csv_args("--format", "csv"))
        self.assertEqual((code, err), (0, ""))
        rows = list(csv.DictReader(io.StringIO(out, newline="")))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["name"], name)
        self.assertEqual((rows[0]["rank"], rows[0]["selection_order"], rows[0]["status"]),
                         ("1", "1", "todo"))
        self.assertEqual((rows[0]["reach_period"], rows[0]["effort_unit"]),
                         ("2026-Q4", "person-days"))
        self.assertEqual((rows[0]["capacity"], rows[0]["used"], rows[0]["remaining"]),
                         ("10", "1", "9"))

    def test_csv_dependencies_optional_columns_and_default_status(self):
        fields = ["id", "name", "reach", "impact", "confidence_pct", "effort", "resource"]
        result = self.successful(raw=self.csv_input([item()], fields), suffix=".csv",
                                  args=self.csv_args())
        self.assertEqual(result["ranked_items"][0]["status"], "todo")
        raw = self.csv_input([item("launch", dependencies="base;other"),
                              item("base", status="done"), item("other")])
        result = self.successful(raw=raw, suffix=".csv", args=self.csv_args())
        self.assertEqual(result["selected_order"], ["other", "launch"])

    def test_csv_formula_leading_text_is_safe_and_json_keeps_original(self):
        names = ["=1+1", "+SUM(A1)", "-1+1", "@SUM(A1)", "  =1", "\t=1", "\r=1", "\n=1"]
        for name in names:
            with self.subTest(name=name):
                data = document([item(name=name)], reach_period="=TODAY()")
                self.assertEqual(self.successful(data)["ranked_items"][0]["name"], name)
                code, out, err = self.run_cli(data, args=("--format", "csv"))
                self.assertEqual((code, err), (0, ""))
                row = next(csv.DictReader(io.StringIO(out, newline="")))
                self.assertEqual(row["name"], "'" + name)
                self.assertEqual(row["reach_period"], "'=TODAY()")

    def test_csv_deferred_row_includes_reason_and_no_selection_order(self):
        code, out, err = self.run_cli(document([item(effort=11)]), args=("--format", "csv"))
        self.assertEqual((code, err), (0, ""))
        row = next(csv.DictReader(io.StringIO(out)))
        self.assertEqual(row["selection_status"], "deferred")
        self.assertEqual(row["selection_order"], "")
        self.assertIn("shortfall 1", row["reason"])

    def test_csv_stdout_is_utf8_without_platform_newline_translation(self):
        source = self.root / "unicode.json"
        source.write_text(json.dumps(document([item(name="Créer, 日本語")])), encoding="utf-8")
        binary = io.BytesIO()
        output = io.TextIOWrapper(binary, encoding="ascii", newline="\r\n", write_through=True)
        errors = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            code = self.mod.main(["--input", str(source), "--format", "csv"])
        output.flush()
        self.assertEqual((code, errors.getvalue()), (0, ""))
        self.assertIn("Créer, 日本語".encode("utf-8"), binary.getvalue())
        self.assertNotIn(b"\r\r\n", binary.getvalue())

    def test_csv_bad_columns_rows_and_syntax_rejected(self):
        raw = self.csv_input([item()])
        for bad in (raw.replace("id,name", "id,id", 1), raw.replace("id,name", "id,unknown", 1),
                    raw.replace(",resource,", ",resources,", 1), raw + "extra,column\n",
                    raw.replace("alpha,Alpha", 'alpha,"unterminated', 1),
                    raw.replace(",Alpha,", ",Alpha,extra,", 1)):
            with self.subTest(bad=bad[:80]):
                self.rejected(raw=bad, suffix=".csv", args=self.csv_args(), message="CSV")

    def test_csv_invalid_numeric_categories_or_dependencies_rejected(self):
        for row in (item(impact="medium"), item(confidence_pct="80%"),
                    item(status="pending"), item(dependencies="alpha;;other")):
            self.rejected(raw=self.csv_input([row]), suffix=".csv", args=self.csv_args(), message="")

    def test_csv_metadata_required_and_capacity_flags_strict(self):
        raw = self.csv_input([item()])
        self.rejected(raw=raw, suffix=".csv", message="metadata")
        for flag in ("engineering=3", "design=NaN", "bad-format", "design=-1"):
            self.rejected(raw=raw, suffix=".csv", args=self.csv_args("--capacity", flag), message="")
        self.rejected(raw=self.csv_input([item(resource="design")]), suffix=".csv",
                      args=self.csv_args(), message="capacity")

    def test_json_rejects_metadata_flags_instead_of_overriding(self):
        for args in (("--reach-period", "2026-Q4"), ("--effort-unit", "person-days"),
                     ("--capacity", "engineering=10")):
            self.rejected(args=args, message="JSON")

    def test_output_is_new_file_and_stdout_stays_empty(self):
        path = self.root / "report.json"
        code, out, err = self.run_cli(args=("--output", str(path)))
        self.assertEqual((code, out, err), (0, "", ""))
        self.assertEqual(json.loads(path.read_text())["selected_order"], ["alpha"])

    def test_existing_output_and_same_input_never_overwritten(self):
        path = self.root / "existing.json"; path.write_bytes(b"keep me")
        self.rejected(args=("--output", str(path)), message="exists")
        self.assertEqual(path.read_bytes(), b"keep me")
        input_path = self.root / "input.json"
        self.rejected(args=("--output", str(input_path)), message="exists")
        self.assertEqual(json.loads(input_path.read_text()), document())

    def test_output_symlink_and_dangling_symlink_never_followed(self):
        target = self.root / "target.json"; target.write_bytes(b"keep me")
        link = self.root / "linked.json"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation unavailable on this platform")
        self.rejected(args=("--output", str(link)), message="exists")
        self.assertEqual(target.read_bytes(), b"keep me")
        link.unlink(); target.unlink(); link.symlink_to(target)
        self.rejected(args=("--output", str(link)), message="exists")
        self.assertFalse(target.exists()); self.assertTrue(link.is_symlink())

    def test_failed_new_output_is_removed(self):
        target = self.root / "partial.json"
        with mock.patch.object(self.mod.os, "fsync", side_effect=OSError("simulated disk full")):
            self.rejected(args=("--output", str(target)), message="simulated disk full")
        self.assertFalse(target.exists())
        self.assertFalse(list(self.root.glob(".prioritize-*.tmp")))

    @unittest.skipUnless(os.name == "nt", "Windows final-path creation semantics")
    def test_windows_link_created_at_commit_is_preserved_without_following(self):
        target = self.root / "outside.json"
        destination = self.root / "report.json"
        try:
            destination.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation unavailable on this platform")
        destination.unlink()
        rename = os.rename
        def race(source, final):
            destination.symlink_to(target)
            return rename(source, final)
        with mock.patch.object(self.mod.os, "rename", side_effect=race):
            self.rejected(args=("--output", str(destination)), message="exists")
        self.assertTrue(destination.is_symlink())
        self.assertFalse(target.exists())
        self.assertFalse(list(self.root.glob(".prioritize-*.tmp")))

    @unittest.skipUnless(os.name == "nt", "Windows final-path creation semantics")
    def test_windows_competing_report_wins_without_being_replaced(self):
        destination = self.root / "report.json"
        competitor = self.root / "competing.tmp"
        competitor.write_bytes(b"completed competing report")
        rename = os.rename
        def race(source, final):
            rename(competitor, final)
            return rename(source, final)
        with mock.patch.object(self.mod.os, "rename", side_effect=race):
            self.rejected(args=("--output", str(destination)), message="exists")
        self.assertEqual(destination.read_bytes(), b"completed competing report")
        self.assertFalse(competitor.exists())
        self.assertFalse(list(self.root.glob(".prioritize-*.tmp")))

    def test_invalid_input_does_not_create_output(self):
        target = self.root / "never-created.json"
        self.rejected(document([item(dependencies=["missing"])]),
                      args=("--output", str(target)), message="missing dependency")
        self.assertFalse(target.exists())

    def test_oversized_invalid_utf8_and_nested_input_rejected(self):
        self.rejected(raw=" " * (1024 * 1024 + 1), message="1 MiB")
        self.rejected(raw="[" * 2000 + "]" * 2000, message="")
        source = self.root / "bytes.json"; source.write_bytes(b"\xff\xfe")
        proc = subprocess.run([sys.executable, "-B", str(TOOL), "--input", str(source)],
                              capture_output=True, timeout=5)
        self.assertEqual((proc.returncode, proc.stdout), (2, b""))
        self.assertIn(b"UTF-8", proc.stderr)

    def test_non_regular_input_rejected_without_blocking(self):
        paths = [self.root]
        if hasattr(os, "mkfifo"):
            fifo = self.root / "pipe.json"; os.mkfifo(fifo); paths.append(fifo)
        for path in paths:
            proc = subprocess.run([sys.executable, "-B", str(TOOL), "--input", str(path)],
                                  capture_output=True, timeout=5)
            self.assertEqual((proc.returncode, proc.stdout), (2, b""))
            self.assertIn(b"regular file", proc.stderr)

    def test_real_cli_success_and_usage_error(self):
        path = self.root / "input.json"; path.write_text(json.dumps(document()))
        proc = subprocess.run([sys.executable, "-B", str(TOOL), "--input", str(path)],
                              capture_output=True, text=True, timeout=5)
        self.assertEqual((proc.returncode, proc.stderr), (0, ""))
        self.assertEqual(json.loads(proc.stdout)["selected_order"], ["alpha"])
        bad = subprocess.run([sys.executable, "-B", str(TOOL), "--input", str(path),
                              "--format", "xlsx"], capture_output=True, text=True, timeout=5)
        self.assertEqual((bad.returncode, bad.stdout), (2, ""))


if __name__ == "__main__":
    unittest.main()
