# Prepare CSV files with GPT-4

Complete “Prepare CSV files with GPT-4” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Prepare CSV files with GPT-4.
- The selected records, date range, and output destination.
- Complete the named fields in flow-prepare-csv-files-cabc7d/INPUTS.json.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking "Execute Workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Execute Workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Operation settings: resource = chat. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** OpenAI: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 3. Split In Batches

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-7 (main, branch 0, input 0).

**Carry forward:** Split In Batches: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 4. Parse JSON

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Parse JSON: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Make JSON Table

Read [the pandas method](../skills/pandas-pro/SKILL.md). Group or collect the incoming values using the named fields and aggregation settings. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Make JSON Table: A grouped result with denominators and group sizes.

**Check:** Totals reconcile with the eligible input rows and missing values follow the stated policy.

## 6. Convert to CSV

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: operation = toFile. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Convert to CSV: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 7. Save to Disk

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0).

**Carry forward:** Save to Disk: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 8. Strip UTF BOM bytes

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Strip UTF BOM bytes: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## 9. Create valid binary

Read [the File Organizer method](../skills/file-organizer/SKILL.md). Read, convert, or write the requested file format using the selected input and output location. Operation settings: mode = jsonToBinary. Read `../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-3 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Create valid binary: A file in the requested format and its location.

**Check:** The file opens correctly and its contents match the preceding step.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Prepare CSV files with GPT-4”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-prepare-csv-files-cabc7d/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-prepare-csv-files-cabc7d/WORKFLOW.json
```
