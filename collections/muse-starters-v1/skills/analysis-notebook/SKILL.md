---
name: analysis-notebook
description: "A question requires calculations that should be inspectable and reproducible."
---

# Build a Reproducible Analysis Narrative

## Use when
A question requires calculations that should be inspectable and reproducible.

## Not for
Manufacturing missing observations, silently changing data definitions, or reporting unrun experiments as measured.

## Inputs
- The data and analytic question
- Available computation tools and output expectations

## Procedure
1. Define the measure and comparison before calculating.
2. Preserve raw inputs and describe each transformation.
3. Run the calculation using available tools or label unexecuted code as unexecuted.
4. Check units, sample sizes and a simple independent arithmetic control.
5. Present the answer, method and limitations with enough detail to reproduce the result.

## Deliver
- A reproducible analysis artifact
- A decision-facing interpretation

## Check the result
- Results match actually executed computations.
- Transformations do not conceal exclusions.
- Uncertainty and sample limits survive presentation.

## Recover or narrow
Retain raw data and the transformation log. Stop the affected calculation on ambiguous units or keys, and continue independent analyses without filling gaps with invented observations.

## Example request
Analyze these task durations and explain the median, spread and outliers with reproducible calculations.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

