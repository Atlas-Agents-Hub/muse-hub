# Automate Customer Support Issue Resolution using AI Text Classifier

Complete “Automate Customer Support Issue Resolution using AI Text Classifier” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Automate Customer Support Issue Resolution using AI Text Classifier.
- The selected records, date range, and output destination.
- Complete the named fields in flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/INPUTS.json.
- Configured connections or tools for jira, notion, scheduler, slack, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Find Simlar Issues

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Find Simlar Issues: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Query KnowledgeBase

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Query KnowledgeBase: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. OpenAI Chat Model3

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model3: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 8. OpenAI Chat Model4

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model4: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 9. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 10. Get Issue Metadata

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Get Issue Metadata: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Get List of Unresolved Long Lived Issues

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Get List of Unresolved Long Lived Issues: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. Execute Workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: mode = each. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Execute Workflow: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 13. Get Issue Comments

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = issueComment, operation = getAll. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Get Issue Comments: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 14. Join Comments

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Join Comments: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 15. Simplify Thread For AI

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Simplify Thread For AI: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. Classify Current Issue State

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-1 (languageModel, branch 0, input 0), step-12 (main, branch 0, input 0).

**Carry forward:** Classify Current Issue State: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 17. Last Message is Not Bot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 1, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Last Message is Not Bot: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 18. Customer Satisfaction Agent

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-4 (languageModel, branch 0, input 0), step-29 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Customer Satisfaction Agent: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 19. KnowledgeBase Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-26 (tool, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-27 (tool, branch 0, input 0), step-16 (outputParser, branch 0, input 0), step-29 (main, branch 2, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** KnowledgeBase Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 20. Add Autoclose Message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = issueComment. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 1, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Add Autoclose Message: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 21. Ask For Feedback Message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = issueComment. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Ask For Feedback Message: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 22. Solution Found?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Solution Found?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 23. Issue Reminder Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-3 (languageModel, branch 0, input 0), step-15 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Issue Reminder Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 24. Report Unhappy Resolution

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 2, input 0), step-17 (data, branch 0, input 0), step-24 (data, branch 0, input 0).

**Carry forward:** Report Unhappy Resolution: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 25. Notify Slack Channel

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 1, input 0), step-17 (data, branch 0, input 0), step-24 (data, branch 0, input 0).

**Carry forward:** Notify Slack Channel: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 26. Close Issue

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-11 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Close Issue: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 27. Send Reminder

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = issueComment. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Send Reminder: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 28. Reply to Issue

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = issueComment. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-18 (main, branch 0, input 0), step-17 (data, branch 0, input 0), step-24 (data, branch 0, input 0).

**Carry forward:** Reply to Issue: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 29. Close Issue2

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Close Issue2: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Automate Customer Support Issue Resolution using AI Text Classifier”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-automate-customer-support-issue-resolution-using-ai-text-classifier-4ab6b0/WORKFLOW.json
```
