# Assistant to chat with Airtable and analyze data

Complete “Assistant to chat with Airtable and analyze data” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Assistant to chat with Airtable and analyze data.
- The selected records, date range, and output destination.
- Complete the named fields in flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/INPUTS.json.
- Configured connections or tools for airtable, http, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Search records

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Search records: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Process data with code

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Process data with code: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Create map image

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Create map image: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. Get list of bases

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get list of bases: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Get base schema

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get base schema: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 8. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 9. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 10. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 11. Get Bases

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = base. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Get Bases: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-14 (tool, branch 0, input 0), step-18 (tool, branch 0, input 0), step-16 (tool, branch 0, input 0), step-17 (tool, branch 0, input 0), step-1 (languageModel, branch 0, input 0), step-3 (memory, branch 0, input 0), step-15 (tool, branch 0, input 0), step-4 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Get Base/Tables schema

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = base, operation = getSchema. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 1, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Get Base/Tables schema: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 14. If filter description exists

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 2, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** If filter description exists: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 15. OpenAI - Create thread

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 3, input 0).

**Carry forward:** OpenAI - Create thread: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 16. Set schema and prompt

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 1, input 0).

**Carry forward:** Set schema and prompt: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. OpenAI - Send message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** OpenAI - Send message: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 18. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 19. Aggregate1

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Aggregate1: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 20. OpenAI - Generate search filter

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** OpenAI - Generate search filter: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 21. OpenAI - Run assistant

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0), step-30 (data, branch 0, input 0).

**Carry forward:** OpenAI - Run assistant: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 22. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-23 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 23. OpenAI - Get messages

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0), step-30 (data, branch 0, input 0).

**Carry forward:** OpenAI - Get messages: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 24. If1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** If1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 25. Airtable - Search records

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Airtable - Search records: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 26. Aggregate2

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Aggregate2: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 27. OpenAI - Download File

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0).

**Carry forward:** OpenAI - Download File: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 28. Upload file to get link

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Upload file to get link: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 29. Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-8 (main, branch 0, input 0), step-9 (main, branch 0, input 0), step-11 (main, branch 0, input 0), step-22 (main, branch 1, input 0).

**Carry forward:** Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 30. Response1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Response1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Assistant to chat with Airtable and analyze data”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-assistant-to-chat-with-airtable-and-analyze-data-883a86/WORKFLOW.json
```
