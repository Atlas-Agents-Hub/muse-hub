# Obsidian Notes Read Aloud using AI Available as a Podcast Feed

Complete “Obsidian Notes Read Aloud using AI Available as a Podcast Feed” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Obsidian Notes Read Aloud using AI Available as a Podcast Feed.
- The selected records, date range, and output destination.
- Complete the named fields in flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/INPUTS.json.
- Configured connections or tools for googlesheets, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Webhook GET Note

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook GET Note: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Webhook GET Podcast Feed

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook GET Podcast Feed: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. OpenAI1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = audio. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** OpenAI1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 4. Get Items from Google Sheets

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Get Items from Google Sheets: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. Manually Enter Other Data for Podcast Feed

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Manually Enter Other Data for Podcast Feed: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Give Audio Unique Name

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Give Audio Unique Name: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Write RSS Feed

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Write RSS Feed: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. Upload Audio to Cloudinary

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Upload Audio to Cloudinary: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Send Audio to Obsidian

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Send Audio to Obsidian: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 11. Return Podcast Feed to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Return Podcast Feed to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 12. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 1), step-4 (main, branch 0, input 0).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 13. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 14. Rename Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Rename Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. Append Item to Google Sheet

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Append Item to Google Sheet: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Obsidian Notes Read Aloud using AI Available as a Podcast Feed”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-obsidian-notes-read-aloud-using-ai-available-as-a-podcast-feed-19e4c9/WORKFLOW.json
```
