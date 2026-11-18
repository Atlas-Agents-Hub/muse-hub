---
name: competing-explanations
description: "Several plausible causes or interpretations fit the same observation."
---

# Compare Explanations With Discriminating Evidence

## Use when
Several plausible causes or interpretations fit the same observation.

## Not for
Treating a popularity signal, search snippet or confident summary as sufficient evidence for a factual conclusion.

## Inputs
- The observed result and timing
- Candidate explanations and relevant source records

## Procedure
1. Write the observation exactly, including timing, units, scope and known measurement limitations.
2. List plausible explanations supplied by the evidence, including a measurement or selection artifact where relevant.
3. For each explanation, state at least one prediction that differs from another explanation under specified conditions.
4. Compare existing observations with those predictions; distinguish contradiction from absence of a measurement.
5. Select the smallest authorized check likely to separate the leading explanations, including an unaffected control.
6. Update the matrix from actual results, retaining unexplained findings and a stop condition when evidence cannot discriminate.

## Deliver
- A competing-explanation matrix
- A bounded next observation
- Deliver named hypotheses, their distinct predictions, observed supporting and contradicting evidence, unresolved assumptions and the next discriminating check. State eliminated, still plausible and favored as different judgments; do not convert a favored account into certainty.

## Check the result
- Correlation is not silently converted to causation.
- A preferred explanation is tested against adverse evidence.
- Unknown facts are not filled in to make a story coherent.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Carry the observation version, hypothesis definitions, prediction matrix, actual measurements, assumptions and next authorized discriminating check. Never rewrite a prior prediction after seeing its result.

## Example request
Why did usage rise after our redesign? Compare the redesign hypothesis with promotion and measurement changes.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

