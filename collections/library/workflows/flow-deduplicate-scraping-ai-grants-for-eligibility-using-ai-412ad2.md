# Deduplicate Scraping AI Grants for Eligibility using AI

Complete “Deduplicate Scraping AI Grants for Eligibility using AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Deduplicate Scraping AI Grants for Eligibility using AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/INPUTS.json.
- Configured connections or tools for airtable, gmail, http, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. Everyday @ 9am

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Everyday @ 9am: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Everyday @ 8.30am

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Everyday @ 8.30am: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 3. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. AI Grants since Yesterday

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** AI Grants since Yesterday: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Get New Eligible Grants Today

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Get New Eligible Grants Today: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Grants to List

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Grants to List: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 8. Generate Email

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Generate Email: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 9. Get Subscribers

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Get Subscribers: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. Only New Grants

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Compare the configured identity fields and keep the selected representative of each distinct record. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Only New Grants: Distinct records and a duplicate count.

**Check:** Two records with the same identity collapse while different identities remain separate.

## 11. Send Subscriber Email

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Send Subscriber Email: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. Get Grant Details

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Get Grant Details: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Summarize Synopsis

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-3 (languageModel, branch 0, input 0).

**Carry forward:** Summarize Synopsis: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 14. Eligibility Factors

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-6 (languageModel, branch 0, input 0).

**Carry forward:** Eligibility Factors: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 15. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-5 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 16. Save to Tracker

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-2 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Save to Tracker: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Deduplicate Scraping AI Grants for Eligibility using AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-deduplicate-scraping-ai-grants-for-eligibility-using-ai-412ad2/WORKFLOW.json
```
