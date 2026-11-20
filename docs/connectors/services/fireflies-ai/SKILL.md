---
name: fireflies-ai-connector
description: "Meeting assistant that automatically records, transcribes, and analyzes conversations"
---

# Fireflies.ai for Muse

Meeting assistant that automatically records, transcribes, and analyzes conversations

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Fireflies.ai**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/index.ts).

## Actions

### Find Meeting by Call Details

Searches meetings based on provided parameters. Returns up to 1,000 meetings; narrow the filters if more match.

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | Finds meetings whose title contains this text. | Optional |
| `hostEmail` | Filter meetings by host email. | Optional |
| `participantEmail` | Filter meetings by participant email | Optional |
| `date` | Finds meetings in the 24 hours starting at this date and time. Pick the date in the date picker to get that day in your time zone. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/lib/actions/find-meeting-by-query.ts).

### Find Meeting by ID

Finds a specific meeting by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `meetingId` | The ID of the meeting to retrieve. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/lib/actions/find-meeting-by-id.ts).

### Find Recent Meeting

Retrieves the latest meeting for a user.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/lib/actions/find-recent-meeting.ts).

### Get User Details

Retrieves profile information by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `userId` | User ID | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/lib/actions/get-user-details.ts).

### Upload Audio

Creates a new meeting in Fireflies for transcription (requires a publicly accessible URL).

| Input | What to provide | Required |
| --- | --- | --- |
| `audioUrl` | The publicly accessible HTTPS URL of your audio or video file (mp3, mp4, wav, m4a, ogg). Fireflies only accepts URLs, not direct file uploads. For private files, use a signed URL with a short expiry. | Yes |
| `title` | Title | Yes |
| `client_reference_id` | Optional. Your own ID for this upload. Fireflies echoes it back in its webhooks. | Optional |
| `custom_language` | Optional. Language of the recording as a code such as "es" or "de". Leave empty for English. | Optional |
| `meeting_date` | Optional. When the meeting happened, as ISO 8601 (for example 2026-03-15 or 2026-03-15T14:30:00Z). Cannot be in the future. | Optional |
| `bypass_size_check` | Bypass_Size_Check | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/lib/actions/upload-audio.ts).

## Events and recurring work

- **[Meeting Summarized](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/lib/triggers/meeting-summarized.ts)** — Triggered when Fireflies finishes the AI summary of a meeting. A resend from Fireflies after notes change fires again, and in rare cases a delivery may fire twice.
- **[New Transcription Completed](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/fireflies-ai/src/lib/triggers/new-transcription-complete.ts)** — Triggered when a new meeting is transcribed. The summary may still be processing at this point; use Meeting Summarized if you need it. A resend from Fireflies after notes change fires again, and in rare cases a delivery may fire twice.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Fireflies.ai to find meeting by call details. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
