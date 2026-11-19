# Route spend requests to approvers by threshold with deputies, reminders and escalation

Complete “Route spend requests to approvers by threshold with deputies, reminders and escalation” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Route spend requests to approvers by threshold with deputies, reminders and escalation.
- The selected records, date range, and output destination.
- Complete the named fields in flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/INPUTS.json.
- Configured connections or tools for http, scheduler.

## 1. Webhook: approval request (form, ERP or Slack)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: approval request (form, ERP or Slack): A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Webhook: decision received (Slack button)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: decision received (Slack button): A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Schedule: every hour

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule: every hour: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 4. Webhook: run escalation sweep now

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: run escalation sweep now: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Error trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Error trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Config (decisions)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Config (decisions): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Config

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Config: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Config (sweep)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-19 (main, branch 0, input 0).

**Carry forward:** Config (sweep): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Config (errors)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Config (errors): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Validate decision

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Validate decision: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 11. Approvals: pending past SLA

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Approvals: pending past SLA: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. HR: who is out of office

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** HR: who is out of office: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Alert ops (Slack)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0).

**Carry forward:** Alert ops (Slack): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 14. Decision valid?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Decision valid?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 15. Pick overdue requests

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Pick overdue requests: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 16. Apply policy: threshold, approver, deputy

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Apply policy: threshold, approver, deputy: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 17. Approvals: log decision

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Approvals: log decision: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 18. Respond 409 (invalid decision)

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 1, input 0).

**Carry forward:** Respond 409 (invalid decision): A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 19. Anything overdue?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Anything overdue?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 20. Auto approved?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Auto approved?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 21. Respond 200 (decision recorded)

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Respond 200 (decision recorded): A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 22. Escalate to deputy or CEO (Slack)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** Escalate to deputy or CEO (Slack): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 23. Approvals: log decision (auto)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Approvals: log decision (auto): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 24. Send approval request (Slack, email)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Send approval request (Slack, email): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 25. Approvals: log escalation

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Approvals: log escalation: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 26. Notify requester

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-7 (main, branch 0, input 0), step-2 (data, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Notify requester: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 27. Sweep summary

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 1, input 0), step-25 (main, branch 0, input 0).

**Carry forward:** Sweep summary: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 28. Outcome

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Outcome: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 29. Respond 200 (request routed)

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Respond 200 (request routed): A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 30. Respond 200 (sweep done)

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Respond 200 (sweep done): A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Route spend requests to approvers by threshold with deputies, reminders and escalation”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-route-spend-requests-to-approvers-by-threshold-with-deputies-reminders-and-esc-b39eb1/WORKFLOW.json
```
