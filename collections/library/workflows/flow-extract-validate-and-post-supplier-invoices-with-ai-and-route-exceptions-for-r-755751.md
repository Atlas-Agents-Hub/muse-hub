# Extract, validate and post supplier invoices with AI and route exceptions for review

Complete “Extract, validate and post supplier invoices with AI and route exceptions for review” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Extract, validate and post supplier invoices with AI and route exceptions for review.
- The selected records, date range, and output destination.
- Complete the named fields in flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/INPUTS.json.
- Configured connections or tools for http.

## 1. Webhook: invoice received (email, drive or upload)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: invoice received (email, drive or upload): A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Error trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Error trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Config (errors)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Config (errors): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Config

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Config: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Alert ops (Slack)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Alert ops (Slack): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. AI: extract fields from document

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** AI: extract fields from document: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 7. Accounting: supplier master

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Accounting: supplier master: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. Accounting: open purchase orders

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Accounting: open purchase orders: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Merge lookups

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-5 (main, branch 0, input 1).

**Carry forward:** Merge lookups: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 10. Validate: TRN, duplicate, totals, PO match, limit

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-2 (data, branch 0, input 0), step-3 (data, branch 0, input 0), step-4 (data, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Validate: TRN, duplicate, totals, PO match, limit: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 11. Route by status

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Route by status: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Review queue: human check

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 1, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Review queue: human check: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Slack: rejected, AP notified

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 2, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Slack: rejected, AP notified: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 14. Accounting: post bill

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Accounting: post bill: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. Outcome

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-10 (main, branch 0, input 0), step-11 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Outcome: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 16. Respond 200 (invoice handled)

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Respond 200 (invoice handled): A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Extract, validate and post supplier invoices with AI and route exceptions for review”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-extract-validate-and-post-supplier-invoices-with-ai-and-route-exceptions-for-r-755751/WORKFLOW.json
```
