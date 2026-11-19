# Transcribing Bank Statements To Markdown Using Gemini Vision AI

Complete “Transcribing Bank Statements To Markdown Using Gemini Vision AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Transcribing Bank Statements To Markdown Using Gemini Vision AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/INPUTS.json.
- Configured connections or tools for googledrive, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Google Gemini Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Get Bank Statement

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Bank Statement: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Split PDF into Images

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Split PDF into Images: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Extract Zip File

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Extract Zip File: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 7. Images To List

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Images To List: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. Sort Pages

Read [the pandas method](../skills/pandas-pro/SKILL.md). Sort by the declared keys and directions with an explicit handling rule for missing values. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Sort Pages: Records in the requested stable order.

**Check:** Ties and missing sort keys preserve the intended ordering.

## 9. Resize Images For AI

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = resize. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Resize Images For AI: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 10. Transcribe to Markdown

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0).

**Carry forward:** Transcribe to Markdown: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. Combine All Pages

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Combine All Pages: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 12. Extract All Deposit Table Rows

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-9 (languageModel, branch 0, input 0).

**Carry forward:** Extract All Deposit Table Rows: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Transcribing Bank Statements To Markdown Using Gemini Vision AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-transcribing-bank-statements-to-markdown-using-muse-vision-ai-db9032/WORKFLOW.json
```
