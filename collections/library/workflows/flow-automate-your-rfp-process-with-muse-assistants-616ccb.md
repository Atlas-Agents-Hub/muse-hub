# Automate Your RFP Process with OpenAI Assistants

Complete “Automate Your RFP Process with OpenAI Assistants” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Automate Your RFP Process with OpenAI Assistants.
- The selected records, date range, and output destination.
- Complete the named fields in flow-automate-your-rfp-process-with-muse-assistants-616ccb/INPUTS.json.
- Configured connections or tools for gmail, googledocs, slack.
- An available model or embedding capability with the requested format and cost limits.

## 1. Wait for Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Wait for Request: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Item List Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Item List Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Get RFP Data

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Get RFP Data: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 5. Set Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Set Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Create new RFP Response Document

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Create new RFP Response Document: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Add Metadata to Response Doc

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Add Metadata to Response Doc: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 8. Extract Questions From RFP

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-6 (languageModel, branch 0, input 0), step-2 (outputParser, branch 0, input 0), step-9 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Extract Questions From RFP: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. Record Question & Answer in Response Doc

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Record Question & Answer in Response Doc: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Answer Question with Context

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = assistant. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Answer Question with Context: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. For Each Question...

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-10 (main, branch 0, input 0).

**Carry forward:** For Each Question...: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 12. Send Chat Notification

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Send Chat Notification: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Send Email Notification

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Send Email Notification: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Automate Your RFP Process with OpenAI Assistants”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-automate-your-rfp-process-with-muse-assistants-616ccb/WORKFLOW.json
```
