# Personal Shopper Chatbot for WooCommerce with RAG using Google Drive and openAI

Complete “Personal Shopper Chatbot for WooCommerce with RAG using Google Drive and openAI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Personal Shopper Chatbot for WooCommerce with RAG using Google Drive and openAI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/INPUTS.json.
- Configured connections or tools for googledrive, http, vector-store, woocommerce.
- An available model or embedding capability with the requested format and cost limits.

## 1. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model2: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Embeddings OpenAI3

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI3: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Token Splitter1

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Token Splitter1: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 5. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Calculator

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Calculator: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 8. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 9. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 10. Default Data Loader2

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: dataType = binary. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-17 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader2: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 11. HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Edit Fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Edit Fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 13. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 14. Information Extractor

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Extract the fields specified by the schema and keep their source context and missing-value state. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-12 (languageModel, branch 0, input 0).

**Carry forward:** Information Extractor: A structured record with source-linked values.

**Check:** Each required field is present or marked missing; invented values are not substituted.

## 15. Google Drive2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = fileFolder. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Google Drive2: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 16. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 17. RAG

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-9 (languageModel, branch 0, input 0), step-7 (vectorStore, branch 0, input 0).

**Carry forward:** RAG: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 18. personal_shopper

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (data, branch 0, input 0).

**Carry forward:** personal_shopper: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 19. Google Drive1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Google Drive1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 20. Qdrant Vector Store1

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-15 (embedding, branch 0, input 0), step-16 (document, branch 0, input 0).

**Carry forward:** Qdrant Vector Store1: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 21. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-6 (tool, branch 0, input 0), step-3 (tool, branch 0, input 0), step-10 (tool, branch 0, input 0), step-5 (languageModel, branch 0, input 0), step-2 (memory, branch 0, input 0), step-11 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Personal Shopper Chatbot for WooCommerce with RAG using Google Drive and openAI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-personal-shopper-chatbot-for-woocommerce-with-rag-using-google-drive-and-muse-ac4b5a/WORKFLOW.json
```
