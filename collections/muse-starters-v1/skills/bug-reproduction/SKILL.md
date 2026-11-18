---
name: bug-reproduction
description: "An owned codebase has a reported defect or failing test."
---

# Reproduce a Defect Before Repairing It

## Use when
An owned codebase has a reported defect or failing test.

## Not for
Unrequested deployments, third-party intrusion, broad rewrites, or executing unreviewed downloaded scripts.

## Inputs
- The relevant source revision and report
- Existing test commands and expected behavior

## Procedure
1. Read the local project instructions and inspect the exact source without overwriting work.
2. Run the narrowest existing test or observed path that demonstrates the defect.
3. Reduce the case while keeping the original failure signature and an unaffected control.
4. Add a regression assertion for the intended behavior.
5. Record the causal hypothesis, evidence and smallest repair boundary.

## Deliver
- A reproducible failing case
- A source-bound regression test

## Check the result
- The observed failure matches the reported defect.
- An unrelated setup failure is not mislabeled reproduction.
- The test fails for the intended reason before a fix.

## Recover or narrow
Preserve the original state and logs. Narrow the failing case, stop after the agreed attempt budget, and return a reproducible next step rather than a speculative broad change.

## Example request
This parser drops the final item. Reproduce the failure on the supplied fixture before changing implementation.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

