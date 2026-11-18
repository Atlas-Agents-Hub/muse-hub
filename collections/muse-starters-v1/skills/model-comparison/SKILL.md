---
name: model-comparison
description: "A user wants evidence that a model or prompt change improves results."
---

# Compare Model Candidates on the Same Frozen Task

## Use when
A user wants evidence that a model or prompt change improves results.

## Not for
Manufacturing missing observations, silently changing data definitions, or reporting unrun experiments as measured.

## Inputs
- The candidate definitions and evaluation cases
- A fixed rubric, resource budget and permissible execution route

## Procedure
1. Freeze the task set, scoring rubric and candidate identities before evaluation.
2. Keep development examples separate from the final comparison.
3. Run candidates under comparable tool access, model settings and budget when supported.
4. Review actual outputs with blinded labels where possible and retain failures.
5. Report per-case results, uncertainty and costs; leave unrun outcomes explicitly empty.

## Deliver
- A frozen comparison protocol
- An honest result table or unrun evaluation packet

## Check the result
- The candidate did not tune on protected final answers.
- All candidates received equivalent inputs and resources.
- A configured evaluation is not reported as an executed improvement.

## Recover or narrow
Retain raw data and the transformation log. Stop the affected calculation on ambiguous units or keys, and continue independent analyses without filling gaps with invented observations.

## Example request
Compare two assistant instructions on the same ten tasks, preserving both failures and token costs.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

