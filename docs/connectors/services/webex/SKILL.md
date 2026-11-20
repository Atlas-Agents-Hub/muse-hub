---
name: webex-connector
description: "Cisco Webex Meetings: create message, create room, create team."
---

# Cisco Webex Meetings for Muse

Cisco Webex Meetings: create message, create room, create team.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Cisco Webex Meetings**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://webexapis.com/v1/authorize>
- Token endpoint: <https://webexapis.com/v1/access_token>

Provider scopes: `meeting:schedules_read`, `spark:all`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/index.ts).

## Actions

### Create Message

Post a plain text or rich text message to a Webex room or send a direct message

| Input | What to provide | Required |
| --- | --- | --- |
| `messageType` | Choose between sending to a room or a direct message to a person | Yes |
| `destination` | Destination | Yes |
| `text` | The message to send | Yes |
| `markdown` | The message in Markdown format for rich text. If provided, text will be used as alternate text | Optional |
| `parentId` | The parent message ID to reply to (optional) | Optional |
| `files` | Public URLs to files to attach (only one file per message) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/lib/actions/create-message.ts).

### Create Room

Create a new Webex room (space). The authenticated user is automatically added as a member.

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | A user-friendly name for the room | Yes |
| `description` | The description of the room. Required if isPublic is true. | Optional |
| `teamId` | The ID for the team with which this room is associated (optional) | Optional |
| `classificationId` | The classificationId for the room (optional) | Optional |
| `isPublic` | Make the room public and discoverable within the org. Note: description is required if this is true. | Optional |
| `isLocked` | Set the space as locked/moderated. The creator becomes a moderator. | Optional |
| `isAnnouncementOnly` | Sets the space into announcement mode. Only moderators can post messages. Note: space must be locked (moderated) to enable this. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/lib/actions/create-room.ts).

### Create Team

Create a new Webex team. The authenticated user is automatically added as a member.

| Input | What to provide | Required |
| --- | --- | --- |
| `name` | A user-friendly name for the team | Yes |
| `description` | The description of the team (optional) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/lib/actions/create-team.ts).

### Find Message

Retrieve details for a specific message by message ID

| Input | What to provide | Required |
| --- | --- | --- |
| `messageId` | The unique identifier for the message | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/lib/actions/find-message.ts).

### Find room

Retrieve details for a specific room by room id

| Input | What to provide | Required |
| --- | --- | --- |
| `roomId` | Room Id | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/lib/actions/find-room.ts).

## Events and recurring work

- **[New meeting](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/lib/triggers/new-meeting.ts)** — Triggers when a new meeting is created.
- **[New room](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/webex/src/lib/triggers/new-room.ts)** — Triggers when a new room is created

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Cisco Webex Meetings to find message. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)

## Run a direct request

From the connector directory, inspect available requests with:

```console
python connector.py inspect webex
```

Available HTTP reads: `read-v1-people-me`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
