# Assistant for Instagram DM inbox. Manychat + Open AI integration

Complete “Assistant for Instagram DM inbox. Manychat + Open AI integration” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Assistant for Instagram DM inbox. Manychat + Open AI integration.
- The selected records, date range, and output destination.
- Complete the named fields in flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/INPUTS.json.
- An available model or embedding capability with the requested format and cost limits.

## 1. ChatGPT model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** ChatGPT model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Getting message from Instagram

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Getting message from Instagram: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Set your system promt for AI

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Set your system promt for AI: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Local n8n memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (data, branch 0, input 0).

**Carry forward:** Local n8n memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 5. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (languageModel, branch 0, input 0), step-2 (memory, branch 0, input 0), step-1 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. Send respond

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Send respond: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Assistant for Instagram DM inbox. Manychat + Open AI integration”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-assistant-for-instagram-dm-inbox-manychat-muse-integration-7ffa5d/WORKFLOW.json
```
