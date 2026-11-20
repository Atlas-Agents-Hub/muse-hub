# Chat with a Google Sheet using AI

Complete “Chat with a Google Sheet using AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Chat with a Google Sheet using AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-chat-with-a-google-sheet-using-ai-d80dd3/INPUTS.json.
- Configured connections or tools for googlesheets, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Chat Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. List columns tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** List columns tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Get customer tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get customer tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Get column values tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get column values tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-7 (tool, branch 0, input 0), step-6 (tool, branch 0, input 0), step-12 (languageModel, branch 0, input 0), step-8 (tool, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Set Google Sheet URL

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set Google Sheet URL: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Get Google sheet contents

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Get Google sheet contents: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. Check operation

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Check operation: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 11. Filter

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 2, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Filter: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 12. Get column names

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Get column names: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Prepare column data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Prepare column data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Prepare output

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-4 (main, branch 0, input 0), step-9 (main, branch 0, input 0).

**Carry forward:** Prepare output: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Chat with a Google Sheet using AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-chat-with-a-google-sheet-using-ai-d80dd3/WORKFLOW.json
```
