# Automate Screenshots with URLbox & Analyze them with AI

Complete “Automate Screenshots with URLbox & Analyze them with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Automate Screenshots with URLbox & Analyze them with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Manual Execution

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Manual Execution: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Setup

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Setup: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. URLbox API Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** URLbox API Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Analyze the Screenshot

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Analyze the Screenshot: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 5. Merge Name & Description

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 1), step-3 (main, branch 0, input 0).

**Carry forward:** Merge Name & Description: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Automate Screenshots with URLbox & Analyze them with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-automate-screenshots-with-urlbox-analyze-them-with-ai-0c50fb/WORKFLOW.json
```
