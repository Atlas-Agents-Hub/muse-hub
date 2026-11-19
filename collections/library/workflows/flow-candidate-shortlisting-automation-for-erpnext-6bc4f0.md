# Candidate Shortlisting Automation for ERPNext

Complete “Candidate Shortlisting Automation for ERPNext” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Candidate Shortlisting Automation for ERPNext.
- The selected records, date range, and output destination.
- Complete the named fields in flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/INPUTS.json.
- Configured connections or tools for erpnext, http, microsoftoutlook, whatsapp.
- An available model or embedding capability with the requested format and cost limits.

## 1. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Txt File to Text (Example)

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = text. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Txt File to Text (Example): Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 3. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Code

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Code: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 5. ApplicantData

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** ApplicantData: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Resume Link Provided

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Resume Link Provided: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. ERPNext - Reject if Resume not Attached

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 1, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** ERPNext - Reject if Resume not Attached: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 8. Applied Against Job

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Applied Against Job: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 9. Reume Attachment Link

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Reume Attachment Link: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. ERPNext - Hold Applicant

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 1, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** ERPNext - Hold Applicant: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. File Type

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** File Type: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Download PDF Resume

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Download PDF Resume: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. PDF to Text

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** PDF to Text: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 14. Merge1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-19 (main, branch 0, input 1).

**Carry forward:** Merge1: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 15. Get Job Opening

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Get Job Opening: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 16. Recruitment AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-7 (languageModel, branch 0, input 0), step-18 (data, branch 0, input 0).

**Carry forward:** Recruitment AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 17. Convert to Fields

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Convert to Fields: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 18. Update Applicant Data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = PUT. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Update Applicant Data: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. If score less than 80

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** If score less than 80: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 20. Reject Applicant

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = PUT. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Reject Applicant: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 21. Accept Applicant

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = PUT. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 1, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Accept Applicant: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 22. Microsoft Outlook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Microsoft Outlook: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 23. WhatsApp Business Cloud

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = send. Read `../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** WhatsApp Business Cloud: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Candidate Shortlisting Automation for ERPNext”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-candidate-shortlisting-automation-for-erpnext-6bc4f0/WORKFLOW.json
```
