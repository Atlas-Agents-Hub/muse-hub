# H11 — Five-door engineering: source-pinned, non-native kit

**Status:** Tested local source contract only, **NOT** an installed Muse skill, original donor door, production writer or host permission. No original owner's data, conversation IDs or credentials are copied into this public kit.

## Original custody and ownership

A read-only inspection of the original owner-controlled five-seam system confirmed its `doorctl.py` at SHA-256 `20af2111089774f23a4c8ac5737d868f5ceeb4e08fdeae93adc9e748f7fb0b19` and **25 local wrapper files**, arranged as five original technical lanes × S1–S5. The original controller is the **sole shared-source writer**. All other lanes can reproduce, prepare proposals or witness; their S3 is proposal-only. This public source contract does not install those 25 wrappers.

See [source/provenance and authority flags](manifest.json) and [25 stage-route projections](stage-routes.json). These route names are labels from the original controller, not callable Hub endpoints. Original verbs: `status`, `select`, `run`. Phase routing: `research → S1`, `reproduce → S2`, `implement → S3`, `regression → S4`, `verify → S5`. This repository **never invokes** the original private VM controller.

## What actually runs locally — the existing Claim Gate workflow

The existing `presets/software-engineer/runtime/claim-gate/engineering_workflow.py` runs a **disposable, reviewed synthetic repair** with the already implemented Claim Gate. The H11 demo composes its original `execute` and `review` operations without creating a competing authority.

| Seam | Observable local evidence | Limit |
| --- | --- | --- |
| S1 Blackbox | Frozen synthetic case and source preimage SHA-256, source-pinned engine | Local source, not owner snapshot |
| S2 Triage | Actual test subprocess reproduces expected RED and exit 1 | One reviewed fictional defect |
| S3 Owner repair | Original workflow checks preimage SHA and patches its own *new disposable* Git tree | No access to original shared source |
| S4 Failures | Original workflow reruns 4 tests with GREEN exit 0, checks source, freezes candidate | No external effects |
| S5 Skills/witness | Original workflow `review` runs in a separate local subprocess, repeats RED→GREEN, reopens source and receipt | Separate process **not** authenticated different host/person |

The source demonstration is deliberately narrower than the original owner's 25 runtime wrappers.

From a reviewed checkout with Python 3.12+ and Git:

```sh
PYTHONPATH=src python -B examples/five_door_offline_demo.py
PYTHONPATH=src python -B examples/five_door_offline_demo.py --to /absolute/NEW-disposable-output
PYTHONPATH=src python -B -m unittest discover -s tests -p test_h11_engineering_doors.py -v
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` first. The `--to` destination is **create-only**, and a prior or interrupted operation is preserved, not replayed. The only executable case is the frozen, reviewed `clamp` fixture; **Python execution is not an OS sandbox**.

A passing local case reports `LOCAL_FIVE_DOOR_REVIEW_PASS_NOT_NATIVE`, S2 RED, S3 scoped preimage-checked repair, S4 GREEN and S5 `REVIEW_PASS`. Original controller invocation, native model, authenticated recipient, effect authorization and original TaskGuard release all remain false.

## Security and acceptance gates

Stop on `UNKNOWN_EFFECT_HOLD`, absent RED, changed source/candidate hash, ambiguous subprocess status, or missing/tampered S5 receipt. Do not retry an uncertain effect simply to get GREEN. The existing Claim Gate remains the only local case/claim authority.

The original owner's TaskGuard **release-before-terminal** and independent retention-witness **P1 holds remain OPEN**; this H11 kit does not modify or repair those original production defects. Live H11 acceptance would require an owner-scoped controller action, authenticated other-lane S5 witness, independent receipt readback, and durable fencing. No local source receipt grants that authority.
