# Hacker News to Video Content

Complete “Hacker News to Video Content” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Hacker News to Video Content.
- The selected records, date range, and output destination.
- Complete the named fields in flow-hacker-news-to-video-content-f5b061/INPUTS.json.
- Configured connections or tools for dropbox, googledrive, hackernews, http, linkedin, microsoftonedrive, s3, twitter, youtube.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Dropbox

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Dropbox: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. YouTube

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = video, operation = upload. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** YouTube: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 4. OpenAI Chat Model3

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model3: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 5. HTTP Request1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** HTTP Request1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 7. Hacker News

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = all. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Hacker News: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Google Drive

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Google Drive: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. Apply the requested service update

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-27`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0).

**Carry forward:** Apply the requested service update: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Limit

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the requested record limit after the relevant filtering and ordering. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Limit: A bounded result and the total eligible count.

**Check:** The retained count does not exceed the limit and selection order is consistent.

## 11. Microsoft OneDrive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Microsoft OneDrive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 12. LinkedIn

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-27 (main, branch 0, input 0).

**Carry forward:** LinkedIn: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Instagram

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0).

**Carry forward:** Instagram: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 14. Upload to Minio

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = upload. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Upload to Minio: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 15. If Topic

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** If Topic: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 16. Article Analysis

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-5 (tool, branch 0, input 0), step-3 (main, branch 1, input 0), step-4 (languageModel, branch 0, input 0), step-6 (outputParser, branch 0, input 0).

**Carry forward:** Article Analysis: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 17. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-14 (main, branch 1, input 0), step-22 (main, branch 1, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 18. Leo - Get imageId

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0).

**Carry forward:** Leo - Get imageId: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 19. Runway - Create Video

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Runway - Create Video: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. Runway - Get Video

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** Runway - Get Video: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 21. Wait2

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Wait2: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 22. Get Image

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Get Image: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 23. Prompt Settings1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Prompt Settings1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 24. Leo - Generate Image

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Leo - Generate Image: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 25. Wait1

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** Wait1: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 26. Image Analysis

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = image, operation = analyze. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** Image Analysis: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 27. Wait3

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-37 (main, branch 0, input 0).

**Carry forward:** Wait3: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 28. Leo - Improve Prompt2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-39 (data, branch 0, input 0).

**Carry forward:** Leo - Improve Prompt2: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 29. Wait4

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-35 (main, branch 0, input 0).

**Carry forward:** Wait4: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 30. Wait6

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-32`, for its exact field mappings, expressions, and settings. Use the output from step-33 (main, branch 0, input 0).

**Carry forward:** Wait6: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 31. Leo - Generate Image2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-33`, for its exact field mappings, expressions, and settings. Use the output from step-30 (main, branch 0, input 0).

**Carry forward:** Leo - Generate Image2: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 32. Leo - Get imageId2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-34`, for its exact field mappings, expressions, and settings. Use the output from step-32 (main, branch 0, input 0).

**Carry forward:** Leo - Get imageId2: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 33. Runway - Create Video2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-35`, for its exact field mappings, expressions, and settings. Use the output from step-34 (main, branch 0, input 0).

**Carry forward:** Runway - Create Video2: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 34. Runway - Get Video2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-36`, for its exact field mappings, expressions, and settings. Use the output from step-31 (main, branch 0, input 0).

**Carry forward:** Runway - Get Video2: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 35. Cre - Generate Video1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-37`, for its exact field mappings, expressions, and settings. Use the output from step-36 (main, branch 0, input 0), step-10 (data, branch 0, input 0), step-12 (data, branch 0, input 0), step-39 (data, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Cre - Generate Video1: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 36. Cre - Get Video

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-38`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Cre - Get Video: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 37. Article Prep

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-39`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Article Prep: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 38. News1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-39 (main, branch 0, input 0), step-14 (data, branch 0, input 0).

**Carry forward:** News1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 39. Leo - Improve Prompt

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0), step-39 (data, branch 0, input 0).

**Carry forward:** Leo - Improve Prompt: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Hacker News to Video Content”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-hacker-news-to-video-content-f5b061/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-hacker-news-to-video-content-f5b061/WORKFLOW.json
```
