# Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call

Complete “Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call.
- The selected records, date range, and output destination.
- Complete the named fields in flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/INPUTS.json.
- Configured connections or tools for clickup, emailsend, http, microsoftoutlook, workflow, zoom.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Create tasks

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Create tasks: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Create follow-up call

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = event, operation = create. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Create follow-up call: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 4. Execute Workflow Trigger

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 5. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 7. Zoom: Get data of last meeting

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Zoom: Get data of last meeting: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Filter: Last 24 hours

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Filter: Last 24 hours: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 9. ClickUp

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** ClickUp: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. Zoom: Get transcripts data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Zoom: Get transcripts data: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. No Recording/Transcript available

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 1, input 0).

**Carry forward:** No Recording/Transcript available: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 12. Filter transcript URL

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Filter transcript URL: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Filter: Only 1 item

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-5 (main, branch 0, input 0).

**Carry forward:** Filter: Only 1 item: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 14. Zoom: Get participants data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-18 (data, branch 0, input 0).

**Carry forward:** Zoom: Get participants data: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. Create meeting summary

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-4 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Create meeting summary: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 16. Sort for mail delivery

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-10 (data, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Sort for mail delivery: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Format to html

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Format to html: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 18. Send meeting summary

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Send meeting summary: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. Create tasks and follow-up call

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (tool, branch 0, input 0), step-1 (languageModel, branch 0, input 0), step-17 (tool, branch 0, input 0), step-11 (main, branch 0, input 0), step-10 (data, branch 0, input 0), step-4 (data, branch 0, input 0), step-9 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Create tasks and follow-up call: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 20. Zoom: Get transcript file

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 1, input 0).

**Carry forward:** Zoom: Get transcript file: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 21. Extract text from transcript file

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = text. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Extract text from transcript file: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 22. Format transcript text

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Format transcript text: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-cal-969617/WORKFLOW.json
```
