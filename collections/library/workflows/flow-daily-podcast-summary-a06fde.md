# Daily Podcast Summary

Complete “Daily Podcast Summary” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Daily Podcast Summary.
- The selected records, date range, and output destination.
- Complete the named fields in flow-daily-podcast-summary-a06fde/INPUTS.json.
- Configured connections or tools for gmail, http, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Genre

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Genre: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. TaddyTopDaily

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** TaddyTopDaily: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 5. Download Podcast

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Download Podcast: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Request Audio Crop

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Request Audio Crop: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 7. Get Download Link

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-11 (main, branch 0, input 0).

**Carry forward:** Get Download Link: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. Wait

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 1, input 0).

**Carry forward:** Wait: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 9. If Downloads Ready

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** If Downloads Ready: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Gmail

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Gmail: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Download Cut MP3

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Download Cut MP3: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Whisper Transcribe Audio

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Whisper Transcribe Audio: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Final Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Final Data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Merge Results

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Merge Results: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 15. HTML

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** HTML: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 16. Summarize Podcast

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Summarize Podcast: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Daily Podcast Summary”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-daily-podcast-summary-a06fde/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-daily-podcast-summary-a06fde/WORKFLOW.json
```
