# Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini

Complete “Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini.
- The selected records, date range, and output destination.
- Complete the named fields in flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Structured Output Parser2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser2: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 2. Parser Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Parser Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Agent Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Agent Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Structured Output Parser1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser1: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 6. Date & Time

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Date & Time: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. Auto-fixing Output Parser6

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-15 (languageModel, branch 0, input 0), step-14 (outputParser, branch 0, input 0).

**Carry forward:** Auto-fixing Output Parser6: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 8. Auto-fixing Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-15 (languageModel, branch 0, input 0), step-5 (outputParser, branch 0, input 0).

**Carry forward:** Auto-fixing Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 9. Semantic Search -Query Maker

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-16 (languageModel, branch 0, input 0), step-1 (main, branch 0, input 0), step-4 (outputParser, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Semantic Search -Query Maker: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Query

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Query: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Query-1 Combined

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Query-1 Combined: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 12. Semantic Search - Result Re-Ranker

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-16 (languageModel, branch 0, input 0), step-6 (main, branch 0, input 0), step-3 (outputParser, branch 0, input 0), step-1 (data, branch 0, input 0), step-11 (data, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Semantic Search - Result Re-Ranker: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-intelligent-web-query-and-semantic-re-ranking-flow-using-brave-and-muse-752452/WORKFLOW.json
```
