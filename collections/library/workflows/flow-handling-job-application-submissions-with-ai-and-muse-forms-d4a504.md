# Handling Job Application Submissions with AI and n8n Forms

Complete “Handling Job Application Submissions with AI and n8n Forms” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Handling Job Application Submissions with AI and n8n Forms.
- The selected records, date range, and output destination.
- Complete the named fields in flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/INPUTS.json.
- Configured connections or tools for airtable, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Step 2 of 2 - Application Form

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Step 2 of 2 - Application Form: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. OpenAI Chat Model2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model2: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Step 1 of 2 - Upload CV

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Step 1 of 2 - Upload CV: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Save to Airtable1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Save to Airtable1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 7. Form Success

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Operation settings: operation = completion. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-10 (main, branch 1, input 0).

**Carry forward:** Form Success: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 8. Extract from File

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-5 (main, branch 0, input 0).

**Carry forward:** Extract from File: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 9. File Upload Retry

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 1, input 0).

**Carry forward:** File Upload Retry: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 10. Classify Document

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-4 (languageModel, branch 0, input 0).

**Carry forward:** Classify Document: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 11. Application Suitability Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-3 (outputParser, branch 0, input 0).

**Carry forward:** Application Suitability Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Redirect To Step 2 of 2

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Operation settings: operation = completion. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Redirect To Step 2 of 2: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 13. Submission Success

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Submission Success: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 14. Save to Airtable

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Save to Airtable: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 15. Upload File to Record

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Upload File to Record: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Handling Job Application Submissions with AI and n8n Forms”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-handling-job-application-submissions-with-ai-and-muse-forms-d4a504/WORKFLOW.json
```
