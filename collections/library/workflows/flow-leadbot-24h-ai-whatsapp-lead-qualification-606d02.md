# LeadBot 24h - AI WhatsApp Lead Qualification

Complete “LeadBot 24h - AI WhatsApp Lead Qualification” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for LeadBot 24h - AI WhatsApp Lead Qualification.
- The selected records, date range, and output destination.
- Complete the named fields in flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/INPUTS.json.
- Configured connections or tools for googlesheets, http.

## 1. WhatsApp Webhook (WAHA)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** WhatsApp Webhook (WAHA): A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Normalize & Score Lead

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Normalize & Score Lead: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Filter Hot Leads

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Filter Hot Leads: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 4. Save Lead to Google Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Save Lead to Google Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 5. Notify Sales Team (Slack/Webhook)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Notify Sales Team (Slack/Webhook): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “LeadBot 24h - AI WhatsApp Lead Qualification”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-leadbot-24h-ai-whatsapp-lead-qualification-606d02/WORKFLOW.json
```
