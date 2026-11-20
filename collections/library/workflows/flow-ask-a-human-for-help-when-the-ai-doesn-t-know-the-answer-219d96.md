# Ask a human for help when the AI doesn t know the answer

Complete “Ask a human for help when the AI doesn t know the answer” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Ask a human for help when the AI doesn t know the answer.
- The selected records, date range, and output destination.
- Complete the named fields in flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/INPUTS.json.
- Configured connections or tools for slack, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 2. GPT4

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** GPT4: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Chat Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Not sure?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (data, branch 0, input 0).

**Carry forward:** Not sure?: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Check if user has provided email

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Check if user has provided email: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Prompt the user to provide an email

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 1, input 0).

**Carry forward:** Prompt the user to provide an email: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (languageModel, branch 0, input 0), step-2 (tool, branch 0, input 0), step-4 (main, branch 0, input 0), step-1 (memory, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. Message Slack for help

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Message Slack for help: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Confirm that we've messaged a human

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Confirm that we've messaged a human: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Ask a human for help when the AI doesn t know the answer”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-ask-a-human-for-help-when-the-ai-doesn-t-know-the-answer-219d96/WORKFLOW.json
```
