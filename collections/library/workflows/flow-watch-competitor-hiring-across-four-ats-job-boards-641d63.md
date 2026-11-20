# Watch competitor hiring across four ATS job boards

Complete “Watch competitor hiring across four ATS job boards” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Watch competitor hiring across four ATS job boards.
- The selected records, date range, and output destination.
- Complete the named fields in flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/INPUTS.json.
- Configured connections or tools for apify, scheduler, slack.

## 1. Every morning at eight

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Every morning at eight: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Companies to watch

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Companies to watch: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Read every board

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = Actors, operation = Run actor and get dataset. Read `../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Read every board: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Only the ones I have not seen

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Compare the configured identity fields and keep the selected representative of each distinct record. Read `../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Only the ones I have not seen: Distinct records and a duplicate count.

**Check:** Two records with the same identity collapse while different identities remain separate.

## 5. Keep what is worth reading

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Keep what is worth reading: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Tell the channel

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Tell the channel: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Watch competitor hiring across four ATS job boards”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-watch-competitor-hiring-across-four-ats-job-boards-641d63/WORKFLOW.json
```
