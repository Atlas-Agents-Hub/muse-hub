# Send a ChatGPT email reply and save responses to Google Sheets

Complete “Send a ChatGPT email reply and save responses to Google Sheets” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Send a ChatGPT email reply and save responses to Google Sheets.
- The selected records, date range, and output destination.
- Complete the named fields in flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/INPUTS.json.
- Configured connections or tools for gmail, googlesheets.
- An available model or embedding capability with the requested format and cost limits.

## 1. On email received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On email received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. On feedback given

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On feedback given: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Identify trigger #2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Identify trigger #2: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Identify trigger #1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-33`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Identify trigger #1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Configure

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-33 (main, branch 0, input 0), step-32 (main, branch 0, input 0).

**Carry forward:** Configure: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Determine which trigger ran

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Operation settings: dataType = string. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-38`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0). Branch 2 ends here; return its result without continuing to another operation.

**Carry forward:** Determine which trigger ran: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Only continue for specific emails

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-38 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Only continue for specific emails: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 8. Record feedback

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-38 (main, branch 1, input 0).

**Carry forward:** Record feedback: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 9. Fallback route

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-38 (main, branch 3, input 0).

**Carry forward:** Fallback route: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 10. Do not send email to this recipient

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-36`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Do not send email to this recipient: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 11. Generate UUID

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Generate UUID: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 12. Thanks for your response!

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Thanks for your response!: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 13. Show HTML page

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Show HTML page: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 14. Extract message content (advanced)

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Extract message content (advanced): Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 15. If no spreadsheet in configuration #2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** If no spreadsheet in configuration #2: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 16. Is text within token limit?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-39`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Is text within token limit?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 17. Generate reply

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-39 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Generate reply: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 18. Store specific sheet IDs #2

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 1, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Store specific sheet IDs #2: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 19. Get sheet IDs #2

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Get sheet IDs #2: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 20. Do nothing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-40`, for its exact field mappings, expressions, and settings. Use the output from step-39 (main, branch 1, input 0).

**Carry forward:** Do nothing: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 21. Send feedback for fine-tuned data

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0), step-25 (main, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** Send feedback for fine-tuned data: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 22. If reply is complete

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-35`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** If reply is complete: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 23. Send reply to database

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-37`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Send reply to database: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 24. Format data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-37 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-6 (data, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Format data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 25. Send email reply

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-35 (main, branch 0, input 0).

**Carry forward:** Send email reply: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 26. Do not send unfinished email reply

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-34`, for its exact field mappings, expressions, and settings. Use the output from step-35 (main, branch 1, input 0).

**Carry forward:** Do not send unfinished email reply: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 27. If no spreadsheet in configuration #1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** If no spreadsheet in configuration #1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 28. Email template

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-20 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Email template: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 29. Get sheet IDs #1

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** Get sheet IDs #1: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 30. Store specific sheet IDs #1

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 1, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Store specific sheet IDs #1: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 31. Send reply to recipient

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = reply. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Send reply to recipient: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 32. If no sheet IDs

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0), step-28 (main, branch 0, input 0).

**Carry forward:** If no sheet IDs: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 33. Get data from `Format data`

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 1, input 0), step-18 (data, branch 0, input 0).

**Carry forward:** Get data from `Format data`: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 34. Create or update rows

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = appendOrUpdate. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Create or update rows: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 35. If spreadsheet doesn't exist

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** If spreadsheet doesn't exist: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 36. Successfully created or updated row

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 1, input 0).

**Carry forward:** Successfully created or updated row: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 37. Create spreadsheet

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = spreadsheet. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-9 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Create spreadsheet: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 38. Store spreadsheet ID

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Store spreadsheet ID: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 39. Get data from `Format data` node

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-18 (data, branch 0, input 0).

**Carry forward:** Get data from `Format data` node: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 40. Paste data

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Paste data: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Send a ChatGPT email reply and save responses to Google Sheets”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-send-a-muse-email-reply-and-save-responses-to-google-sheets-d7f1d3/WORKFLOW.json
```
