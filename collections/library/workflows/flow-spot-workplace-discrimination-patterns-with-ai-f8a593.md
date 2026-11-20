# Spot Workplace Discrimination Patterns with AI

Complete “Spot Workplace Discrimination Patterns with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Spot Workplace Discrimination Patterns with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-spot-workplace-discrimination-patterns-with-ai-f8a593/INPUTS.json.
- Configured connections or tools for http, quickchart.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. OpenAI Chat Model2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model2: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. SET company_name

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** SET company_name: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Define dictionary of demographic keys

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Define dictionary of demographic keys: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. ScrapingBee Search Glassdoor

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** ScrapingBee Search Glassdoor: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. Extract company url path

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Extract company url path: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 9. ScrapingBee GET company page contents

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** ScrapingBee GET company page contents: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Extract reviews page url path

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Extract reviews page url path: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 11. ScrapingBee GET Glassdoor Reviews Content

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** ScrapingBee GET Glassdoor Reviews Content: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Extract Overall Review Summary

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Extract Overall Review Summary: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 13. Extract Demographics Module

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Operation settings: operation = extractHtmlContent. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Extract Demographics Module: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 14. Extract overall ratings and distribution percentages

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-3 (languageModel, branch 0, input 0), step-13 (main, branch 0, input 0).

**Carry forward:** Extract overall ratings and distribution percentages: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 15. Extract demographic distributions

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-2 (languageModel, branch 0, input 0), step-14 (main, branch 0, input 0).

**Carry forward:** Extract demographic distributions: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 16. Define contributions to variance

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Define contributions to variance: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Set variance and std_dev

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-15 (data, branch 0, input 0).

**Carry forward:** Set variance and std_dev: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 18. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-16 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 19. Calculate Z-Scores and Effect Sizes

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Calculate Z-Scores and Effect Sizes: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 20. Calculate P-Scores

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Calculate P-Scores: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 21. Format dataset for scatterplot

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Format dataset for scatterplot: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 22. Sort Effect Sizes

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Sort Effect Sizes: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 23. Specify additional parameters for scatterplot

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Specify additional parameters for scatterplot: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 24. Quickchart Scatterplot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Quickchart Scatterplot: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 25. QuickChart Bar Chart

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** QuickChart Bar Chart: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 26. Text Analysis of Bias Data

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-5 (languageModel, branch 0, input 0), step-20 (main, branch 0, input 0).

**Carry forward:** Text Analysis of Bias Data: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Spot Workplace Discrimination Patterns with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-spot-workplace-discrimination-patterns-with-ai-f8a593/WORKFLOW.json
```
