# Send Escalating WhatsApp Invoice Reminders from Google Sheets (Hebrew)

Complete “Send Escalating WhatsApp Invoice Reminders from Google Sheets (Hebrew)” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Send Escalating WhatsApp Invoice Reminders from Google Sheets (Hebrew).
- The selected records, date range, and output destination.
- Complete the named fields in flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/INPUTS.json.
- Configured connections or tools for googlesheets, http, scheduler.

## 1. When Each Day at 09:00

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When Each Day at 09:00: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Read Invoices from Sheets

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = sheet, operation = read. Read `../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Read Invoices from Sheets: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Calculate Overdue Tier

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForAllItems. Read `../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Calculate Overdue Tier: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 4. Post WhatsApp Reminder

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Post WhatsApp Reminder: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Update Sent Status in Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = sheet, operation = update. Read `../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Update Sent Status in Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Send Escalating WhatsApp Invoice Reminders from Google Sheets (Hebrew)”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-send-escalating-whatsapp-invoice-reminders-from-google-sheets-hebrew-6f50cb/WORKFLOW.json
```
