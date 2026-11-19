# Extract insights & analyse YouTube comments via Assistant chat

Complete “Extract insights & analyse YouTube comments via Assistant chat” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Extract insights & analyse YouTube comments via Assistant chat.
- The selected records, date range, and output destination.
- Complete the named fields in flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/INPUTS.json.
- Configured connections or tools for http, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. get_channel_details

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** get_channel_details: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. get_video_description

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** get_video_description: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. get_list_of_videos

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** get_list_of_videos: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. get_list_of_comments

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** get_list_of_comments: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. search

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** search: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 9. analyze_thumbnail

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** analyze_thumbnail: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. video_transcription

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** video_transcription: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 11. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Postgres Chat Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-11 (data, branch 0, input 0).

**Carry forward:** Postgres Chat Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 13. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-6 (tool, branch 0, input 0), step-1 (languageModel, branch 0, input 0), step-7 (tool, branch 0, input 0), step-4 (tool, branch 0, input 0), step-2 (tool, branch 0, input 0), step-8 (tool, branch 0, input 0), step-9 (memory, branch 0, input 0), step-5 (tool, branch 0, input 0), step-3 (tool, branch 0, input 0), step-11 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Get Comments

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 2, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Get Comments: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. Get Channel Details

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Get Channel Details: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 16. Get Video Description

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 1, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Get Video Description: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 17. Run Query

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 3, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Run Query: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 18. Get Videos by Channel

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 4, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Get Videos by Channel: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. Get Video Transcription

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 6, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Get Video Transcription: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 5, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 21. Edit Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Edit Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 22. Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-17 (main, branch 0, input 0), step-16 (main, branch 0, input 0), step-14 (main, branch 0, input 0), step-15 (main, branch 0, input 0), step-18 (main, branch 0, input 0), step-21 (main, branch 0, input 0).

**Carry forward:** Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Extract insights & analyse YouTube comments via Assistant chat”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-extract-insights-analyse-youtube-comments-via-assistant-chat-268641/WORKFLOW.json
```
