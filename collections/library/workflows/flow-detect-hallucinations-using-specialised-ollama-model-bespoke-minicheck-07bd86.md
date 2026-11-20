# Detect hallucinations using specialised Ollama model bespoke-minicheck

Complete “Detect hallucinations using specialised Ollama model bespoke-minicheck” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Detect hallucinations using specialised Ollama model bespoke-minicheck.
- The selected records, date range, and output destination.
- Complete the named fields in flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/INPUTS.json.
- An available model or embedding capability with the requested format and cost limits.

## 1. Ollama Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Ollama Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Ollama Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Ollama Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. When Executed by Another Workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When Executed by Another Workflow: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Edit Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Edit Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Code

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-9 (main, branch 0, input 0).

**Carry forward:** Code: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. Merge1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 1), step-6 (main, branch 0, input 0), step-9 (main, branch 0, input 0).

**Carry forward:** Merge1: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 8. Split Out1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Split Out1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 9. Basic LLM Chain4

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-4 (languageModel, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Basic LLM Chain4: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-3 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 11. Filter

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Filter: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 12. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 13. Basic LLM Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-13 (languageModel, branch 0, input 0).

**Carry forward:** Basic LLM Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Detect hallucinations using specialised Ollama model bespoke-minicheck”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-detect-hallucinations-using-specialised-ollama-model-bespoke-minicheck-07bd86/WORKFLOW.json
```
