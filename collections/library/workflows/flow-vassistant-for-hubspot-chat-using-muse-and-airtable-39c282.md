# vAssistant for Hubspot Chat using OpenAi and Airtable

Complete “vAssistant for Hubspot Chat using OpenAi and Airtable” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for vAssistant for Hubspot Chat using OpenAi and Airtable.
- The selected records, date range, and output destination.
- Complete the named fields in flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/INPUTS.json.
- Configured connections or tools for airtable, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. IF2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** IF2: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 3. getHubspotMessage

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** getHubspotMessage: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 5. Airtable

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Airtable: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. IF1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** IF1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. OpenAi Create Thread

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** OpenAi Create Thread: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = assistant. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 1, input 0), step-1 (data, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. createThread

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** createThread: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. OpenAI Run1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0), step-20 (data, branch 0, input 0).

**Carry forward:** OpenAI Run1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. OpenAI Run

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** OpenAI Run: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Submit Data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Submit Data: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 13. Select Function

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Operation settings: dataType = string. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 1, input 0).

**Carry forward:** Select Function: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 14. Code1

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Code1: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 15. Wait2

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Wait2: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 16. HTTP Request1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 1, input 0).

**Carry forward:** HTTP Request1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 17. Code

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Code: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 18. Submit Data1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Submit Data1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. Wait3

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Wait3: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 20. Get Run

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-9 (main, branch 0, input 0), step-13 (main, branch 0, input 0), step-17 (main, branch 0, input 0), step-3 (main, branch 0, input 0), step-23 (main, branch 0, input 0).

**Carry forward:** Get Run: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 21. HTTP Request

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** HTTP Request: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 22. Completed, Action or Inprogress

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Operation settings: dataType = string. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Completed, Action or Inprogress: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 23. Wait

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 3, input 0).

**Carry forward:** Wait: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 24. Wait1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 2, input 0).

**Carry forward:** Wait1: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 25. respondHubspotMessage1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** respondHubspotMessage1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 26. Get Last Message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Get Last Message: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “vAssistant for Hubspot Chat using OpenAi and Airtable”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-vassistant-for-hubspot-chat-using-muse-and-airtable-39c282/WORKFLOW.json
```
