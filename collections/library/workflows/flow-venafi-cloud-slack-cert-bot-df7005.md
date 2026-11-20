# Venafi Cloud Slack Cert Bot

Complete “Venafi Cloud Slack Cert Bot” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Venafi Cloud Slack Cert Bot.
- The selected records, date range, and output destination.
- Complete the named fields in flow-venafi-cloud-slack-cert-bot-df7005/INPUTS.json.
- Configured connections or tools for http, slack, venafitlsprotectcloud, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Parse Webhook

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Parse Webhook: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Route Message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Route Message: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. Respond to webhook success

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 2, input 0).

**Carry forward:** Respond to webhook success: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 5. Close Modal Popup

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 1, input 0).

**Carry forward:** Close Modal Popup: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 6. Respond to Slack Webhook - Vulnerability

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Respond to Slack Webhook - Vulnerability: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 7. Get Slack Team ID

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Get Slack Team ID: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Manual Issue Certificate

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Manual Issue Certificate: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 9. Venafi Request Certificate

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Venafi Request Certificate: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Extract Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Extract Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Get Slack User ID

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Get Slack User ID: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Execute Workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Execute Workflow: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 13. Venafi TLS Protect Cloud1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Venafi TLS Protect Cloud1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 14. Translate Slack User ID to Email

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Translate Slack User ID to Email: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 15. VirusTotal HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = GET. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** VirusTotal HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 16. Summarize output to save on tokens

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Summarize output to save on tokens: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Merge User and Team Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 1), step-8 (main, branch 0, input 0).

**Carry forward:** Merge User and Team Data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 18. Send Auto Generated Confirmation1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Send Auto Generated Confirmation1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. Merge Requestor and VT Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 1), step-10 (main, branch 0, input 0).

**Carry forward:** Merge Requestor and VT Data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 20. Auto Issue Certificate Based on 0 Malicious Reports

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Auto Issue Certificate Based on 0 Malicious Reports: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 21. Auto Issue Certificate

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Auto Issue Certificate: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 22. Generate Report For Manual Approval

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** Generate Report For Manual Approval: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 23. Venafi TLS Protect Cloud

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Venafi TLS Protect Cloud: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 24. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 25. Send Auto Generated Confirmation

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-16 (data, branch 0, input 0), step-18 (data, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Send Auto Generated Confirmation: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 26. Send Message Request for Manual Approval

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-13 (data, branch 0, input 0), step-18 (data, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Send Message Request for Manual Approval: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Venafi Cloud Slack Cert Bot”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-venafi-cloud-slack-cert-bot-df7005/WORKFLOW.json
```
