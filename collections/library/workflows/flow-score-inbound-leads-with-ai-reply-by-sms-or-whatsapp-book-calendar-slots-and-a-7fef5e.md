# Score inbound leads with AI, reply by SMS or WhatsApp, book calendar slots and alert sales

Complete “Score inbound leads with AI, reply by SMS or WhatsApp, book calendar slots and alert sales” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Score inbound leads with AI, reply by SMS or WhatsApp, book calendar slots and alert sales.
- The selected records, date range, and output destination.
- Complete the named fields in flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/INPUTS.json.
- Configured connections or tools for http.

## 1. Webhook: new lead (form / ad / GHL)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: new lead (form / ad / GHL): A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Webhook: voice agent call ended (Retell / VAPI)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: voice agent call ended (Retell / VAPI): A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Error trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Error trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. Config (calls)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Config (calls): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Config

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Config: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Config (errors)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Config (errors): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Parse call payload

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Parse call payload: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. Alert ops (Slack)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-32 (main, branch 0, input 0).

**Carry forward:** Alert ops (Slack): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Normalise + dedupe (24h)

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Normalise + dedupe (24h): Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. AI: summarise call + detect booking intent

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** AI: summarise call + detect booking intent: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Not a duplicate?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Not a duplicate?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Skip duplicate

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0).

**Carry forward:** Skip duplicate: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. CRM: upsert caller

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-21 (data, branch 0, input 0).

**Carry forward:** CRM: upsert caller: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 14. AI: qualify lead

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** AI: qualify lead: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. CRM: call summary note

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0), step-21 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** CRM: call summary note: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 16. Merge lead + AI verdict

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Merge lead + AI verdict: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 17. Appointment requested?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Appointment requested?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 18. CRM: upsert contact (HubSpot / GHL)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** CRM: upsert contact (HubSpot / GHL): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. Calendar: slots

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0), step-21 (data, branch 0, input 0).

**Carry forward:** Calendar: slots: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. Attach contact id

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Attach contact id: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 21. Hot lead?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Hot lead?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 22. Book first slot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0), step-21 (data, branch 0, input 0), step-23 (data, branch 0, input 0).

**Carry forward:** Book first slot: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 23. Reply in < 60 s (SMS / WhatsApp / email)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Reply in < 60 s (SMS / WhatsApp / email): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 24. Nurture: start 5-day sequence

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** Nurture: start 5-day sequence: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 25. SMS confirmation

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0), step-21 (data, branch 0, input 0).

**Carry forward:** SMS confirmation: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 26. Calendar: next open slots

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Calendar: next open slots: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 27. Respond (call)

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 1, input 0), step-28 (main, branch 0, input 0), step-21 (data, branch 0, input 0), step-22 (data, branch 0, input 0), step-27 (data, branch 0, input 0).

**Carry forward:** Respond (call): Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 28. Offer 3 slots

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Offer 3 slots: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 29. CRM: task for sales rep (15 min SLA)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** CRM: task for sales rep (15 min SLA): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 30. Slack alert to sales

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Slack alert to sales: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 31. CRM: note with AI summary

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-16 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** CRM: note with AI summary: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 32. Respond to webhook

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Respond to webhook: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Score inbound leads with AI, reply by SMS or WhatsApp, book calendar slots and alert sales”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-score-inbound-leads-with-ai-reply-by-sms-or-whatsapp-book-calendar-slots-and-a-7fef5e/WORKFLOW.json
```
