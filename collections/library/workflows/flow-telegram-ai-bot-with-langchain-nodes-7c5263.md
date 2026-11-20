# Telegram AI bot with LangChain nodes

Complete “Telegram AI bot with LangChain nodes” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Telegram AI bot with LangChain nodes.
- The selected records, date range, and output destination.
- Complete the named fields in flow-telegram-ai-bot-with-langchain-nodes-7c5263/INPUTS.json.
- Configured connections or tools for http, telegram, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Listen for incoming events

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Listen for incoming events: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Generate image in Dall-E 3

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Generate image in Dall-E 3: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-6 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 6. Dall-E 3 Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-6 (data, branch 0, input 0).

**Carry forward:** Dall-E 3 Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (tool, branch 0, input 0), step-1 (languageModel, branch 0, input 0), step-2 (memory, branch 0, input 0), step-6 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Send back an image

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendPhoto. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Send back an image: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. Telegram

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-6 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Telegram: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. add response field

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** add response field: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Correct errors

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0), step-11 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Correct errors: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Telegram AI bot with LangChain nodes”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-telegram-ai-bot-with-langchain-nodes-7c5263/WORKFLOW.json
```
