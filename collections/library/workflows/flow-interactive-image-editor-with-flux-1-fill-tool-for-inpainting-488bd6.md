# 🎨 Interactive Image Editor with FLUX.1 Fill Tool for Inpainting

Complete “🎨 Interactive Image Editor with FLUX.1 Fill Tool for Inpainting” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for 🎨 Interactive Image Editor with FLUX.1 Fill Tool for Inpainting.
- The selected records, date range, and output destination.
- Complete the named fields in flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/INPUTS.json.
- Configured connections or tools for http.

## 1. Webhook

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Webhook: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. NO OP

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 1, input 0).

**Carry forward:** NO OP: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 3. Mockups

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Mockups: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 4. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 1), step-10 (main, branch 0, input 0).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 5. FLUX Fill

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** FLUX Fill: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 6. Editor page

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Editor page: Typed records or an explicit parse-error record.

**Check:** Valid samples parse and malformed or missing fields remain visible.

## 7. Respond to Webhook

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-11 (main, branch 0, input 0).

**Carry forward:** Respond to Webhook: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 8. Wait 3 sec

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-4 (main, branch 1, input 0).

**Carry forward:** Wait 3 sec: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 9. Is Ready?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Is Ready?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Check FLUX status

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Check FLUX status: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 11. Get Fill Image

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Get Fill Image: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Show the image to user

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Show the image to user: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “🎨 Interactive Image Editor with FLUX.1 Fill Tool for Inpainting”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-interactive-image-editor-with-flux-1-fill-tool-for-inpainting-488bd6/WORKFLOW.json
```
