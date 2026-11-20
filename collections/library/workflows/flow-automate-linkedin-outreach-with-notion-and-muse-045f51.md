# Automate LinkedIn Outreach with Notion and OpenAI

Complete “Automate LinkedIn Outreach with Notion and OpenAI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Automate LinkedIn Outreach with Notion and OpenAI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-automate-linkedin-outreach-with-notion-and-muse-045f51/INPUTS.json.
- Configured connections or tools for http, linkedin, notion, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. query entries from Notion table for today

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = databasePage, operation = getAll. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** query entries from Notion table for today: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. get all content from post page

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = block, operation = getAll. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** get all content from post page: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Pull together all text blocks + image

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Pull together all text blocks + image: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 5. Fetch image from post

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Fetch image from post: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Reformat Post Text

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = assistant. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Reformat Post Text: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Combine text+image

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-5 (main, branch 0, input 1).

**Carry forward:** Combine text+image: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 8. Post on LinkedIn

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Post on LinkedIn: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. Set post status to "Done"

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = databasePage, operation = update. Read `../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Set post status to "Done": The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Automate LinkedIn Outreach with Notion and OpenAI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-automate-linkedin-outreach-with-notion-and-muse-045f51/WORKFLOW.json
```
