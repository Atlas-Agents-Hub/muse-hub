# Scrape and summarize webpages with AI

Complete “Scrape and summarize webpages with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Scrape and summarize webpages with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-scrape-and-summarize-webpages-with-ai-471156/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Execute Workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Execute Workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 3. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Fetch essay list

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Fetch essay list: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 6. Extract essay names

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Extract essay names: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 7. Split out into items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Split out into items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 8. Limit to first 3

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Limit to first 3: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 9. Fetch essay texts

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Fetch essay texts: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Summarization Chain

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Summarize the selected source with its required sections, audience, and length while retaining consequential details. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-11 (languageModel, branch 0, input 0), step-9 (document, branch 0, input 0).

**Carry forward:** Summarization Chain: A summary linked to its source material.

**Check:** Names, quantities, dates, and key conclusions match the source.

## 11. Extract title

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Extract title: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 12. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-13 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 13. Clean up

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Clean up: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Scrape and summarize webpages with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-scrape-and-summarize-webpages-with-ai-471156/WORKFLOW.json
```
