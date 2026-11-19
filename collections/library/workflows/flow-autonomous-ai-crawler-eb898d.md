# Autonomous AI crawler

Complete “Autonomous AI crawler” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Autonomous AI crawler.
- The selected records, date range, and output destination.
- Complete the named fields in flow-autonomous-ai-crawler-eb898d/INPUTS.json.
- Configured connections or tools for http, supabase, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Text

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Text: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 2. Set domain (text)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Set domain (text): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Set domain (URL)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Set domain (URL): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. JSON Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** JSON Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 6. Execute workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute workflow: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 7. Add protocool to domain (text)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Add protocool to domain (text): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Add protocool to domain (URL)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Add protocool to domain (URL): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Get companies

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Get companies: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. URLs

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-27 (data, branch 0, input 0).

**Carry forward:** URLs: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 11. Get website (text)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Get website (text): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Get website (URL)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** Get website (URL): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Select company name and website

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Select company name and website: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Convert HTML to Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Convert HTML to Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 15. Retrieve URLs

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Retrieve URLs: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 16. Crawl website

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-1 (tool, branch 0, input 0), step-2 (tool, branch 0, input 0), step-4 (outputParser, branch 0, input 0), step-3 (languageModel, branch 0, input 0), step-8 (main, branch 0, input 0).

**Carry forward:** Crawl website: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 17. Map company name and website

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Map company name and website: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 18. Split out URLs

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Split out URLs: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 19. Set response (text)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Set response (text): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 20. Set social media array

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Set social media array: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. Merge all data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 1), step-5 (main, branch 0, input 0).

**Carry forward:** Merge all data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 22. Filter out empty hrefs

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Filter out empty hrefs: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 23. Insert new row

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Insert new row: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 24. Remove duplicated

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Compare the configured identity fields and keep the selected representative of each distinct record. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Remove duplicated: Distinct records and a duplicate count.

**Check:** Two records with the same identity collapse while different identities remain separate.

## 25. Set domain to path

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-27 (data, branch 0, input 0).

**Carry forward:** Set domain to path: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 26. Filter out invalid URLs

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Filter out invalid URLs: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 27. Aggregate URLs

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Aggregate URLs: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 28. Set response (URL)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Set response (URL): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Autonomous AI crawler”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-autonomous-ai-crawler-eb898d/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-autonomous-ai-crawler-eb898d/WORKFLOW.json
```
