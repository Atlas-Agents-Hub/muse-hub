# Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI

Complete “Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/INPUTS.json.
- Configured connections or tools for googlesheets, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. DeepSeek Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** DeepSeek Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Set Parameters

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Set Parameters: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Get reviews

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Get reviews: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Extract

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Extract: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 7. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 8. Limit1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Limit1: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 9. Get Google Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = appendOrUpdate. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Get Google Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Get rows

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Get rows: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 11. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Get Single review

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Get Single review: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Extract review

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Extract review: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 14. Information Extractor

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-15 (languageModel, branch 0, input 0).

**Carry forward:** Information Extractor: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 15. Sentiment Analysis

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-16 (languageModel, branch 0, input 0), step-2 (main, branch 0, input 0).

**Carry forward:** Sentiment Analysis: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 16. Update sheet

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = appendOrUpdate. Read `../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-14 (main, branch 1, input 0), step-14 (main, branch 2, input 0), step-1 (data, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Update sheet: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-scrape-trustpilot-reviews-with-muse-analyze-sentiment-d02355/WORKFLOW.json
```
