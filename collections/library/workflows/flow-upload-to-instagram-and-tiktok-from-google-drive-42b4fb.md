# Upload to Instagram and Tiktok from Google Drive

Complete “Upload to Instagram and Tiktok from Google Drive” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Upload to Instagram and Tiktok from Google Drive.
- The selected records, date range, and output destination.
- Complete the named fields in flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/INPUTS.json.
- Configured connections or tools for googledrive, http, telegram.
- An available model or embedding capability with the requested format and cost limits.

## 1. Google Drive Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Google Drive Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Error Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Error Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 3. Google Drive

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = download. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Google Drive: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Choose the next branch

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Choose the next branch: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 5. Telegram

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Telegram: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 6. Read video from Google Drive

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Read video from Google Drive: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 7. Get Audio from Video

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = audio, operation = transcribe. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Get Audio from Video: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 8. Generate Description for Videos in Tiktok and Instagram

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Generate Description for Videos in Tiktok and Instagram: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 9. Read Video from Google Drive2

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Read Video from Google Drive2: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 10. Read Video from Google Drive

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-7 (data, branch 0, input 0).

**Carry forward:** Read Video from Google Drive: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 11. Upload Video and Description to Tiktok

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Upload Video and Description to Tiktok: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 12. Upload Video and Description to Instagram

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0), step-8 (data, branch 0, input 0).

**Carry forward:** Upload Video and Description to Instagram: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Upload to Instagram and Tiktok from Google Drive”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-upload-to-instagram-and-tiktok-from-google-drive-42b4fb/WORKFLOW.json
```
