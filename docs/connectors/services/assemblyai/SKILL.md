---
name: assemblyai-connector
description: "Transcribe and extract data from audio using AssemblyAI's Speech AI."
---

# AssemblyAI for Muse

Transcribe and extract data from audio using AssemblyAI's Speech AI.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **AssemblyAI**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/index.ts).

## Actions

### Get Transcript

Retrieves a transcript by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/transcripts/get-transcript.ts).

### Get Transcript Paragraphs

Retrieve the paragraphs of the transcript by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/transcripts/get-paragraphs.ts).

### Get Transcript Redacted Audio

Get the result of the redacted audio model.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Id | See action definition |
| `download_file` | Download file? | Yes |
| `download_file_name` | The desired file name for storing in ActivePieces. Make sure the file extension is correct. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/transcripts/get-redacted-audio.ts).

### Get Transcript Sentences

Retrieve the sentences of the transcript by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/transcripts/get-sentences.ts).

### Get Transcript Subtitles

Export the transcript as SRT or VTT subtitles.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | Transcript ID | Yes |
| `format` | Subtitles Format | Yes |
| `chars_per_caption` | The maximum number of characters per caption | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/transcripts/get-subtitles.ts).

### List transcripts

Retrieve a list of transcripts you created.
Transcripts are sorted from newest to oldest. The previous URL always points to a page with older transcripts.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/transcripts/list-transcripts.ts).

### Retrieve LeMUR response

Retrieve a LeMUR response that was previously generated.

| Input | What to provide | Required |
| --- | --- | --- |
| `request_id` | Request_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/lemur/get-lemur-response.ts).

### Upload File

Upload a media file to AssemblyAI's servers.

| Input | What to provide | Required |
| --- | --- | --- |
| `file` | The File or URL of the audio or video file. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/assemblyai/src/lib/actions/files/upload.ts).

## Try it

> Use AssemblyAI to get transcript. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
