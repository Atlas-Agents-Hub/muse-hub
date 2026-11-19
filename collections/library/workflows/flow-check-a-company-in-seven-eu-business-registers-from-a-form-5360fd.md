# Check a company in seven EU business registers from a form

Complete “Check a company in seven EU business registers from a form” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Check a company in seven EU business registers from a form.
- The selected records, date range, and output destination.
- Complete the named fields in flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/INPUTS.json.
- Configured connections or tools for apify.

## 1. Someone submits the form

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Someone submits the form: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Look up the official register

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = Actors, operation = Run actor and get dataset. Read `../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Look up the official register: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. Is the company still active

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Is the company still active: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. Passed, keep the register fields

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Passed, keep the register fields: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 5. Not active, send it to a human

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 1, input 0).

**Carry forward:** Not active, send it to a human: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Check a company in seven EU business registers from a form”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-check-a-company-in-seven-eu-business-registers-from-a-form-5360fd/WORKFLOW.json
```
