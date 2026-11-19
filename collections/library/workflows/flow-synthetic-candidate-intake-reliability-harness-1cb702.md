# Synthetic Candidate Intake Reliability Harness

Complete “Synthetic Candidate Intake Reliability Harness” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Synthetic Candidate Intake Reliability Harness.
- The selected records, date range, and output destination.
- Complete the named fields in flow-synthetic-candidate-intake-reliability-harness-1cb702/INPUTS.json.

## 1. Run synthetic tests

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-synthetic-candidate-intake-reliability-harness-1cb702/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Run synthetic tests: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Synthetic fixtures

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-synthetic-candidate-intake-reliability-harness-1cb702/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Synthetic fixtures: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Normalize and assert contracts

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-synthetic-candidate-intake-reliability-harness-1cb702/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Normalize and assert contracts: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Synthetic Candidate Intake Reliability Harness”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-synthetic-candidate-intake-reliability-harness-1cb702/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-synthetic-candidate-intake-reliability-harness-1cb702/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-synthetic-candidate-intake-reliability-harness-1cb702/WORKFLOW.json
```
