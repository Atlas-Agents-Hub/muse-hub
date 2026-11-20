# Customer Support Channel and Ticketing System with Slack and Linear

Complete “Customer Support Channel and Ticketing System with Slack and Linear” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Customer Support Channel and Ticketing System with Slack and Linear.
- The selected records, date range, and output destination.
- Complete the named fields in flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/INPUTS.json.
- Configured connections or tools for linear, scheduler, slack.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Structured Output Parser

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Structured Output Parser: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 3. Schedule Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the requested time zone and cadence to define when this flow starts; retain a manual run option. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Schedule Trigger: A trigger specification with a time zone and manual entry.

**Check:** The next occurrence matches the requested local time and frequency.

## 4. Slack

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = search. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Slack: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Get Values

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get Values: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Get Existing Issues

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Get Existing Issues: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Collect Descriptions

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Collect Descriptions: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 8. Get Hashes Only

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Get Hashes Only: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-11 (main, branch 0, input 1).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 10. Create New Ticket?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Create New Ticket?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 11. Generate Ticket Using ChatGPT

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-2 (languageModel, branch 0, input 0), step-6 (main, branch 0, input 0), step-3 (outputParser, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Generate Ticket Using ChatGPT: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Create Ticket

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-5 (data, branch 0, input 0).

**Carry forward:** Create Ticket: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Customer Support Channel and Ticketing System with Slack and Linear”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-customer-support-channel-and-ticketing-system-with-slack-and-linear-f17cf8/WORKFLOW.json
```
