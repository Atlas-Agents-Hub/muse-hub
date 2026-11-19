# Narrating over a Video using Multimodal AI

Complete “Narrating over a Video using Multimodal AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Narrating over a Video using Multimodal AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-narrating-over-a-video-using-multimodal-ai-4e397f/INPUTS.json.
- Configured connections or tools for googledrive, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Download Video

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Download Video: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Capture Frames

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Capture Frames: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. Split Out Frames

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Split Out Frames: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 6. For Every 15 Frames

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-9 (main, branch 0, input 0).

**Carry forward:** For Every 15 Frames: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 7. Resize Frame

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = resize. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Resize Frame: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 8. Aggregate Frames

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Aggregate Frames: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 9. Generate Narration Script

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-1 (languageModel, branch 0, input 0).

**Carry forward:** Generate Narration Script: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Convert to Binary

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = toBinary. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** Convert to Binary: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 11. Stay Within Service Limits

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Stay Within Service Limits: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 12. Use Text-to-Speech

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = audio. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Use Text-to-Speech: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Combine Script

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Combine Script: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 14. Upload to GDrive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Upload to GDrive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Narrating over a Video using Multimodal AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-narrating-over-a-video-using-multimodal-ai-4e397f/WORKFLOW.json
```
