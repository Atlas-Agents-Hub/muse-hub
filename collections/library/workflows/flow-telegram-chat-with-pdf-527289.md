# Telegram chat with PDF

Complete “Telegram chat with PDF” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Telegram chat with PDF.
- The selected records, date range, and output destination.
- Complete the named fields in flow-telegram-chat-with-pdf-527289/INPUTS.json.
- Configured connections or tools for telegram, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Telegram Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Telegram Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Embeddings

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 3. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 5. Groq Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Groq Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. Check If is a document

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Check If is a document: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: dataType = binary. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 8. Pinecone Vector Store1

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-13 (embedding, branch 0, input 0).

**Carry forward:** Pinecone Vector Store1: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 9. Telegram get File

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = file. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Telegram get File: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Vector Store Retriever

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Retriever: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 11. Change to application/pdf

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Change to application/pdf: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 12. Question and Answer Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-9 (languageModel, branch 0, input 0), step-10 (main, branch 1, input 0), step-7 (retriever, branch 0, input 0).

**Carry forward:** Question and Answer Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Telegram Response

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-1 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Telegram Response: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 14. Pinecone Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-2 (embedding, branch 0, input 0), step-3 (document, branch 0, input 0), step-11 (main, branch 0, input 0).

**Carry forward:** Pinecone Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 15. Limit to 1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Limit to 1: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 16. Stop and Error

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 1, input 0).

**Carry forward:** Stop and Error: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 17. Telegram Response about Database

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-1 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Telegram Response about Database: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 18. Stop and Error1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** Stop and Error1: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Telegram chat with PDF”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-telegram-chat-with-pdf-527289/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-telegram-chat-with-pdf-527289/WORKFLOW.json
```
