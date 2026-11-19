# AI Data Extraction with Dynamic Prompts and Airtable

Complete “AI Data Extraction with Dynamic Prompts and Airtable” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for AI Data Extraction with Dynamic Prompts and Airtable.
- The selected records, date range, and output destination.
- Complete the named fields in flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/INPUTS.json.
- Configured connections or tools for airtable, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Airtable Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Airtable Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Get Table Schema

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = base, operation = getSchema. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Get Table Schema: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Set Airtable Vars

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-31 (main, branch 0, input 0).

**Carry forward:** Set Airtable Vars: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. Get Prompt Fields

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Get Prompt Fields: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. Get Table Schema1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = base, operation = getSchema. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-33`, for its exact field mappings, expressions, and settings. Use the output from step-32 (main, branch 0, input 0).

**Carry forward:** Get Table Schema1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 9. FieldsChanged Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-36`, for its exact field mappings, expressions, and settings. Use the output from step-32 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** FieldsChanged Webhook: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Get Webhook Payload

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-30 (data, branch 0, input 0).

**Carry forward:** Get Webhook Payload: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Get "Input" Field

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-34`, for its exact field mappings, expressions, and settings. Use the output from step-33 (main, branch 0, input 0), step-32 (data, branch 0, input 0).

**Carry forward:** Get "Input" Field: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Parse Event

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-2 (data, branch 0, input 0), step-30 (data, branch 0, input 0).

**Carry forward:** Parse Event: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. RecordsChanged Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-35`, for its exact field mappings, expressions, and settings. Use the output from step-34 (main, branch 0, input 0), step-32 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** RecordsChanged Webhook: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 14. Event Type

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Event Type: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 15. Event Ref

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 1, input 0), step-1 (main, branch 2, input 0).

**Carry forward:** Event Ref: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 16. Event Ref1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Event Ref1: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 17. Filter Valid Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Filter Valid Fields: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 18. Get Row

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Get Row: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 19. Filter Valid Rows

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** Filter Valid Rows: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 20. Fetch Records

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Fetch Records: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 21. Loop Over Items1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0), step-16 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 22. Row Ref

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** Row Ref: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 23. Get File Data1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Get File Data1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 24. Extract from File1

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Extract from File1: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 25. Get Result1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Get Result1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 26. Generate Field Value1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-20 (languageModel, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Generate Field Value1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 27. Update Row

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-18 (data, branch 0, input 0).

**Carry forward:** Update Row: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 28. Add Row ID to Payload

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Add Row ID to Payload: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 29. Update Record

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0), step-19 (data, branch 0, input 0).

**Carry forward:** Update Record: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 30. Get File Data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Get File Data: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 31. Extract from File

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Extract from File: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 32. Get Result

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-18 (data, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Get Result: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 33. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0), step-25 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 34. Row Reference

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 1, input 0).

**Carry forward:** Row Reference: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 35. Generate Field Value

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-21 (languageModel, branch 0, input 0), step-18 (data, branch 0, input 0).

**Carry forward:** Generate Field Value: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 36. Fields to Update

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-11 (data, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Fields to Update: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “AI Data Extraction with Dynamic Prompts and Airtable”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-ai-data-extraction-with-dynamic-prompts-and-airtable-6a0a11/WORKFLOW.json
```
