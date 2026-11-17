"""Source-grounded H00–H21 readiness projections; never a task dispatcher."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/discovery/hub-feature-status.json"
README = ROOT / "docs/HUB_FEATURE_READINESS.md"
TITLES = (
    "Source and fleet preflight",
    "Rights and source catalog",
    "Public discovery experience",
    "258/402 route compatibility",
    "Personal Muse terminal",
    "Muse-to-local coding bridge",
    "Browser-operated MCP fallback",
    "Official gadget and TypeScript SDK",
    "Desktop Commander setup",
    "CUA Driver cross-host bridge",
    "Tailscale/local shell gateway",
    "Neutral five-door engineering workflow",
    "Neutral Family Link envelope",
    "Cross-role plan to selected transport",
    "Neutral Companion Home rooms",
    "Portable animation director",
    "Rights-reviewed Arcade",
    "Notebook persistence",
    "Apple Watch/Gadget expansion",
    "Installation and recovery journeys",
    "End-to-end gate with negative cases",
    "Distribution and release",
)
DEPS = (
    (), ("H00",), ("H01",), ("H00",), ("H03",), ("H00",),
    ("H02",), ("H02",), ("H02",), ("H08",), ("H08",),
    ("H00",), ("H00",), ("H04", "H05", "H09", "H12"),
    ("H00",), ("H14",), ("H14",), ("H14",), ("H07",),
    ("H02", "H05", "H08", "H11", "H12"),
    ("H13", "H14", "H16", "H17", "H19"), ("H20",),
)


def load():
    return json.loads(DOC.read_text(encoding="utf-8"))


class FeatureReadinessContract(unittest.TestCase):
    def test_exact_22_features_and_original_dependency_edges(self):
        record = load()
        self.assertEqual(record["schema"], "muse-hub/h00-h21-feature-readiness/v1")
        self.assertEqual(record["baseline_public_main"], "08a0b652fae4385abf32a03204ae58f45f9ea6e4")
        tasks = record["tasks"]
        self.assertEqual(len(tasks), 22)
        self.assertEqual([x["id"] for x in tasks], [f"H{i:02d}" for i in range(22)])
        self.assertEqual([x["title"] for x in tasks], list(TITLES))
        self.assertEqual([tuple(x["dependencies"]) for x in tasks], list(DEPS))
        for task in tasks:
            self.assertIn(task["priority"], ("P0", "P1", "P2"))
            self.assertTrue(task["minimum_acceptance"])
            self.assertTrue(task["next_verification"])
            self.assertTrue(task["evidence_status"])
            self.assertEqual(task["native_runtime_verified"], False)
            self.assertEqual(task["site_deployed"], False)
            self.assertNotEqual(task["status"], "COMPLETE")

    def test_prior_merges_and_H11_source_are_grounded_in_real_files(self):
        t = {x["id"]: x for x in load()["tasks"]}
        for id_, location in (
            ("H02", "hub/site/index.html"),
            ("H03", "tools/compare_muse_routes.py"),
            ("H11", "kits/engineering-doors/manifest.json"),
            ("H12", "kits/family-handoff/envelope-contract.json"),
        ):
            self.assertIn(location, t[id_]["source_paths"])
            self.assertTrue((ROOT / location).is_file(), location)
        self.assertEqual(t["H03"]["status"], "SOURCE_MERGED_CI_VERIFIED")
        self.assertEqual(t["H12"]["status"], "SOURCE_MERGED_NATIVE_NOT_VERIFIED")
        self.assertEqual(t["H11"]["status"], "SOURCE_ONLY_NATIVE_NOT_VERIFIED")

    def test_security_native_and_release_gates_cannot_turn_green_by_docs(self):
        record = load()
        gates = record["production_holds"]
        self.assertEqual({x["id"] for x in gates},
                         {"T12_TASKGUARD_TERMINAL", "T12_RETENTION_WITNESS",
                          "NATIVE_MUSE_AUTH", "H12_REAL_RECIPIENT"})
        self.assertTrue(all(x["status"] == "OPEN" for x in gates))
        self.assertIs(record["native_muse_account_invoked"], False)
        self.assertIs(record["new_public_release_published"], False)
        self.assertIs(record["standalone_muse_hub_site_published"], False)
        self.assertEqual(record["draft_release_tag"], "v1.1.0")
        tasks = {x["id"]: x for x in record["tasks"]}
        for key in ("H04", "H13", "H14", "H20", "H21"):
            self.assertIn(tasks[key]["status"], {
                "PROVIDER_BLOCKED", "NOT_VERIFIED", "PRIVATE_DONOR_NOT_HUB",
                "RELEASE_NOT_READY", "SOURCE_ONLY_INCOMPLETE",
                "SOURCE_IMPLEMENTED_NOT_NATIVE",
            })
        self.assertIn("NO_NATIVE_GRANTS", record["boundary_notes"])

    def test_reader_table_matches_exact_machine_readable_ids_and_statuses(self):
        text = README.read_text(encoding="utf-8")
        for row in load()["tasks"]:
            lines = [line for line in text.splitlines()
                     if line.startswith("| " + row["id"] + " |")]
            self.assertEqual(len(lines), 1, row["id"])
            self.assertIn(row["title"], lines[0])
            self.assertIn(row["status"], lines[0])
        self.assertIn("HUB_FEATURE_READINESS.md", (ROOT / "docs/README.md").read_text(encoding="utf-8"))
        self.assertIn("H11", text)
        self.assertIn("T12", text)
        self.assertIn("NOT", text)


if __name__ == "__main__":
    unittest.main()
