# B2B Demo Lead Rescue Desk - Enrich Score Route and Escalate

Complete “B2B Demo Lead Rescue Desk - Enrich Score Route and Escalate” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for B2B Demo Lead Rescue Desk - Enrich Score Route and Escalate.
- The selected records, date range, and output destination.
- Complete the named fields in flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/INPUTS.json.
- Configured connections or tools for gmail, googlesheets, http.

## 1. Lead Intake Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Lead Intake Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Normalize, Score, and Assign Owner

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Normalize, Score, and Assign Owner: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. Has Usable Contact?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Has Usable Contact?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. Build Missing Contact Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Build Missing Contact Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Fetch Submitted Page Context

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Fetch Submitted Page Context: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Respond Missing Contact

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Respond Missing Contact: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 7. Extract Page Signals

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Extract Page Signals: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. Build Audit Row

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Build Audit Row: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Append Lead Audit Row

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Append Lead Audit Row: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Route by Priority

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Route by Priority: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 11. Build Hot Lead Alert

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Build Hot Lead Alert: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Build Review Queue Alert

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** Build Review Queue Alert: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Build Normal Lead Note

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 2, input 0).

**Carry forward:** Build Normal Lead Note: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Send Hot Lead Gmail Alert

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Send Hot Lead Gmail Alert: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 15. Send Review Queue Gmail Alert

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Send Review Queue Gmail Alert: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 16. Send Normal Lead Gmail Alert

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Send Normal Lead Gmail Alert: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 17. Needs Executive Escalation?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Needs Executive Escalation?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 18. Send Executive Escalation

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Send Executive Escalation: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. Build Success Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 1, input 0), step-18 (main, branch 0, input 0), step-14 (main, branch 0, input 0), step-16 (main, branch 0, input 0).

**Carry forward:** Build Success Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 20. Respond Success

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Respond Success: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “B2B Demo Lead Rescue Desk - Enrich Score Route and Escalate”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-b2b-demo-lead-rescue-desk-enrich-score-route-and-escalate-8b9a67/WORKFLOW.json
```
