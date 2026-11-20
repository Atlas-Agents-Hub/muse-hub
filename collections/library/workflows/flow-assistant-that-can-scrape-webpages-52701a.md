# Assistant that can scrape webpages

Complete “Assistant that can scrape webpages” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Assistant that can scrape webpages.
- The selected records, date range, and output destination.
- Complete the named fields in flow-assistant-that-can-scrape-webpages-52701a/INPUTS.json.
- Configured connections or tools for http, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. On new manual Chat Message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On new manual Chat Message: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. HTTP_Request_Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** HTTP_Request_Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. QUERY_PARAMS

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** QUERY_PARAMS: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. ReAct AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-16 (tool, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-1 (main, branch 0, input 0).

**Carry forward:** ReAct AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 7. CONFIG

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** CONFIG: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Is error?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Is error?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Exctract HTML Body

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0).

**Carry forward:** Exctract HTML Body: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Stringify error message

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Stringify error message: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Remove extra tags

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Remove extra tags: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Simplify?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Simplify?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 14. Simplify output

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Simplify output: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. Convert to Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0), step-9 (main, branch 0, input 0).

**Carry forward:** Convert to Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 16. Send Page Content

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Send Page Content: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Assistant that can scrape webpages”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-assistant-that-can-scrape-webpages-52701a/WORKFLOW.json
```
