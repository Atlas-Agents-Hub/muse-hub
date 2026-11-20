# Survey Insights with Qdrant, Python and Information Extractor

Complete “Survey Insights with Qdrant, Python and Information Extractor” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Survey Insights with Qdrant, Python and Information Extractor.
- The selected records, date range, and output destination.
- Complete the named fields in flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/INPUTS.json.
- Configured connections or tools for googlesheets, http, vector-store, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 4. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 6. Get Sheet Details

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Get Sheet Details: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 7. Get Survey Results

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Get Survey Results: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Set Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Set Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (textSplitter, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 10. Convert to Question Answer Pairs

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Convert to Question Answer Pairs: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Create Insights Sheet

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** Create Insights Sheet: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. QA Pairs to List

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** QA Pairs to List: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 13. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0), step-1 (embedding, branch 0, input 0), step-2 (document, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 14. Get Survey Headers

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** Get Survey Headers: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 15. Prep Values For Trigger

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Prep Values For Trigger: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. Extract Questions

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Extract Questions: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Trigger Insights

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Trigger Insights: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 18. Questions to List

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Questions to List: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 19. Get Payload of Points

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Get Payload of Points: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. Clusters To List

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Clusters To List: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 21. Prep Output For Export

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0), step-10 (data, branch 0, input 0).

**Carry forward:** Prep Output For Export: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 22. Export To Sheets

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-12 (data, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** Export To Sheets: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 23. Export To Sheets1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-12 (data, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** Export To Sheets1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 24. For Each Question...

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-16 (main, branch 0, input 0), step-8 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** For Each Question...: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 25. Prep Values For Export

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 1, input 0), step-17 (data, branch 0, input 0).

**Carry forward:** Prep Values For Export: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 26. Has Clusters?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Has Clusters?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 27. Only Clusters With 3+ points

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Only Clusters With 3+ points: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 28. Apply K-means Clustering Algorithm

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Apply K-means Clustering Algorithm: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 29. Survey Insights Agent

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-13 (languageModel, branch 0, input 0), step-10 (main, branch 0, input 0).

**Carry forward:** Survey Insights Agent: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 30. Find All Answers

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 1, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Find All Answers: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Survey Insights with Qdrant, Python and Information Extractor”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-survey-insights-with-qdrant-python-and-information-extractor-d7bf53/WORKFLOW.json
```
