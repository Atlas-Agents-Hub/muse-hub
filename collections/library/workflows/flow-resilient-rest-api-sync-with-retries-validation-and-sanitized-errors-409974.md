# Resilient REST API Sync with Retries, Validation, and Sanitized Errors

Complete “Resilient REST API Sync with Retries, Validation, and Sanitized Errors” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Resilient REST API Sync with Retries, Validation, and Sanitized Errors.
- The selected records, date range, and output destination.
- Complete the named fields in flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/INPUTS.json.
- Configured connections or tools for http.

## 1. Run Demo

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Run Demo: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Set Demo Configuration

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set Demo Configuration: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Fetch API Records

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Fetch API Records: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Normalize and Validate Records

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Normalize and Validate Records: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. Validated Records

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Validated Records: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 6. Sanitize Failure

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0), step-4 (main, branch 1, input 0).

**Carry forward:** Sanitize Failure: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. Failure Record

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Failure Record: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Resilient REST API Sync with Retries, Validation, and Sanitized Errors”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-resilient-rest-api-sync-with-retries-validation-and-sanitized-errors-409974/WORKFLOW.json
```
