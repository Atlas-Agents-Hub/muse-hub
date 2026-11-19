# GCF Token Optimization for LLM Tool Responses

Complete “GCF Token Optimization for LLM Tool Responses” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for GCF Token Optimization for LLM Tool Responses.
- The selected records, date range, and output destination.
- Complete the named fields in flow-gcf-token-optimization-for-llm-tool-responses-69f284/INPUTS.json.
- Configured connections or tools for gcf, http.

## 1. When clicking 'Execute workflow'

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking 'Execute workflow': A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. GET /contributors (100 records)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** GET /contributors (100 records): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 3. Batch into Array

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForAllItems. Read `../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Batch into Array: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 4. GCF Encode

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = encode. Read `../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** GCF Encode: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. GCF Decode (lossless)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = decode. Read `../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** GCF Decode (lossless): A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “GCF Token Optimization for LLM Tool Responses”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-gcf-token-optimization-for-llm-tool-responses-69f284/WORKFLOW.json
```
