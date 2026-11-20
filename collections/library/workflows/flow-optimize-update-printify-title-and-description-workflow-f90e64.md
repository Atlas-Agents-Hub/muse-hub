# Optimize & Update Printify Title and Description Workflow

Complete “Optimize & Update Printify Title and Description Workflow” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Optimize & Update Printify Title and Description Workflow.
- The selected records, date range, and output destination.
- Complete the named fields in flow-optimize-update-printify-title-and-description-workflow-f90e64/INPUTS.json.
- Configured connections or tools for googlesheets, http, toolwikipedia.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Google Sheets Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Sheets Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Calculator

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Calculator: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 4. Wikipedia

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Wikipedia: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Brand Guidelines + Custom Instructions

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Brand Guidelines + Custom Instructions: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Printify - Get Shops1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Printify - Get Shops1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. Printify - Get Shops

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Printify - Get Shops: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Printify - Get Products

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Printify - Get Products: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Printify - Update Product

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = PUT. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Printify - Update Product: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 12. GS - Add Product Option

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** GS - Add Product Option: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Update Product Option

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = appendOrUpdate. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-13 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Update Product Option: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 14. If1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** If1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 15. Number of Options

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Number of Options: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. Calculate Options

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-16 (main, branch 0, input 0).

**Carry forward:** Calculate Options: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 17. Remember Options

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Remember Options: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 18. Generate Title and Desc

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-8 (tool, branch 0, input 0), step-7 (tool, branch 0, input 0), step-13 (main, branch 0, input 0), step-10 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Generate Title and Desc: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 19. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-4 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 20. Split - id, title, desc

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0).

**Carry forward:** Split - id, title, desc: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Optimize & Update Printify Title and Description Workflow”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-optimize-update-printify-title-and-description-workflow-f90e64/WORKFLOW.json
```
