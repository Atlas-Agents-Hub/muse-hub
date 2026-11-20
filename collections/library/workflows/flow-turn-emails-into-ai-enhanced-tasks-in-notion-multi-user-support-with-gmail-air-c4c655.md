# Turn Emails into AI-Enhanced Tasks in Notion (Multi-User Support) with Gmail, Airtable and Softr

Complete “Turn Emails into AI-Enhanced Tasks in Notion (Multi-User Support) with Gmail, Airtable and Softr” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Turn Emails into AI-Enhanced Tasks in Notion (Multi-User Support) with Gmail, Airtable and Softr.
- The selected records, date range, and output destination.
- Complete the named fields in flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/INPUTS.json.
- Configured connections or tools for airtable, gmail, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Gmail Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. When clicking ‘Test workflow’

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 4. Calculator

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Calculator: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 5. Structured Output Parser1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser1: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 6. Calculator1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Calculator1: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 7. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 8. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 9. Globals

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Globals: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Get all labels

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = label. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Get all labels: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Filter for unprocessed mails

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Filter for unprocessed mails: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 12. Required labels

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Required labels: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 13. Extract Route ID

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Extract Route ID: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Get Route by ID

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Get Route by ID: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 15. No Operation, do nothing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** No Operation, do nothing: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 16. Active Routes Only

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Active Routes Only: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 17. Send notification about missing route

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Send notification about missing route: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 18. Generate Actionable Task

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-22 (tool, branch 0, input 0), step-5 (main, branch 0, input 0), step-23 (languageModel, branch 0, input 0), step-21 (outputParser, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Generate Actionable Task: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 19. Get Summary & Meta Data

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-2 (tool, branch 0, input 0), step-1 (languageModel, branch 0, input 0), step-24 (main, branch 0, input 0), step-3 (outputParser, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Get Summary & Meta Data: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 20. Format Notion Page Blocks

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0), step-11 (data, branch 0, input 0), step-24 (data, branch 0, input 0).

**Carry forward:** Format Notion Page Blocks: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 21. Create Notion Page

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Create Notion Page: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 22. Add Label "Processed"

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = addLabels. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-13 (data, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Add Label "Processed": The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 23. Deactivate Route

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0).

**Carry forward:** Deactivate Route: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 24. Send notification about deactivated route

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Send notification about deactivated route: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 25. Add Label "Error"

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = addLabels. Read `../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-9 (main, branch 0, input 0), step-13 (data, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Add Label "Error": The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Turn Emails into AI-Enhanced Tasks in Notion (Multi-User Support) with Gmail, Airtable and Softr”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-turn-emails-into-ai-enhanced-tasks-in-notion-multi-user-support-with-gmail-air-c4c655/WORKFLOW.json
```
