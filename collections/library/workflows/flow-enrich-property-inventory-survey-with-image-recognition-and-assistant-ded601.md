# Enrich Property Inventory Survey with Image Recognition and Assistant

Complete “Enrich Property Inventory Survey with Image Recognition and Assistant” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Enrich Property Inventory Survey with Image Recognition and Assistant.
- The selected records, date range, and output destination.
- Complete the named fields in flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/INPUTS.json.
- Configured connections or tools for airtable, http, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Test workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Test workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Firecrawl Web Scaper Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Firecrawl Web Scaper Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Reverse Image Search Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Reverse Image Search Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Get Applicable Rows

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Applicable Rows: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Edit Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Edit Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Analyse Image

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Analyse Image: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Actions Router

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Actions Router: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 11. Firecrawl Scrape API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 1, input 0).

**Carry forward:** Firecrawl Scrape API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Object Identifier Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-15 (outputParser, branch 0, input 0), step-14 (tool, branch 0, input 0), step-9 (tool, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Object Identifier Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Fallback Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 2, input 0).

**Carry forward:** Fallback Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. SERP Google Reverse Image API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** SERP Google Reverse Image API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. Scrape Success?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Scrape Success?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 16. Enrich Product Rows

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Enrich Product Rows: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 17. Reverse Image Search Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Reverse Image Search Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 18. Firecrawl Scrape Success Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Firecrawl Scrape Success Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 19. Firecrawl scrape Error Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** Firecrawl scrape Error Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Enrich Property Inventory Survey with Image Recognition and Assistant”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-enrich-property-inventory-survey-with-image-recognition-and-assistant-ded601/WORKFLOW.json
```
