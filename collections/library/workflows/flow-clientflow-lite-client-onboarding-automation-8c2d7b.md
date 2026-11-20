# ClientFlow Lite - Client Onboarding Automation

Complete “ClientFlow Lite - Client Onboarding Automation” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for ClientFlow Lite - Client Onboarding Automation.
- The selected records, date range, and output destination.
- Complete the named fields in flow-clientflow-lite-client-onboarding-automation-8c2d7b/INPUTS.json.
- Configured connections or tools for gmail, googlesheets.

## 1. New Client

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** New Client: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Validate

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Validate: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Gmail: Welcome Email

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Gmail: Welcome Email: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 4. Log to Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Log to Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 5. Respond

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Respond: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “ClientFlow Lite - Client Onboarding Automation”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-clientflow-lite-client-onboarding-automation-8c2d7b/WORKFLOW.json
```
