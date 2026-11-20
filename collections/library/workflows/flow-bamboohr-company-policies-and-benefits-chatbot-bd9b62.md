# BambooHR Company Policies and Benefits Chatbot

Complete “BambooHR Company Policies and Benefits Chatbot” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for BambooHR Company Policies and Benefits Chatbot.
- The selected records, date range, and output destination.
- Complete the named fields in flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/INPUTS.json.
- Configured connections or tools for bamboohr, vector-store, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Employee Lookup Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Employee Lookup Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. OpenAI Chat Model2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model2: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. OpenAI Chat Model3

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model3: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. OpenAI Chat Model4

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model4: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. OpenAI Chat Model5

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model5: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 7. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 8. Employee initiates a conversation

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Employee initiates a conversation: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 9. AI-Powered HR Benefits and Company Policies Chatbot

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** AI-Powered HR Benefits and Company Policies Chatbot: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 10. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 11. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 12. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 13. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 14. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 15. Embeddings OpenAI1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 16. Auto-fixing Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-15 (languageModel, branch 0, input 0), step-16 (outputParser, branch 0, input 0).

**Carry forward:** Auto-fixing Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 17. GET all files

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = file, operation = getAll. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** GET all files: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 18. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: dataType = binary. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 19. Supabase Vector Store Retrieval

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-9 (embedding, branch 0, input 0).

**Carry forward:** Supabase Vector Store Retrieval: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 20. Text Classifier

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-11 (languageModel, branch 0, input 0), step-25 (main, branch 0, input 0).

**Carry forward:** Text Classifier: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 21. Filter out files from undesired categories

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Filter out files from undesired categories: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 22. GET all employees

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** GET all employees: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 23. GET all employees (second path)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 1, input 0).

**Carry forward:** GET all employees (second path): A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 24. Vector Store Tool

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (languageModel, branch 0, input 0), step-24 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Tool: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 25. Split out individual files

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Split out individual files: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 26. Filter out other employees

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0), step-25 (data, branch 0, input 0).

**Carry forward:** Filter out other employees: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 27. Extract departments

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Extract departments: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 28. HR AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-39`, for its exact field mappings, expressions, and settings. Use the output from step-6 (languageModel, branch 0, input 0), step-7 (tool, branch 0, input 0), step-10 (tool, branch 0, input 0), step-5 (memory, branch 0, input 0), step-23 (main, branch 0, input 0).

**Carry forward:** HR AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 29. Filter out non-pdf files

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Filter out non-pdf files: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 30. Stringify employee record for response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Stringify employee record for response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 31. Ensure uniqueness in department list

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-31 (main, branch 0, input 0), step-26 (data, branch 0, input 0).

**Carry forward:** Ensure uniqueness in department list: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 32. Download file from BambooHR

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = file, operation = download. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Download file from BambooHR: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 33. Extract department

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-33`, for its exact field mappings, expressions, and settings. Use the output from step-12 (languageModel, branch 0, input 0), step-32 (main, branch 0, input 0).

**Carry forward:** Extract department: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 34. Supabase Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-3 (embedding, branch 0, input 0), step-2 (document, branch 0, input 0), step-21 (main, branch 0, input 0).

**Carry forward:** Supabase Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 35. Retrieve all employees

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-34`, for its exact field mappings, expressions, and settings. Use the output from step-33 (main, branch 0, input 0).

**Carry forward:** Retrieve all employees: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 36. Filter out other departments

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-35`, for its exact field mappings, expressions, and settings. Use the output from step-34 (main, branch 0, input 0), step-33 (data, branch 0, input 0).

**Carry forward:** Filter out other departments: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 37. Extract relevant employee fields

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-36`, for its exact field mappings, expressions, and settings. Use the output from step-35 (main, branch 0, input 0).

**Carry forward:** Extract relevant employee fields: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 38. Identify most senior employee

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-37`, for its exact field mappings, expressions, and settings. Use the output from step-13 (languageModel, branch 0, input 0), step-14 (outputParser, branch 0, input 0), step-36 (main, branch 0, input 0).

**Carry forward:** Identify most senior employee: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 39. Format name for response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json`, node `step-38`, for its exact field mappings, expressions, and settings. Use the output from step-37 (main, branch 0, input 0).

**Carry forward:** Format name for response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “BambooHR Company Policies and Benefits Chatbot”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-bamboohr-company-policies-and-benefits-chatbot-bd9b62/WORKFLOW.json
```
