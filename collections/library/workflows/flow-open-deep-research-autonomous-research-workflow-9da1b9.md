# Open Deep Research - Autonomous Research Workflow

Complete “Open Deep Research - Autonomous Research Workflow” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Open Deep Research - Autonomous Research Workflow.
- The selected records, date range, and output destination.
- Complete the named fields in flow-open-deep-research-autonomous-research-workflow-9da1b9/INPUTS.json.
- Configured connections or tools for http, toolwikipedia.
- An available model or embedding capability with the requested format and cost limits.

## 1. Chat Message Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Message Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. LLM Memory Buffer (Input Context)

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** LLM Memory Buffer (Input Context): A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 3. LLM Memory Buffer (Report Context)

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** LLM Memory Buffer (Report Context): A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 4. Fetch Wikipedia Information

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Fetch Wikipedia Information: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. LLM Response Provider (OpenRouter)

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** LLM Response Provider (OpenRouter): A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. Generate Search Queries using LLM

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-3 (languageModel, branch 0, input 0).

**Carry forward:** Generate Search Queries using LLM: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Parse and Chunk JSON Data

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Parse and Chunk JSON Data: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. Split Data for SerpAPI Batching

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-5 (main, branch 0, input 0).

**Carry forward:** Split Data for SerpAPI Batching: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 9. Split Data for Jina AI Batching

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-6 (main, branch 0, input 0).

**Carry forward:** Split Data for Jina AI Batching: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 10. Perform SerpAPI Search Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Perform SerpAPI Search Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Perform Jina AI Analysis Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** Perform Jina AI Analysis Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Format SerpAPI Organic Results

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Format SerpAPI Organic Results: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. Extract Relevant Context via LLM

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-12 (memory, branch 0, input 0), step-3 (languageModel, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Extract Relevant Context via LLM: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Generate Comprehensive Research Report

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-14 (tool, branch 0, input 0), step-8 (main, branch 0, input 0), step-13 (memory, branch 0, input 0), step-3 (languageModel, branch 0, input 0).

**Carry forward:** Generate Comprehensive Research Report: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Open Deep Research - Autonomous Research Workflow”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-open-deep-research-autonomous-research-workflow-9da1b9/WORKFLOW.json
```
