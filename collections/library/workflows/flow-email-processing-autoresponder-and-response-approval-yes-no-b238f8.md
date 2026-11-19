# email processing autoresponder and response approval (Yes No)

Complete “email processing autoresponder and response approval (Yes No)” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for email processing autoresponder and response approval (Yes No).
- The selected records, date range, and output destination.
- Complete the named fields in flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/INPUTS.json.
- Configured connections or tools for emailreadimap, emailsend, gmail, vector-store.
- An available model or embedding capability with the requested format and cost limits.

## 1. Email Trigger (IMAP)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Email Trigger (IMAP): A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 2. DeepSeek R1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** DeepSeek R1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Embeddings OpenAI

Read [the Embeddings Guide method](../skills/embeddings-guide/SKILL.md). Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Embeddings OpenAI: Vectors paired with stable source identifiers.

**Check:** All vectors use one compatible dimension and each maps back to its original text.

## 4. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 6. Qdrant Vector Store

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Use the configured corpus, query, and retrieval settings to collect evidence for the current request. Operation settings: mode = retrieve-as-tool. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (embedding, branch 0, input 0).

**Carry forward:** Qdrant Vector Store: Ranked evidence with source identifiers and scores where available.

**Check:** Relevant items are retrievable and unrelated or out-of-scope material is excluded.

## 7. Email Summarization Chain

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Summarize the selected source with its required sections, audience, and length while retaining consequential details. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-3 (languageModel, branch 0, input 0).

**Carry forward:** Email Summarization Chain: A summary linked to its source material.

**Check:** Names, quantities, dates, and key conclusions match the source.

## 8. Set Email

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0), step-7 (main, branch 0, input 0).

**Carry forward:** Set Email: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Approve?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Approve?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Send Draft

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = sendAndWait. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Send Draft: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Write email

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-9 (languageModel, branch 0, input 0), step-10 (main, branch 0, input 0), step-5 (tool, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Write email: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Send Email

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Send Email: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “email processing autoresponder and response approval (Yes No)”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-email-processing-autoresponder-and-response-approval-yes-no-b238f8/WORKFLOW.json
```
