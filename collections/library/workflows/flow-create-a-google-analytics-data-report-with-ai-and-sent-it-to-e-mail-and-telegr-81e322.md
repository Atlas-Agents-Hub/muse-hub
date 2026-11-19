# Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram

Complete “Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram.
- The selected records, date range, and output destination.
- Complete the named fields in flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/INPUTS.json.
- Configured connections or tools for emailsend, googleanalytics, scheduler, telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Calculator

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Calculator: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Google Analytics Letzte 7 Tage

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Google Analytics Letzte 7 Tage: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Assign data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Assign data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Summarize Data

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Summarize Data: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 6. Calculation same period previous year

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Calculation same period previous year: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. Google Analytics: Past 7 days of the previous year

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Google Analytics: Past 7 days of the previous year: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Assign data1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Assign data1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Summarize Data1

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Summarize Data1: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 10. Processing for email

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-6 (tool, branch 0, input 0), step-9 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Processing for email: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. Send Email

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Send Email: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. Processing for Telegram

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Processing for Telegram: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Telegram

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Telegram: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-create-a-google-analytics-data-report-with-ai-and-sent-it-to-e-mail-and-telegr-81e322/WORKFLOW.json
```
