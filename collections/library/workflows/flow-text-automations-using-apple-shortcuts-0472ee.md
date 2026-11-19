# Text automations using Apple Shortcuts

Complete “Text automations using Apple Shortcuts” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Text automations using Apple Shortcuts.
- The selected records, date range, and output destination.
- Complete the named fields in flow-text-automations-using-apple-shortcuts-0472ee/INPUTS.json.
- An available model or embedding capability with the requested format and cost limits.

## 1. Webhook from Shortcut

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook from Shortcut: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 3. OpenAI - Make Shorter

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 3, input 0).

**Carry forward:** OpenAI - Make Shorter: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 4. OpenAI - Make Longer

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 4, input 0).

**Carry forward:** OpenAI - Make Longer: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 5. OpenAI - Correct Grammar

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 2, input 0).

**Carry forward:** OpenAI - Correct Grammar: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. OpenAI - To Spanish

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** OpenAI - To Spanish: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. OpenAI - To English

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 1, input 0).

**Carry forward:** OpenAI - To English: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Respond to Shortcut

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-7 (main, branch 0, input 0), step-5 (main, branch 0, input 0), step-4 (main, branch 0, input 0), step-6 (main, branch 0, input 0).

**Carry forward:** Respond to Shortcut: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Text automations using Apple Shortcuts”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-text-automations-using-apple-shortcuts-0472ee/WORKFLOW.json
```
