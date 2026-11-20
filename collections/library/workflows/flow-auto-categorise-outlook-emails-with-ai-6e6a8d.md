# Auto Categorise Outlook Emails with AI

Complete “Auto Categorise Outlook Emails with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Auto Categorise Outlook Emails with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-auto-categorise-outlook-emails-with-ai-6e6a8d/INPUTS.json.
- Configured connections or tools for microsoftoutlook.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Ollama Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Ollama Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Microsoft Outlook23

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Microsoft Outlook23: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Filter1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-21 (main, branch 0, input 0).

**Carry forward:** Filter1: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 5. Microsoft Outlook18

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 2, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook18: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 6. Microsoft Outlook19

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = move. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook19: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 7. Markdown1

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0).

**Carry forward:** Markdown1: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 8. varEmal1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** varEmal1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Microsoft Outlook20

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 4, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook20: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. Microsoft Outlook21

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 6, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook21: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. If1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-18 (main, branch 0, input 0).

**Carry forward:** If1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 12. Microsoft Outlook22

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 5, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook22: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Catch Errors1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 1, input 0).

**Carry forward:** Catch Errors1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 14. varJSON1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** varJSON1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 15. varID & Category1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-13 (main, branch 0, input 0), step-21 (data, branch 0, input 0).

**Carry forward:** varID & Category1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. Microsoft Outlook Move Message1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = move. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook Move Message1: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 17. AI Agent1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-13 (data, branch 0, input 0).

**Carry forward:** AI Agent1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 18. Merge1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-17 (main, branch 1, input 5), step-3 (main, branch 0, input 0), step-7 (main, branch 0, input 1), step-9 (main, branch 0, input 3), step-11 (main, branch 0, input 2), step-15 (main, branch 0, input 6), step-23 (main, branch 0, input 4).

**Carry forward:** Merge1: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 19. Switch1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-26`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Switch1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 20. Microsoft Outlook10

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = move. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook10: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 21. Microsoft Outlook12

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 0, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook12: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 22. Loop Over Items1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-25 (main, branch 0, input 0), step-16 (main, branch 0, input 0), step-19 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** Loop Over Items1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 23. Microsoft Outlook13

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 1, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook13: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 24. Microsoft Outlook15

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = move. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook15: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 25. Microsoft Outlook16

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-26 (main, branch 3, input 0), step-20 (data, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook16: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 26. Microsoft Outlook17

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = move. Read `../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-22 (data, branch 0, input 0).

**Carry forward:** Microsoft Outlook17: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Auto Categorise Outlook Emails with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-auto-categorise-outlook-emails-with-ai-6e6a8d/WORKFLOW.json
```
