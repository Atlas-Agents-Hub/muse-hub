# Receive and Send Messages Across WhatsApp, Instagram and Facebook Messenger with Fiwano

Complete “Receive and Send Messages Across WhatsApp, Instagram and Facebook Messenger with Fiwano” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Receive and Send Messages Across WhatsApp, Instagram and Facebook Messenger with Fiwano.
- The selected records, date range, and output destination.
- Complete the named fields in flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/INPUTS.json.
- Configured connections or tools for fiwano.

## 1. Fiwano Trigger

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Fiwano Trigger: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Example — route by message type

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Example — route by message type: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 3. Example — send text reply

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Example — send text reply: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 4. Example — send attachment reply

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 1, input 0).

**Carry forward:** Example — send attachment reply: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 5. Check the finished result

Read [the Support Ops method](../skills/support-ops/SKILL.md). Inspect the complete result against the original task, the selected source, and the requested output format.

**Carry forward:** A checked result with its source and next action.

**Check:** The deliverable addresses the task and matches the selected source material.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Receive and Send Messages Across WhatsApp, Instagram and Facebook Messenger with Fiwano”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-receive-and-send-messages-across-whatsapp-instagram-and-facebook-messenger-wit-cd8b8c/WORKFLOW.json
```
