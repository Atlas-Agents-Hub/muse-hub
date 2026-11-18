"""Exercise shipped library helpers with known answers and invalid inputs.

Each helper is copied to a temporary workspace and executed in a separate
Python process. The repository's helper modules are never imported by test
discovery. Tests compare computed facts and preserve source and input bytes.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "collections/library"


def hashes(directory: Path) -> dict[str, str]:
    return {
        path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in directory.rglob("*") if path.is_file()
    }


class LibraryToolExamples(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="muse-library-example-")
        self.addCleanup(temporary.cleanup)
        self.workspace = Path(temporary.name)

    def copy_skill(self, skill_id: str) -> Path:
        catalog = json.loads((LIBRARY / "catalog.json").read_text(encoding="utf-8"))
        rows = [row for row in catalog["skills"] if row["id"] == skill_id]
        self.assertEqual(len(rows), 1, skill_id)
        source = LIBRARY / rows[0]["path"]
        before = hashes(source)
        self.addCleanup(lambda: self.assertEqual(before, hashes(source), "Repository source changed"))
        destination = self.workspace / skill_id
        shutil.copytree(source, destination)
        return destination

    def run_helper(self, work: Path, script: str, *args: str) -> subprocess.CompletedProcess:
        before = hashes(work)
        environment = {
            key: os.environ[key] for key in ("PATH", "SYSTEMROOT", "WINDIR") if key in os.environ
        }
        environment.update({"HOME": str(self.workspace), "USERPROFILE": str(self.workspace)})
        result = subprocess.run(
            [sys.executable, "-I", "-B", script, *args],
            cwd=work, env=environment, capture_output=True, text=True, timeout=20,
        )
        after = hashes(work)
        for name, digest in before.items():
            self.assertEqual(after.get(name), digest, f"Helper modified its source or input: {name}")
        return result

    def rag_api(self, body: str) -> dict:
        work = self.copy_skill("rag-architect")
        runner = work / "probe.py"
        runner.write_text(
            "import contextlib, io, json, runpy\n"
            "with contextlib.redirect_stdout(io.StringIO()):\n"
            "    module = runpy.run_path('retrieval_evaluator.py')\n"
            + textwrap.indent(textwrap.dedent(body).strip() + "\n", "    ")
            + "print(json.dumps(result, sort_keys=True, allow_nan=False))\n",
            encoding="utf-8",
        )
        result = self.run_helper(work, "probe.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def rag_inputs(self, work: Path) -> None:
        (work / "queries.json").write_text('[{"id":"q","query":"apple"}]', encoding="utf-8")
        (work / "truth.json").write_text('{"q":["apple"]}', encoding="utf-8")
        (work / "corpus").mkdir()
        (work / "corpus/apple.txt").write_text("apple pear", encoding="utf-8")
        (work / "corpus/other.txt").write_text("orange", encoding="utf-8")

    def test_retrieval_metrics_penalize_unfilled_result_slots(self):
        report = self.rag_api("""
            class FixedResults:
                def search(self, query, k):
                    return [('a', 1.0)]
            result = module['RetrievalEvaluator']().evaluate(
                [{'id': 'q', 'query': 'apple'}], {'q': ['a', 'b']}, FixedResults(), [2])
        """)
        metrics = report["aggregate_metrics"]
        self.assertEqual(metrics["mean_precision@2"], 0.5)
        self.assertEqual(metrics["mean_recall@2"], 0.5)
        self.assertEqual(metrics["mean_reciprocal_rank"], 1.0)
        self.assertAlmostEqual(metrics["mean_ndcg@2"], 1 / (1 + 1 / math.log2(3)))

    def test_retrieval_metrics_use_rank_and_relevance(self):
        report = self.rag_api("""
            class FixedResults:
                def search(self, query, k):
                    return [('irrelevant', 0.9), ('a', 0.8), ('b', 0.7)][:k]
            result = module['RetrievalEvaluator']().evaluate(
                [{'id': 'q', 'query': 'apple'}], {'q': ['a', 'b']}, FixedResults(), [1, 2, 3])
        """)
        metrics = report["aggregate_metrics"]
        self.assertEqual(metrics["mean_precision@1"], 0)
        self.assertEqual(metrics["mean_recall@1"], 0)
        self.assertEqual(metrics["mean_precision@2"], 0.5)
        self.assertAlmostEqual(metrics["mean_precision@3"], 2 / 3)
        self.assertEqual(metrics["mean_recall@3"], 1)
        self.assertEqual(metrics["mean_reciprocal_rank"], 0.5)
        self.assertAlmostEqual(metrics["mean_ndcg@3"], (1 / math.log2(3) + 0.5) / (1 + 1 / math.log2(3)))

    def test_retrieval_zero_results_has_zero_metrics(self):
        report = self.rag_api("""
            class FixedResults:
                def search(self, query, k):
                    return []
            result = module['RetrievalEvaluator']().evaluate(
                [{'id': 'q', 'query': 'apple'}], {'q': ['a']}, FixedResults(), [1, 2])
        """)
        self.assertTrue(all(value == 0 for value in report["aggregate_metrics"].values()))
        self.assertEqual(report["failure_analysis"]["zero_results_count"], 1)

    def test_tfidf_uses_complete_document_norm(self):
        result = self.rag_api("""
            document = module['Document']
            retriever = module['TFIDFRetriever']([
                document('dilute', 'dilute', 'apple pear plum mango'),
                document('focused', 'focused', 'apple'),
                document('unrelated', 'unrelated', 'orange'),
            ])
            result = dict(retriever.search('apple', 3))
        """)
        self.assertEqual(set(result), {"focused", "dilute"})
        self.assertAlmostEqual(result["focused"], 1)
        expected = math.log(1.5) / math.sqrt(math.log(1.5) ** 2 + 3 * math.log(3) ** 2)
        self.assertAlmostEqual(result["dilute"], expected)
        self.assertGreater(result["focused"], result["dilute"])

    def test_retrieval_cli_rejects_nonpositive_cutoffs_without_report(self):
        work = self.copy_skill("rag-architect")
        self.rag_inputs(work)
        for cutoff in ("0", "-1"):
            with self.subTest(cutoff=cutoff):
                result = self.run_helper(work, "retrieval_evaluator.py", "queries.json", "corpus",
                                         "truth.json", "--k-values", cutoff, "--output", "report.json")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("positive integer", result.stdout + result.stderr)
                self.assertFalse((work / "report.json").exists())

    def test_retrieval_cli_rejects_duplicate_document_ids(self):
        work = self.copy_skill("rag-architect")
        self.rag_inputs(work)
        (work / "corpus/nested").mkdir()
        (work / "corpus/nested/apple.txt").write_text("different document", encoding="utf-8")
        result = self.run_helper(work, "retrieval_evaluator.py", "queries.json", "corpus",
                                 "truth.json", "--output", "report.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Document IDs must be unique", result.stdout + result.stderr)
        self.assertFalse((work / "report.json").exists())

    def test_csv_profile_reports_counts_statistics_and_measured_completeness(self):
        work = self.copy_skill("data-quality-auditor")
        (work / "input.csv").write_text("score,label\n10,a\n20,a\n,b\n40,c\n", encoding="utf-8")
        result = self.run_helper(work, "scripts/data_profiler.py", "--file", "input.csv", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["total_rows"], 4)
        score, label = report["columns"]
        self.assertEqual((score["null_count"], score["non_null_count"], score["unique_count"]), (1, 3, 3))
        self.assertEqual((score["min"], score["max"], score["mean"], score["std"]), (10, 40, 23.3333, 15.2753))
        self.assertEqual(label["unique_count"], 3)
        self.assertEqual(report["dqs"], {"score": 87.5, "score_name": "completeness", "dimensions": {"completeness": 87.5}})

    def test_csv_single_numeric_value_has_no_sample_standard_deviation(self):
        work = self.copy_skill("data-quality-auditor")
        (work / "input.csv").write_text("value\n7\n", encoding="utf-8")
        result = self.run_helper(work, "scripts/data_profiler.py", "--file", "input.csv", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        profile = json.loads(result.stdout)["columns"][0]
        self.assertEqual(profile["mean"], 7)
        self.assertIsNone(profile["std"])

    def test_csv_nonfinite_values_are_reported_without_invalid_json_numbers(self):
        work = self.copy_skill("data-quality-auditor")
        (work / "input.csv").write_text("value\n1\ninf\n-inf\n", encoding="utf-8")
        result = self.run_helper(work, "scripts/data_profiler.py", "--file", "input.csv", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        def reject_constant(value):
            raise AssertionError(f"Non-JSON numeric constant: {value}")
        profile = json.loads(result.stdout, parse_constant=reject_constant)["columns"][0]
        self.assertEqual(profile["nonfinite_count"], 2)
        self.assertNotIn("mean", profile)

    def test_csv_short_rows_count_missing_cells(self):
        work = self.copy_skill("data-quality-auditor")
        (work / "input.csv").write_text("a,b\n1,2\n3\n", encoding="utf-8")
        result = self.run_helper(work, "scripts/data_profiler.py", "--file", "input.csv", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["columns"][1]["null_count"], 1)
        self.assertEqual(report["dqs"]["score"], 75)

    def test_csv_rejects_ambiguous_headers_extra_fields_and_unknown_columns(self):
        work = self.copy_skill("data-quality-auditor")
        for text, extra_args, message in (
            ("value,value\n1,2\n", (), "must be unique"),
            ("value\n1,2\n", (), "more fields"),
            ("value\n1\n", ("--columns", "missing"), "columns not found"),
            ("value\n", (), "no data rows"),
        ):
            with self.subTest(message=message):
                (work / "input.csv").write_text(text, encoding="utf-8")
                result = self.run_helper(work, "scripts/data_profiler.py", "--file", "input.csv", "--format", "json", *extra_args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(result.stdout, "")

    def design_matrix(self, work: Path, rows: str, *args: str) -> tuple[int, dict]:
        (work / "matrix.csv").write_text("surface,kind,state,status,evidence,note\n" + rows, encoding="utf-8")
        result = self.run_helper(work, "scripts/state_matrix_checker.py", "--matrix", "matrix.csv", "--output", "json", *args)
        self.assertNotIn("Traceback", result.stderr)
        return result.returncode, json.loads(result.stdout)

    def test_design_state_matrix_accepts_complete_evidenced_page(self):
        work = self.copy_skill("design-qa")
        code, report = self.design_matrix(work,
            "Page,page,narrow_320,DONE,test:reflow,\n"
            "Page,page,wide_1440,DONE,test:wide,\n"
            "Page,page,long_content,DONE,test:long,\n")
        self.assertEqual(code, 0)
        self.assertEqual(report["verdict"], "COMPLETE")
        self.assertEqual(report["coverage_pct"], 100)
        self.assertEqual(report["findings"], [])

    def test_design_state_matrix_reports_missing_reflow_as_blocking(self):
        work = self.copy_skill("design-qa")
        code, report = self.design_matrix(work,
            "Page,page,wide_1440,DONE,test:wide,\n"
            "Page,page,long_content,DONE,test:long,\n")
        self.assertEqual(code, 4)
        self.assertEqual(report["verdict"], "BLOCKED")
        self.assertEqual(report["counts"]["BLOCKER"], 1)
        finding = report["findings"][0]
        self.assertEqual((finding["state"], finding["code"]), ("narrow_320", "MISSING_BLOCKING"))

    def test_design_state_matrix_rejects_duplicate_states_even_when_they_agree(self):
        work = self.copy_skill("design-qa")
        for previous in ("MISSING", "DONE"):
            with self.subTest(previous=previous):
                code, report = self.design_matrix(work,
                    f"Page,page,narrow_320,{previous},test:first,\n"
                    "Page,page,narrow_320,DONE,test:second,\n"
                    "Page,page,wide_1440,DONE,test:wide,\n"
                    "Page,page,long_content,DONE,test:long,\n")
                self.assertEqual(code, 3)
                self.assertEqual(report["verdict"], "INVALID_INPUT")
                self.assertIn("duplicate state", " ".join(report["errors"]))

    def test_design_state_matrix_rejects_unknown_status(self):
        work = self.copy_skill("design-qa")
        code, report = self.design_matrix(work, "Page,page,narrow_320,BROKEN,test:reflow,\n")
        self.assertEqual(code, 3)
        self.assertEqual(report["verdict"], "INVALID_INPUT")
        self.assertIn("unknown status", " ".join(report["errors"]))

    def test_design_state_matrix_reports_missing_evidence_file(self):
        work = self.copy_skill("design-qa")
        code, report = self.design_matrix(work,
            "Page,page,narrow_320,DONE,shots/reflow.png,\n"
            "Page,page,wide_1440,DONE,test:wide,\n"
            "Page,page,long_content,DONE,test:long,\n", "--evidence-root", ".")
        self.assertEqual(code, 2)
        self.assertEqual(report["verdict"], "FINDINGS")
        self.assertEqual(report["findings"][0]["code"], "EVIDENCE_NOT_FOUND")

    def test_database_sample_preserves_all_declared_indexes(self):
        work = self.copy_skill("database-designer")
        result = self.run_helper(work, "schema_analyzer.py", "--input", "assets/sample_schema.json",
                                 "--output-format", "json", "--generate-erd")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["schema_overview"], {
            "total_tables": 6, "total_columns": 41, "tables_with_primary_keys": 6,
            "total_foreign_keys": 7, "total_indexes": 17,
        })
        self.assertIn("erDiagram", report["mermaid_erd"])

    def test_database_existing_foreign_key_index_is_not_reported_missing(self):
        work = self.copy_skill("database-designer")
        schema = {"tables": {
            "users": {"columns": {"id": {"type": "INTEGER"}}, "primary_key": ["id"]},
            "orders": {"columns": {
                "id": {"type": "INTEGER"},
                "user_id": {"type": "INTEGER", "foreign_key": "users.id"},
            }, "primary_key": ["id"], "indexes": [{"name": "idx_orders_user", "columns": ["USER_ID"]}]},
        }}
        (work / "input.json").write_text(json.dumps(schema), encoding="utf-8")
        result = self.run_helper(work, "schema_analyzer.py", "--input", "input.json", "--output-format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["schema_overview"]["total_indexes"], 1)
        self.assertEqual(report["missing_indexes"], [])
        schema["tables"]["orders"]["indexes"] = []
        (work / "input.json").write_text(json.dumps(schema), encoding="utf-8")
        result = self.run_helper(work, "schema_analyzer.py", "--input", "input.json", "--output-format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        missing = json.loads(result.stdout)["missing_indexes"]
        self.assertEqual([(row["table"], row["column"]) for row in missing], [("orders", "user_id")])

    def test_database_rejects_indexes_that_reference_missing_columns(self):
        work = self.copy_skill("database-designer")
        schema = {"tables": {"users": {
            "columns": {"id": {"type": "INTEGER"}}, "primary_key": ["id"],
            "indexes": [{"name": "idx_missing", "columns": ["missing"]}],
        }}}
        (work / "input.json").write_text(json.dumps(schema), encoding="utf-8")
        result = self.run_helper(work, "schema_analyzer.py", "--input", "input.json",
                                 "--output-format", "json", "--output", "report.json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown columns: missing", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertFalse((work / "report.json").exists())

    def test_tool_schemas_keep_required_fields_at_the_correct_object_level(self):
        work = self.copy_skill("agent-designer")
        tools = {"tools": [{
            "name": "lookup", "purpose": "Look up a record", "category": "data",
            "inputs": [
                {"name": "query", "type": "string", "required": True},
                {"name": "options", "type": "object", "required": True,
                 "properties": {"limit": {"type": "integer", "minimum": 1}},
                 "required_properties": ["limit"], "additional_properties": False},
            ], "outputs": [], "error_conditions": [], "side_effects": [],
            "idempotent": True, "rate_limits": {}, "dependencies": [],
            "examples": [], "security_requirements": [],
        }]}
        (work / "tools.json").write_text(json.dumps(tools), encoding="utf-8")
        result = self.run_helper(work, "tool_schema_generator.py", "tools.json", "-o", "schemas")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        tool = json.loads((work / "schemas.json").read_text(encoding="utf-8"))["tool_schemas"][0]
        for schema in (tool["openai_schema"]["parameters"], tool["anthropic_schema"]["input_schema"]):
            self.assertEqual(schema["required"], ["query", "options"])
            self.assertNotIn("required", schema["properties"]["query"])
            options = schema["properties"]["options"]
            self.assertEqual(options["required"], ["limit"])
            self.assertEqual(options["properties"]["limit"], {"type": "integer", "minimum": 1})
            self.assertFalse(options["additionalProperties"])

    def test_tool_schemas_sample_has_valid_required_array_shapes(self):
        work = self.copy_skill("agent-designer")
        # Exercise Windows' default console encoding even on UTF-8 Linux runners.
        # A per-process wrapper preserves isolated mode and the input's contents.
        (work / "cp1252_schema_runner.py").write_text(
            "import runpy, sys\n"
            "sys.stdout.reconfigure(encoding='cp1252', errors='strict')\n"
            "sys.stderr.reconfigure(encoding='cp1252', errors='strict')\n"
            "sys.argv[0] = 'tool_schema_generator.py'\n"
            "runpy.run_path('tool_schema_generator.py', run_name='__main__')\n",
            encoding="utf-8",
        )
        result = self.run_helper(work, "cp1252_schema_runner.py", "assets/sample_tool_descriptions.json",
                                 "--validate", "-o", "schemas")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS: Valid", result.stdout)
        for suffix in ("_openai", "_anthropic", "_validation", "_examples"):
            self.assertIsInstance(json.loads((work / f"schemas{suffix}.json").read_text(encoding="utf-8")), dict)
        schemas = json.loads((work / "schemas.json").read_text(encoding="utf-8"))["tool_schemas"]
        self.assertEqual(len(schemas), 5)
        def check_node(node):
            if isinstance(node, dict):
                if "required" in node:
                    self.assertIsInstance(node["required"], list)
                    self.assertTrue(all(isinstance(value, str) for value in node["required"]))
                for value in node.values():
                    check_node(value)
            elif isinstance(node, list):
                for value in node:
                    check_node(value)
        for tool in schemas:
            self.assertNotIn("generated_at", tool["metadata"])
            check_node(tool["openai_schema"]["parameters"])
            check_node(tool["anthropic_schema"]["input_schema"])

    def test_tool_schema_generator_rejects_invalid_json_without_output(self):
        work = self.copy_skill("agent-designer")
        (work / "tools.json").write_text('{"tools": [', encoding="utf-8")
        result = self.run_helper(work, "tool_schema_generator.py", "tools.json", "-o", "schemas")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Error:", result.stderr)
        self.assertFalse((work / "schemas.json").exists())


if __name__ == "__main__":
    unittest.main()
