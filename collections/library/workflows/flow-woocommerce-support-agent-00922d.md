# WooCommerce Support-Agent

Complete “WooCommerce Support-Agent” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for WooCommerce Support-Agent.
- The selected records, date range, and output destination.
- Complete the named fields in flow-woocommerce-support-agent-00922d/INPUTS.json.
- Configured connections or tools for dhl, http, woocommerce, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. WooCommerce_Tool

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** WooCommerce_Tool: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Chat Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 5. Webhook Example Page

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook Example Page: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Example encrypted email

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-28`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Example encrypted email: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. If email provided

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0).

**Carry forward:** If email provided: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 8. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 9. Decrypt email

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-28 (main, branch 0, input 0).

**Carry forward:** Decrypt email: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 10. Decrypt email address

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-23 (main, branch 0, input 0).

**Carry forward:** Decrypt email address: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 11. No email provided

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 1, input 0).

**Carry forward:** No email provided: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 12. WooCommerce - Get User

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = customer, operation = getAll. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** WooCommerce - Get User: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 13. Mock Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-31`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0).

**Carry forward:** Mock Data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-31 (data, branch 0, input 0).

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 15. If user found

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0).

**Carry forward:** If user found: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 16. WooCommerce Get Orders

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** WooCommerce Get Orders: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 17. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-30`, for its exact field mappings, expressions, and settings. Use the output from step-31 (main, branch 0, input 0), step-22 (tool, branch 0, input 0), step-21 (languageModel, branch 0, input 0), step-12 (memory, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 18. No customer found

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** No customer found: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 19. If order found

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** If order found: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 20. No order found

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** No order found: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. Extract Tracking Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Extract Tracking Data: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 22. If contains DHL data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** If contains DHL data: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 23. Split Out

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Split Out: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 24. DHL

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** DHL: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 25. Add Error Information

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 1, input 0), step-9 (data, branch 0, input 0).

**Carry forward:** Add Error Information: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 26. Merge Tracking Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 0, input 0), step-18 (main, branch 0, input 1).

**Carry forward:** Merge Tracking Data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 27. Aggregate

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Aggregate: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 28. Merge Orders

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-5 (main, branch 1, input 1).

**Carry forward:** Merge Orders: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 29. Merge Order and Tracking Data

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-15 (main, branch 0, input 1).

**Carry forward:** Merge Order and Tracking Data: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 30. Send Response

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Send Response: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “WooCommerce Support-Agent”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-woocommerce-support-agent-00922d/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-woocommerce-support-agent-00922d/WORKFLOW.json
```
