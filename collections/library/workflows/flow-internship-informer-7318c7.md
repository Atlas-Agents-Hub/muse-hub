# Internship Informer

Complete “Internship Informer” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Internship Informer.
- The selected records, date range, and output destination.
- Complete the named fields in flow-internship-informer-7318c7/INPUTS.json.
- Configured connections or tools for datatable, googlecalendar, googlesheets, http, telegram, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Telegram Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Telegram Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. serpapi_request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** serpapi_request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 3. Analyst Fallback

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Analyst Fallback: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Splitter Fallback

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Splitter Fallback: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. Splitter Main

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Splitter Main: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 6. Analyst Main

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Analyst Main: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 7. Text Guard

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Text Guard: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 8. Splitter Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-27 (languageModel, branch 0, input 1), step-28 (languageModel, branch 0, input 0).

**Carry forward:** Splitter Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. Notify User

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Notify User: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. JSON Format Fixer

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** JSON Format Fixer: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 11. check_duplicate

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-5 (data, branch 0, input 0).

**Carry forward:** check_duplicate: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. Output Parser

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Output Parser: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 13. Check for duplicate valid

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Check for duplicate valid: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 14. Not Duplicate?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Not Duplicate?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 15. Deadline Exists?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Deadline Exists?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 16. Add event reminder

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-13 (data, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Add event reminder: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 17. Get Mobile Numbers

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 1, input 0), step-17 (main, branch 0, input 0).

**Carry forward:** Get Mobile Numbers: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 18. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-21 (main, branch 0, input 0).

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 19. Append Valid

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Append Valid: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 20. Send Whatsapp Message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 1, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** Send Whatsapp Message: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 21. Insert row

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Insert row: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 22. Append Rejected

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-13 (data, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Append Rejected: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 23. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 1, input 1), step-15 (main, branch 1, input 0).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 24. Wait

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 1, input 0).

**Carry forward:** Wait: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 25. Resend failed message

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Resend failed message: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 26. Loop Over Each Link

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-22 (main, branch 0, input 0), step-23 (main, branch 0, input 0), step-26 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Each Link: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 27. Firecrawl Scrape

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0).

**Carry forward:** Firecrawl Scrape: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 28. Pre-Check

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Pre-Check: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 29. For 2027?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** For 2027?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 30. Analyst Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-10 (tool, branch 0, input 0), step-11 (languageModel, branch 0, input 1), step-12 (tool, branch 0, input 0), step-29 (languageModel, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Analyst Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Internship Informer”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-internship-informer-7318c7/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-internship-informer-7318c7/WORKFLOW.json
```
