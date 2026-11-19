# Website leads to Google Sheets with Telegram alert and auto-reply (Italian)

Complete “Website leads to Google Sheets with Telegram alert and auto-reply (Italian)” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Website leads to Google Sheets with Telegram alert and auto-reply (Italian).
- The selected records, date range, and output destination.
- Complete the named fields in flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/INPUTS.json.
- Configured connections or tools for gmail, googlesheets, telegram.

## 1. Nuovo lead dal sito

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Nuovo lead dal sito: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Estrai campi del lead

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Estrai campi del lead: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Salva nel Registro Lead

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Salva nel Registro Lead: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 4. Avvisami su Telegram

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Avvisami su Telegram: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 5. Email di cortesia al cliente

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Email di cortesia al cliente: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Website leads to Google Sheets with Telegram alert and auto-reply (Italian)”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-website-leads-to-google-sheets-with-telegram-alert-and-auto-reply-italian-b59615/WORKFLOW.json
```
