# Modular & Customizable Email Routing Text Classifier for eCommerce

Complete “Modular & Customizable Email Routing Text Classifier for eCommerce” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Modular & Customizable Email Routing Text Classifier for eCommerce.
- The selected records, date range, and output destination.
- Complete the named fields in flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/INPUTS.json.
- Configured connections or tools for emailsend, googlesheets.
- An available model or embedding capability with the requested format and cost limits.

## 1. On form submission

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On form submission: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Text Classifier

Read [the Data Labeling method](../skills/data-labeling/SKILL.md). Apply the supplied category definitions and retain the evidence supporting the selected label. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-3 (languageModel, branch 0, input 0), step-1 (main, branch 0, input 0). Branch 1 ends here; return its result without continuing to another operation.

**Carry forward:** Text Classifier: A label and the relevant source evidence for each item.

**Check:** Ambiguous examples and items outside the category set are handled explicitly.

## 4. Prod. Dep.

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Prod. Dep.: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 5. Quote Dep.

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Quote Dep.: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 6. Gen. Dep.

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 2, input 0).

**Carry forward:** Gen. Dep.: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 7. Order Dep.

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 3, input 0).

**Carry forward:** Order Dep.: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 8. Other Dep.

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 4, input 0).

**Carry forward:** Other Dep.: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 9. Prod DB

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Prod DB: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 10. General DB

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** General DB: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Order DB

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Order DB: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 12. Other DB

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Other DB: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 13. Quote DB

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = append. Read `../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Quote DB: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Modular & Customizable Email Routing Text Classifier for eCommerce”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-modular-customizable-email-routing-text-classifier-for-ecommerce-79da78/WORKFLOW.json
```
