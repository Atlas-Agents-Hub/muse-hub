# Create dynamic Twitter profile banner

Complete “Create dynamic Twitter profile banner” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Create dynamic Twitter profile banner.
- The selected records, date range, and output destination.
- Complete the named fields in flow-create-dynamic-twitter-profile-banner-202468/INPUTS.json.
- Configured connections or tools for http.

## 1. On clicking 'execute'

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On clicking 'execute': A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Fetch bg

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Fetch bg: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 3. Fetch new followers

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Fetch new followers: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Item Lists

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Item Lists: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 5. Fetching images

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Fetching images: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Resize

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = resize. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Resize: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 7. Crop

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = multiStep. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Crop: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 8. Resize1

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = resize. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Resize1: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 9. Function

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Function: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = mergeByIndex. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-4 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 11. Edit Image

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = multiStep. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Edit Image: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 12. HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Create dynamic Twitter profile banner”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-create-dynamic-twitter-profile-banner-202468/WORKFLOW.json
```
