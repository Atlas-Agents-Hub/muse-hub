# Breakdown Documents into Study Notes using Templating MistralAI and Qdrant

Complete “Breakdown Documents into Study Notes using Templating MistralAI and Qdrant” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Breakdown Documents into Study Notes using Templating MistralAI and Qdrant.
- The selected records, date range, and output destination.
- Complete the named fields in flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/INPUTS.json.
- Configured connections or tools for vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Local File Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Local File Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Item List Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Item List Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. Embeddings Mistral Cloud1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings Mistral Cloud1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Mistral Cloud Chat Model2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Mistral Cloud Chat Model2: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Mistral Cloud Chat Model3

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Mistral Cloud Chat Model3: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 7. Embeddings Mistral Cloud

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings Mistral Cloud: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 8. Mistral Cloud Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Mistral Cloud Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 9. Mistral Cloud Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Mistral Cloud Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 10. Qdrant Vector Store1

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store1: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 11. Settings

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Settings: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. Vector Store Retriever

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-16 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Retriever: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 13. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (textSplitter, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 14. Import File

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Import File: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 15. Get FileType

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0).

**Carry forward:** Get FileType: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 16. Extract from PDF

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Extract from PDF: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 17. Extract from DOCX

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = ods. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 1, input 0).

**Carry forward:** Extract from DOCX: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 18. Extract from TEXT

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = text. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 2, input 0).

**Carry forward:** Extract from TEXT: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 19. Prep Incoming Doc

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0), step-31 (main, branch 0, input 0), step-32 (main, branch 0, input 0).

**Carry forward:** Prep Incoming Doc: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 20. Summarization Chain

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Summarize the selected source with its required sections, audience, and length while retaining consequential details. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-33`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-6 (languageModel, branch 0, input 0).

**Carry forward:** Summarization Chain: A summary linked to its source material.

**Check:** Names, quantities, dates, and key conclusions match the source.

## 21. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-34`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-2 (document, branch 0, input 0), step-4 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 22. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = chooseBranch. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-34 (main, branch 0, input 1), step-33 (main, branch 0, input 0).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 23. Prep For AI

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-33 (data, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Prep For AI: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 24. Get Doc Types

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Get Doc Types: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 25. Split Out Doc Types

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Split Out Doc Types: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 26. For Each Doc Type...

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-11 (main, branch 0, input 0).

**Carry forward:** For Each Doc Type...: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 27. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-35 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 28. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 29. Discover

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-14 (retriever, branch 0, input 0), step-17 (languageModel, branch 0, input 0).

**Carry forward:** Discover: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 30. 2secs

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** 2secs: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 31. Generate

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-20 (languageModel, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Generate: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 32. Interview

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-35`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0), step-13 (outputParser, branch 0, input 0), step-5 (languageModel, branch 0, input 0), step-25 (data, branch 0, input 0).

**Carry forward:** Interview: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 33. Get Generated Documents

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-25 (data, branch 0, input 0).

**Carry forward:** Get Generated Documents: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 34. To Binary

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = toText. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** To Binary: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 35. Export to Folder

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = write. Read `../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0), step-11 (data, branch 0, input 0), step-23 (data, branch 0, input 0).

**Carry forward:** Export to Folder: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Breakdown Documents into Study Notes using Templating MistralAI and Qdrant”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant-0d02de/WORKFLOW.json
```
