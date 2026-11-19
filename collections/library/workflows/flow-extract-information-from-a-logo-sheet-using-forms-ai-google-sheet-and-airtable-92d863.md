# Extract Information from a Logo Sheet using forms, AI, Google Sheet and Airtable

Complete “Extract Information from a Logo Sheet using forms, AI, Google Sheet and Airtable” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Extract Information from a Logo Sheet using forms, AI, Google Sheet and Airtable.
- The selected records, date range, and output destination.
- Complete the named fields in flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/INPUTS.json.
- Configured connections or tools for airtable.
- An available model or embedding capability with the requested format and cost limits.

## 1. On form submission

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On form submission: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. gpt-4o

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** gpt-4o: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Get Schema

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-33`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get Schema: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 4. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 5. Map Agent Input

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Map Agent Input: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. make it a readable list

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-33 (main, branch 0, input 0).

**Carry forward:** make it a readable list: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 7. Retrieve and Parser Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-29 (languageModel, branch 0, input 0), step-28 (main, branch 0, input 0), step-4 (outputParser, branch 0, input 0).

**Carry forward:** Retrieve and Parser Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. JSON it

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** JSON it: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Split Out Tools

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Split Out Tools: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 10. Split Out each Attribute String

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 1, input 0).

**Carry forward:** Split Out each Attribute String: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 11. Table: Tools

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Table: Tools: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 12. Check if Attribute exists

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = upsert. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Check if Attribute exists: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-13 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 14. Map Attribute ID

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Map Attribute ID: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. Loop Over Attributes

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-7 (main, branch 0, input 0).

**Carry forward:** Loop Over Attributes: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 16. Wait for Attribute Creation

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = chooseBranch. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 1), step-12 (main, branch 0, input 0).

**Carry forward:** Wait for Attribute Creation: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 17. Change each Attribute to the corresponding RecID

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Change each Attribute to the corresponding RecID: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 18. Generate Unique Hash for Name

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Generate Unique Hash for Name: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 19. Create if not Exist

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = upsert. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Create if not Exist: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 20. Merge Old Data + RecID

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 1), step-14 (main, branch 0, input 0).

**Carry forward:** Merge Old Data + RecID: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 21. Only what we need

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Only what we need: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 22. Determine Attributes we should save

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Determine Attributes we should save: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 23. Split Out similar

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Split Out similar: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 24. Merge1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-19 (main, branch 0, input 1).

**Carry forward:** Merge1: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 25. Generate Unique Hash for Similar

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Generate Unique Hash for Similar: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 26. It Should exists

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = upsert. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** It Should exists: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 27. All Similar

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** All Similar: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 28. Merge2

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = chooseBranch. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 1), step-18 (main, branch 0, input 0).

**Carry forward:** Merge2: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 29. Change each Smiliar to the corresponding RecID

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0), step-23 (data, branch 0, input 0).

**Carry forward:** Change each Smiliar to the corresponding RecID: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 30. Determine Similar we should save

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Determine Similar we should save: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 31. Save all this juicy data

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = upsert. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Save all this juicy data: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 32. Table: Attributes

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Table: Attributes: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 33. All Attributes

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** All Attributes: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Extract Information from a Logo Sheet using forms, AI, Google Sheet and Airtable”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-extract-information-from-a-logo-sheet-using-forms-ai-google-sheet-and-airtable-92d863/WORKFLOW.json
```
