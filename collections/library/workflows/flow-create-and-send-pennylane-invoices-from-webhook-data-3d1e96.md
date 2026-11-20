# Create and send Pennylane invoices from webhook data

Complete “Create and send Pennylane invoices from webhook data” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Create and send Pennylane invoices from webhook data.
- The selected records, date range, and output destination.
- Complete the named fields in flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/INPUTS.json.
- Configured connections or tools for http.

## 1. WH Receive Invoice Data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** WH Receive Invoice Data: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Code Validate Payload

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Code Validate Payload: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 3. PL Search Customer

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** PL Search Customer: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. IF Customer Exists

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** IF Customer Exists: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 5. PL Create Customer

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 1, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** PL Create Customer: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Set Customer ID

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-5 (main, branch 0, input 0).

**Carry forward:** Set Customer ID: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Code Build Invoice Payload

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Code Build Invoice Payload: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. PL Create Invoice

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** PL Create Invoice: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. IF Send Email

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** IF Send Email: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Wait PDF Generation

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Wait PDF Generation: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 11. PL Send Invoice Email

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** PL Send Invoice Email: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Set Email Attempt

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-16 (main, branch 0, input 0).

**Carry forward:** Set Email Attempt: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. IF Email Sent

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** IF Email Sent: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 14. Code Evaluate Email Retry

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 1, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Code Evaluate Email Retry: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 15. IF Can Retry Email

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** IF Can Retry Email: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 16. Set Output Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 1, input 0), step-14 (main, branch 0, input 0), step-2 (data, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Set Output Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Set Email Delivery Failed

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 1, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Set Email Delivery Failed: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Create and send Pennylane invoices from webhook data”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-create-and-send-pennylane-invoices-from-webhook-data-3d1e96/WORKFLOW.json
```
