---
name: dataset-intake
description: "A supplied dataset is about to support analysis or model development."
---

# Inspect a Dataset Before Using It

## Use when
A supplied dataset is about to support analysis or model development.

## Not for
Manufacturing missing observations, silently changing data definitions, or reporting unrun experiments as measured.

## Inputs
- The actual data and data dictionary
- Intended use, access restrictions and known collection methods

## Procedure
1. Identify the intended analysis or model task, available data sources and actual permitted use; record unknown provenance without inventing consent.
2. Define the unit of observation, stable record key, grouping key, time fields and target label before profiling.
3. Check schema, types, missing values and duplicate identities; distinguish exact repeats from conflicting records.
4. Inspect train/dev/test partitions by entity and source family, not just row ID; check whether labels or post-outcome fields leak into features.
5. Compare coverage and collection times with the target population and decision horizon; document exclusions and unsupported generalization.
6. Produce the intake decision and a reversible remediation proposal, preserving original bytes and unresolved rights or quality issues.

## Deliver
- A dataset inventory with quality issues
- A scoped cleaning and use proposal
- Deliver a bounded data card: source and use scope, schema, row and entity counts, duplicate/conflict findings, missingness, partition leakage, temporal limitations and an admit/hold decision for the stated use. Preserve raw input and do not train or upload automatically.

## Check the result
- Raw input remains unchanged.
- Missing values are not silently treated as zero.
- Permitted use and technical suitability are separate questions.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Preserve raw digests, data dictionary, grouping and timing rules, allowed-use evidence, conflict list and partition decisions. Resume the specific unresolved check; do not silently resplit a consumed test set.

## Example request
Inspect this survey export before we analyze satisfaction, including duplicate respondents and missing responses.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

