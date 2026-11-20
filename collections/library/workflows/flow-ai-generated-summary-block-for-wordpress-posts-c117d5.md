# AI-Generated Summary Block for WordPress Posts

Complete “AI-Generated Summary Block for WordPress Posts” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for AI-Generated Summary Block for WordPress Posts.
- The selected records, date range, and output destination.
- Complete the named fields in flow-ai-generated-summary-block-for-wordpress-posts-c117d5/INPUTS.json.
- Configured connections or tools for googlesheets, http, slack, wordpress.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Webhook

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 4. Schedule Trigger

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 5. Set fields - From Webhook input

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Set fields - From Webhook input: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Date & Time - Substract

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Operation settings: operation = subtractFromDate. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Date & Time - Substract: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. WordPress - Get All Posts

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** WordPress - Get All Posts: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. WordPress - Get Last Posts

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** WordPress - Get Last Posts: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 9. WordPress - Get Post1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** WordPress - Get Post1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 10. HTML to Markdown

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0).

**Carry forward:** HTML to Markdown: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 11. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Google Sheets - Add Row

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Google Sheets - Add Row: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Slack - Notify Channel

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0), step-16 (data, branch 0, input 0).

**Carry forward:** Slack - Notify Channel: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 14. Set fields - Prepare data for Gsheets & Slack

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-11 (data, branch 0, input 0).

**Carry forward:** Set fields - Prepare data for Gsheets & Slack: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. WordPress - Get Post2

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** WordPress - Get Post2: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 16. Text Classifier

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-3 (languageModel, branch 0, input 0).

**Carry forward:** Text Classifier: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 17. Loop Over Items

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (main, branch 1, input 0), step-13 (main, branch 0, input 0), step-21 (main, branch 0, input 0).

**Carry forward:** Loop Over Items: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 18. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 19. Wordpress - Update Post

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-2 (data, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** Wordpress - Update Post: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 20. Google Sheets - Get rows

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 1, input 0).

**Carry forward:** Google Sheets - Get rows: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 21. No Operation, do nothing

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** No Operation, do nothing: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “AI-Generated Summary Block for WordPress Posts”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-ai-generated-summary-block-for-wordpress-posts-c117d5/WORKFLOW.json
```
