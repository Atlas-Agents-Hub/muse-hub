# Use AI to organize your Todoist Inbox

Complete “Use AI to organize your Todoist Inbox” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Use AI to organize your Todoist Inbox.
- The selected records, date range, and output destination.
- Complete the named fields in flow-use-ai-to-organize-your-todoist-inbox-41842c/INPUTS.json.
- Configured connections or tools for scheduler, todoist.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Your Projects

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Your Projects: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Get inbox tasks

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Get inbox tasks: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. If task is not a subtask

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** If task is not a subtask: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 5. Categorize

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-3 (data, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Categorize: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. If other or ai hallucinates

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** If other or ai hallucinates: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 7. Update priority in todoist

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-3 (data, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Update priority in todoist: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Use AI to organize your Todoist Inbox”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-use-ai-to-organize-your-todoist-inbox-41842c/WORKFLOW.json
```
