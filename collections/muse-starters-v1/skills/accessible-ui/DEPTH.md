# Inspect a Real Interface for Access Barriers — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Accessibility review is evidence about a complete user task across interaction states, not a screenshot score. Separate semantic structure, keyboard operation, focus management, visual perception and assistive-technology observations. Record the actual browser, viewport and assistive technology used. Record untested states explicitly and tie each observed barrier to the pages and interactions actually checked. Use the applicable W3C standard and its exceptions rather than a memorized checklist alone.

## Output contract

Deliver a scoped barrier report with reproducible steps, affected task, observed behavior, expected behavior, evidence location, severity and the smallest repair. Include positive controls and an explicit not-tested list. Conformance remains undetermined when required pages, processes or criteria are untested.

## Choose the right action

### Only a screenshot is available.
Review visible contrast, text, hierarchy and layout within its limits; list keyboard and screen-reader behavior as untested.

**Avoid:** Do not claim keyboard operability or complete WCAG conformance from pixels.

### An automated scan reports zero violations.
Continue the manual interaction and assistive-technology checks required by the scope.

**Avoid:** Do not treat the scan as proof of every criterion.

### A dialog closes but focus disappears.
Record the trigger, close action and observed focus target; repair return to the appropriate invoking context.

**Avoid:** Do not equate disappearance of the dialog with completion of the interaction.

### A criterion has an exception or scope condition.
Inspect the current normative wording and document why it applies or does not apply.

**Avoid:** Do not apply a simplified numeric rule without its conditions.

### The user requests an audit only.
Return evidence and proposed repairs without modifying the implementation.

**Avoid:** Do not redesign, publish or change source under an audit-only request.

## Worked example

**Input:** A modal opens from button A. Keyboard entry, trapped focus and Escape close pass; after close focus lands on the document body instead of A. No screen reader was run.

**Method:** Classify the observed focus-return barrier, retain the passing keyboard checks and state the untested assistive-technology dimension.

**Result:** The focus-return check fails; screen-reader behavior is not tested; overall conformance is undetermined. The proposed repair restores an appropriate invoking focus target and is verified by reopening and closing the modal.

## Edge or recovery example 1 (example)

**Input:** Only a static image of the same modal is supplied, and a report says keyboard and screen-reader checks passed.

**Method:** Separate image inspection from interaction evidence.

**Result:** Those interaction passes are unsupported and must become not tested. Visible observations may still be useful, but no runtime accessibility claim is made.

## Failure diagnosis

### The report marks untested states as passing.
**Likely cause:** A checklist default was mistaken for an observation.

**Repair:** Change those states to not tested and identify the missing interaction evidence.

**Recheck:** Every pass has a reproducible observed check.

### A fix improves one control but breaks navigation order.
**Likely cause:** The component was tested in isolation only.

**Repair:** Rerun the full task and focus sequence with adjacent controls.

**Recheck:** The repaired task is operable and the unaffected control remains correct.

### The audit claims a specific screen-reader announcement that was never heard.
**Likely cause:** Source inspection was promoted to assistive-technology evidence.

**Repair:** Replace the claim with a source-level expectation and mark the runtime check untested.

**Recheck:** Observation type and tool provenance are explicit.

## Preserve for the next turn

Preserve the journey, state matrix, tool/browser versions, observed steps, criterion references and unresolved checks. Resume at the missing interaction or repaired flow; do not rerun a whole-site audit or claim universal accessibility from a sampled task.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `accessible-ui-r3-standard`, `accessible-ui-r3-edge`, `accessible-ui-r3-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
