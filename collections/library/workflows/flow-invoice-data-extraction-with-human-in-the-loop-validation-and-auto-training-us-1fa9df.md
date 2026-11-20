# Invoice data extraction with human-in-the-loop validation and auto-training using Cradl AI

Complete “Invoice data extraction with human-in-the-loop validation and auto-training using Cradl AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Invoice data extraction with human-in-the-loop validation and auto-training using Cradl AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/INPUTS.json.
- Configured connections or tools for cradlai, gmail, googlesheets.

## 1. Gmail Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Filter PDF attachments

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Filter PDF attachments: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Mark a message as read

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = markAsRead. Read `../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-1 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Mark a message as read: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 4. Extract invoice details with AI

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Extract invoice details with AI: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Split out each invoice line

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Split out each invoice line: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 6. Add invoice line to Google Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Add invoice line to Google Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Invoice data extraction with human-in-the-loop validation and auto-training using Cradl AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-invoice-data-extraction-with-human-in-the-loop-validation-and-auto-training-us-1fa9df/WORKFLOW.json
```
