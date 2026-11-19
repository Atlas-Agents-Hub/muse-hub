# Analyze Suspicious Email Contents with ChatGPT Vision

Complete “Analyze Suspicious Email Contents with ChatGPT Vision” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Analyze Suspicious Email Contents with ChatGPT Vision.
- The selected records, date range, and output destination.
- Complete the named fields in flow-analyze-suspicious-email-contents-with-muse-vision-666293/INPUTS.json.
- Configured connections or tools for http, jira.
- An available model or embedding capability with the requested format and cost limits.

## 1. Gmail Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Microsoft Outlook Trigger

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Microsoft Outlook Trigger: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 3. Set Gmail Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set Gmail Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Retrieve Headers of Email

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Retrieve Headers of Email: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Format Headers

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Format Headers: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 6. Set Outlook Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-2 (data, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Set Outlook Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Set Email Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-5 (main, branch 0, input 0).

**Carry forward:** Set Email Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Screenshot HTML

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Screenshot HTML: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Retrieve Screenshot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Retrieve Screenshot: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. ChatGPT Analysis

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** ChatGPT Analysis: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. Create Jira Ticket

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Create Jira Ticket: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. Rename Screenshot

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Rename Screenshot: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. Upload Screenshot of Email to Jira

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = issueAttachment. Read `../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Upload Screenshot of Email to Jira: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Analyze Suspicious Email Contents with ChatGPT Vision”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-analyze-suspicious-email-contents-with-muse-vision-666293/WORKFLOW.json
```
