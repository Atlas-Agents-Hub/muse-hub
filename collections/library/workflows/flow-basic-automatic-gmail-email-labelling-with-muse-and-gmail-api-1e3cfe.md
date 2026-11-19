# Basic Automatic Gmail Email Labelling with OpenAI and Gmail API

Complete “Basic Automatic Gmail Email Labelling with OpenAI and Gmail API” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Basic Automatic Gmail Email Labelling with OpenAI and Gmail API.
- The selected records, date range, and output destination.
- Complete the named fields in flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/INPUTS.json.
- Configured connections or tools for gmail.
- An available model or embedding capability with the requested format and cost limits.

## 1. Gmail Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model1

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model1: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Gmail - read labels

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: resource = label. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail - read labels: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Gmail - get message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = get. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail - get message: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Gmail - add label to message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = addLabels. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail - add label to message: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Gmail - create label

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: resource = label, operation = create. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Gmail - create label: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## 7. Window Buffer Memory

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Window Buffer Memory: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 8. Wait

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Use the declared delay or completion condition and record the job or event identifier before resuming. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Wait: A completion observation or a saved continuation point.

**Check:** The flow resumes for the expected result and does not repeat a completed write.

## 9. Gmail labelling agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 0, input 0), step-2 (languageModel, branch 0, input 0), step-4 (tool, branch 0, input 0), step-3 (tool, branch 0, input 0), step-6 (tool, branch 0, input 0), step-8 (memory, branch 0, input 0), step-5 (tool, branch 0, input 0).

**Carry forward:** Gmail labelling agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Basic Automatic Gmail Email Labelling with OpenAI and Gmail API”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-basic-automatic-gmail-email-labelling-with-muse-and-gmail-api-1e3cfe/WORKFLOW.json
```
