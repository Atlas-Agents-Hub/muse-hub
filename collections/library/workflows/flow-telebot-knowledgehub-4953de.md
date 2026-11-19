# TeleBot KnowledgeHub

Complete “TeleBot KnowledgeHub” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for TeleBot KnowledgeHub.
- The selected records, date range, and output destination.
- Complete the named fields in flow-telebot-knowledgehub-4953de/INPUTS.json.
- Configured connections or tools for telegram, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Embeddings HuggingFace Inference

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings HuggingFace Inference: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 2. Telegram Message Trigger1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Telegram Message Trigger1: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Embeddings HuggingFace Inference1

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings HuggingFace Inference1: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 5. Upload your file here

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Upload your file here: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Groq Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Groq Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 7. Simple Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-12 (data, branch 0, input 0).

**Carry forward:** Simple Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 8. Retrieve documents

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = retrieve-as-tool. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-13 (embedding, branch 0, input 0).

**Carry forward:** Retrieve documents: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 9. Default Data Loader1

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader1: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 10. Get a chat1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = chat. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Get a chat1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Simple Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-5 (document, branch 0, input 0), step-7 (main, branch 0, input 0), step-10 (embedding, branch 0, input 0).

**Carry forward:** Simple Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 12. AI Agent1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-1 (memory, branch 0, input 0), step-2 (tool, branch 0, input 0), step-6 (main, branch 0, input 0), step-9 (languageModel, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** AI Agent1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 13. Reply in Telegram1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Reply in Telegram1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “TeleBot KnowledgeHub”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-telebot-knowledgehub-4953de/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-telebot-knowledgehub-4953de/WORKFLOW.json
```
