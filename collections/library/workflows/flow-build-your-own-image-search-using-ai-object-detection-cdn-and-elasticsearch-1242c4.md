# Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearch

Complete “Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearch” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearch.
- The selected records, date range, and output destination.
- Complete the named fields in flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/INPUTS.json.
- Configured connections or tools for elasticsearch, http.

## 1. When clicking "Test workflow"

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When clicking "Test workflow": A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Set Variables

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-6`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Set Variables: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Fetch Source Image

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-6 (main, branch 0, input 0).

**Carry forward:** Fetch Source Image: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Use Detr-Resnet-50 Object Classification

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-7`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Use Detr-Resnet-50 Object Classification: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 5. Split Out Results Only

Read [the Reconcile Versioned Events Without Resurrection method](../../muse-starters-v1/skills/incremental-pipeline/SKILL.md). Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-7 (main, branch 0, input 0).

**Carry forward:** Split Out Results Only: Batch output and a continuation position.

**Check:** Each input record is processed once and a restart continues from the saved position.

## 6. Filter Score >= 0.9

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0).

**Carry forward:** Filter Score >= 0.9: Selected records and the corresponding match counts.

**Check:** A matching record and a near-miss take the intended paths.

## 7. Fetch Source Image Again

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-10`, for its exact field mappings, expressions, and settings. Use the output from step-4 (main, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Fetch Source Image Again: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 8. Crop Object From Image

Read [the Image Retoucher method](../skills/image-retoucher/SKILL.md). Apply the requested image operation, dimensions, and export settings to the selected asset. Operation settings: operation = crop. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-5`, for its exact field mappings, expressions, and settings. Use the output from step-10 (main, branch 0, input 0).

**Carry forward:** Crop Object From Image: An image with the specified format and dimensions.

**Check:** Inspect the visual result and confirm its dimensions and readability.

## 9. Upload to Cloudinary

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-8`, for its exact field mappings, expressions, and settings. Use the output from step-5 (main, branch 0, input 0).

**Carry forward:** Upload to Cloudinary: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 10. Create Docs In Elasticsearch

Read [the Reconcile an Uncertain Operation Without Replaying It method](../../muse-starters-v1/skills/effect-reconciliation/SKILL.md). Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier. Operation settings: operation = create. Read `../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json`, node `step-9`, for its exact field mappings, expressions, and settings. Use the output from step-8 (main, branch 0, input 0), step-5 (data, branch 0, input 0), step-6 (data, branch 0, input 0).

**Carry forward:** Create Docs In Elasticsearch: The service result and a readback of the affected resource.

**Check:** The exact target and payload match the request; the returned record confirms the effect.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearch”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-build-your-own-image-search-using-ai-object-detection-cdn-and-elasticsearch-1242c4/WORKFLOW.json
```
