# Analyze feedback using AWS Comprehend and send it to a Mattermost channel

Complete “Analyze feedback using AWS Comprehend and send it to a Mattermost channel” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Analyze feedback using AWS Comprehend and send it to a Mattermost channel.
- The selected records, date range, and output destination.
- Complete the named fields in flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/INPUTS.json.
- Configured connections or tools for awscomprehend, mattermost.

## 1. Typeform Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Typeform Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. AWS Comprehend

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = detectSentiment. Read `../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** AWS Comprehend: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. Mattermost

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Mattermost: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. NoOp

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** NoOp: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Analyze feedback using AWS Comprehend and send it to a Mattermost channel”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel-8ed66b/WORKFLOW.json
```
