# Summarize Umami data with AI (via Openrouter) and save it to Baserow

Complete “Summarize Umami data with AI (via Openrouter) and save it to Baserow” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Summarize Umami data with AI (via Openrouter) and save it to Baserow.
- The selected records, date range, and output destination.
- Complete the named fields in flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/INPUTS.json.
- Configured connections or tools for baserow, http, scheduler.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 3. Get view stats from Umami

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-1 (main, branch 0, input 0).

**Carry forward:** Get view stats from Umami: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Parse Umami data

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Parse Umami data: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. Send data to A.I.

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Send data to A.I.: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Get page data from Umami

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Get page data from Umami: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 7. Parse Umami data1

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Parse Umami data1: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. Get page view data from Umami

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Get page view data from Umami: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Parse Umami

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Parse Umami: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. Send data to A.I.1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Send data to A.I.1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Save data to Baserow

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Save data to Baserow: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Summarize Umami data with AI (via Openrouter) and save it to Baserow”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-summarize-umami-data-with-ai-via-openrouter-and-save-it-to-baserow-86957b/WORKFLOW.json
```
