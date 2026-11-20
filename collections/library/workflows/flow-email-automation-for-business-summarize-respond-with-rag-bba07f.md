# Email Automation for Business Summarize & Respond with RAG

Complete “Email Automation for Business Summarize & Respond with RAG” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Email Automation for Business Summarize & Respond with RAG.
- The selected records, date range, and output destination.
- Complete the named fields in flow-email-automation-for-business-summarize-respond-with-rag-bba07f/INPUTS.json.
- Configured connections or tools for emailreadimap, emailsend, googledrive, http, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Email Trigger (IMAP)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Email Trigger (IMAP): A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 2. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Token Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Token Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 4. Embeddings OpenAI1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 5. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. DeepSeek

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** DeepSeek: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 7. OpenAI 4-o-mini

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI 4-o-mini: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 8. DeepSeek R1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** DeepSeek R1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 9. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 10. Create collection

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Create collection: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Refresh collection

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Refresh collection: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: dataType = binary. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-17 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 13. Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 14. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = retrieve-as-tool. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 15. Get folder

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = fileFolder. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Get folder: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 16. Email Summarization Chain

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Summarize the selected source with its required sections, audience, and length while retaining consequential details. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-3 (languageModel, branch 0, input 0).

**Carry forward:** Email Summarization Chain: A summary linked to its source material.

**Check:** Names, quantities, dates, and key conclusions match the source.

## 17. Download Files

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Download Files: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 18. Email Classifier

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-23 (languageModel, branch 0, input 0), step-8 (main, branch 0, input 0).

**Carry forward:** Email Classifier: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 19. Qdrant Vector Store1

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-19 (embedding, branch 0, input 0), step-16 (document, branch 0, input 0).

**Carry forward:** Qdrant Vector Store1: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 20. Do nothing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 1, input 0).

**Carry forward:** Do nothing: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 21. Write email

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-21 (languageModel, branch 0, input 0), step-7 (main, branch 0, input 0), step-5 (tool, branch 0, input 0).

**Carry forward:** Write email: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 22. Review email

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-22 (languageModel, branch 0, input 0), step-9 (main, branch 0, input 0).

**Carry forward:** Review email: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 23. Send Email

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Send Email: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Email Automation for Business Summarize & Respond with RAG”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-email-automation-for-business-summarize-respond-with-rag-bba07f/WORKFLOW.json
```
