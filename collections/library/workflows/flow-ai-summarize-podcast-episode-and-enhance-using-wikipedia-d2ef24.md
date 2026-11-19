# AI Summarize podcast episode and enhance using Wikipedia

Complete “AI Summarize podcast episode and enhance using Wikipedia” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for AI Summarize podcast episode and enhance using Wikipedia.
- The selected records, date range, and output destination.
- Complete the named fields in flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/INPUTS.json.
- Configured connections or tools for gmail, toolwikipedia.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Execute Workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Execute Workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. GPT3.5 - Research

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** GPT3.5 - Research: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. GPT3.5 - Summarize

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** GPT3.5 - Summarize: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 6. GPT 4 - Extract

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** GPT 4 - Extract: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 7. Wikipedia1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Wikipedia1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Podcast Episode Transcript

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Podcast Episode Transcript: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. Workflow Input to JSON Document

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (textSplitter, branch 0, input 0).

**Carry forward:** Workflow Input to JSON Document: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 10. Summarize Transcript

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Summarize the selected source with its required sections, audience, and length while retaining consequential details. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-14 (languageModel, branch 0, input 0), step-2 (main, branch 0, input 0), step-3 (document, branch 0, input 0).

**Carry forward:** Summarize Transcript: A summary linked to its source material.

**Check:** Names, quantities, dates, and key conclusions match the source.

## 11. Extract Topics & Questions

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-7 (languageModel, branch 0, input 0), step-6 (main, branch 0, input 0), step-11 (outputParser, branch 0, input 0).

**Carry forward:** Extract Topics & Questions: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Topics

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Topics: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 13. Research & Explain Topics

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-8 (tool, branch 0, input 0), step-13 (languageModel, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Research & Explain Topics: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Format topic text & title

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-12 (data, branch 0, input 0), step-5 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Format topic text & title: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 15. Send Digest

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Send Digest: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “AI Summarize podcast episode and enhance using Wikipedia”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-ai-summarize-podcast-episode-and-enhance-using-wikipedia-d2ef24/WORKFLOW.json
```
