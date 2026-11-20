# Learn Anything from HN - Get Top Resource Recommendations from Hacker News

Complete “Learn Anything from HN - Get Top Resource Recommendations from Hacker News” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Learn Anything from HN - Get Top Resource Recommendations from Hacker News.
- The selected records, date range, and output destination.
- Complete the named fields in flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/INPUTS.json.
- Configured connections or tools for emailsend, hackernews, http.
- An available model or embedding capability with the requested format and cost limits.

## 1. Google Gemini Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Gemini Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. GetTopicFromToLearn

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** GetTopicFromToLearn: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. SearchAskHN

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = all. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** SearchAskHN: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. SplitOutChildrenIDs

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** SplitOutChildrenIDs: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 5. FindHNComments

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** FindHNComments: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. CombineIntoSingleText

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** CombineIntoSingleText: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 7. Basic LLM Chain

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-1 (languageModel, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Basic LLM Chain: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Convert2HTML

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: mode = markdownToHtml. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Convert2HTML: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 9. SendEmailWithTopResources

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-6 (data, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** SendEmailWithTopResources: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Finished

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Finished: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Learn Anything from HN - Get Top Resource Recommendations from Hacker News”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-learn-anything-from-hn-get-top-resource-recommendations-from-hacker-news-5ff94e/WORKFLOW.json
```
