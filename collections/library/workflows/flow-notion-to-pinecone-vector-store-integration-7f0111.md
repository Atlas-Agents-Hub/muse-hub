# Notion to Pinecone Vector Store Integration

Complete “Notion to Pinecone Vector Store Integration” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Notion to Pinecone Vector Store Integration.
- The selected records, date range, and output destination.
- Complete the named fields in flow-notion-to-pinecone-vector-store-integration-7f0111/INPUTS.json.
- Configured connections or tools for notion, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Token Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Token Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 2. Notion - Page Added Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Notion - Page Added Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Embeddings Google Gemini

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings Google Gemini: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Notion - Retrieve Page Content

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = block, operation = getAll. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Notion - Retrieve Page Content: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Create metadata and load content

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (textSplitter, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Create metadata and load content: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 6. Filter Non-Text Content

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Filter Non-Text Content: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 7. Summarize - Concatenate Notion's blocks content

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Summarize - Concatenate Notion's blocks content: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 8. Pinecone Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (embedding, branch 0, input 0), step-6 (document, branch 0, input 0), step-5 (main, branch 0, input 0).

**Carry forward:** Pinecone Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Notion to Pinecone Vector Store Integration”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-notion-to-pinecone-vector-store-integration-7f0111/WORKFLOW.json
```
