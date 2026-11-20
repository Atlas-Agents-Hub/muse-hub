---
name: localai-connector
description: "The free, Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required."
---

# LocalAI for Muse

The free, Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **LocalAI**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Server URL** (`base_url`): The address of your LocalAI server, for example http://localhost:8080/v1. It must be reachable from Muse.
- **Access Token** (`access_token`): One of the API keys your server was started with (--api-keys or API_KEY). Leave empty if the server has no keys.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/localai/src/index.ts).

## Actions

### Ask LocalAI

Ask LocalAI anything you want!

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model | See action definition |
| `prompt` | Question | Yes |
| `temperature` | Higher is more random, lower is more focused. Defaults to 0.9. | Optional |
| `maxTokens` | Longest answer to generate, in tokens. Defaults to 2048. | Optional |
| `topP` | Nucleus sampling, from 0 to 1. Defaults to 1. | Optional |
| `frequencyPenalty` | From -2 to 2. Higher repeats lines less. Defaults to 0. | Optional |
| `presencePenalty` | From -2 to 2. Higher moves to new topics. Defaults to 0.6. | Optional |
| `roles` | Messages sent before the question, each with a role and content. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/localai/src/lib/actions/send-prompt.ts).

### Create Embedding

Turn text into a vector for semantic search or clustering.

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model | See action definition |
| `input` | The text to turn into a vector. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/localai/src/lib/actions/create-embedding.ts).

### List Models

List the models installed on your LocalAI server.

| Input | What to provide | Required |
| --- | --- | --- |
| `contains` | Only return models whose id includes this text. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/localai/src/lib/actions/list-models.ts).

### Text to Speech

Turn text into a spoken audio file.

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model | See action definition |
| `text` | The text to read aloud. | Yes |
| `voice` | For models with several voices. Empty uses the default. | Optional |
| `format` | Not every LocalAI backend supports every format. | Yes |
| `fileName` | Name for the audio file, without the extension. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/localai/src/lib/actions/text-to-speech.ts).

### Transcribe Audio

Turn speech in an audio file into text.

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model | See action definition |
| `audio` | The recording to transcribe. | Yes |
| `language` | Language code of the speech. Empty auto-detects. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/localai/src/lib/actions/transcribe-audio.ts).

## Try it

> Use LocalAI to list models. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
