# OpenAI examples ChatGPT, DALLE-2, Whisper-1 – 5-in-1

Complete “OpenAI examples ChatGPT, DALLE-2, Whisper-1 – 5-in-1” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for OpenAI examples ChatGPT, DALLE-2, Whisper-1 – 5-in-1.
- The selected records, date range, and output destination.
- Complete the named fields in flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Execute Workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Execute Workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Set-ex4

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set-ex4: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. ChatGPT-ex

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** ChatGPT-ex: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 4. LoadMP3

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** LoadMP3: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 5. ChatGPT-ex4

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** ChatGPT-ex4: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. Whisper-transcribe

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Whisper-transcribe: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 7. HTML-ex4

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** HTML-ex4: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 8. Text-example

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Text-example: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. davinci-003-complete

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** davinci-003-complete: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. ChatGPT-ex2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** ChatGPT-ex2: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. ChatGPT-ex1.1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** ChatGPT-ex1.1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Code-ex3.1

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Code-ex3.1: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. davinci-003-edit

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: operation = edit. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** davinci-003-edit: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. ChatGPT-ex1.2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** ChatGPT-ex1.2: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 15. ChatGPT-ex3.1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** ChatGPT-ex3.1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 16. ChatGPT-ex3.2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** ChatGPT-ex3.2: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 17. DALLE-ex3.3

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image. Read `../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** DALLE-ex3.3: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “OpenAI examples ChatGPT, DALLE-2, Whisper-1 – 5-in-1”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-muse-examples-muse-dalle-2-whisper-1-5-in-1-6dc990/WORKFLOW.json
```
