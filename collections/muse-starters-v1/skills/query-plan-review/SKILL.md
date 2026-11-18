---
name: query-plan-review
description: "A supplied SQLite query plan or measured slow query needs a grounded index and access-path review."
---

# Read a Query Plan Before Changing Indexes

## Use when
A supplied SQLite query plan or measured slow query needs a grounded index and access-path review.

## Not for
Executing unreviewed SQL, claiming every scan is slow, or transferring SQLite text-format heuristics to an unrelated database engine.

## Inputs
- Exact SQL and parameters, engine version, schema and the original plan detail rows.
- Observed cardinalities, representative timings and the workload constraints for reads and writes.

## Procedure
1. Read the actual query, schema and plan from the same engine version; reject an empty plan.
2. Classify recognized SQLite access rows without rewriting or dropping the original text.
3. Distinguish full table access from a covering-index scan, selective search and temporary B-tree sorting.
4. Locate selective predicates, join order, ordering and covering opportunities in the actual SQL.
5. Test one justified index change in an authorized disposable database with representative parameter values.
6. Return observed timings and query correctness separately from the plan classification; retain unknown rows and failed hypotheses.

## Deliver
- Return classified supplied plan rows and retained unclassified rows; propose a concrete measurement and index hypothesis only where source evidence supports it. Include exact SQL/parameter identity, engine version, cardinality, before/after latency and write-cost tradeoffs when those are actually observed. performance_proven and query_executed remain false for text-only inspection.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Return classified supplied plan rows and retained unclassified rows; propose a concrete measurement and index hypothesis only where source evidence supports it. Include exact SQL/parameter identity, engine version, cardinality, before/after latency and write-cost tradeoffs when those are actually observed. performance_proven and query_executed remain false for text-only inspection.

## Example request
Plan rows include SCAN users, SEARCH orders USING INDEX order_id, and a temporary ordering B-tree.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

