---
name: literature-triage
description: "A person supplies papers or requests a bounded literature map."
---

# Triage a Literature Set Without Losing Its Limits

## Use when
A person supplies papers or requests a bounded literature map.

## Not for
Treating a popularity signal, search snippet or confident summary as sufficient evidence for a factual conclusion.

## Inputs
- The research question and inclusion criteria
- Papers or permitted search sources

## Procedure
1. Freeze the question, eligible populations, designs, outcomes and date boundaries from the user or supplied protocol.
2. Normalize bibliographic identities conservatively, retaining original titles and identifiers; do not merge distinct studies because titles resemble one another.
3. Separate exact duplicates from companion reports of the same underlying study, with an explicit reason for each relation.
4. Screen title and abstract for obvious exclusions, then inspect accessible full text for the decisive criteria. Record unknown criteria explicitly.
5. Extract effect definitions, sample, follow-up and design limitations only from inspected material; do not pool incompatible measures.
6. Synthesize relevant independent study families, contradictions and gaps. State whether screening was single-reviewer and what remains unreviewed.

## Deliver
- A study-comparison table
- A reading order driven by unresolved questions
- Return record dispositions, study-family groupings, eligibility reasons, access limitations and a bounded synthesis by question. Keep inaccessible full text unresolved rather than excluded for an invented methodological reason. Report search coverage accurately; a supplied-paper triage is not a systematic review of the whole literature.

## Check the result
- Duplicate cohorts are not counted as independent replication.
- Missing methods remain unknown.
- Study limitations survive the summary.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Preserve the protocol version, original record IDs, dedup and study-family map, exact screening reasons, access flags and extracted locators. Resume unresolved full-text decisions without rescreening settled records.

## Example request
Compare these eight papers and identify which three are most useful for understanding the disagreement.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

