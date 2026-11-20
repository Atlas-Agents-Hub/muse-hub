# Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB

Complete “Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB.
- The selected records, date range, and output destination.
- Complete the named fields in flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/INPUTS.json.
- Configured connections or tools for http, nocodb, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule Trigger each week

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger each week: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Retrieve the web page for further processsing

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Retrieve the web page for further processsing: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 3. Extract the HTML with the right css class

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Extract the HTML with the right css class: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Extract date

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Extract date: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 5. Create single link items

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Create single link items: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 6. Create single date items

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Create single date items: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 7. Merge date & links

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-17 (main, branch 0, input 1).

**Carry forward:** Merge date & links: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 8. Select posts of last 7 days

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Select posts of last 7 days: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. HTTP Request1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** HTTP Request1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Extract individual posts

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Extract individual posts: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 11. Merge Content with Date & Link

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-8 (main, branch 0, input 1).

**Carry forward:** Merge Content with Date & Link: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 12. Summary

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Summary: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Keywords

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Keywords: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Rename keywords

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Rename keywords: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. Rename Summary

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Rename Summary: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-4 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 17. Merge ChatGPT output with Date & Link

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 1), step-11 (main, branch 0, input 0).

**Carry forward:** Merge ChatGPT output with Date & Link: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 18. NocoDB news database

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** NocoDB news database: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-scrape-and-summarize-posts-of-a-news-site-without-rss-feed-using-ai-and-save-t-105d3c/WORKFLOW.json
```
