# Post New Live Tennis Matches to Discord on a Schedule

Complete “Post New Live Tennis Matches to Discord on a Schedule” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Post New Live Tennis Matches to Discord on a Schedule.
- The selected records, date range, and output destination.
- Complete the named fields in flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/INPUTS.json.
- Configured connections or tools for discord, http, scheduler.

## 1. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Get Live Matches

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Live Matches: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 3. Split Out Matches

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Split Out Matches: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 4. Only New Matches

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Compare the configured identity fields and keep the selected representative of each distinct record. Read `../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Only New Matches: Distinct records and a duplicate count.

**Check:** Two records with the same identity collapse while different identities remain separate.

## 5. Discord

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Discord: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Post New Live Tennis Matches to Discord on a Schedule”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-post-new-live-tennis-matches-to-discord-on-a-schedule-3e81f2/WORKFLOW.json
```
