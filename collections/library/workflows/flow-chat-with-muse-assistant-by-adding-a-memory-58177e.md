# Chat with OpenAI Assistant (by adding a memory)

Complete “Chat with OpenAI Assistant (by adding a memory)” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Chat with OpenAI Assistant (by adding a memory).
- The selected records, date range, and output destination.
- Complete the named fields in flow-chat-with-muse-assistant-by-adding-a-memory-58177e/INPUTS.json.
- An available model or embedding capability with the requested format and cost limits.

## 1. Calculator

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Calculator: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 2. Chat Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-9 (memory, branch 0, input 0).

**Carry forward:** Chat Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 4. OpenAI Assistant

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (tool, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** OpenAI Assistant: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 5. Chat Memory Manager

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-9 (memory, branch 0, input 0).

**Carry forward:** Chat Memory Manager: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 6. Chat Memory Manager1

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Operation settings: mode = insert. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-9 (memory, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Chat Memory Manager1: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 7. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 8. Edit Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Edit Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Limit

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Limit: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Chat with OpenAI Assistant (by adding a memory)”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-chat-with-muse-assistant-by-adding-a-memory-58177e/WORKFLOW.json
```
