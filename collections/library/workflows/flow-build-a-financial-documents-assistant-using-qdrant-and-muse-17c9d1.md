# Build a Financial Documents Assistant using Qdrant and Mistral.ai

Complete “Build a Financial Documents Assistant using Qdrant and Mistral.ai” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Build a Financial Documents Assistant using Qdrant and Mistral.ai.
- The selected records, date range, and output destination.
- Complete the named fields in flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/INPUTS.json.
- Configured connections or tools for http, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Local File Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Local File Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Mistral Cloud Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Mistral Cloud Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Embeddings Mistral Cloud1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings Mistral Cloud1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. When clicking "Test workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Test workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Embeddings Mistral Cloud

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings Mistral Cloud: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 6. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 7. Chat Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 8. Qdrant Vector Store1

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-13 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store1: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 9. Set Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-2 (main, branch 0, input 0).

**Carry forward:** Set Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 11. Vector Store Retriever

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-23 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Retriever: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 12. Handle File Event

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Handle File Event: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 13. Question and Answer Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-12 (retriever, branch 0, input 0), step-11 (languageModel, branch 0, input 0).

**Carry forward:** Question and Answer Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Search For Existing Point

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Search For Existing Point: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. Search For Existing Point1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 1, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Search For Existing Point1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 16. Has Existing Point?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Has Existing Point?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 17. Has Existing Point?1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Has Existing Point?1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 18. Delete Existing Point

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Delete Existing Point: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. Delete Existing Point1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Delete Existing Point1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. Remap for File_Added Flow

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Remap for File_Added Flow: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. Read File

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 2, input 0), step-14 (main, branch 0, input 0).

**Carry forward:** Read File: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 22. Prepare Embedding Document

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Prepare Embedding Document: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 23. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-6 (document, branch 0, input 0), step-5 (embedding, branch 0, input 0), step-8 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Build a Financial Documents Assistant using Qdrant and Mistral.ai”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-build-a-financial-documents-assistant-using-qdrant-and-muse-17c9d1/WORKFLOW.json
```
