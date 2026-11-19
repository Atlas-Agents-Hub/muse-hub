# Easy Image Captioning with Gemini 1.5 Pro

Complete “Easy Image Captioning with Gemini 1.5 Pro” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Easy Image Captioning with Gemini 1.5 Pro.
- The selected records, date range, and output destination.
- Complete the named fields in flow-easy-image-captioning-with-muse-1-5-pro-c06a19/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Get Image

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Image: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Get Info

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = information. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Get Info: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 6. Resize For AI

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = resize. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Resize For AI: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 7. Image Captioning Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-3 (outputParser, branch 0, input 0).

**Carry forward:** Image Captioning Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Merge Image & Caption

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-11 (main, branch 0, input 1).

**Carry forward:** Merge Image & Caption: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 9. Calculate Positioning

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Calculate Positioning: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. Merge Caption & Positions

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 1), step-8 (main, branch 0, input 0).

**Carry forward:** Merge Caption & Positions: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 11. Apply Caption to Image

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = multiStep. Read `../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Apply Caption to Image: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Easy Image Captioning with Gemini 1.5 Pro”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-easy-image-captioning-with-muse-1-5-pro-c06a19/WORKFLOW.json
```
