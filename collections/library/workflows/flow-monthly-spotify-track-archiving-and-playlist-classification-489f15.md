# Monthly Spotify Track Archiving and Playlist Classification

Complete “Monthly Spotify Track Archiving and Playlist Classification” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Monthly Spotify Track Archiving and Playlist Classification.
- The selected records, date range, and output destination.
- Complete the named fields in flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/INPUTS.json.
- Configured connections or tools for googlesheets, http, scheduler, spotify.
- An available model or embedding capability with the requested format and cost limits.

## 1. Monthly Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Monthly Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Anthropic Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Anthropic Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Get Playlist

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = playlist, operation = getUserPlaylists. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Get Playlist: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Get Tracks

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = library. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Get Tracks: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Retrieve relevant info

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Retrieve relevant info: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Filter my playlist

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Filter my playlist: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 8. Batch preparation

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Batch preparation: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. Playlists informations

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Playlists informations: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Limit2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Limit2: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 11. Get Track details

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Get Track details: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Get logged playlists

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Get logged playlists: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 13. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 14. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-1 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 15. Excluding logged playlists

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0), step-9 (main, branch 0, input 1).

**Carry forward:** Excluding logged playlists: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 16. Simplify Tracks informations

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Simplify Tracks informations: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Log new playlists

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** Log new playlists: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 18. Limit

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Limit: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 19. Get logged tracks

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Get logged tracks: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 20. Excluding logged tracks

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-14 (main, branch 0, input 1).

**Carry forward:** Excluding logged tracks: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 21. Log new tracks

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Log new tracks: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 22. Classify new tracks

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Classify new tracks: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 23. Aggregate by 200 tracks

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0).

**Carry forward:** Aggregate by 200 tracks: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 24. Basic LLM Chain - AI Classification

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-5 (languageModel, branch 0, input 0), step-22 (main, branch 0, input 0), step-8 (outputParser, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Basic LLM Chain - AI Classification: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 25. Split Out1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Split Out1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 26. Filter

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Filter: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 27. Split Out2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Split Out2: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 28. Batch preparation1

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Batch preparation1: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 29. Manual Verification

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 1), step-29 (main, branch 0, input 0).

**Carry forward:** Manual Verification: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 30. Spotify

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = playlist. Read `../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Spotify: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Monthly Spotify Track Archiving and Playlist Classification”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-monthly-spotify-track-archiving-and-playlist-classification-489f15/WORKFLOW.json
```
