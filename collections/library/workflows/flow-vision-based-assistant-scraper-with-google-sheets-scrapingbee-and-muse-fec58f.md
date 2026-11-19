# ✨ Vision-Based Assistant Scraper - with Google Sheets, ScrapingBee, and Gemini

Complete “✨ Vision-Based Assistant Scraper - with Google Sheets, ScrapingBee, and Gemini” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for ✨ Vision-Based Assistant Scraper - with Google Sheets, ScrapingBee, and Gemini.
- The selected records, date range, and output destination.
- Complete the named fields in flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/INPUTS.json.
- Configured connections or tools for googlesheets, http, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. HTML-Scraping Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** HTML-Scraping Tool: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. HTML-based Scraping Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** HTML-based Scraping Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Set fields - from AI agent query

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Set fields - from AI agent query: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Google Sheets - Get list of URLs

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Google Sheets - Get list of URLs: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. ScrapingBee- Get page HTML

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** ScrapingBee- Get page HTML: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Set fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Set fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. HTML to Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** HTML to Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 11. ScrapingBee - Get page screenshot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** ScrapingBee - Get page screenshot: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Vision-based Scraping Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-4 (languageModel, branch 0, input 0), step-9 (tool, branch 0, input 0), step-3 (outputParser, branch 0, input 0), step-8 (main, branch 0, input 0).

**Carry forward:** Vision-based Scraping Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 14. Google Sheets - Create Rows

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Google Sheets - Create Rows: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “✨ Vision-Based Assistant Scraper - with Google Sheets, ScrapingBee, and Gemini”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-vision-based-assistant-scraper-with-google-sheets-scrapingbee-and-muse-fec58f/WORKFLOW.json
```
