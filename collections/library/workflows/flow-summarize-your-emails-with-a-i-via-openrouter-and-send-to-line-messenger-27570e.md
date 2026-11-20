# Summarize your emails with A.I. (via Openrouter) and send to Line messenger

Complete “Summarize your emails with A.I. (via Openrouter) and send to Line messenger” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Summarize your emails with A.I. (via Openrouter) and send to Line messenger.
- The selected records, date range, and output destination.
- Complete the named fields in flow-summarize-your-emails-with-a-i-via-openrouter-and-send-to-line-messenger-27570e/INPUTS.json.
- Configured connections or tools for emailreadimap, http.

## 1. Read emails (IMAP)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-summarize-your-emails-with-a-i-via-openrouter-and-send-to-line-messenger-27570e/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Read emails (IMAP): A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 2. Send email to A.I. to summarize

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-summarize-your-emails-with-a-i-via-openrouter-and-send-to-line-messenger-27570e/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Send email to A.I. to summarize: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 3. Send summarized content to messenger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-summarize-your-emails-with-a-i-via-openrouter-and-send-to-line-messenger-27570e/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Send summarized content to messenger: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Check the finished result

Read [the Email Template Builder method](../skills/email-template-builder/SKILL.md). Inspect the complete result against the original task, the selected source, and the requested output format.

**Carry forward:** A checked result with its source and next action.

**Check:** The deliverable addresses the task and matches the selected source material.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Summarize your emails with A.I. (via Openrouter) and send to Line messenger”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-summarize-your-emails-with-a-i-via-openrouter-and-send-to-line-messenger-27570e/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-summarize-your-emails-with-a-i-via-openrouter-and-send-to-line-messenger-27570e/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-summarize-your-emails-with-a-i-via-openrouter-and-send-to-line-messenger-27570e/WORKFLOW.json
```
