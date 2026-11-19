# AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow

Complete “AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow.
- The selected records, date range, and output destination.
- Complete the named fields in flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/INPUTS.json.
- Configured connections or tools for googledrive, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Embeddings OpenAI1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 2. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 3. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. On new manual Chat Message

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On new manual Chat Message: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 6. Webhook1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook1: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 7. When clicking "Execute Workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Execute Workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 8. Qdrant Vector Store1

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-1 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store1: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 9. Google Drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Google Drive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. Binary to Document

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (textSplitter, branch 0, input 0).

**Carry forward:** Binary to Document: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 11. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-11 (embedding, branch 0, input 0), step-9 (document, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 12. Vector Store Retriever

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-13 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Retriever: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 13. Retrieval QA Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-14 (languageModel, branch 0, input 0), step-5 (retriever, branch 0, input 0), step-2 (main, branch 0, input 0).

**Carry forward:** Retrieval QA Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-ai-crew-to-automate-fundamental-stock-analysis-q-a-workflow-d79555/WORKFLOW.json
```
