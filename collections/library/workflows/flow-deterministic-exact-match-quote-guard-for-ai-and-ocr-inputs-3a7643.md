# Deterministic Exact-Match Quote Guard for AI and OCR Inputs

Complete “Deterministic Exact-Match Quote Guard for AI and OCR Inputs” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Deterministic Exact-Match Quote Guard for AI and OCR Inputs.
- The selected records, date range, and output destination.
- Complete the named fields in flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/INPUTS.json.

## 1. Receive Synthetic Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Receive Synthetic Request: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Validate Untrusted Extraction

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Validate Untrusted Extraction: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Is Input Valid

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Is Input Valid: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. Build Rejected Response

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 1, input 0).

**Carry forward:** Build Rejected Response: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. Exact Match and Calculate

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Exact Match and Calculate: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 6. Is Quote Ready

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Is Quote Ready: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Respond Rejected

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Respond Rejected: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 8. Respond Quotable

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Respond Quotable: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 9. Respond Needs Review

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 1, input 0).

**Carry forward:** Respond Needs Review: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Deterministic Exact-Match Quote Guard for AI and OCR Inputs”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-deterministic-exact-match-quote-guard-for-ai-and-ocr-inputs-3a7643/WORKFLOW.json
```
