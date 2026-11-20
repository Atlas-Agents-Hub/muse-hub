# Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI

Complete “Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/INPUTS.json.
- Configured connections or tools for http, vector-store, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Embeddings Mistral Cloud

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings Mistral Cloud: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 5. Window Buffer Memory1

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory1: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 6. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 7. Ask Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Ask Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Search Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Search Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 9. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 10. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-25 (memory, branch 0, input 0).

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 11. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Get Tax Code Zip File

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Tax Code Zip File: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Get Mistral Embeddings

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Get Mistral Embeddings: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 14. Use Qdrant Scroll API

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 1, input 0).

**Carry forward:** Use Qdrant Scroll API: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-28 (tool, branch 0, input 0), step-29 (tool, branch 0, input 0), step-26 (languageModel, branch 0, input 0), step-23 (memory, branch 0, input 0), step-24 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 16. Extract Zip Files

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Extract Zip Files: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 17. Use Qdrant Search API1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Use Qdrant Search API1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 18. Get Search Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Get Search Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 19. Files as Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Files as Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 20. Get Ask Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Get Ask Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. Extract PDF Contents

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = pdf. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Extract PDF Contents: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 22. Extract From Chapter

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Extract From Chapter: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 23. Map To Sections

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Map To Sections: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 24. Sections To List

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Sections To List: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 25. Only Valid Sections

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Only Valid Sections: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 26. Content Chunking @ 50k Chars

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** Content Chunking @ 50k Chars: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 27. Split Out Chunks

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Split Out Chunks: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 28. For Each Section...

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0), step-17 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** For Each Section...: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 29. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-3 (document, branch 0, input 0), step-2 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 30. 1sec

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** 1sec: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 31. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (textSplitter, branch 0, input 0), step-15 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-build-a-tax-code-assistant-with-qdrant-muse-81ff0a/WORKFLOW.json
```
