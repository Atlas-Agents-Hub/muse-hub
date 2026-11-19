# Flux AI Image Generator

Complete “Flux AI Image Generator” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Flux AI Image Generator.
- The selected records, date range, and output destination.
- Complete the named fields in flow-flux-ai-image-generator-275cc0/INPUTS.json.
- Configured connections or tools for http, s3.

## 1. n8n Form Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** n8n Form Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Route by style

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Route by style: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 3. Vivid Pop Explosion

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 4, input 0).

**Carry forward:** Vivid Pop Explosion: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. AI Dystopia

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 2, input 0).

**Carry forward:** AI Dystopia: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Post-Analog Glitchscape

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 1, input 0).

**Carry forward:** Post-Analog Glitchscape: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Neon Fauvism

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 3, input 0).

**Carry forward:** Neon Fauvism: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 7. None

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 5, input 0).

**Carry forward:** None: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 8. Hyper-Surreal Escape

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Hyper-Surreal Escape: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 9. Call hugginface inference api

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (main, branch 0, input 0), step-4 (main, branch 0, input 0), step-1 (main, branch 0, input 0), step-9 (main, branch 0, input 0), step-3 (main, branch 0, input 0).

**Carry forward:** Call hugginface inference api: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Upload image to S3

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = upload. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Upload image to S3: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 11. Serve webpage

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Serve webpage: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 12. Respond with error

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 1, input 0), step-11 (main, branch 1, input 0).

**Carry forward:** Respond with error: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Flux AI Image Generator”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-flux-ai-image-generator-275cc0/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-flux-ai-image-generator-275cc0/WORKFLOW.json
```
