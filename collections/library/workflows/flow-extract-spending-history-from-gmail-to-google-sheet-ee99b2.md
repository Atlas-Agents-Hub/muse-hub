# Extract spending history from gmail to google sheet

Complete “Extract spending history from gmail to google sheet” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Extract spending history from gmail to google sheet.
- The selected records, date range, and output destination.
- Complete the named fields in flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/INPUTS.json.
- Configured connections or tools for googlesheets.
- An available model or embedding capability with the requested format and cost limits.

## 1. Get invoice

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get invoice: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Groq Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Groq Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Get payment

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get payment: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Structured Output Parser1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser1: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 6. Google Gemini Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 7. Extract invoice

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Extract invoice: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 8. Extract payment

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Extract payment: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 9. Invoice data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Invoice data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Payment data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Payment data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-14 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Set data 1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** Set data 1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Set data 2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 2, input 0).

**Carry forward:** Set data 2: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. HTML

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** HTML: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 15. Extract details1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-16 (languageModel, branch 0, input 0), step-17 (outputParser, branch 0, input 0).

**Carry forward:** Extract details1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 16. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 17. Set data 0

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-15 (data, branch 0, input 0).

**Carry forward:** Set data 0: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 18. Send1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Send1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-11 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 20. Extract details

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-8 (languageModel, branch 0, input 0), step-7 (outputParser, branch 0, input 0).

**Carry forward:** Extract details: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 21. Send

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Send: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Extract spending history from gmail to google sheet”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-extract-spending-history-from-gmail-to-google-sheet-ee99b2/WORKFLOW.json
```
