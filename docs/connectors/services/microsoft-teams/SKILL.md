---
name: microsoft-teams-connector
description: "Microsoft Teams: create channel, find channel, find team member."
---

# Microsoft Teams for Muse

Microsoft Teams: create channel, find channel, find team member.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Microsoft Teams**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{cloud}/{tenantId}/oauth2/v2.0/authorize>
- Token endpoint: <https://{cloud}/{tenantId}/oauth2/v2.0/token>
- **Cloud** (`cloud`): ProviderField
- **Tenant ID** (`tenantId`): ShortText

Provider scopes: `Channel.Create`, `Channel.ReadBasic.All`, `ChannelMessage.Read.All`, `ChannelMessage.Send`, `Chat.ReadWrite`, `OnlineMeetingRecording.Read.All`, `OnlineMeetingTranscript.Read.All`, `Presence.Read.All`, `Team.ReadBasic.All`, `TeamMember.Read.All`, `User.Read`, `User.ReadBasic.All`, `email`, `offline_access`, `openid`, `profile`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/index.ts).

## Actions

### Create Channel

Create a new channel in Microsoft Teams.

| Input | What to provide | Required |
| --- | --- | --- |
| `teamId` | Team Id | See action definition |
| `channelDisplayName` | Channel Name | Yes |
| `channelDescription` | Channel Description | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/create-channel.ts).

### Find Channel

Finds channels by name.

| Input | What to provide | Required |
| --- | --- | --- |
| `teamId` | Team Id | See action definition |
| `channelName` | Channel Name | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/find-channel.ts).

### Find Team Member

Finds a team member by email or display name.

| Input | What to provide | Required |
| --- | --- | --- |
| `teamId` | Team Id | See action definition |
| `searchBy` | Search By | Yes |
| `searchValue` | Email address or name to search for. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/find-team-member.ts).

### Get Channel Message

Fetch a specific channel message by team, channel, and message ID (optionally a reply).

| Input | What to provide | Required |
| --- | --- | --- |
| `teamId` | Team Id | See action definition |
| `channelId` | Channel Id | See action definition |
| `messageId` | The ID of the channel message to retrieve. | Yes |
| `replyId` | Provide to fetch a specific reply under the message. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/get-channel-message.ts).

### Get Chat Message

Fetch a specific chat message by chat and message ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `chatId` | Chat Id | See action definition |
| `messageId` | The ID of the message to retrieve. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/get-chat-message.ts).

### Get Meeting Recording

Retrieves recordings for a Teams meeting. Provide a Recording to fetch its metadata; omit it to list all available recordings.

| Input | What to provide | Required |
| --- | --- | --- |
| `meetingIdentifierType` | Meeting Identifier Type | See action definition |
| `meetingIdentifierValue` | Meeting Identifier Value | See action definition |
| `recordingId` | Recording Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/get-meeting-recording.ts).

### Get Meeting Transcript

Retrieves transcripts for a Teams meeting. Provide a Transcript to fetch its text content; omit it to list all available transcripts.

| Input | What to provide | Required |
| --- | --- | --- |
| `meetingIdentifierType` | Meeting Identifier Type | See action definition |
| `meetingIdentifierValue` | Meeting Identifier Value | See action definition |
| `transcriptId` | Transcript Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/get-meeting-transcript.ts).

### Send Chat Message

Sends a message in an existing chat.

| Input | What to provide | Required |
| --- | --- | --- |
| `chatId` | Chat Id | See action definition |
| `contentType` | Content Type | Yes |
| `content` | Message | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/actions/send-chat-message.ts).

## Events and recurring work

- **[New Channel](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/triggers/new-channel.ts)** — Triggers when a new channel is created in a team.
- **[New Channel Message](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/triggers/new-channel-message.ts)** — Triggers when a new message is posted in a channel.
- **[New Chat Message](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-teams/src/lib/triggers/new-chat-message.ts)** — Triggers when a new message is received in a chat.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Microsoft Teams to find channel. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
