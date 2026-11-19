# Qualifying Appointment Requests with AI & n8n Forms

Complete “Qualifying Appointment Requests with AI & n8n Forms” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Qualifying Appointment Requests with AI & n8n Forms.
- The selected records, date range, and output destination.
- Complete the named fields in flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/INPUTS.json.
- Configured connections or tools for gmail, googlecalendar, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. n8n Form Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** n8n Form Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Summarise Enquiry

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-11 (languageModel, branch 0, input 0), step-17 (main, branch 0, input 0).

**Carry forward:** Summarise Enquiry: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. Enquiry Classifier

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-6 (languageModel, branch 0, input 0).

**Carry forward:** Enquiry Classifier: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 7. Decline

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Operation settings: operation = completion. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 1, input 0).

**Carry forward:** Decline: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 8. Terms & Conditions

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Terms & Conditions: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 9. Wait for Approval

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendAndWait. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Wait for Approval: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Has Approval?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Has Approval?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 11. Has Accepted?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Has Accepted?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Create Appointment

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-17 (data, branch 0, input 0), step-18 (data, branch 0, input 0).

**Carry forward:** Create Appointment: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 13. Send Rejection

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Send Rejection: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 14. Decline1

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Operation settings: operation = completion. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 1, input 0).

**Carry forward:** Decline1: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 15. Enter Date & Time

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Enter Date & Time: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 16. Get Form Values

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Get Form Values: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Trigger Approval Process

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: mode = each. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Trigger Approval Process: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 18. Send Receipt

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Send Receipt: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. Form End

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Operation settings: operation = completion. Read `../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Form End: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Qualifying Appointment Requests with AI & n8n Forms”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-qualifying-appointment-requests-with-ai-muse-forms-8634d0/WORKFLOW.json
```
