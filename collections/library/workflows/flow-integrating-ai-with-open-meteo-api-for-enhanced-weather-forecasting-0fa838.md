# Integrating AI with Open-Meteo API for Enhanced Weather Forecasting

Complete “Integrating AI with Open-Meteo API for Enhanced Weather Forecasting” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Integrating AI with Open-Meteo API for Enhanced Weather Forecasting.
- The selected records, date range, and output destination.
- Complete the named fields in flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/INPUTS.json.
- Configured connections or tools for http.
- An available model or embedding capability with the requested format and cost limits.

## 1. OpenAI Chat Model

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Choose an available model route suited to the requested text, vision, audio, or structured-output task. Read `../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** OpenAI Chat Model: A model configuration with the required input and output shape.

**Check:** The configured route supports the task format and fits the requested runtime and cost limits.

## 2. Chat Memory Buffer

Read [the Context Window Management method](../skills/context-window-management/SKILL.md). Associate only the needed prior context with the current session and use the requested retention boundary. Read `../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** Chat Memory Buffer: A session-scoped context record.

**Check:** A second session cannot read or overwrite this session’s context.

## 3. A tool to get the weather forecast based on geolocation

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** A tool to get the weather forecast based on geolocation: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. A tool for inputting the city and obtaining geolocation

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** A tool for inputting the city and obtaining geolocation: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. When chat message received

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Use the output from step-4 (memory, branch 0, input 0).

**Carry forward:** When chat message received: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 6. Generic AI Tool Agent

Read [the Agent Architecture method](../skills/agent-designer/SKILL.md). Use the supplied prompt, context, and output schema to produce the task result with the available model capability. Read `../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (languageModel, branch 0, input 0), step-4 (memory, branch 0, input 0), step-1 (main, branch 0, input 0), step-6 (tool, branch 0, input 0), step-5 (tool, branch 0, input 0).

**Carry forward:** Generic AI Tool Agent: The requested answer, draft, analysis, or structured result.

**Check:** The result follows the supplied context and schema and addresses the user request.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Integrating AI with Open-Meteo API for Enhanced Weather Forecasting”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting-0fa838/WORKFLOW.json
```
