# Generate Seedance videos with Vancine API and bounded polling

Complete “Generate Seedance videos with Vancine API and bounded polling” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Generate Seedance videos with Vancine API and bounded polling.
- The selected records, date range, and output destination.
- Complete the named fields in flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/INPUTS.json.
- Configured connections or tools for http.

## 1. manualTrigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** manualTrigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. setFields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** setFields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. submitTask

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** submitTask: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. saveTaskId

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** saveTaskId: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. ifCompleted

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** ifCompleted: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 6. ifFailed

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** ifFailed: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. ifTimeout

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0).

**Carry forward:** ifTimeout: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 8. continuePolling

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 1, input 0).

**Carry forward:** continuePolling: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. waitInterval

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-16 (main, branch 0, input 0).

**Carry forward:** waitInterval: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 10. pollTask

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** pollTask: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. carryState

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** carryState: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. mergeResults

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = append. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-7 (main, branch 0, input 1).

**Carry forward:** mergeResults: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 13. mergeState

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForAllItems. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** mergeState: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 14. outputResult

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** outputResult: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. failNode

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** failNode: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 16. timeoutFail

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** timeoutFail: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Generate Seedance videos with Vancine API and bounded polling”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-generate-seedance-videos-with-vancine-api-and-bounded-polling-dfc65f/WORKFLOW.json
```
