# RAG Context-Aware Chunking Google Drive to Pinecone via OpenRouter & Gemini

Complete “RAG Context-Aware Chunking Google Drive to Pinecone via OpenRouter & Gemini” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for RAG Context-Aware Chunking Google Drive to Pinecone via OpenRouter & Gemini.
- The selected records, date range, and output destination.
- Complete the named fields in flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/INPUTS.json.
- Configured connections or tools for googledrive, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenRouter Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenRouter Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Embeddings Google Gemini

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings Google Gemini: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 5. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 6. Get Document From Google Drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Document From Google Drive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Extract Text Data From Google Document

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = text. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Extract Text Data From Google Document: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 8. Split Document Text Into Sections

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Split Document Text Into Sections: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. Prepare Sections For Looping

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Prepare Sections For Looping: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 10. AI Agent - Prepare Context

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 1, input 0), step-3 (languageModel, branch 0, input 0), step-10 (data, branch 0, input 0).

**Carry forward:** AI Agent - Prepare Context: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 11. Concatenate the context and section text

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Concatenate the context and section text: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-11 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 13. Pinecone Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (document, branch 0, input 0), step-5 (embedding, branch 0, input 0), step-13 (main, branch 0, input 0).

**Carry forward:** Pinecone Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “RAG Context-Aware Chunking Google Drive to Pinecone via OpenRouter & Gemini”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-rag-context-aware-chunking-google-drive-to-pinecone-via-openrouter-muse-fcc953/WORKFLOW.json
```
