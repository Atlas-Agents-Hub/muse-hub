# AI product imagines

Complete “AI product imagines” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for AI product imagines.
- The selected records, date range, and output destination.
- Complete the named fields in flow-ai-product-imagines-355242/INPUTS.json.
- Configured connections or tools for googledrive, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Google Drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = fileFolder. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Google Drive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Google Drive1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Google Drive1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Google Drive2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = fileFolder. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Google Drive2: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Google Drive3

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Google Drive3: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 9. OpenAI1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** OpenAI1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. OpenAI2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** OpenAI2: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. AI prompt agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (languageModel, branch 0, input 0), step-10 (outputParser, branch 0, input 0), step-16 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** AI prompt agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 13. HTTP Request1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** HTTP Request1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 14. Loop Over Items1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-17 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 15. Wait

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 1, input 0).

**Carry forward:** Wait: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 16. Convert to File

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = toBinary. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Convert to File: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 17. Google Drive4

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Google Drive4: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “AI product imagines”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-ai-product-imagines-355242/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-ai-product-imagines-355242/WORKFLOW.json
```
