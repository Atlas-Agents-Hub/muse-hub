# Chat with local LLMs using n8n and Ollama

Complete “Chat with local LLMs using n8n and Ollama” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Chat with local LLMs using n8n and Ollama.
- The selected records, date range, and output destination.
- Complete the named fields in flow-chat-with-local-llms-using-muse-and-ollama-05127d/INPUTS.json.
- An available model or embedding capability with the requested format and cost limits.

## 1. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-local-llms-using-muse-and-ollama-05127d/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Ollama Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-chat-with-local-llms-using-muse-and-ollama-05127d/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Ollama Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Chat LLM Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-chat-with-local-llms-using-muse-and-ollama-05127d/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (languageModel, branch 0, input 0), step-1 (main, branch 0, input 0).

**Carry forward:** Chat LLM Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Chat with local LLMs using n8n and Ollama”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-chat-with-local-llms-using-muse-and-ollama-05127d/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-chat-with-local-llms-using-muse-and-ollama-05127d/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-chat-with-local-llms-using-muse-and-ollama-05127d/WORKFLOW.json
```
