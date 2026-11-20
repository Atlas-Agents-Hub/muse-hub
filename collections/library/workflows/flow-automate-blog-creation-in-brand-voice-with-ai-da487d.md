# Automate Blog Creation in Brand Voice with AI

Complete “Automate Blog Creation in Brand Voice with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Automate Blog Creation in Brand Voice with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-automate-blog-creation-in-brand-voice-with-ai-da487d/INPUTS.json.
- Configured connections or tools for http, wordpress.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. OpenAI Chat Model2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model2: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Get Blog

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Blog: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Extract Article URLs

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Extract Article URLs: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 7. Split Out URLs

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Split Out URLs: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 8. Latest Articles

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Latest Articles: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 9. Get Article

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Get Article: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Extract Article Content

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Extract Article Content: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 11. Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 12. Combine Articles

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Combine Articles: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 13. Capture Existing Article Structure

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-4 (languageModel, branch 0, input 0).

**Carry forward:** Capture Existing Article Structure: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Extract Voice Characteristics

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0).

**Carry forward:** Extract Voice Characteristics: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 15. Article Style & Brand Voice

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 1), step-15 (main, branch 0, input 0).

**Carry forward:** Article Style & Brand Voice: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 16. New Article Instruction

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** New Article Instruction: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Content Generation Agent

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-3 (languageModel, branch 0, input 0), step-18 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Content Generation Agent: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 18. Save as Draft

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Save as Draft: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Automate Blog Creation in Brand Voice with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-automate-blog-creation-in-brand-voice-with-ai-da487d/WORKFLOW.json
```
