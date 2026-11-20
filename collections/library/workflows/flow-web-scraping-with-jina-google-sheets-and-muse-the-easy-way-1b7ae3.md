# Web Scraping with Jina, Google Sheets and OpenAI the EASY way

Complete “Web Scraping with Jina, Google Sheets and OpenAI the EASY way” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Web Scraping with Jina, Google Sheets and OpenAI the EASY way.
- The selected records, date range, and output destination.
- Complete the named fields in flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/INPUTS.json.
- Configured connections or tools for googlesheets, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Test workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Test workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Jina Fetch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Jina Fetch: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Information Extractor

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-4 (languageModel, branch 0, input 0).

**Carry forward:** Information Extractor: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 5. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 6. Save to Google Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Save to Google Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Web Scraping with Jina, Google Sheets and OpenAI the EASY way”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-web-scraping-with-jina-google-sheets-and-muse-the-easy-way-1b7ae3/WORKFLOW.json
```
