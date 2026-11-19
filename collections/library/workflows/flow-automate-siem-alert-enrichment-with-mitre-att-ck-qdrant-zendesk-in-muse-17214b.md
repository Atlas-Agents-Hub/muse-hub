# Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n

Complete “Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n.
- The selected records, date range, and output destination.
- Complete the named fields in flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/INPUTS.json.
- Configured connections or tools for googledrive, vector-store, zendesk.
- An available model or embedding capability with the requested format and cost limits.

## 1. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 5. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 6. Get all Zendesk Tickets

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get all Zendesk Tickets: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 8. Embeddings OpenAI1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 9. Token Splitter1

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Token Splitter1: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 10. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 11. Embeddings OpenAI2

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI2: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 12. Pull Mitre Data From Gdrive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Pull Mitre Data From Gdrive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 13. Query Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = retrieve-as-tool. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-9 (embedding, branch 0, input 0).

**Carry forward:** Query Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 14. Qdrant Vector Store query

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = retrieve-as-tool. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-14 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store query: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 15. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 16. Extract from File

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: operation = fromJson. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Extract from File: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 17. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (languageModel, branch 0, input 0), step-8 (memory, branch 0, input 0), step-19 (tool, branch 0, input 0), step-1 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 18. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 19. Embed JSON in Qdrant Collection

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-5 (embedding, branch 0, input 0), step-6 (document, branch 0, input 0).

**Carry forward:** Embed JSON in Qdrant Collection: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 20. AI Agent1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0), step-13 (languageModel, branch 0, input 0), step-16 (outputParser, branch 0, input 0), step-20 (tool, branch 0, input 0).

**Carry forward:** AI Agent1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 21. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0), step-21 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 22. Update Zendesk with Mitre Data

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Update Zendesk with Mitre Data: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 23. Move on to next ticket

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Move on to next ticket: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-automate-siem-alert-enrichment-with-mitre-att-ck-qdrant-zendesk-in-muse-17214b/WORKFLOW.json
```
