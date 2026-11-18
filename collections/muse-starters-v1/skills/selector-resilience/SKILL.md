---
name: selector-resilience
description: "A browser workflow has supplied candidate locator observations and needs a unique, visible, stable target before an authorized action."
---

# Choose a Locator From Actual Target Observations

## Use when
A browser workflow has supplied candidate locator observations and needs a unique, visible, stable target before an authorized action.

## Not for
Inventing DOM inspection, bypassing authentication, using screen coordinates without observation, or clicking an ambiguous match.

## Inputs
- The intended target identity and candidate locator observations from the real page or an explicitly labeled fixture.
- For each candidate: strategy, match count, visibility, stability and bound target identity.

## Procedure
1. State the exact intended control, page and frame instead of guessing from a vague button label.
2. Read actual candidate match counts, visibility, stability and target binding; label fixture observations honestly.
3. Reject missing, duplicated, hidden, unstable or wrong-target observations before considering preference order.
4. Choose a deterministic eligible candidate using semantic strategy preference and stable candidate identity.
5. Have the existing browser adapter refresh the observation immediately before the approved action and verify the resulting state.
6. Preserve rejected candidates and any page drift so a later turn does not reuse an obsolete locator blindly.

## Deliver
- Return the selected candidate ID or null, all eligible IDs, rejected IDs with reasons and whether more observation is needed. The report never claims a browser action or authenticated target observation. Include actual page/frame identity and observation age in the host handoff where available.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Return the selected candidate ID or null, all eligible IDs, rejected IDs with reasons and whether more observation is needed. The report never claims a browser action or authenticated target observation. Include actual page/frame identity and observation age in the host handoff where available.

## Example request
A role locator matches two submit buttons; a unique test ID points to delete instead.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

