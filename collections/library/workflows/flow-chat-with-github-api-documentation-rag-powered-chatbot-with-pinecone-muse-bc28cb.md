# Chat with GitHub API Documentation RAG-Powered Chatbot with Pinecone & OpenAI

Complete “Chat with GitHub API Documentation RAG-Powered Chatbot with Pinecone & OpenAI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Chat with GitHub API Documentation RAG-Powered Chatbot with Pinecone & OpenAI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/INPUTS.json.
- Configured connections or tools for http, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Generate User Query Embedding

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Generate User Query Embedding: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. Generate Embeddings

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Generate Embeddings: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 5. Recursive Character Text Splitter

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Split the selected material using the configured size, overlap, separators, and source metadata. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Recursive Character Text Splitter: Source-linked chunks with stable identifiers.

**Check:** A boundary sample preserves meaning and overlapping chunks are traceable to the same source.

## 6. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 7. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 8. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 9. Pinecone Vector Store (Querying)

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (embedding, branch 0, input 0).

**Carry forward:** Pinecone Vector Store (Querying): Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 10. HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Default Data Loader

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-5 (textSplitter, branch 0, input 0).

**Carry forward:** Default Data Loader: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 12. Vector Store Tool

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (languageModel, branch 0, input 0), step-13 (vectorStore, branch 0, input 0).

**Carry forward:** Vector Store Tool: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 13. Pinecone Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = insert. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-4 (document, branch 0, input 0), step-14 (embedding, branch 0, input 0).

**Carry forward:** Pinecone Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 14. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (languageModel, branch 0, input 0), step-10 (tool, branch 0, input 0), step-9 (memory, branch 0, input 0), step-6 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Chat with GitHub API Documentation RAG-Powered Chatbot with Pinecone & OpenAI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-muse-bc28cb/WORKFLOW.json
```
