# Advanced AI Demo (Presented at AI Developers #14 meetup)

Complete “Advanced AI Demo (Presented at AI Developers #14 meetup)” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Advanced AI Demo (Presented at AI Developers #14 meetup).
- The selected records, date range, and output destination.
- Complete the named fields in flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/INPUTS.json.
- Configured connections or tools for gmail, http, slack, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. PDFs to download

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** PDFs to download: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 2. Anthropic Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Anthropic Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Get calendar availability

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get calendar availability: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 5. Book appointment

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Book appointment: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 7. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 8. On new email to nathan's inbox

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On new email to nathan's inbox: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 9. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 10. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 11. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 12. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 13. Embeddings OpenAI2

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI2: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 14. Read Pinecone Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-7 (embedding, branch 0, input 0).

**Carry forward:** Read Pinecone Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 15. Appointment booking agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-18 (tool, branch 0, input 0), step-13 (languageModel, branch 0, input 0), step-16 (memory, branch 0, input 0), step-14 (tool, branch 0, input 0).

**Carry forward:** Appointment booking agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 16. Assign label with AI

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-20 (languageModel, branch 0, input 0), step-22 (main, branch 0, input 0).

**Carry forward:** Assign label with AI: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 17. Whether email contains n8n

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Whether email contains n8n: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 18. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Operation settings: dataType = binary. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (textSplitter, branch 0, input 0), step-10 (data, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 19. Download PDF

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Download PDF: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. Send message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Send message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 21. Insert into Pinecone vector store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-4 (embedding, branch 0, input 0), step-5 (document, branch 0, input 0).

**Carry forward:** Insert into Pinecone vector store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 22. Execute JavaScript

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Execute JavaScript: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 23. Add automation label

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = addLabels. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Add automation label: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 24. Add music label

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = addLabels. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 1, input 0).

**Carry forward:** Add music label: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 25. Vector Store Retriever

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-11 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Retriever: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 26. Question and Answer Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-6 (languageModel, branch 0, input 0), step-8 (retriever, branch 0, input 0), step-19 (main, branch 0, input 0).

**Carry forward:** Question and Answer Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Advanced AI Demo (Presented at AI Developers #14 meetup)”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-advanced-ai-demo-presented-at-ai-developers-14-meetup-4ce287/WORKFLOW.json
```
