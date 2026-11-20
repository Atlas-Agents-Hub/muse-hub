# CV Resume PDF Parsing with Multimodal Vision AI

Complete “CV Resume PDF Parsing with Multimodal Vision AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for CV Resume PDF Parsing with Multimodal Vision AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/INPUTS.json.
- Configured connections or tools for googledrive, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Download Resume

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Download Resume: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. PDF-to-Image API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** PDF-to-Image API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Resize Converted Image

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = resize. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Resize Converted Image: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 7. Candidate Resume Analyser

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-7 (languageModel, branch 0, input 0), step-2 (outputParser, branch 0, input 0).

**Carry forward:** Candidate Resume Analyser: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Should Proceed To Stage 2?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Should Proceed To Stage 2?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “CV Resume PDF Parsing with Multimodal Vision AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-cv-resume-pdf-parsing-with-multimodal-vision-ai-b0887f/WORKFLOW.json
```
