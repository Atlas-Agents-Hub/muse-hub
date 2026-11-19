# Visualize your SQL Agent queries with OpenAI and Quickchart.io

Complete “Visualize your SQL Agent queries with OpenAI and Quickchart.io” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Visualize your SQL Agent queries with OpenAI and Quickchart.io.
- The selected records, date range, and output destination.
- Complete the named fields in flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/INPUTS.json.
- Configured connections or tools for http, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. OpenAI Chat Model Classifier

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model Classifier: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Execute "Generate a chart" tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute "Generate a chart" tool: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-6 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 6. Information Extractor - User question

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-1 (languageModel, branch 0, input 0), step-6 (main, branch 0, input 0).

**Carry forward:** Information Extractor - User question: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 7. OpenAI - Generate Chart definition with Structured Output

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** OpenAI - Generate Chart definition with Structured Output: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. Set response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Set response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-1 (languageModel, branch 0, input 0), step-10 (memory, branch 0, input 0), step-14 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Text Classifier - Chart required?

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-11 (languageModel, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Text Classifier - Chart required?: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 11. User question + Agent initial response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** User question + Agent initial response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Set Text output

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Set Text output: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Execute Workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Execute Workflow: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 14. Set Text + Chart output

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Set Text + Chart output: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Visualize your SQL Agent queries with OpenAI and Quickchart.io”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-visualize-your-sql-agent-queries-with-muse-and-quickchart-io-01227b/WORKFLOW.json
```
