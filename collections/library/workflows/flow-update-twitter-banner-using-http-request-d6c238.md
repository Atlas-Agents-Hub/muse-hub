# Update Twitter banner using HTTP request

Complete “Update Twitter banner using HTTP request” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Update Twitter banner using HTTP request.
- The selected records, date range, and output destination.
- Complete the named fields in flow-update-twitter-banner-using-http-request-d6c238/INPUTS.json.
- Configured connections or tools for http.

## 1. On clicking 'execute'

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-update-twitter-banner-using-http-request-d6c238/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On clicking 'execute': A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-update-twitter-banner-using-http-request-d6c238/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 3. HTTP Request1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-update-twitter-banner-using-http-request-d6c238/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** HTTP Request1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Check the finished result

Read [the Social Content method](../skills/social-content/SKILL.md). Inspect the complete result against the original task, the selected source, and the requested output format.

**Carry forward:** A checked result with its source and next action.

**Check:** The deliverable addresses the task and matches the selected source material.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Update Twitter banner using HTTP request”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-update-twitter-banner-using-http-request-d6c238/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-update-twitter-banner-using-http-request-d6c238/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-update-twitter-banner-using-http-request-d6c238/WORKFLOW.json
```
