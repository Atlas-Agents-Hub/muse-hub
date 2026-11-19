# Chat Assistant (OpenAI assistant) with Postgres Memory And API Calling Capabalities

Complete “Chat Assistant (OpenAI assistant) with Postgres Memory And API Calling Capabalities” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Chat Assistant (OpenAI assistant) with Postgres Memory And API Calling Capabalities.
- The selected records, date range, and output destination.
- Complete the named fields in flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/INPUTS.json.
- Configured connections or tools for http, mysql.
- An available model or embedding capability with the requested format and cost limits.

## 1. External API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** External API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 2. Chat Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Products in Daatabase

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = executeQuery. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Products in Daatabase: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Knowledge Base

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Knowledge Base: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 6. Postgres Chat Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (data, branch 0, input 0).

**Carry forward:** Postgres Chat Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 7. Postgres Chat Memory1

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (data, branch 0, input 0).

**Carry forward:** Postgres Chat Memory1: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 8. Edit Fields1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Edit Fields1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = assistant. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-7 (memory, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Edit Fields2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Edit Fields2: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. OpenAI2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = assistant. Read `../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 1, input 0), step-3 (main, branch 0, input 0), step-10 (tool, branch 0, input 0), step-9 (tool, branch 0, input 0), step-6 (memory, branch 0, input 0), step-8 (tool, branch 0, input 0).

**Carry forward:** OpenAI2: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Chat Assistant (OpenAI assistant) with Postgres Memory And API Calling Capabalities”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-chat-assistant-muse-assistant-with-postgres-memory-and-api-calling-capabalitie-940080/WORKFLOW.json
```
