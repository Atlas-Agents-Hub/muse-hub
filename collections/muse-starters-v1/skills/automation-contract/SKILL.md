---
name: automation-contract
description: "A browser, desktop or connector workflow needs an explicit dependency and external-effect contract before the existing host executes it."
---

# Review a Bounded Automation Plan Before Execution

## Use when
A browser, desktop or connector workflow needs an explicit dependency and external-effect contract before the existing host executes it.

## Not for
Granting tool access, authenticating approval from a JSON flag, creating a new scheduler or carrying out operations on unapproved targets.

## Inputs
- Step identities, dependencies, effect kinds, targets and declared idempotency keys.
- The user-approved target scope and the existing host capability and approval boundaries.

## Procedure
1. Recover the actual user goal, target account or application, existing tools and previously attempted operations.
2. Assign stable step identities and distinguish observations and drafts from consequential external effects.
3. Validate every dependency and reject cycles, unknown predecessors and undeclared target scope.
4. Check declared approval and idempotency coverage for effects, then propagate blocked prerequisites.
5. Prepare the largest independent read-only output without treating missing optional integrations as global failure.
6. Hand the inert plan to the original qualified executor with actor, approval, readback and stop conditions; do not dispatch from this checker.

## Deliver
- Return ordered step IDs, blocked steps with concrete reasons and a ready-for-host-review or blocked classification. execution_authorized and external_actions_performed are always false. A useful handoff includes the original user request, exact target identities, observable success conditions, failure reconciliation and evidence required by the existing executor.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Return ordered step IDs, blocked steps with concrete reasons and a ready-for-host-review or blocked classification. execution_authorized and external_actions_performed are always false. A useful handoff includes the original user request, exact target identities, observable success conditions, failure reconciliation and evidence required by the existing executor.

## Example request
A read step feeds a send step whose approval is false and whose idempotency key is once.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

