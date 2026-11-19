# 🤖🧑 💻 Assistant for Top n8n Creators Leaderboard Reporting

Complete “🤖🧑 💻 Assistant for Top n8n Creators Leaderboard Reporting” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for 🤖🧑 💻 Assistant for Top n8n Creators Leaderboard Reporting.
- The selected records, date range, and output destination.
- Complete the named fields in flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/INPUTS.json.
- Configured connections or tools for gmail, googledrive, http, scheduler, telegram, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. gpt-4o-mini

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** gpt-4o-mini: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. When Executed by Another Workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When Executed by Another Workflow: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Workflow Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Workflow Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. n8n Creators Stats Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-7 (languageModel, branch 0, input 0), step-9 (tool, branch 0, input 0), step-20 (main, branch 0, input 0).

**Carry forward:** n8n Creators Stats Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Global Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Global Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. stats_aggregate_creators

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** stats_aggregate_creators: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. creator-summary

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = toText. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** creator-summary: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 10. stats_aggregate_workflows

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** stats_aggregate_workflows: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Google Drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = createFromText. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Google Drive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. Convert Markdown to HTML

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: mode = markdownToHtml. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Convert Markdown to HTML: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 13. Create Top 10 Workflows List

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (languageModel, branch 0, input 0), step-25 (main, branch 0, input 0).

**Carry forward:** Create Top 10 Workflows List: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Save creator-summary.md

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = write. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Save creator-summary.md: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 15. Convert Top 10 Markdown to HTML

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: mode = markdownToHtml. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** Convert Top 10 Markdown to HTML: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 16. Gmail Creators & Workflows Report

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Gmail Creators & Workflows Report: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 17. Telegram Top 10 Workflows List

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** Telegram Top 10 Workflows List: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 18. Parse Workflow Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Parse Workflow Data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 19. Parse Creators Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Parse Creators Data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 20. Split Out Creators

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Split Out Creators: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 21. Split Out Workflows

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Split Out Workflows: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 22. Gmail Top 10 Workflows List

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Gmail Top 10 Workflows List: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 23. Sort By Top Weekly Creator Inserts

Read [the pandas method](../skills/pandas-pro/SKILL.md). Sort by the declared keys and directions with an explicit handling rule for missing values. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Sort By Top Weekly Creator Inserts: Records in the requested stable order.

**Check:** Ties and missing sort keys preserve the intended ordering.

## 24. Sort By Top Weekly Workflow Inserts

Read [the pandas method](../skills/pandas-pro/SKILL.md). Sort by the declared keys and directions with an explicit handling rule for missing values. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Sort By Top Weekly Workflow Inserts: Records in the requested stable order.

**Check:** Ties and missing sort keys preserve the intended ordering.

## 25. Take Top 10 Creators

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Take Top 10 Creators: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 26. Take Top 50 Workflows

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Take Top 50 Workflows: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 27. Creators Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Creators Data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 28. Workflows Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Workflows Data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 29. Merge Creators & Workflows

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-14 (main, branch 0, input 1).

**Carry forward:** Merge Creators & Workflows: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 30. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 31. Workflow Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Workflow Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “🤖🧑 💻 Assistant for Top n8n Creators Leaderboard Reporting”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-assistant-for-top-muse-creators-leaderboard-reporting-f2f79a/WORKFLOW.json
```
