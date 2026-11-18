---
name: interaction-state-coverage
description: "An interface flow needs an explicit state graph covering entry, loading, success, empty, error and recovery behavior before implementation or QA."
---

# Review Interface States and Recovery Paths

## Use when
An interface flow needs an explicit state graph covering entry, loading, success, empty, error and recovery behavior before implementation or QA.

## Not for
Claiming a browser flow was exercised, inferring screen-reader behavior from a diagram, or treating a complete declared graph as proof of a working application.

## Inputs
- Declared states, initial state, terminal states and the required-state checklist.
- Event-labeled transitions, actual component behavior and any observed failure or recovery evidence.

## Procedure
1. Define the user goal and enumerate actual states, including absence, loading, failure and cancellation where relevant.
2. Choose one initial state, mark terminal states explicitly and freeze the required-state checklist.
3. Describe each transition as origin, event and target; reject missing identities and nondeterministic duplicate events.
4. Traverse reachable states and identify missing requirements, unreachable screens and nonterminal dead ends.
5. Add meaningful recovery transitions and verify that the design preserves entered data and user orientation where required.
6. Exercise the implemented flow in a real browser or device separately; return specification findings without inventing runtime coverage.

## Deliver
- Return reachable and unreachable states, missing required states, nonterminal dead ends and a scoped declared-graph status. browser_tested is always false. A complete design handoff includes each state purpose, visible feedback, event contract, error recovery, focus behavior and the exact runtime checks still needed.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Return reachable and unreachable states, missing required states, nonterminal dead ends and a scoped declared-graph status. browser_tested is always false. A complete design handoff includes each state purpose, visible feedback, event contract, error recovery, focus behavior and the exact runtime checks still needed.

## Example request
A flow declares idle, loading, success and error, but only connects idle to loading and loading to success; empty is required.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

