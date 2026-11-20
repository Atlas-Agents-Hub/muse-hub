# FlowScribe Lite - AI Content Repurposing 4 Platforms

Complete “FlowScribe Lite - AI Content Repurposing 4 Platforms” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for FlowScribe Lite - AI Content Repurposing 4 Platforms.
- The selected records, date range, and output destination.
- Complete the named fields in flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/INPUTS.json.
- Configured connections or tools for googlesheets.
- An available model or embedding capability with the requested format and cost limits.

## 1. Receive Content

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Receive Content: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Validate Input

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Validate Input: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. AI: Quick Analysis

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** AI: Quick Analysis: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 4. Merge Data

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Merge Data: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. Generate: Twitter Thread

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Generate: Twitter Thread: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. Generate: LinkedIn Post

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Generate: LinkedIn Post: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Generate: Instagram Caption

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Generate: Instagram Caption: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Generate: Facebook Post

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Generate: Facebook Post: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. Collect Results

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-6 (main, branch 0, input 0), step-7 (main, branch 0, input 0), step-8 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Collect Results: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. Save to Google Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Save to Google Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Respond: Success

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Respond: Success: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “FlowScribe Lite - AI Content Repurposing 4 Platforms”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-flowscribe-lite-ai-content-repurposing-4-platforms-d353dc/WORKFLOW.json
```
