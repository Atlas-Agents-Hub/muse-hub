# Send daily translated Calvin and Hobbes Comics to Discord

Complete “Send daily translated Calvin and Hobbes Comics to Discord” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Send daily translated Calvin and Hobbes Comics to Discord.
- The selected records, date range, and output destination.
- Complete the named fields in flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/INPUTS.json.
- Configured connections or tools for discord, http, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. param

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** param: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Information Extractor

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-5 (languageModel, branch 0, input 0).

**Carry forward:** Information Extractor: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 6. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Discord

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-3 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Discord: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Send daily translated Calvin and Hobbes Comics to Discord”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-send-daily-translated-calvin-and-hobbes-comics-to-discord-e743d5/WORKFLOW.json
```
