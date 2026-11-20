# Generate a product image with Magic Hour

Complete “Generate a product image with Magic Hour” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Generate a product image with Magic Hour.
- The selected records, date range, and output destination.
- Complete the named fields in flow-generate-a-product-image-with-magic-hour-c370f4/INPUTS.json.
- Configured connections or tools for http, magichour.

## 1. Run manually

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Run manually: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Magic Hour

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = image, operation = generate. Read `../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Magic Hour: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Require complete

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Require complete: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. Download result

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Download result: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Stop incomplete job

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Stop incomplete job: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Generate a product image with Magic Hour”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-generate-a-product-image-with-magic-hour-c370f4/WORKFLOW.json
```
