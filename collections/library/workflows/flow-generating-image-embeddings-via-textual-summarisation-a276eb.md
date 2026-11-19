# Generating Image Embeddings via Textual Summarisation

Complete “Generating Image Embeddings via Textual Summarisation” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Generating Image Embeddings via Textual Summarisation.
- The selected records, date range, and output destination.
- Complete the named fields in flow-generating-image-embeddings-via-textual-summarisation-a276eb/INPUTS.json.
- Configured connections or tools for googledrive, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Test workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Test workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 3. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 4. Embeddings OpenAI1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 5. Search for Image

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = load. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-9 (embedding, branch 0, input 0).

**Carry forward:** Search for Image: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 6. Google Drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Google Drive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Get Color Information

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = information. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Get Color Information: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 8. Resize Image

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = resize. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Resize Image: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 9. Get Image Keywords

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Get Image Keywords: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Combine Image Analysis

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 1), step-3 (main, branch 0, input 0).

**Carry forward:** Combine Image Analysis: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 11. Document for Embedding

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Document for Embedding: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (textSplitter, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 13. In-Memory Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-12 (embedding, branch 0, input 0), step-5 (document, branch 0, input 0), step-8 (main, branch 0, input 0).

**Carry forward:** In-Memory Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Generating Image Embeddings via Textual Summarisation”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-generating-image-embeddings-via-textual-summarisation-a276eb/WORKFLOW.json
```
