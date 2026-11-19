# Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack

Complete “Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack.
- The selected records, date range, and output destination.
- Complete the named fields in flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/INPUTS.json.
- Configured connections or tools for googlesheets, http, rssfeedread, scheduler, slack.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 4. Google Sheets - Get article monitored database

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Google Sheets - Get article monitored database: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Set field - existing_url

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Set field - existing_url: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Google Sheets - Get RSS Feed url followed

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Google Sheets - Get RSS Feed url followed: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. RSS Read

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** RSS Read: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Code

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Code: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. No Operation, do nothing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** No Operation, do nothing: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 11. Relevance Classification for Topic Monitoring

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-14 (languageModel, branch 0, input 0).

**Carry forward:** Relevance Classification for Topic Monitoring: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 12. Jina AI - Read URL

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Jina AI - Read URL: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Set fields - Not relevant articles

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Set fields - Not relevant articles: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Google Sheets - Add relevant articles

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Google Sheets - Add relevant articles: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 15. Basic LLM Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (languageModel, branch 0, input 0), step-12 (main, branch 0, input 0).

**Carry forward:** Basic LLM Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 16. Set Fields - Relevant Articles

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-5 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Set Fields - Relevant Articles: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Slack1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Slack1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 18. Google Sheets - Add relevant article

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Google Sheets - Add relevant article: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-information-monitoring-with-muse-google-sheets-jina-ai-and-slack-2106de/WORKFLOW.json
```
