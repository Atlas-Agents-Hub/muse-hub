# LINE Assistant with Google Calendar and Gmail Integration

Complete “LINE Assistant with Google Calendar and Gmail Integration” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for LINE Assistant with Google Calendar and Gmail Integration.
- The selected records, date range, and output destination.
- Complete the named fields in flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/INPUTS.json.
- Configured connections or tools for gmail, googlecalendar, http, toolwikipedia.
- An available model or embedding capability with the requested format and cost limits.

## 1. Google Calendar Create

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Calendar Create: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 2. Google Calendar Read

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Calendar Read: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Gmail Read

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail Read: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 5. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. Wikipedia

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Wikipedia: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Line Receiving

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Line Receiving: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 8. Switch Between Text and Others

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Switch Between Text and Others: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 9. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-4 (tool, branch 0, input 0), step-14 (tool, branch 0, input 0), step-3 (languageModel, branch 0, input 0), step-13 (tool, branch 0, input 0), step-2 (memory, branch 0, input 0), step-12 (tool, branch 0, input 0), step-6 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. Error Handling from AI Response

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Error Handling from AI Response: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Line Answering (Error Case)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 1, input 0), step-8 (main, branch 1, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Line Answering (Error Case): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Text Cleansing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Text Cleansing: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Line Answering (Ordinary Case)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Line Answering (Ordinary Case): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “LINE Assistant with Google Calendar and Gmail Integration”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-line-assistant-with-google-calendar-and-gmail-integration-6cb998/WORKFLOW.json
```
