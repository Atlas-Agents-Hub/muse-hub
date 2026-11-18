---
name: spreadsheet-reconcile
description: "A workbook contains totals, formulas or records that need verification."
---

# Reconcile a Spreadsheet to Its Source Records

## Use when
A workbook contains totals, formulas or records that need verification.

## Not for
Manufacturing missing observations, silently changing data definitions, or reporting unrun experiments as measured.

## Inputs
- The workbook and source records
- Relevant ranges, units and expected reconciliation rules

## Procedure
1. Inspect the source records, workbook sheets and intended reporting period; identify which fields and formulas are authoritative.
2. Define a stable matching key and normalize only explicitly equivalent formats, retaining original values and currency.
3. Detect duplicate identities, missing rows, extra rows and conflicting amounts before calculating totals.
4. Recompute subtotals with exact arithmetic and inspect formula ranges, hidden rows and excluded records where the workbook interface permits.
5. Explain differences at row level and distinguish rounding, timing, currency, sign and genuine data errors.
6. Deliver proposed fixes or apply only authorized narrow changes, then reread affected cells and recheck the reconciliation.

## Deliver
- A cell-level discrepancy report
- Reconciled totals and proposed corrections
- Deliver a reconciliation table with source row IDs, workbook references, matched/missing/duplicate/conflicting records, totals by currency, formula or range findings and proposed corrections. Preserve originals and require the actual requested authority before changing a live workbook.

## Check the result
- Formulas are not replaced by hardcoded results without request.
- Units and signs are consistent.
- Reconciliation explains residual differences rather than hiding them.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Keep source versions, matching keys, original cell references, exact amounts, currency/sign rules and proposed/applied changes. Resume with authoritative readback of the affected rows, not a wholesale workbook rewrite.

## Example request
Find why the monthly total differs from the invoice list without changing the original workbook.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

