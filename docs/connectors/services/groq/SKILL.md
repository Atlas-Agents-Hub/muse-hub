---
name: groq-connector
description: "Use Groq's fast language models and audio processing capabilities."
---

# Groq for Muse

Use Groq's fast language models and audio processing capabilities.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Groq**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/groq/src/index.ts).

## Actions

### Ask AI

Send a question or instruction to a Groq model and get a text reply.

| Input | What to provide | Required |
| --- | --- | --- |
| `model` | Model | See action definition |
| `prompt` | What you want the model to answer or do. | Yes |
| `temperature` | From 0 to 2. Lower is more focused, higher is more varied. | Optional |
| `maxTokens` | Longest reply in tokens, about 4 characters each. | Yes |
| `topP` | From 0 to 1. Adjust this or Temperature, not both. | Optional |
| `frequencyPenalty` | From -2 to 2. Groq models do not support this yet. | Optional |
| `presencePenalty` | From -2 to 2. Groq models do not support this yet. | Optional |
| `memoryKey` | Runs that share this ID continue one conversation. Empty: no memory. | Optional |
| `memoryInfo` | Memory Info | Optional |
| `roles` | Messages sent before the question, such as a system instruction. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/groq/src/lib/actions/ask-ai.ts).

### Transcribe Audio

Turn speech in an audio file into text, in the language spoken.

| Input | What to provide | Required |
| --- | --- | --- |
| `file` | flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav or webm. | Yes |
| `model` | Model | See action definition |
| `language` | ISO-639-1 code of the spoken language, for better accuracy. | Optional |
| `prompt` | Spellings or text that came just before, in the audio's language. | Optional |
| `temperature` | From 0 to 1. Groq recommends 0. | Optional |
| `responseFormat` | Text returns the words alone; Verbose JSON adds segment timings. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/groq/src/lib/actions/transcribe-audio.ts).

### Translate Audio

Turn speech in any supported language into English text.

| Input | What to provide | Required |
| --- | --- | --- |
| `file` | flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav or webm. | Yes |
| `model` | Model | See action definition |
| `prompt` | Spellings or earlier text in English to guide the translation. | Optional |
| `temperature` | From 0 to 1. Groq recommends 0. | Optional |
| `responseFormat` | Text returns the words alone; Verbose JSON adds segment timings. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/groq/src/lib/actions/translate-audio.ts).

## Try it

> Use Groq to ask ai. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
