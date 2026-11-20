# Auto-Categorize blog posts in wordpress using A.I.

Complete “Auto-Categorize blog posts in wordpress using A.I.” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Auto-Categorize blog posts in wordpress using A.I..
- The selected records, date range, and output destination.
- Complete the named fields in flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/INPUTS.json.
- Configured connections or tools for wordpress.
- An available model or embedding capability with the requested format and cost limits.

## 1. When clicking ‘Test workflow’

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking ‘Test workflow’: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 3. Get All Wordpress Posts

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Get All Wordpress Posts: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. AI Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (languageModel, branch 0, input 0), step-3 (main, branch 0, input 0).

**Carry forward:** AI Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## 5. Wordpress

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = update. Read `../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-3 (data, branch 0, input 0).

**Carry forward:** Wordpress: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Auto-Categorize blog posts in wordpress using A.I.”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-auto-categorize-blog-posts-in-wordpress-using-a-i-3efacb/WORKFLOW.json
```
