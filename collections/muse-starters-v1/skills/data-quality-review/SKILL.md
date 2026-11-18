---
name: data-quality-review
description: "A cleaning or migration step may change the meaning or completeness of records."
---

# Test Data Transformations Against Explicit Invariants

## Use when
A cleaning or migration step may change the meaning or completeness of records.

## Not for
Manufacturing missing observations, silently changing data definitions, or reporting unrun experiments as measured.

## Inputs
- The original and transformed data
- The intended transformation and invariant rules

## Procedure
1. Read the actual transformation and source contract, including keys, business version, deletion semantics and permitted scope.
2. Capture immutable before-state evidence and define invariants appropriate to the operation, not merely a generic row count.
3. Exercise normal, duplicate, late-arriving, conflicting and empty-window cases using authorized fixtures or supplied records.
4. Check that newer source versions supersede older ones and identical replays do not create duplicate effects.
5. Verify that aggregate refreshes replace the exact intended window, including an empty result, while preserving outside partitions.
6. Report discrepancies and repair the smallest transformation boundary, then rerun the violated invariant and unaffected controls.

## Deliver
- A transformation reconciliation
- A reusable invariant checklist
- Deliver the transformation contract, before/after invariant results, exact discrepant keys or partitions, accepted replays, quarantined conflicts and a bounded repair. Distinguish a fixture check from production pipeline guarantees such as exactly-once delivery.

## Check the result
- Every dropped row has an explicit reason.
- Key collisions are not silently resolved.
- A successful script exit is not treated as semantic correctness.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Preserve input and output digests, key/version semantics, transformation version, authorized window, conflicts and invariant results. Resume the specific failed boundary without silently changing the source contract.

## Example request
Check this cleaned contact table against the original export and account for every removed or merged row.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

