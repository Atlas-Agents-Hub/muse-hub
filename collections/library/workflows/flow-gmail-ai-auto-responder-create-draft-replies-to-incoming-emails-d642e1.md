# Gmail AI Auto-Responder Create Draft Replies to incoming emails

Complete “Gmail AI Auto-Responder Create Draft Replies to incoming emails” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Gmail AI Auto-Responder Create Draft Replies to incoming emails.
- The selected records, date range, and output destination.
- Complete the named fields in flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/INPUTS.json.
- Configured connections or tools for gmail.
- An available model or embedding capability with the requested format and cost limits.

## 1. Gmail Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. JSON Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** JSON Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. OpenAI Chat

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Assess if message needs a reply

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-3 (outputParser, branch 0, input 0), step-4 (languageModel, branch 0, input 0), step-1 (main, branch 0, input 0).

**Carry forward:** Assess if message needs a reply: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. If Needs Reply

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** If Needs Reply: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Generate email reply

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-5 (languageModel, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Generate email reply: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Gmail - Create Draft

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = draft. Read `../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Gmail - Create Draft: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Gmail AI Auto-Responder Create Draft Replies to incoming emails”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-gmail-ai-auto-responder-create-draft-replies-to-incoming-emails-d642e1/WORKFLOW.json
```
