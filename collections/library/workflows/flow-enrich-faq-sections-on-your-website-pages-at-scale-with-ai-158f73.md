# Enrich FAQ sections on your website pages at scale with AI

Complete “Enrich FAQ sections on your website pages at scale with AI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Enrich FAQ sections on your website pages at scale with AI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/INPUTS.json.
- Configured connections or tools for googledrive, googlesheets, strapi, workflow.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Execute Workflow Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Execute Workflow Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 4. Switch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-24`, for its exact field mappings, expressions, and settings. Use the output from step-16 (main, branch 0, input 0).

**Carry forward:** Switch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 5. Define Sheets

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Define Sheets: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Sheets To List...

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Sheets To List...: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 7. Single Integration Cred-only

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 1, input 0).

**Carry forward:** Single Integration Cred-only: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Single Integration Native

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 0, input 0).

**Carry forward:** Single Integration Native: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Categories

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 3, input 0).

**Carry forward:** Categories: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Single Integration Non-native

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Operation settings: mode = raw. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-21`, for its exact field mappings, expressions, and settings. Use the output from step-24 (main, branch 2, input 0).

**Carry forward:** Single Integration Non-native: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 11. Question to List1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-13 (main, branch 0, input 0), step-12 (main, branch 0, input 0), step-21 (main, branch 0, input 0).

**Carry forward:** Question to List1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 12. Get Services

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** Get Services: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 13. For Each Sheet...

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-18 (main, branch 0, input 0), step-10 (main, branch 0, input 0).

**Carry forward:** For Each Sheet...: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 14. Execute Workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: mode = each. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-17`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 0, input 0).

**Carry forward:** Execute Workflow: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 15. Prepare Job

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-18`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0), step-15 (data, branch 0, input 0).

**Carry forward:** Prepare Job: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 16. For Each Service...

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-19`, for its exact field mappings, expressions, and settings. Use the output from step-22 (main, branch 1, input 0), step-17 (main, branch 0, input 0), step-15 (main, branch 0, input 0). Branch 0 ends here; return its result without continuing to another operation.

**Carry forward:** For Each Service...: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 17. If has Data

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-22`, for its exact field mappings, expressions, and settings. Use the output from step-19 (main, branch 1, input 0).

**Carry forward:** If has Data: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 18. Needs AI Completion?1

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-23`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 1, input 0).

**Carry forward:** Needs AI Completion?1: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 19. AI Completion1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-29`, for its exact field mappings, expressions, and settings. Use the output from step-2 (languageModel, branch 0, input 0), step-23 (main, branch 1, input 0), step-16 (data, branch 0, input 0).

**Carry forward:** AI Completion1: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 20. Format QA Pair1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-29 (main, branch 0, input 0), step-23 (main, branch 0, input 0).

**Carry forward:** Format QA Pair1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 21. For Each Question...1

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-5 (main, branch 0, input 0).

**Carry forward:** For Each Question...1: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 22. Update Row Status

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-20`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-16 (data, branch 0, input 0).

**Carry forward:** Update Row Status: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 23. Strapi

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-25`, for its exact field mappings, expressions, and settings. Use the output from step-20 (main, branch 0, input 0).

**Carry forward:** Strapi: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 24. Questions to Object...1

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Questions to Object...1: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 25. Format DisplayName + Questions1

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-16 (data, branch 0, input 0).

**Carry forward:** Format DisplayName + Questions1: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 26. Create From Text

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = createFromText. Read `../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-16 (data, branch 0, input 0).

**Carry forward:** Create From Text: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Enrich FAQ sections on your website pages at scale with AI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-enrich-faq-sections-on-your-website-pages-at-scale-with-ai-158f73/WORKFLOW.json
```
