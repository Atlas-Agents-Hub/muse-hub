# Conversational Interviews with AI Agents and n8n Forms

Complete “Conversational Interviews with AI Agents and n8n Forms” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Conversational Interviews with AI Agents and n8n Forms.
- The selected records, date range, and output destination.
- Complete the named fields in flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/INPUTS.json.
- Configured connections or tools for googlesheets, redis.
- An available model or embedding capability with the requested format and cost limits.

## 1. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Groq Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Groq Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Start Interview

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Start Interview: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Query By Session

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Query By Session: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. UUID

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** UUID: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 6. Create Session

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = set. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Create Session: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Valid Session?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0).

**Carry forward:** Valid Session?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 8. Window Buffer Memory2

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-9 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory2: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 9. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-9 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 10. Generate Row2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Generate Row2: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. 404 Not Found

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** 404 Not Found: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 12. Show Transcript

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Show Transcript: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 13. Update Session

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = push. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Update Session: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 14. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-25 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 15. Set Interview Topic

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Set Interview Topic: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. Stop Interview?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Stop Interview?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 17. Update Session1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = push. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Update Session1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 18. Generate Row

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-23 (data, branch 0, input 0).

**Carry forward:** Generate Row: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 19. AI Researcher

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-24 (languageModel, branch 0, input 0), step-5 (main, branch 0, input 0), step-8 (main, branch 0, input 0), step-17 (memory, branch 0, input 0).

**Carry forward:** AI Researcher: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 20. Parse Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Parse Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. Send Reply To Agent

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Send Reply To Agent: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 22. Get Answer

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 1, input 0).

**Carry forward:** Get Answer: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 23. Update Session2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = push. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Update Session2: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 24. Redirect to Completion Screen

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Operation settings: operation = completion. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Redirect to Completion Screen: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 25. Save to Google Sheet

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0), step-6 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Save to Google Sheet: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 26. Session to List

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Session to List: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 27. Messages To JSON

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0), step-6 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Messages To JSON: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 28. Generate Row1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Generate Row1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 29. Get Session

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Get Session: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 30. Clear For Next Interview

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Operation settings: mode = delete. Read `../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-18 (memory, branch 0, input 0).

**Carry forward:** Clear For Next Interview: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Conversational Interviews with AI Agents and n8n Forms”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-conversational-interviews-with-ai-agents-and-muse-forms-ce5de8/WORKFLOW.json
```
