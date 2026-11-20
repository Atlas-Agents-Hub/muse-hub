# AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs

Complete “AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs.
- The selected records, date range, and output destination.
- Complete the named fields in flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 3. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. OpenAI - Speech to Text

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = audio, operation = transcribe. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** OpenAI - Speech to Text: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 5. Get Chat

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-4 (memory, branch 0, input 0), step-11 (main, branch 0, input 0).

**Carry forward:** Get Chat: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 6. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 7. Basic LLM Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-5 (languageModel, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Basic LLM Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Insert Chat

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Operation settings: mode = insert. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-4 (memory, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Insert Chat: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 9. Limit

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Limit: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 10. ElevenLabs - Generate Audio

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** ElevenLabs - Generate Audio: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-ai-voice-chat-using-webhook-memory-manager-muse-elevenlabs-98bc47/WORKFLOW.json
```
