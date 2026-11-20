# Translate Telegram audio messages with AI (55 supported languages)

Complete “Translate Telegram audio messages with AI (55 supported languages)” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Translate Telegram audio messages with AI (55 supported languages).
- The selected records, date range, and output destination.
- Complete the named fields in flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/INPUTS.json.
- Configured connections or tools for telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. Telegram Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Telegram Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Settings

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Settings: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Input Error Handling

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Input Error Handling: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Telegram1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = file. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Telegram1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 6. OpenAI2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = audio, operation = transcribe. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** OpenAI2: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. Auto-detect and translate

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-4 (languageModel, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Auto-detect and translate: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = audio. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. Text reply

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Text reply: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Audio reply

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendAudio. Read `../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Audio reply: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Translate Telegram audio messages with AI (55 supported languages)”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-translate-telegram-audio-messages-with-ai-55-supported-languages-cd5bc3/WORKFLOW.json
```
