---
name: minimal-repair
description: "A reproduced defect has an authorized source boundary and regression test."
---

# Repair the Smallest Causal Boundary

## Use when
A reproduced defect has an authorized source boundary and regression test.

## Not for
Unrequested deployments, third-party intrusion, broad rewrites, or executing unreviewed downloaded scripts.

## Inputs
- The failing case and source baseline
- The change scope and relevant test suite

## Procedure
1. Read the failing regression, expected behavior and exact source revision; verify that the reproduced defect belongs to the authorized files.
2. Trace the incorrect value or state to its earliest controllable cause and identify the invariant to restore.
3. Define unaffected controls and boundary cases before editing; keep unrelated refactoring out of the patch.
4. Make one maintainable causal change and run the red regression plus controls on the changed revision.
5. Run the relevant integration and parent checks, inspecting failures rather than treating a green focused test as complete coverage.
6. Review the diff for accidental behavior changes, preserve remaining failures and deliver exact resume and rollback instructions.

## Deliver
- A bounded repair with regression coverage
- A truthful change and test report
- Deliver the reproduced failure, causal explanation, exact changed files, focused and relevant broader test results, limitations and rollback instructions. A patch is proposed until executed evidence shows the intended behavior; deployment is a separate effect.

## Check the result
- The original failing case now passes.
- Nearby valid behavior remains intact.
- Skips and unrun integration tests are not reported as passed.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Preserve the base and candidate identities, failing command, invariant, patch, unaffected controls, full-suite results and unmerged work. Resume from the first unverified gate, never by resetting the owner's tree.

## Example request
Fix the reproduced off-by-one bug without rewriting the parser, and test empty and single-item inputs.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

