# Author and Publish Blog Posts From Google Sheets

Complete “Author and Publish Blog Posts From Google Sheets” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Author and Publish Blog Posts From Google Sheets.
- The selected records, date range, and output destination.
- Complete the named fields in flow-author-and-publish-blog-posts-from-google-sheets-468dfd/INPUTS.json.
- Configured connections or tools for googlesheets, http, scheduler.
- An available model or embedding capability with the requested format and cost limits.

## 1. ScheduleTrigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** ScheduleTrigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. ManualTrigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** ManualTrigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. AgentLLM

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** AgentLLM: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Settings

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (main, branch 0, input 0).

**Carry forward:** Settings: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Schedule

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Schedule: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. fetchConfig

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** fetchConfig: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Config

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Config: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 8. PreparedData

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** PreparedData: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. IfTakeAction

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** IfTakeAction: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. IfActionPublish

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** IfActionPublish: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 11. IfPromptExists

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0).

**Carry forward:** IfPromptExists: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. IfScheduledNow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** IfScheduledNow: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 13. Basic LLM Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-7 (languageModel, branch 0, input 0), step-14 (main, branch 0, input 0).

**Carry forward:** Basic LLM Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 14. PrepareXmlPost

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** PrepareXmlPost: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 15. RecombinedDataRow

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** RecombinedDataRow: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 16. CreatePost

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** CreatePost: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 17. HandleXMLRPCResponse

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: mode = runOnceForEachItem. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** HandleXMLRPCResponse: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 18. LogStatus

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** LogStatus: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 19. SaveBackToSheet

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0), step-1 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** SaveBackToSheet: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 20. LogPublished

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** LogPublished: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 21. PostingSuccessful

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-19 (data, branch 0, input 0).

**Carry forward:** PostingSuccessful: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 22. SetToPublish

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-1 (data, branch 0, input 0), step-9 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** SetToPublish: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Author and Publish Blog Posts From Google Sheets”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-author-and-publish-blog-posts-from-google-sheets-468dfd/WORKFLOW.json
```
