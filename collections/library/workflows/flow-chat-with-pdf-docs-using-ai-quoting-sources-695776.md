# Chat with PDF docs using AI (quoting sources)

Complete “Chat with PDF docs using AI (quoting sources)” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Chat with PDF docs using AI (quoting sources).
- The selected records, date range, and output destination.
- Complete the named fields in flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/INPUTS.json.
- Configured connections or tools for googledrive, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Execute Workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Execute Workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 5. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 6. Chat Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 7. Embeddings OpenAI2

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI2: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 8. Set max chunks to send to model

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Set max chunks to send to model: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Set file URL in Google Drive

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set file URL in Google Drive: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Get top chunks matching query

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = load. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-9 (embedding, branch 0, input 0), step-11 (main, branch 0, input 0).

**Carry forward:** Get top chunks matching query: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 11. Download file

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Download file: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. Add in metadata

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Add in metadata: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. Prepare chunks

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Prepare chunks: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 14. Answer the query based on chunks

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-10 (languageModel, branch 0, input 0), step-12 (outputParser, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Answer the query based on chunks: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 15. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: dataType = binary. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-18 (textSplitter, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 16. Compose citations

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-16 (data, branch 0, input 0).

**Carry forward:** Compose citations: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 17. Add to Pinecone vector store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (embedding, branch 0, input 0), step-3 (document, branch 0, input 0).

**Carry forward:** Add to Pinecone vector store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 18. Generate response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Generate response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Chat with PDF docs using AI (quoting sources)”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-chat-with-pdf-docs-using-ai-quoting-sources-695776/WORKFLOW.json
```
