# Classify lemlist replies using OpenAI and automate reply handling

Complete “Classify lemlist replies using OpenAI and automate reply handling” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Classify lemlist replies using OpenAI and automate reply handling.
- The selected records, date range, and output destination.
- Complete the named fields in flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/INPUTS.json.
- Configured connections or tools for http, lemlist, slack.
- An available model or embedding capability with the requested format and cost limits.

## 1. Lemlist Trigger - On new reply

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Lemlist Trigger - On new reply: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 4. Format text with Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Format text with Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 5. Categorize lemlist reply

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-3 (languageModel, branch 0, input 0), step-4 (outputParser, branch 0, input 0), step-1 (main, branch 0, input 0).

**Carry forward:** Categorize lemlist reply: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 6. Merge data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 1), step-1 (main, branch 0, input 0).

**Carry forward:** Merge data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 7. Route reply to the right branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Route reply to the right branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 8. Send alert to Slack

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Send alert to Slack: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. Lemlist - Unsubscribe

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = lead, operation = unsubscribe. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** Lemlist - Unsubscribe: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. lemlist - Mark as interested

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 2, input 0).

**Carry forward:** lemlist - Mark as interested: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Classify lemlist replies using OpenAI and automate reply handling”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-classify-lemlist-replies-using-muse-and-automate-reply-handling-b5c982/WORKFLOW.json
```
