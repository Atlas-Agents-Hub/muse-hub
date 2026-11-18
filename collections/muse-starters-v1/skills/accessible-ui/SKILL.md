---
name: accessible-ui
description: "A built interface needs a focused accessibility and usability pass."
---

# Inspect a Real Interface for Access Barriers

## Use when
A built interface needs a focused accessibility and usability pass.

## Not for
Unrequested deployments, third-party intrusion, broad rewrites, or executing unreviewed downloaded scripts.

## Inputs
- The rendered page or supplied screenshots
- Target tasks, viewport and input modes

## Procedure
1. Identify the specific user journey, required interaction states and requested standard; use the existing implementation rather than inventing a redesign.
2. Inspect semantic names, roles, states and error associations where source or accessibility-tree access exists; mark screenshot-only limits.
3. Exercise keyboard traversal, activation, dialog entry/exit and focus return through the actual task, recording what happened.
4. Check zoom/reflow, contrast, reduced-motion behavior and content alternatives within the requested scope using available tools.
5. Use a real screen reader or other relevant assistive technology when available; record its actual combination and do not substitute a markup guess for observed speech.
6. Prioritize barriers by task impact, propose a bounded repair and rerun the affected flow plus an unaffected control before describing it as fixed.

## Deliver
- A barrier report tied to actual states
- A focused verification checklist
- Deliver a scoped barrier report with reproducible steps, affected task, observed behavior, expected behavior, evidence location, severity and the smallest repair. Include positive controls and an explicit not-tested list. Conformance remains undetermined when required pages, processes or criteria are untested.

## Check the result
- A screenshot is not treated as proof of screen-reader behavior.
- The main task remains usable at the requested viewport.
- Fixes are checked in the rendered interface, not source alone.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Preserve the journey, state matrix, tool/browser versions, observed steps, criterion references and unresolved checks. Resume at the missing interaction or repaired flow; do not rerun a whole-site audit or claim universal accessibility from a sampled task.

## Example request
Review this mobile modal for focus, scrolling and toolbar overlap; distinguish measured findings from screenshot-only concerns.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Check an HTML page
Run the included [HTML source checker](SOURCE_CHECK.md) to find missing document language, empty page titles, duplicate IDs and markup that needs a closer look. The guide includes two example pages and next steps for browser testing.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

