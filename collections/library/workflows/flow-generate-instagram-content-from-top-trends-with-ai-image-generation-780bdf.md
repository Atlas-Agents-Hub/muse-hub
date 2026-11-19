# Generate Instagram Content from Top Trends with AI Image Generation

Complete “Generate Instagram Content from Top Trends with AI Image Generation” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Generate Instagram Content from Top Trends with AI Image Generation.
- The selected records, date range, and output destination.
- Complete the named fields in flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/INPUTS.json.
- Configured connections or tools for facebookgraphapi, http, postgres, scheduler, telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. Schedule Trigger1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger1: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 2. Replicate params

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Replicate params: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Instagram params

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Instagram params: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Telegram Params

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Telegram Params: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Rapid Api params

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Rapid Api params: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. get top trends on instagram #blender3d

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** get top trends on instagram #blender3d: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 7. get top trends on instagram #isometric

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** get top trends on instagram #isometric: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. filter the image content

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** filter the image content: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 9. filter the image content-2

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** filter the image content-2: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. merge the array content

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 1), step-25 (main, branch 0, input 0).

**Carry forward:** merge the array content: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 11. Check Data on Database Is Exist

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = select. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 1, input 0).

**Carry forward:** Check Data on Database Is Exist: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. If Data is Exist

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** If Data is Exist: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 13. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-14 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 14. If media status is finished

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** If media status is finished: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 15. send error message to telegram

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** send error message to telegram: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 16. insert data on db

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 1, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** insert data on db: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 17. Analyze Image and give the content

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Analyze Image and give the content: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 18. If media status is finished1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** If media status is finished1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 19. Analyze Content And Generate Instagram Caption

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0).

**Carry forward:** Analyze Content And Generate Instagram Caption: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 20. Prepare data on Instagram

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0), step-20 (data, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Prepare data on Instagram: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 21. Check Status Of Media Before Uploaded

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Check Status Of Media Before Uploaded: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 22. Publish Media on Instagram

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Publish Media on Instagram: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 23. Check status of post

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Check status of post: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 24. Generate image on flux

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-19 (data, branch 0, input 0).

**Carry forward:** Generate image on flux: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 25. Telegram

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 1, input 0), step-8 (data, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Telegram: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 26. Telegram1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Telegram1: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 27. Telegram2

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 1, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Telegram2: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Generate Instagram Content from Top Trends with AI Image Generation”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-generate-instagram-content-from-top-trends-with-ai-image-generation-780bdf/WORKFLOW.json
```
