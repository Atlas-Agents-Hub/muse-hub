# Publish one video natively to TikTok Instagram and YouTube with PostWire

Complete “Publish one video natively to TikTok Instagram and YouTube with PostWire” with the connected steps, field mappings, and result checks below.

## Bring these inputs

- The request and source material for Publish one video natively to TikTok Instagram and YouTube with PostWire.
- The selected records, date range, and output destination.
- Complete the named fields in flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/INPUTS.json.
- Configured connections or tools for http.

## 1. When you click Test workflow

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Record the supplied event, file, or record batch and its selection criteria. Read `../workflow-assets/flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/WORKFLOW.json`, node `step-1`, for its exact field mappings, expressions, and settings. Start from the configured inputs.

**Carry forward:** When you click Test workflow: A named input record or bounded batch.

**Check:** The input type, required fields, and selection scope match this request.

## 2. Your idea, video and platforms

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Apply the field assignments, type conversions, and expressions to the incoming records. Read `../workflow-assets/flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/WORKFLOW.json`, node `step-2`, for its exact field mappings, expressions, and settings. Use the output from step-1 (main, branch 0, input 0).

**Carry forward:** Your idea, video and platforms: Mapped records with the expected field names and types.

**Check:** Required fields survive mapping and record counts reconcile.

## 3. Write a native caption per platform

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/WORKFLOW.json`, node `step-3`, for its exact field mappings, expressions, and settings. Use the output from step-2 (main, branch 0, input 0).

**Carry forward:** Write a native caption per platform: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## 4. Publish to every connected account

Read [the Review a Bounded Automation Plan Before Execution method](../../muse-starters-v1/skills/automation-contract/SKILL.md). Use the configured HTTP method, URL, headers, and body with the expected response format. Operation settings: method = POST. Read `../workflow-assets/flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/WORKFLOW.json`, node `step-4`, for its exact field mappings, expressions, and settings. Use the output from step-3 (main, branch 0, input 0), step-2 (data, branch 0, input 0).

**Carry forward:** Publish to every connected account: A response with status, typed body, and relevant pagination or job identifiers.

**Check:** The response status and body satisfy the operation contract and the request targets the selected service.

## Check the finished work

- Trace a representative input through the selected branches to its final result.
- Check record counts, required fields, and the requested output format.
- Read back each requested service change and preserve its returned identifier.

## Finish

Deliver the requested result for “Publish one video natively to TikTok Instagram and YouTube with PostWire”, including the source record identifiers and completed output location.

## Workflow files

Open [WORKFLOW.json](../workflow-assets/flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/WORKFLOW.json) for the operation graph, branch conditions, field mappings, and transformations. Fill [INPUTS.json](../workflow-assets/flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/INPUTS.json) with your selected sources, destinations, connections, and model capability. Follow numbered branch edges when a decision has more than one output; carry each named result into the operations that depend on it.

Model and embedding operations use your available capability. Use the configured service adapter for network operations and local tools for data transformations. An expression names an input field or earlier step result; a transformation reference describes the calculation to apply to those records. Check a representative input before continuing through a batch or a loop.

Inspect the dependency order and required connections from the extracted package folder:

```sh
python -B ../../../tools/workflow_library.py ../workflow-assets/flow-publish-one-video-natively-to-tiktok-instagram-and-youtube-with-postwire-35be2a/WORKFLOW.json
```
