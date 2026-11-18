"""H11: existing-engine five-door source integration, never native activation."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from muse_presets.public_export import PublicExportError, select_public_files

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "kits" / "engineering-doors"
SOURCE_ENGINE = ROOT / "presets/software-engineer/runtime/claim-gate/engineering_workflow.py"
DEMO = ROOT / "examples/five_door_offline_demo.py"
STAGES = ["S1", "S2", "S3", "S4", "S5"]
LANES = [
    "controller", "connection_presentation", "games",
    "seam_testing", "qualification",
]
REQUIRED = {
    "kits/engineering-doors/README.md",
    "kits/engineering-doors/manifest.json",
    "kits/engineering-doors/stage-routes.json",
}
ENGINE_PIN = "467b69836e3b08b189f2635388854563ad2b758ff7fca66705688326408b79a4"
ORIGINAL_PIN = "20af2111089774f23a4c8ac5737d868f5ceeb4e08fdeae93adc9e748f7fb0b19"


class FiveDoorSourceTests(unittest.TestCase):
    def test_five_lanes_five_ordered_stages_and_real_source_pins(self):
        manifest = json.loads((KIT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema"], "muse-hub/five-door-source-contract/v1")
        self.assertEqual(manifest["stage_order"], STAGES)
        self.assertEqual(manifest["lanes"], LANES)
        self.assertEqual(manifest["original_local_entrypoint_count"], 25)
        self.assertEqual(manifest["original_doorctl_sha256"], ORIGINAL_PIN)
        self.assertEqual(manifest["existing_engine_path"], SOURCE_ENGINE.relative_to(ROOT).as_posix())
        self.assertEqual(manifest["existing_engine_sha256"], ENGINE_PIN)
        self.assertEqual(hashlib.sha256(SOURCE_ENGINE.read_bytes()).hexdigest(), ENGINE_PIN)
        for name in ("native_muse_activated", "external_effect_authorized",
                     "shared_source_writes_enabled", "original_controller_replaced",
                     "independent_host_authenticated", "production_taskguard_fixed",
                     "production_retention_witness_proven", "publication_authorized"):
            self.assertIs(manifest[name], False, name)
        self.assertEqual(manifest["source_grade"], "PINNED_OFFLINE_CONTRACT_ONLY")
        self.assertIn("UNKNOWN_EFFECT_HOLD", manifest["stop_states"])

    def test_route_matrix_is_exact_25_and_all_hub_actions_source_only(self):
        routes = json.loads((KIT / "stage-routes.json").read_text(encoding="utf-8"))
        self.assertEqual(routes["schema"], "muse-hub/five-door-stage-routes/v1")
        self.assertEqual(routes["stage_order"], STAGES)
        self.assertEqual(routes["original_commands"], ["status", "select", "run"])
        values = routes["routes"]
        self.assertEqual(len(values), 25)
        self.assertEqual(set(values), {f"{lane}.{s}" for lane in LANES for s in STAGES})
        for lane in LANES:
            for stage in STAGES:
                with self.subTest(route=(lane,stage)):
                    row = values[f"{lane}.{stage}"]
                    self.assertEqual(row["lane"], lane)
                    self.assertEqual(row["stage"], stage)
                    self.assertEqual(row["mode"], "SOURCE_CONTRACT_ONLY_NO_ORIGINAL_INVOKE")
                    self.assertIs(row["hub_shared_source_mutation_authorized"], False)
                    self.assertIs(row["native_tool_registered"], False)
                    self.assertEqual(row["original_controller_may_apply"],
                                     lane == "controller" and stage == "S3")
        self.assertEqual(routes["phase_to_stage"], {
            "research": "S1", "reproduce": "S2", "implement": "S3",
            "regression": "S4", "verify": "S5",
        })
        body = (KIT / "stage-routes.json").read_text(encoding="utf-8")
        self.assertNotIn("/home/hatch", body)
        self.assertNotIn("chat_hint", body)

    def test_disposable_real_red_cas_green_independent_local_reopen(self):
        self.assertTrue(DEMO.is_file())
        with tempfile.TemporaryDirectory(prefix="muse-h11-e2e-") as d:
            path = Path(d) / "source-fixture"
            env = dict(os.environ, PYTHONPATH=str(ROOT / "src"),
                       PYTHONDONTWRITEBYTECODE="1")
            cmd = [sys.executable, "-B", str(DEMO), "--to", str(path)]
            proc = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True,
                                  text=True, timeout=90)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            evidence = json.loads(proc.stdout)
            self.assertEqual(evidence["status"],
                             "LOCAL_FIVE_DOOR_REVIEW_PASS_NOT_NATIVE")
            self.assertEqual([x["stage"] for x in evidence["stages"]], STAGES)
            self.assertEqual(evidence["stages"][1]["test_exit_code"], 1)
            self.assertEqual(evidence["stages"][3]["test_exit_code"], 0)
            self.assertEqual(evidence["stages"][3]["tests_run"], 4)
            self.assertEqual(evidence["stages"][4]["verdict"], "REVIEW_PASS")
            for key in ("native_muse_invoked", "external_effect_authorized",
                        "original_controller_invoked", "independent_identity_authenticated",
                        "os_sandboxed", "original_taskguard_released"):
                self.assertIs(evidence[key], False)
            self.assertTrue((path / "work" / "candidate.json").is_file())
            self.assertTrue((path / "review" / "REVIEW.json").is_file())
            self.assertTrue((path / "engine" / "runtime" / "claim-gate" /
                             "engineering_workflow.py").is_file())
            candidate = (path / "work" / "candidate.json").read_bytes()
            self.assertEqual(evidence["stages"][4]["candidate_sha256"],
                             hashlib.sha256(candidate).hexdigest())
            reviewer = json.loads((path / "review" / "REVIEW.json").read_text())
            self.assertEqual(reviewer["candidate_sha256"],
                             evidence["stages"][4]["candidate_sha256"])
            self.assertIs(reviewer["identity_authenticated"], False)
            before = hashlib.sha256(candidate).hexdigest()
            repeat = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True,
                                    text=True, timeout=15)
            self.assertNotEqual(repeat.returncode, 0)
            self.assertEqual(hashlib.sha256(candidate).hexdigest(), before)
            self.assertEqual(hashlib.sha256((path / "work" / "candidate.json").read_bytes()).hexdigest(), before)

    def test_original_engine_fails_closed_for_unknown_effect_and_tampered_preimage(self):
        self.assertTrue(DEMO.is_file())
        sys.path.insert(0, str(ROOT / "examples"))
        try:
            from five_door_offline_demo import accept_workflow_result
        finally:
            sys.path.pop(0)
        with self.assertRaisesRegex(ValueError, "UNKNOWN_OR_INCOMPLETE"):
            accept_workflow_result({"status": "UNKNOWN_EFFECT_HOLD"})
        with self.assertRaisesRegex(ValueError, "UNKNOWN_OR_INCOMPLETE"):
            accept_workflow_result({"status": "RED_NOT_REPRODUCED"})
        with self.assertRaises(ValueError):
            accept_workflow_result({
                "status": "GREEN_TESTED",
                "native_muse_invoked": True,
                "external_effect_authorized": False,
            })

    def test_public_export_remains_exact_allowlist(self):
        selected = select_public_files(ROOT, verify_manifest=False)
        self.assertTrue(REQUIRED.issubset(selected))
        with tempfile.TemporaryDirectory(prefix="h11-export-negative-") as d:
            root = Path(d)
            (root / "kits/engineering-doors").mkdir(parents=True)
            for name in REQUIRED:
                (root / name).write_text("reviewed-only", encoding="utf-8")
            self.assertEqual(set(select_public_files(root, verify_manifest=False)), REQUIRED)
            (root / "kits/engineering-doors/private-receipts.json").write_text(
                '{"owner":"private"}', encoding="utf-8"
            )
            with self.assertRaisesRegex(PublicExportError, "UNAPPROVED_COLLECTION_PATH"):
                select_public_files(root, verify_manifest=False)

    def test_run_guide_describes_actual_workflow_and_recovery(self):
        readme = (KIT / "README.md").read_text(encoding="utf-8")
        for term in ("five_door_offline_demo.py", "Python 3.12+", "Git",
                     "Windows PowerShell", "Capture", "Reproduce", "Repair",
                     "Check", "Review", "manifest.json", "stage-routes.json"):
            self.assertIn(term, readme)
        self.assertIn("inspect the original operation before repeating it", readme)
        self.assertIn("separate process", readme)
        docs = (ROOT / "docs/README.md").read_text(encoding="utf-8")
        self.assertIn("WORKFLOWS.md", docs)
        workflows = (ROOT / "docs/WORKFLOWS.md").read_text(encoding="utf-8")
        self.assertIn("software_engineer_workflow_demo.py", workflows)


if __name__ == "__main__":
    unittest.main()
