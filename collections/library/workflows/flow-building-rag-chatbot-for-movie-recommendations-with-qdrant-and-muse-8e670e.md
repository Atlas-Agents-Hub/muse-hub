# Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI

Complete “Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/INPUTS.json.
- Configured connections or tools for github, http, vector-store, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Call n8n Workflow Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Call n8n Workflow Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 4. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 6. Token Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Token Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 7. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 8. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 9. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-9 (languageModel, branch 0, input 0), step-11 (memory, branch 0, input 0), step-10 (tool, branch 0, input 0), step-8 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 10. Embedding Recommendation Request with Open AI

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Embedding Recommendation Request with Open AI: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. GitHub

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = file, operation = get. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** GitHub: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. Embedding Anti-Recommendation Request with Open AI

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Embedding Anti-Recommendation Request with Open AI: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Extracting Embedding

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Extracting Embedding: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Extracting Embedding1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Extracting Embedding1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. Extract from File

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Extract from File: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 16. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-22 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 17. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (textSplitter, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 18. Calling Qdrant Recommendation API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Calling Qdrant Recommendation API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-4 (embedding, branch 0, input 0), step-3 (main, branch 0, input 0), step-5 (document, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 20. Split Out1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Split Out1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 21. Retrieving Recommended Movies Meta Data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Retrieving Recommended Movies Meta Data: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 22. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 23. Merge1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 1), step-15 (main, branch 0, input 0).

**Carry forward:** Merge1: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 24. Selecting Fields Relevant for Agent

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Selecting Fields Relevant for Agent: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 25. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-muse-8e670e/WORKFLOW.json
```
