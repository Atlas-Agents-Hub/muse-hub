---
name: schema-evolution
description: "A table or API-owned record schema must evolve without losing data or silently breaking consumers."
---

# Review a Schema Change Before Migration

## Use when
A table or API-owned record schema must evolve without losing data or silently breaking consumers.

## Not for
Executing production DDL, assuming a logical comparison proves zero downtime, or approving destructive migrations without the database owner.

## Inputs
- Current and proposed column contracts, including logical types and nullability.
- Observed row count, consumer expectations, database version and operational constraints.

## Procedure
1. Read both schema versions and reject duplicate column identities before comparison.
2. Classify additions, removals, type changes and tighter nullability independently; a rename is not assumed from similar names.
3. Determine whether current rows need values for newly required columns; keep zero-row and nonempty-table cases distinct.
4. Trace application readers and writers, defaults, indexes, foreign keys and engine-specific locking outside the small logical checker.
5. Draft expand/backfill/validate/contract phases with explicit source and target versions; test a disposable database when authorized.
6. Deliver the logical report and actual test evidence separately from migration approval or deployment status.

## Deliver
- Produce added, removed, retyped and nullability-tightened columns; list required backfills; state the observed row count and the limits of a logical-only review. Include a migration sequence, validation queries to be reviewed by the owner, consumer compatibility notes and a rollback boundary. The tool returns a comparison, not executed DDL.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Produce added, removed, retyped and nullability-tightened columns; list required backfills; state the observed row count and the limits of a logical-only review. Include a migration sequence, validation queries to be reviewed by the owner, consumer compatibility notes and a rollback boundary. The tool returns a comparison, not executed DDL.

## Example request
A populated customer table has integer id; add nullable text note.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

