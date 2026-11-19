# Summarize the New Documents from Google Drive and Save Summary in Google Sheet

Complete “Summarize the New Documents from Google Drive and Save Summary in Google Sheet” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Summarize the New Documents from Google Drive and Save Summary in Google Sheet.
- The selected records, date range, and output destination.
- Complete the named fields in flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/INPUTS.json.
- Configured connections or tools for googledocs, googlesheets, toolwikipedia.
- An available model or embedding capability with the requested format and cost limits.

## 1. Wikipedia

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Wikipedia: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 2. Calculator

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Calculator: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Google Drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Drive: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Google Docs

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Google Docs: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Generate Summary AI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-2 (tool, branch 0, input 0), step-3 (tool, branch 0, input 0), step-1 (main, branch 0, input 0).

**Carry forward:** Generate Summary AI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. Google Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Google Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Summarize the New Documents from Google Drive and Save Summary in Google Sheet”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-summarize-the-new-documents-from-google-drive-and-save-summary-in-google-sheet-66e9b1/WORKFLOW.json
```
