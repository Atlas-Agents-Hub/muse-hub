# 🤖🧠 Assistant Chatbot + LONG TERM Memory + Note Storage + Telegram

Complete “🤖🧠 Assistant Chatbot + LONG TERM Memory + Note Storage + Telegram” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for 🤖🧠 Assistant Chatbot + LONG TERM Memory + Note Storage + Telegram.
- The selected records, date range, and output destination.
- Complete the named fields in flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/INPUTS.json.
- Configured connections or tools for googledocs, telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Save Notes

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Save Notes: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 3. gpt-4o-mini

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** gpt-4o-mini: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Save Long Term Memories

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Save Long Term Memories: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 5. Retrieve Notes

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Retrieve Notes: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 7. Retrieve Long Term Memories

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Retrieve Long Term Memories: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 1), step-6 (main, branch 0, input 0).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 9. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 10. AI Tools Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-10 (tool, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-4 (memory, branch 0, input 0), step-5 (tool, branch 0, input 0), step-1 (data, branch 0, input 0). Branch 1 ends here; return its result without continuing to another operation.

**Carry forward:** AI Tools Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. Chat Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Chat Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Telegram Response

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Telegram Response: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “🤖🧠 Assistant Chatbot + LONG TERM Memory + Note Storage + Telegram”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-assistant-chatbot-long-term-memory-note-storage-telegram-5c8aeb/WORKFLOW.json
```
