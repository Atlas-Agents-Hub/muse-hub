# Assistant to chat with you Search Console Data, using OpenAI and Postgres

Complete “Assistant to chat with you Search Console Data, using OpenAI and Postgres” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Assistant to chat with you Search Console Data, using OpenAI and Postgres.
- The selected records, date range, and output destination.
- Complete the named fields in flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/INPUTS.json.
- Configured connections or tools for http, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Postgres Chat Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Postgres Chat Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Webhook - ChatInput

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook - ChatInput: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Call Search Console Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Call Search Console Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Tool calling

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Tool calling: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Set fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Set fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Set fields - Consruct API CALL

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Set fields - Consruct API CALL: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-1 (memory, branch 0, input 0), step-6 (tool, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Search Console - Get Custom Insights

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Search Console - Get Custom Insights: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. ## Search Console - Get List of Properties

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 1, input 0).

**Carry forward:** ## Search Console - Get List of Properties: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 13. Set fields - Create searchConsoleDataArray

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Set fields - Create searchConsoleDataArray: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Set fields - Create searchConsoleDataArray 2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Set fields - Create searchConsoleDataArray 2: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. Array aggregation - response to AI Agent

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Array aggregation - response to AI Agent: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 16. Array aggregation - response to AI Agent1

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Array aggregation - response to AI Agent1: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Assistant to chat with you Search Console Data, using OpenAI and Postgres”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-assistant-to-chat-with-you-search-console-data-using-muse-and-postgres-cc5541/WORKFLOW.json
```
