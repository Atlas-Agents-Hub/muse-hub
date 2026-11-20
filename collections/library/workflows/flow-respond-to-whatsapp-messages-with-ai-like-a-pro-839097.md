# Respond to WhatsApp Messages with AI Like a Pro!

Complete “Respond to WhatsApp Messages with AI Like a Pro!” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Respond to WhatsApp Messages with AI Like a Pro!.
- The selected records, date range, and output destination.
- Complete the named fields in flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/INPUTS.json.
- Configured connections or tools for http, toolwikipedia, whatsapp.
- An available model or embedding capability with the requested format and cost limits.

## 1. WhatsApp Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** WhatsApp Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Wikipedia

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Wikipedia: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Google Gemini Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Google Gemini Chat Model2

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model2: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 7. Split Out Message Parts

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Split Out Message Parts: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 8. Redirect Message Types

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Redirect Message Types: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 9. Get Text

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 3, input 0).

**Carry forward:** Get Text: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 10. Get Audio URL

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = media, operation = mediaUrlGet. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Get Audio URL: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Get Video URL

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = media, operation = mediaUrlGet. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0).

**Carry forward:** Get Video URL: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. Get Image URL

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = media, operation = mediaUrlGet. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 2, input 0).

**Carry forward:** Get Image URL: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Text Summarizer

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-21 (languageModel, branch 0, input 0).

**Carry forward:** Text Summarizer: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. Download Video

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Download Video: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 15. Download Audio

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Download Audio: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 16. Download Image

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Download Image: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 17. Image Explainer

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-20 (languageModel, branch 0, input 0).

**Carry forward:** Image Explainer: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 18. Google Gemini Audio

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Google Gemini Audio: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. Google Gemini Video

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Google Gemini Video: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. Format Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Format Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. Format Response1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Format Response1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 22. Get User's Message

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-15 (main, branch 0, input 0), step-23 (main, branch 0, input 0), step-22 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-10 (data, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Get User's Message: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 23. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-11 (tool, branch 0, input 0), step-9 (main, branch 0, input 0), step-8 (memory, branch 0, input 0), step-17 (languageModel, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 24. Respond to User

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = send. Read `../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Respond to User: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Respond to WhatsApp Messages with AI Like a Pro!”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-respond-to-whatsapp-messages-with-ai-like-a-pro-839097/WORKFLOW.json
```
