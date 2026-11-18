---
name: incremental-pipeline
description: "An incremental import contains late events, duplicates, deletions or conflicting versions and needs a deterministic reconciliation."
---

# Reconcile Versioned Events Without Resurrection

## Use when
An incremental import contains late events, duplicates, deletions or conflicting versions and needs a deterministic reconciliation.

## Not for
Claiming distributed exactly-once delivery, deleting production tombstones, or choosing a conflicting payload without a source-owned rule.

## Inputs
- An immutable prior state keyed by business identifier and source version.
- A bounded event batch with key, version, value and explicit deletion marker.

## Procedure
1. Freeze the previous state and incoming batch without mutating either supplied object.
2. Validate key uniqueness in the state, integer versions and null-valued tombstones.
3. Detect contradictory same-key/same-version records across the full batch before applying any candidate change.
4. For nonconflicting input select the highest source version, preserving deletion markers as state.
5. Calculate duplicate and stale-event counts independent of arrival order and reconcile every applied key.
6. Hand off the candidate state and conflicts to the existing transaction owner; never mark a database commit from a pure calculation.

## Deliver
- Return a newly calculated state, applied keys, stale-event count, duplicate-event count and any conflicting keys. Conflict returns the original state without partial application. Preserve source and batch digests, version semantics and deletion retention requirements for a real pipeline owner. External writes remain false.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Return a newly calculated state, applied keys, stale-event count, duplicate-event count and any conflicting keys. Conflict returns the original state without partial application. Preserve source and batch digests, version semantics and deletion retention requirements for a real pipeline owner. External writes remain false.

## Example request
State contains A version 3 deleted; incoming A version 2 value 10 and a repeat of the tombstone.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

