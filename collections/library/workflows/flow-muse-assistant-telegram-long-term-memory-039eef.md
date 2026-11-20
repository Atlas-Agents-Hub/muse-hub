# 🐋🤖 DeepSeek Assistant + Telegram + LONG TERM Memory 🧠

Complete “🐋🤖 DeepSeek Assistant + Telegram + LONG TERM Memory 🧠” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for 🐋🤖 DeepSeek Assistant + Telegram + LONG TERM Memory 🧠.
- The selected records, date range, and output destination.
- Complete the named fields in flow-muse-assistant-telegram-long-term-memory-039eef/INPUTS.json.
- Configured connections or tools for googledocs, telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. Save Long Term Memories

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Save Long Term Memories: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 2. DeepSeek-V3 Chat

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** DeepSeek-V3 Chat: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Listen for Telegram Events

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Listen for Telegram Events: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Validation

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Validation: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Check User & Chat ID

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Check User & Chat ID: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 6. Message Router

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0). Branch 0, 2 ends here; return its result without continuing to another operation.

**Carry forward:** Message Router: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Retrieve Long Term Memories

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0).

**Carry forward:** Retrieve Long Term Memories: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Error message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 3, input 0), step-1 (main, branch 1, input 0).

**Carry forward:** Error message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0), step-12 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 10. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-15 (languageModel, branch 0, input 0), step-11 (tool, branch 0, input 0), step-12 (data, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. Telegram Response

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Telegram Response: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. Response Error message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 1, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Response Error message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “🐋🤖 DeepSeek Assistant + Telegram + LONG TERM Memory 🧠”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-muse-assistant-telegram-long-term-memory-039eef/WORKFLOW.json
```
