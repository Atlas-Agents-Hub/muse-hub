# Telegram AI Bot NeurochainAI Text & Image - NeurochainAI Basic API Integration

Complete “Telegram AI Bot NeurochainAI Text & Image - NeurochainAI Basic API Integration” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Telegram AI Bot NeurochainAI Text & Image - NeurochainAI Basic API Integration.
- The selected records, date range, and output destination.
- Complete the named fields in flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/INPUTS.json.
- Configured connections or tools for http, telegram.

## 1. Telegram Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Telegram Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 3. TYPING - ACTION

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendChatAction. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 1, input 0), step-18 (main, branch 2, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** TYPING - ACTION: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 4. Code1

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Code1: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. NeurochainAI - REST API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** NeurochainAI - REST API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Telegram2

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Telegram2: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 7. AI Response

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** AI Response: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 8. Switch2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** Switch2: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 9. NeurochainAI - Flux

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** NeurochainAI - Flux: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. No response

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** No response: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Prompt too short

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 1, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Prompt too short: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. Code

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Code: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. Switch1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 1, input 0).

**Carry forward:** Switch1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 14. HTTP Request3

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** HTTP Request3: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. Telegram3

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 1, input 0), step-1 (data, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Telegram3: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 16. Telegram6

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Telegram6: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 17. Telegram7

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = deleteMessage. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Telegram7: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 18. Telegram1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendPhoto. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Telegram1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. Telegram5

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = deleteMessage. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Telegram5: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 20. Telegram4

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = deleteMessage. Read `../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Telegram4: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Telegram AI Bot NeurochainAI Text & Image - NeurochainAI Basic API Integration”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-telegram-ai-bot-neurochainai-text-image-neurochainai-basic-api-integration-94f2d0/WORKFLOW.json
```
