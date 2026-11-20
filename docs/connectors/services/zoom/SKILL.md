---
name: zoom-connector
description: "Video conferencing, web conferencing, webinars, screen sharing"
---

# Zoom for Muse

Video conferencing, web conferencing, webinars, screen sharing

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Zoom**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://zoom.us/oauth/authorize>
- Token endpoint: <https://zoom.us/oauth/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/index.ts).

## Actions

### Create Zoom Meeting

Create a new Zoom Meeting

| Input | What to provide | Required |
| --- | --- | --- |
| `topic` | The meeting's topic | Yes |
| `start_time` | Meeting start date-time, for example 2026-11-01T15:00:00 (read in the Timezone below) or 2026-11-01T15:00:00Z (UTC). | Optional |
| `timezone` | IANA timezone for the start time, for example America/New_York. Defaults to UTC. | Optional |
| `duration` | Duration of the meeting | Optional |
| `auto_recording` | Auto Recording | Optional |
| `audio` | Audio | Optional |
| `agenda` | The meeting's agenda | Optional |
| `password` | The password required to join the meeting. By default, a password can only have a maximum length of 10 characters and only contain alphanumeric characters and the @, -, _, and * characters. | Optional |
| `pre_schedule` | Whether the prescheduled meeting was created via the GSuite app. | Optional |
| `schedule_for` | The email address or user ID of the user to schedule a meeting for. | Optional |
| `join_url` | Not used by Zoom (kept for compatibility). Zoom creates the join URL and returns it in the output. | Optional |
| `require_authentication` | When on, only participants signed in to a Zoom account can join. Turn off to let anyone with the link join. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/create-meeting.ts).

### Delete Meeting

Delete a meeting, or one occurrence of a recurring meeting.

| Input | What to provide | Required |
| --- | --- | --- |
| `meeting_id` | Meeting_Id | See action definition |
| `occurrence_id` | Occurrence_Id | See action definition |
| `schedule_for_reminder` | Email the host and alternative hosts that the meeting was cancelled. | Optional |
| `cancel_meeting_reminder` | Email registrants that the meeting was cancelled. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/delete-meeting.ts).

### Find Zoom Meeting

Retrieve the details of an existing meeting.

| Input | What to provide | Required |
| --- | --- | --- |
| `meeting_id` | Meeting_Id | See action definition |
| `occurrence_id` | Meeting Occurrence ID. Provide this field to view meeting details of a particular occurrence of the recurring meeting. | Optional |
| `show_previous_occurrences` | Set to true if you would like to view meeting details of all previous occurrences of a recurring meeting. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/find-meeting.ts).

### Get Current User

Get the profile of the Zoom user behind this connection.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/get-current-user.ts).

### Get Meeting

Get the details of a meeting by its meeting ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `meeting_id` | Meeting_Id | See action definition |
| `occurrence_id` | Occurrence_Id | See action definition |
| `show_previous_occurrences` | For recurring meetings: also include occurrences that already happened. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/get-meeting.ts).

### List Cloud Recordings

List the cloud recordings of the connected user between two dates (paid Zoom plan with cloud recording).

| Input | What to provide | Required |
| --- | --- | --- |
| `from` | Start date in YYYY-MM-DD format (UTC), for example 2026-10-01. | Yes |
| `to` | End date in YYYY-MM-DD format (UTC), at most one month after From Date. Defaults to today, or to one month after From Date if that is earlier. Required with Next Page Token: use the To value from the previous page so every page covers the same dates. | Optional |
| `page_size` | Page_Size | See action definition |
| `next_page_token` | Next_Page_Token | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/list-recordings.ts).

### List Meetings

List the meetings of the connected Zoom user, one page at a time.

| Input | What to provide | Required |
| --- | --- | --- |
| `type` | Which meetings to list. | Optional |
| `page_size` | Page_Size | See action definition |
| `next_page_token` | Next_Page_Token | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/list-meetings.ts).

### List Past Meeting Instances

List the ended instances (UUID and start time) of a meeting.

| Input | What to provide | Required |
| --- | --- | --- |
| `meeting_id` | Meeting_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zoom/src/lib/actions/list-past-meeting-instances.ts).

## Try it

> Use Zoom to find zoom meeting. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect zoom
```

Available HTTP reads: `read-v2-users-me`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
