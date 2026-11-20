# Qualify replies from Pipedrive persons with AI

Complete “Qualify replies from Pipedrive persons with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Qualify replies from Pipedrive persons with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/INPUTS.json.
- Configured connections or tools for pipedrive.
- An available model or embedding capability with the requested format and cost limits.

## 1. Email box 2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Email box 2: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Email box 1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Email box 1: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Get email

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-10 (main, branch 0, input 0).

**Carry forward:** Get email: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Search Person in CRM

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = person, operation = search. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Search Person in CRM: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Get person from CRM

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = person, operation = get. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get person from CRM: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. In campaign?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** In campaign?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Is interested?

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Is interested?: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Get response

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Get response: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. IF interested

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** IF interested: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Create deal in CRM

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Create deal in CRM: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Qualify replies from Pipedrive persons with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-qualify-replies-from-pipedrive-persons-with-ai-c7d721/WORKFLOW.json
```
