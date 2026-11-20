# Make OpenAI Citation for File Retrieval RAG

Complete “Make OpenAI Citation for File Retrieval RAG” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Make OpenAI Citation for File Retrieval RAG.
- The selected records, date range, and output destination.
- Complete the named fields in flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 2. Create a simple Trigger to have the Chat button within N8N

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Create a simple Trigger to have the Chat button within N8N: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. OpenAI Assistant with Vector Store

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = assistant. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (memory, branch 0, input 0), step-3 (main, branch 0, input 0).

**Carry forward:** OpenAI Assistant with Vector Store: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 4. Get ALL Thread Content

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Get ALL Thread Content: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Split all message iterations from a thread

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Split all message iterations from a thread: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 6. Split all content from a single message

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Split all content from a single message: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 7. Split all citations from a single message

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Split all citations from a single message: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 8. Retrieve file name from a file ID

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Retrieve file name from a file ID: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. Regularize output

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Regularize output: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 11. Finnaly format the output

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Finnaly format the output: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 12. Optional Markdown to HTML

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Optional Markdown to HTML: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Make OpenAI Citation for File Retrieval RAG”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-make-muse-citation-for-file-retrieval-rag-3c0a2a/WORKFLOW.json
```
