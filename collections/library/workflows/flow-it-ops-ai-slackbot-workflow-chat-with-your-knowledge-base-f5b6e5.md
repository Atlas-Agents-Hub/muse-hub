# IT Ops AI SlackBot Workflow - Chat with your knowledge base

Complete “IT Ops AI SlackBot Workflow - Chat with your knowledge base” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for IT Ops AI SlackBot Workflow - Chat with your knowledge base.
- The selected records, date range, and output destination.
- Complete the named fields in flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/INPUTS.json.
- Configured connections or tools for slack, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Call Confluence Workflow Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Call Confluence Workflow Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Receive DMs

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Receive DMs: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Verify Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Verify Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 5. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-9 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 6. Check if Bot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Check if Bot: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. No Operation, do nothing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** No Operation, do nothing: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 8. Send Initial Message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Send Initial Message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-2 (languageModel, branch 0, input 0), step-6 (main, branch 0, input 0), step-4 (memory, branch 0, input 0), step-10 (tool, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Delete Initial Message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = delete. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-6 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Delete Initial Message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Send Message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-11 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Send Message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “IT Ops AI SlackBot Workflow - Chat with your knowledge base”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-it-ops-ai-slackbot-workflow-chat-with-your-knowledge-base-f5b6e5/WORKFLOW.json
```
