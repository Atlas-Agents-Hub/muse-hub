# Automated Hugging Face Paper Summary Fetching & Categorization Workflow

Complete “Automated Hugging Face Paper Summary Fetching & Categorization Workflow” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Automated Hugging Face Paper Summary Fetching & Categorization Workflow.
- The selected records, date range, and output destination.
- Complete the named fields in flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/INPUTS.json.
- Configured connections or tools for http.

## 1. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Image URL hardcode

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Image URL hardcode: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Variables for medoids

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Variables for medoids: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Total Points in Collection

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Total Points in Collection: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Each Crop Counts

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Each Crop Counts: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Info About Crop Labeled Clusters

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Info About Crop Labeled Clusters: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Embed image

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Embed image: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. Get similarity of medoids

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-4 (data, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Get similarity of medoids: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Compare scores

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Compare scores: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Automated Hugging Face Paper Summary Fetching & Categorization Workflow”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-automated-hugging-face-paper-summary-fetching-categorization-workflow-3e96ac/WORKFLOW.json
```
