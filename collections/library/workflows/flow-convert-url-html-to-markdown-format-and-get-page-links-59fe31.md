# Convert URL HTML to Markdown Format and Get Page Links

Complete “Convert URL HTML to Markdown Format and Get Page Links” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Convert URL HTML to Markdown Format and Get Page Links.
- The selected records, date range, and output destination.
- Complete the named fields in flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/INPUTS.json.
- Configured connections or tools for http.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Get urls from own data source

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get urls from own data source: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 3. Example fields from data source

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Example fields from data source: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Split out page URLs

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Split out page URLs: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 5. 40 items at a time

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** 40 items at a time: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 6. Retrieve Page Markdown and Links

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 1, input 0).

**Carry forward:** Retrieve Page Markdown and Links: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 7. Wait

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Wait: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 8. Connect to your own data source

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Connect to your own data source: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 9. 10 at a time

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-6 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** 10 at a time: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 10. Markdown data and Links

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Markdown data and Links: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Convert URL HTML to Markdown Format and Get Page Links”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-convert-url-html-to-markdown-format-and-get-page-links-59fe31/WORKFLOW.json
```
