# Chat with your event schedule from Google Sheets in Telegram

Complete “Chat with your event schedule from Google Sheets in Telegram” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Chat with your event schedule from Google Sheets in Telegram.
- The selected records, date range, and output destination.
- Complete the named fields in flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/INPUTS.json.
- Configured connections or tools for googlesheets, telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. n8nInput

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** n8nInput: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. LLM

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** LLM: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. telegramInput

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** telegramInput: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. SendTyping

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendChatAction. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** SendTyping: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 5. n8nChatSettings

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** n8nChatSettings: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. telegramChatSettings

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** telegramChatSettings: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Settings

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-8 (main, branch 0, input 0).

**Carry forward:** Settings: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-3 (data, branch 0, input 0).

**Carry forward:** Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 9. Schedule

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Schedule: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. ScheduleToMarkdown

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** ScheduleToMarkdown: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 11. ScheduleBot

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-14 (languageModel, branch 0, input 0), step-15 (memory, branch 0, input 0), step-5 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** ScheduleBot: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. SetResponse

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** SetResponse: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 14. telegramResponse

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0), step-3 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** telegramResponse: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 15. n8nResponse

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** n8nResponse: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Chat with your event schedule from Google Sheets in Telegram”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-chat-with-your-event-schedule-from-google-sheets-in-telegram-ab2a56/WORKFLOW.json
```
