# Send a random recipe once a day to Telegram

Complete “Send a random recipe once a day to Telegram” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Send a random recipe once a day to Telegram.
- The selected records, date range, and output destination.
- Complete the named fields in flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/INPUTS.json.
- Configured connections or tools for airtable, http, scheduler, telegram.

## 1. Cron

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Cron: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Telegram Trigger - people join bot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Telegram Trigger - people join bot: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Telegram - Welcome Message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Telegram - Welcome Message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 4. Airtable2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = list. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Airtable2: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Airtable

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = list. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Airtable: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Get recipes

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Get recipes: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 7. Set

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Set: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Get recipes from API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Get recipes from API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Telegram Recipe Image

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendPhoto. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Telegram Recipe Image: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Telegram Recipe URL

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-13 (data, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Telegram Recipe URL: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Recipe Photo

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendPhoto. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Recipe Photo: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. Recipe URL

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-12 (data, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Recipe URL: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Set1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Set1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 15. Airtable1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Airtable1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Send a random recipe once a day to Telegram”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-send-a-random-recipe-once-a-day-to-telegram-b8be63/WORKFLOW.json
```
