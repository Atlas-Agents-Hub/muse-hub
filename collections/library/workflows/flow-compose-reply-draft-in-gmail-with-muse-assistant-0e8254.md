# Compose reply draft in Gmail with OpenAI Assistant

Complete “Compose reply draft in Gmail with OpenAI Assistant” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Compose reply draft in Gmail with OpenAI Assistant.
- The selected records, date range, and output destination.
- Complete the named fields in flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/INPUTS.json.
- Configured connections or tools for gmail, http, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule trigger (1 min)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule trigger (1 min): A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Get threads with specific labels

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = thread. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Get threads with specific labels: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 3. Loop over threads

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-8 (main, branch 0, input 0).

**Carry forward:** Loop over threads: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 4. Get thread messages

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = thread, operation = get. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** Get thread messages: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Return last message in thread

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Return last message in thread: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 6. Convert raw to base64

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Convert raw to base64: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. Get single message content

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Get single message content: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Add email draft to thread

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Add email draft to thread: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Remove AI label from email

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = thread, operation = removeLabels. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Remove AI label from email: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Map fields for further processing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-13 (data, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Map fields for further processing: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Convert response to HTML

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: mode = markdownToHtml. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Convert response to HTML: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 12. Build email raw

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Build email raw: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Ask OpenAI Assistant

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = assistant. Read `../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Ask OpenAI Assistant: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Compose reply draft in Gmail with OpenAI Assistant”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-compose-reply-draft-in-gmail-with-muse-assistant-0e8254/WORKFLOW.json
```
