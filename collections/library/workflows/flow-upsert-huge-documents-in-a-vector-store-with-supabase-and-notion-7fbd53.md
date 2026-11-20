# Upsert huge documents in a vector store with Supabase and Notion

Complete “Upsert huge documents in a vector store with Supabase and Notion” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Upsert huge documents in a vector store with Supabase and Notion.
- The selected records, date range, and output destination.
- Complete the named fields in flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/INPUTS.json.
- Configured connections or tools for notion, scheduler, supabase, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 2. Notion Trigger

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Notion Trigger: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 3. Token Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Token Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 4. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 7. Get updated pages

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = databasePage, operation = getAll. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Get updated pages: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Supabase Vector Store1

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-1 (embedding, branch 0, input 0).

**Carry forward:** Supabase Vector Store1: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 9. Input Reference

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-16 (main, branch 0, input 0).

**Carry forward:** Input Reference: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 10. Vector Store Retriever

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-17 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Retriever: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 11. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-2 (textSplitter, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 12. Question and Answer Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (languageModel, branch 0, input 0), step-5 (retriever, branch 0, input 0), step-7 (main, branch 0, input 0).

**Carry forward:** Question and Answer Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Limit1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Limit1: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 14. Delete old embeddings if exist

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = delete. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Delete old embeddings if exist: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 15. Get page blocks

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = block, operation = getAll. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** Get page blocks: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 16. Supabase Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-1 (embedding, branch 0, input 0), step-13 (document, branch 0, input 0), step-19 (main, branch 0, input 0).

**Carry forward:** Supabase Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 17. Concatenate to single string

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Concatenate to single string: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 18. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-14 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 19. Limit

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Limit: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Upsert huge documents in a vector store with Supabase and Notion”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion-7fbd53/WORKFLOW.json
```
