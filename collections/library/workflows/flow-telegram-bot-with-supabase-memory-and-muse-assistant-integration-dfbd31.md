# Telegram Bot with Supabase memory and OpenAI assistant integration

Complete “Telegram Bot with Supabase memory and OpenAI assistant integration” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Telegram Bot with Supabase memory and OpenAI assistant integration.
- The selected records, date range, and output destination.
- Complete the named fields in flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/INPUTS.json.
- Configured connections or tools for http, supabase, telegram.

## 1. Get New Message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Get New Message: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Find User

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Operation settings: operation = getAll. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Find User: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 3. If User exists

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Evaluate the branch rules in order and route the result to the corresponding numbered output. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** If User exists: The selected branch with the values used to make the decision.

**Check:** Both a matching case and the fallback follow the correct edges.

## 4. OPENAI - Create thread

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-9 (main, branch 1, input 0).

**Carry forward:** OPENAI - Create thread: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Create User

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured service operation and its filters to retrieve the selected records or resource. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Create User: A service result with source identifiers and pagination state.

**Check:** The selected account, resource, fields, and complete page range match the request.

## 6. Merge

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Join the incoming branches using the declared mode, matching keys, and unmatched-record policy. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 1), step-9 (main, branch 0, input 0).

**Carry forward:** Merge: A joined result with the match and unmatched counts.

**Check:** Duplicate keys and missing partners produce the intended output cardinality.

## 7. OPENAI - Send message

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** OPENAI - Send message: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. OPENAI - Run assistant

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** OPENAI - Run assistant: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 9. OPENAI - Get messages

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0), step-4 (data, branch 0, input 0).

**Carry forward:** OPENAI - Get messages: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Send Message to User

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Read `../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0), step-1 (data, branch 0, input 0).

**Carry forward:** Send Message to User: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Telegram Bot with Supabase memory and OpenAI assistant integration”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-telegram-bot-with-supabase-memory-and-muse-assistant-integration-dfbd31/WORKFLOW.json
```
