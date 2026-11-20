# DaoXE Multi-Model Chat with Automatic Fallback

Complete “DaoXE Multi-Model Chat with Automatic Fallback” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for DaoXE Multi-Model Chat with Automatic Fallback.
- The selected records, date range, and output destination.
- Complete the named fields in flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/INPUTS.json.
- Configured connections or tools for http.

## 1. When clicking 'Test workflow'

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking 'Test workflow': A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Set inputs

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set inputs: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Primary model (DaoXE)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Primary model (DaoXE): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Fallback model (DaoXE)

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Fallback model (DaoXE): A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Answer (primary)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Answer (primary): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 6. Answer (fallback)

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Answer (fallback): Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “DaoXE Multi-Model Chat with Automatic Fallback”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-daoxe-multi-model-chat-with-automatic-fallback-14eda6/WORKFLOW.json
```
