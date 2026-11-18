---
name: claim-audit
description: "A factual or completion claim needs an evidence-bounded judgment."
---

# Audit a Claim Against Its Actual Evidence

## Use when
A factual or completion claim needs an evidence-bounded judgment.

## Not for
Treating a popularity signal, search snippet or confident summary as sufficient evidence for a factual conclusion.

## Inputs
- The exact claim and intended audience
- The supporting artifact and sources

## Procedure
1. Split the claim into independently checkable propositions.
2. Match each proposition to the smallest adequate source location.
3. Distinguish evidence that a component exists from evidence that it produced the claimed result.
4. Seek a counterexample or scope mismatch for important propositions.
5. Return supported wording and the unresolved propositions without rewriting history.

## Deliver
- A proposition-to-evidence table
- Corrected claim wording

## Check the result
- The verdict does not exceed the evidence scope.
- A self-authored receipt is not treated as independent authority.
- Unsupported does not automatically mean false.

## Recover or narrow
Report the supported findings and the search boundary. Separate unavailable evidence from evidence of absence, and show what observation would resolve the uncertainty.

## Example request
A report says the whole workflow is complete after unit tests. Check exactly which parts the evidence establishes.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

