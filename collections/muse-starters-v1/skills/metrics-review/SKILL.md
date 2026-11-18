---
name: metrics-review
description: "A team needs to understand a performance change and decide what to do."
---

# Review Metrics Without Inventing the Story

## Use when
A team needs to understand a performance change and decide what to do.

## Not for
Fabricated customer evidence, deceptive outreach, unapproved spending, or treating proposed commitments as accepted.

## Inputs
- The metric definitions and observed data
- The decision period and known operational changes

## Procedure
1. Recover the metric definition, source version, period boundaries and population for each comparison.
2. Check completeness, missing denominators, event duplication and any measurement-definition change before calculating.
3. Recompute counts and rates with explicit units, separating absolute, relative and percentage-point changes.
4. Inspect exposure and relevant segment composition; compare within segments when an aggregate can mislead.
5. Separate observed association from causal explanation, accounting for concurrent changes and selection effects.
6. Return a bounded decision and the smallest next measurement that would resolve a material uncertainty.

## Deliver
- A definition-aware metric review
- A next experiment or decision
- Deliver the original figures, reproducible calculations, comparability assessment, supported interpretation, alternative explanations and a decision-relevant next check. Preserve unknown or zero denominators explicitly. Label any recommendation as judgment rather than a measured effect.

## Check the result
- Like-for-like periods are compared.
- Percent changes include relevant counts.
- An action recommendation is distinguished from a proven causal explanation.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Keep metric definitions, source versions, period and population filters, numerators/denominators, formulas and open alternative explanations. Resume the missing comparison or calculation, not an unsupported causal narrative.

## Example request
Our support resolution rate fell this month. Check whether case mix or reporting changes explain it.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

