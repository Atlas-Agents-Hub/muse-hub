---
name: code-review
description: "A source diff needs an actionable correctness and maintainability review."
---

# Review a Change for Concrete Failure Paths

## Use when
A source diff needs an actionable correctness and maintainability review.

## Not for
Unrequested deployments, third-party intrusion, broad rewrites, or executing unreviewed downloaded scripts.

## Inputs
- The exact diff and intended behavior
- Relevant contracts, callers and tests

## Procedure
1. Read changed code together with its callers and invariants.
2. Trace boundary inputs, failure handling and state transitions.
3. Separate reproducible defects from preferences or speculative risks.
4. Propose a minimal reproducer and regression assertion for each material finding.
5. Return ranked findings with file locations and explicitly note uninspected areas.

## Deliver
- Prioritized source-bound findings
- Concrete regression suggestions

## Check the result
- Every defect finding has a plausible input-to-failure path.
- The review does not claim test execution without output.
- Style preferences do not obscure correctness risks.

## Recover or narrow
Preserve the original state and logs. Narrow the failing case, stop after the agreed attempt budget, and return a reproducible next step rather than a speculative broad change.

## Example request
Review this transaction patch for data-loss paths and show the smallest case for each genuine issue.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

