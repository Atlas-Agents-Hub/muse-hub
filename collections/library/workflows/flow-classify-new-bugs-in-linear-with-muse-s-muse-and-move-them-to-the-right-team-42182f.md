# Classify new bugs in Linear with OpenAI s GPT-4 and move them to the right team

Complete “Classify new bugs in Linear with OpenAI s GPT-4 and move them to the right team” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Classify new bugs in Linear with OpenAI s GPT-4 and move them to the right team.
- The selected records, date range, and output destination.
- Complete the named fields in flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/INPUTS.json.
- Configured connections or tools for http, linear, slack.
- An available model or embedding capability with the requested format and cost limits.

## 1. Linear Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Linear Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Set me up

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set me up: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Only tickets that need to be classified

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Only tickets that need to be classified: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 4. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 5. Get all linear teams

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Get all linear teams: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Merge data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = chooseBranch. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-4 (main, branch 0, input 1).

**Carry forward:** Merge data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 7. Check if AI was able to find a team

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Check if AI was able to find a team: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 8. Set team ID

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Set team ID: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Notify in Slack

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 1, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Notify in Slack: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Update team

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Update team: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Classify new bugs in Linear with OpenAI s GPT-4 and move them to the right team”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-classify-new-bugs-in-linear-with-muse-s-muse-and-move-them-to-the-right-team-42182f/WORKFLOW.json
```
