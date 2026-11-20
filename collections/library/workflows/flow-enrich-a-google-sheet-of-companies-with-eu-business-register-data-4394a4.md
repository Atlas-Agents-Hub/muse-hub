# Enrich a Google Sheet of companies with EU business register data

Complete “Enrich a Google Sheet of companies with EU business register data” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Enrich a Google Sheet of companies with EU business register data.
- The selected records, date range, and output destination.
- Complete the named fields in flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/INPUTS.json.
- Configured connections or tools for apify, googlesheets.

## 1. Run it

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Run it: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Read the sheet

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Read the sheet: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Look up the official register

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = Actors, operation = Run actor and get dataset. Read `../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Look up the official register: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Keep the columns worth writing back

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Keep the columns worth writing back: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Write it back to the sheet

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = appendOrUpdate. Read `../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0).

**Carry forward:** Write it back to the sheet: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Enrich a Google Sheet of companies with EU business register data”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-enrich-a-google-sheet-of-companies-with-eu-business-register-data-4394a4/WORKFLOW.json
```
