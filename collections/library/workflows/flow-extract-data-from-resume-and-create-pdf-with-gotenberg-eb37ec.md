# Extract data from resume and create PDF with Gotenberg

Complete “Extract data from resume and create PDF with Gotenberg” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Extract data from resume and create PDF with Gotenberg.
- The selected records, date range, and output destination.
- Complete the named fields in flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/INPUTS.json.
- Configured connections or tools for http, telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Telegram trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Telegram trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Auth

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Auth: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 6. Auto-fixing Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (languageModel, branch 0, input 0), step-5 (outputParser, branch 0, input 0).

**Carry forward:** Auto-fixing Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 7. No operation (unauthorized)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** No operation (unauthorized): An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 8. Check if start message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Check if start message: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 9. No operation (start message)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0).

**Carry forward:** No operation (start message): An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 10. Get file

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = file. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Get file: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Extract text from PDF

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Extract text from PDF: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 12. Parse resume data

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-1 (languageModel, branch 0, input 0), step-15 (main, branch 0, input 0), step-3 (outputParser, branch 0, input 0).

**Carry forward:** Parse resume data: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Set parsed fileds

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-32 (main, branch 0, input 0).

**Carry forward:** Set parsed fileds: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Personal info

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Personal info: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. Technologies

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Technologies: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. Convert education to HTML

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Convert education to HTML: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 17. Convert employment history to HTML

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Convert employment history to HTML: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 18. Convert projects to HTML

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Convert projects to HTML: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 19. Convert volunteering to HTML

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Convert volunteering to HTML: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 20. Employment history

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Employment history: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. Education

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Education: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 22. Projects

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Projects: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 23. Volunteering

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Volunteering: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 24. Merge personal info and technologies

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 1), step-17 (main, branch 0, input 0).

**Carry forward:** Merge personal info and technologies: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 25. Merge education and employment history

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 1), step-19 (main, branch 0, input 0).

**Carry forward:** Merge education and employment history: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 26. Merge projects and volunteering

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-22 (main, branch 0, input 1).

**Carry forward:** Merge projects and volunteering: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 27. Merge other data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-33`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 1), step-23 (main, branch 0, input 0).

**Carry forward:** Merge other data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 28. Merge all

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-33 (main, branch 0, input 1), step-25 (main, branch 0, input 0).

**Carry forward:** Merge all: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 29. Set final data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Set final data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 30. Convert raw to base64

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** Convert raw to base64: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 31. Convert to HTML

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = toBinary. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Convert to HTML: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 32. Generate plain PDF doc

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0).

**Carry forward:** Generate plain PDF doc: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 33. Send PDF to the user

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendDocument. Read `../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0), step-16 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Send PDF to the user: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Extract data from resume and create PDF with Gotenberg”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-extract-data-from-resume-and-create-pdf-with-gotenberg-eb37ec/WORKFLOW.json
```
