# UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports

Complete “UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports.
- The selected records, date range, and output destination.
- Complete the named fields in flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/INPUTS.json.
- Configured connections or tools for airtable, gmail, googleanalytics, http, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 3. Google Analytics

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Analytics: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Create UTM Link & Send To Database

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Create UTM Link & Send To Database: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Schedule Google Analytics Report To Marketing Manager

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Google Analytics Report To Marketing Manager: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 6. Google Analytics Data Analysis Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-3 (tool, branch 0, input 0), step-1 (languageModel, branch 0, input 0), step-2 (memory, branch 0, input 0), step-9 (main, branch 0, input 0).

**Carry forward:** Google Analytics Data Analysis Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Set UTM Parameters For Link

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Set UTM Parameters For Link: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Send Summary Report To Marketing Manager

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Send Summary Report To Marketing Manager: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. Create UTM Link With Parameters

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Create UTM Link With Parameters: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. Submit UTM Link To Database

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = upsert. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Submit UTM Link To Database: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Create QR Code With Submitted QR Link

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Create QR Code With Submitted QR Link: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports-86ae4b/WORKFLOW.json
```
