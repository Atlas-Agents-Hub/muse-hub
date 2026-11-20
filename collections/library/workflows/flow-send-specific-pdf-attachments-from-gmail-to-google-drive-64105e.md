# Send specific PDF attachments from Gmail to Google Drive using OpenAI

Complete “Send specific PDF attachments from Gmail to Google Drive using OpenAI” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Send specific PDF attachments from Gmail to Google Drive using OpenAI.
- The selected records, date range, and output destination.
- Complete the named fields in flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/INPUTS.json.
- Configured connections or tools for googledrive.
- An available model or embedding capability with the requested format and cost limits.

## 1. On email received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-12`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** On email received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Configure

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-12 (main, branch 0, input 0).

**Carry forward:** Configure: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Has attachments?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-15`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-12 (data, branch 0, input 0).

**Carry forward:** Has attachments?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. There are no attachments

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-16`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 1, input 0).

**Carry forward:** There are no attachments: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 5. Iterate over email attachments

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-15 (main, branch 0, input 0).

**Carry forward:** Iterate over email attachments: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 6. Is PDF

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Is PDF: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 7. Read PDF

Read [the Markdown Documents method](../skills/md-document/SKILL.md). Read the configured file type and preserve text, structure, tables, and source locations needed by later stages. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Read PDF: Extracted document content linked to the original file.

**Check:** Representative pages or records match the source and unreadable content is identified.

## 8. Not a PDF

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Not a PDF: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 9. Is text within token limit?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-14`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Is text within token limit?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 10. Ignore large PDFs

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-13`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 1, input 0).

**Carry forward:** Ignore large PDFs: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 11. OpenAI matches PDF textual content

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** OpenAI matches PDF textual content: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 12. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Operation settings: mode = combine. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-14 (main, branch 0, input 1), step-9 (main, branch 0, input 0).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 13. Is matched

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Is matched: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 14. This is a matched PDF

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** This is a matched PDF: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 15. This is not a matched PDF

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Inspect the incoming data at this point and retain the fields required by the next operation. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 1, input 0).

**Carry forward:** This is not a matched PDF: An inspected intermediate result.

**Check:** The expected records and fields are present before the flow continues.

## 16. Upload file to folder

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Upload file to folder: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Send specific PDF attachments from Gmail to Google Drive using OpenAI”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-send-specific-pdf-attachments-from-gmail-to-google-drive-64105e/WORKFLOW.json
```
