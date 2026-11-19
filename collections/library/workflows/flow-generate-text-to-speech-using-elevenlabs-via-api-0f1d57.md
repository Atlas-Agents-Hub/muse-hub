# Generate Text-to-Speech Using Elevenlabs via API

Complete “Generate Text-to-Speech Using Elevenlabs via API” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Generate Text-to-Speech Using Elevenlabs via API.
- The selected records, date range, and output destination.
- Complete the named fields in flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/INPUTS.json.
- Configured connections or tools for http.

## 1. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. If params correct

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** If params correct: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 3. Generate voice

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Generate voice: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Error

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 1, input 0).

**Carry forward:** Error: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 5. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Generate Text-to-Speech Using Elevenlabs via API”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-generate-text-to-speech-using-elevenlabs-via-api-0f1d57/WORKFLOW.json
```
