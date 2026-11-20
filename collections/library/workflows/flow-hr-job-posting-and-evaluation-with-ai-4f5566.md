# HR Job Posting and Evaluation with AI

Complete “HR Job Posting and Evaluation with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for HR Job Posting and Evaluation with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-hr-job-posting-and-evaluation-with-ai-4f5566/INPUTS.json.
- Configured connections or tools for airtable, emailsend, googlecalendar, googledrive.
- An available model or embedding capability with the requested format and cost limits.

## 1. On form submission

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On form submission: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. Airtable2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Airtable2: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. job_posting

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** job_posting: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. candidate_insights

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** candidate_insights: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Google Calendar

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Calendar: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. job_posting1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** job_posting1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. candidate_insights1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** candidate_insights1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 9. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 10. Airtable1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Airtable1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 11. Upload CV to google drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Upload CV to google drive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. applicant details

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** applicant details: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Airtable

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Airtable: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 14. download CV

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** download CV: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 15. Extract from File

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Extract from File: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 16. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (tool, branch 0, input 0), step-6 (main, branch 0, input 0), step-8 (languageModel, branch 0, input 0), step-10 (outputParser, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 17. shortlisted?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** shortlisted?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 18. Rejected

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** Rejected: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. Potential Hire

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Potential Hire: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 20. generate questionnaires

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (tool, branch 0, input 0), step-13 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** generate questionnaires: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 21. questionnaires

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** questionnaires: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 22. update questionnaires

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-15 (data, branch 0, input 0).

**Carry forward:** update questionnaires: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 23. Personalize email

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-18 (tool, branch 0, input 0), step-19 (tool, branch 0, input 0), step-17 (main, branch 0, input 0).

**Carry forward:** Personalize email: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 24. Edit Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Edit Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 25. Send Email

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Send Email: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 26. Book Meeting

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-24 (tool, branch 0, input 0).

**Carry forward:** Book Meeting: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 27. update phone meeting time

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** update phone meeting time: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 28. Screening Questions

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-27 (tool, branch 0, input 0), step-28 (tool, branch 0, input 0), step-25 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Screening Questions: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 29. Edit Fields1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Edit Fields1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 30. screening questions

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** screening questions: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “HR Job Posting and Evaluation with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-hr-job-posting-and-evaluation-with-ai-4f5566/WORKFLOW.json
```
