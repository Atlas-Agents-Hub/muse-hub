"""Run the engineering repair workflow against a reviewed clamp fixture.

The example uses a new temporary workspace and verifies each repair stage."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from muse_presets.workflow_fixture import fixture_case
from muse_presets.engineering_pack import inspect_engineer_pack
from software_engineer_workflow_demo import demonstrate

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "presets/software-engineer/runtime/claim-gate/engineering_workflow.py"
ENGINE_PIN = "467b69836e3b08b189f2635388854563ad2b758ff7fca66705688326408b79a4"
SCHEMA = "muse-hub/engineering-review-result/v1"


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _require(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)


def accept_workflow_result(report: object) -> dict:
    """Fail closed if RED/GREEN evidence or effect boundaries are missing."""
    if type(report) is not dict or report.get("status") != "LOCAL_ENGINEERING_WORKFLOW_GREEN":
        raise ValueError("UNKNOWN_OR_INCOMPLETE_WORKFLOW_RESULT")
    if report.get("native_muse_invoked") is not False or report.get("external_effect_authorized") is not False:
        raise ValueError("UNAUTHORIZED_EFFECT_CLAIM")
    if report.get("os_sandboxed") is not False or report.get("independent_review_status") != "PENDING_EXTERNAL_REVIEWS":
        raise ValueError("MISCLASSIFIED_SOURCE_REVIEW")
    data = report.get("workflow")
    if not isinstance(data, dict) or not (
        data.get("red_exit") == 1
        and data.get("green_exit") == 0
        and data.get("green_tests") == 4
        and isinstance(data.get("candidate_sha256"), str)
        and len(data["candidate_sha256"]) == 64
        and data.get("baseline_commit") != data.get("patched_commit")
        and data.get("patch_sha256")
    ):
        raise ValueError("UNKNOWN_OR_INCOMPLETE_WORKFLOW_RESULT")
    return data


def _load_manifest() -> dict:
    src = ENGINE
    if src.is_symlink() or not src.is_file() or _sha(src.read_bytes()) != ENGINE_PIN:
        raise ValueError("PINNED_ENGINE_SOURCE_MISMATCH")
    manifest = json.loads((ROOT / "kits/engineering-doors/manifest.json").read_text(encoding="utf-8"))
    if (
        manifest.get("schema") != "muse-hub/five-door-source-contract/v1"
        or manifest.get("existing_engine_sha256") != ENGINE_PIN
        or manifest.get("stage_order") != ["S1", "S2", "S3", "S4", "S5"]
        or manifest.get("shared_source_writes_enabled") is not False
        or manifest.get("external_effect_authorized") is not False
        or manifest.get("native_muse_activated") is not False
    ):
        raise ValueError("ENGINE_SOURCE_AUTHORITY_NOT_ADMITTED")
    return manifest


def run_offline_case(destination: Path) -> dict:
    _load_manifest()
    dest = Path(destination)
    # demonstrate() delegates safety checks and mutation to the existing
    # create-only engineering_pack / original workflow; no new writer.
    report = demonstrate(dest)
    work = accept_workflow_result(report)
    engine = dest / "engine"
    _require(inspect_engineer_pack(engine).get("status") == "LOCAL_MATCH", "STAGED_ENGINE_SOURCE_DRIFT")
    case = fixture_case()
    candidate_file = dest / "work/candidate.json"
    _require(candidate_file.is_file() and not candidate_file.is_symlink(), "CANDIDATE_MISSING")
    candidate_bytes = candidate_file.read_bytes()
    _require(_sha(candidate_bytes) == work["candidate_sha256"], "CANDIDATE_SOURCE_PIN_MISMATCH")
    candidate = json.loads(candidate_bytes)
    _require(candidate.get("case") == case and candidate.get("author_id") == "source-author",
             "CANDIDATE_CASE_DRIFT")
    pre = case["files"]["bounds.py"].encode("utf-8")
    post = case["patch"][0]["after_utf8"].encode("utf-8")
    patched_file = dest / "work/repo/bounds.py"
    _require(_sha(pre) == case["patch"][0]["before_sha256"], "PREIMAGE_SOURCE_MISMATCH")
    _require(_sha(patched_file.read_bytes()) == _sha(post), "S3_SOURCE_PATCH_DRIFT")
    cli = engine / "runtime/claim-gate/engineering_workflow.py"
    review_args = [
        sys.executable, "-I", "-B", str(cli), "review",
        "--candidate", str(candidate_file),
        "--candidate-sha256", work["candidate_sha256"],
        "--author", case["author_id"],
        "--reviewer", "independent-local-reviewer",
        "--to", str(dest / "review"),
        "--reviewed-code",
    ]
    proc = subprocess.run(review_args, cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=90)
    if proc.returncode != 0:
        raise ValueError("S5_LOCAL_REVIEW_FAILED:" + proc.stderr[-300:])
    verdict = json.loads(proc.stdout)
    reopened = json.loads((dest / "review/REVIEW.json").read_text(encoding="utf-8"))
    _require(verdict == reopened and reopened.get("verdict") == "REVIEW_PASS",
             "S5_REVIEW_WITNESS_DRIFT")
    _require(reopened.get("candidate_sha256") == work["candidate_sha256"]
             and reopened.get("replayed_green_tests") == 4
             and reopened.get("replayed_red_failures") == [case["expected_failures"][0]],
             "S5_REVIEW_NOT_REPRODUCED")
    _require(reopened.get("identity_authenticated") is False
             and reopened.get("native_muse_invoked") is False
             and reopened.get("external_effect_authorized") is False,
             "S5_FALSE_NATIVE_AUTHORITY")
    _require(_sha(candidate_file.read_bytes()) == work["candidate_sha256"],
             "S5_CANDIDATE_CHANGED_ON_REOPEN")
    return {
        "schema": SCHEMA,
        "status": "ENGINEERING_REVIEW_PASSED",
        "stages": [
            {"stage": "S1", "status": "SOURCE_CAPTURED_LOCAL",
             "source_sha256": _sha(pre), "candidate_case_sha256": candidate["case_sha256"]},
            {"stage": "S2", "status": "RED_REPRODUCED",
             "test_exit_code": work["red_exit"],
             "expected_failure": work["original_failure"]},
            {"stage": "S3", "status": "CAS_SCOPED_DISPOSABLE_REPAIR",
             "preimage_sha256": _sha(pre), "after_sha256": _sha(post),
             "patch_sha256": work["patch_sha256"]},
            {"stage": "S4", "status": "GREEN_TESTED",
             "test_exit_code": work["green_exit"], "tests_run": work["green_tests"]},
            {"stage": "S5", "status": "REPLAYED_IN_SEPARATE_LOCAL_PROCESS",
             "verdict": "REVIEW_PASS", "candidate_sha256": work["candidate_sha256"],
             },
        ],
        "external_effect_authorized": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--to", type=Path,
                        help="new disposable directory for preserving the entire review trail")
    args = parser.parse_args(argv)
    try:
        if args.to is not None:
            output = run_offline_case(args.to)
        else:
            with tempfile.TemporaryDirectory(prefix="engineering-review-") as temp:
                output = run_offline_case(Path(temp) / "fixture")
        print(json.dumps(output, sort_keys=True))
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(json.dumps({
            "status": "REFUSED_OR_UNKNOWN",
            "reason": type(exc).__name__ + ":" + str(exc)[:240],
                "external_effect_authorized": False,
        }, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
