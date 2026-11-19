# Convert Markdown into a branded PDF with a table of contents using PDFMint

Complete “Convert Markdown into a branded PDF with a table of contents using PDFMint” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Convert Markdown into a branded PDF with a table of contents using PDFMint.
- The selected records, date range, and output destination.
- Complete the named fields in flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/INPUTS.json.
- Configured connections or tools for pdfmint.

## 1. Receive the Markdown document

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Receive the Markdown document: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Set your document branding

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set your document branding: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Check the request is usable

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Check the request is usable: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. Check remaining quota

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = usage. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Check remaining quota: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Is there quota left?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Is there quota left?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 6. Build the cover, contents and body

Read [the JavaScript method](../skills/javascript-pro/SKILL.md). Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Build the cover, contents and body: Transformed records plus a representative before-and-after example.

**Check:** The example agrees with the transformation and invalid or empty input has a defined result.

## 7. Render the Markdown as PDF

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = pdf. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Render the Markdown as PDF: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 8. Did the render succeed?

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Did the render succeed?: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 9. Explain what went wrong

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0), step-5 (main, branch 1, input 0), step-8 (main, branch 1, input 0).

**Carry forward:** Explain what went wrong: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 10. Return the PDF

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0).

**Carry forward:** Return the PDF: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## 11. Return the error as JSON

Read [the Team Communications method](../skills/team-communications/SKILL.md). Format the result for its intended recipient or response channel, including the requested fields and attachments. Read `../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json`, node `step-11`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Return the error as JSON: A finished response with its associated output files.

**Check:** The response destination and contents match the request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Convert Markdown into a branded PDF with a table of contents using PDFMint”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-convert-markdown-into-a-branded-pdf-with-a-table-of-contents-using-pdfmint-a43009/WORKFLOW.json
```
