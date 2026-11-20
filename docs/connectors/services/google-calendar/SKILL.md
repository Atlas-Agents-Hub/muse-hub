---
name: google-calendar-connector
description: "Get organized and stay on schedule"
---

# Google Calendar for Muse

Get organized and stay on schedule

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Calendar**.
2. Configure **OAuth 2.0 account connection; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/index.ts).

## Actions

### Find Busy/Free Periods in Calendar

Finds busy periods across calendars in a time range.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/find-busy-free-periods.ts).

### Find Free Time Slots

Computes open time slots shared across one or more calendars within a window, by inverting their busy blocks.

| Input | What to provide | Required |
| --- | --- | --- |
| `calendar_ids` | The calendars whose schedules must all be free. A slot is returned only when it is open on every selected calendar. | Yes |
| `start_date` | Start of the search window, as an absolute ISO 8601 timestamp (e.g. "2026-06-01T09:00:00Z"). Prefer absolute times over relative ones. | Yes |
| `end_date` | End of the search window, as an absolute ISO 8601 timestamp (e.g. "2026-06-05T18:00:00Z"). | Yes |
| `min_duration_minutes` | Discard any open slot shorter than this many minutes. Leave empty to return every open slot regardless of length. | Optional |
| `working_hours_start` | If set together with Working Hours End, each day's open slots are clipped to this hour range, interpreted in UTC (not the calendar's local time zone). Example: 9 for 09:00 UTC. Leave both unset to return slots across the full window. | Optional |
| `working_hours_end` | Upper bound of the daily working-hours window. Example: 17 for 5 PM. Ignored unless Working Hours Start is also set. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/find-free-slots.ts).

### Get Event

Fetch the full details of a single Google Calendar event by its event ID.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/ai-get-event.ts).

### Get Event by ID

Fetch event details by its unique ID from Google Calendar.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/get-event-by-id.ts).

### Get Events

Lists events in a calendar, with optional filters.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/get-events.ts).

### List Recurring Event Instances

Lists the individual occurrences of one recurring event series, each with its own instance event ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `calendar_id` | Calendar_Id | See action definition |
| `event_id` | The event ID of the recurring SERIES (the parent), e.g. "abc123def456". Obtain it from Search Events Across Calendars or Get all Events. Individual instance IDs will not work here. | Yes |
| `time_min` | Optional lower bound (inclusive) for an instance's end time, as an ISO 8601 timestamp with offset (e.g. "2026-06-01T00:00:00Z"). | Optional |
| `time_max` | Optional upper bound (exclusive) for an instance's start time, as an ISO 8601 timestamp with offset (e.g. "2026-06-30T23:59:59Z"). | Optional |
| `show_deleted` | Whether to include cancelled (deleted) instances of the series in the result. Defaults to false. | Optional |
| `max_results` | Maximum number of instances to return per page (1-2500). Defaults to the API default of 250. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/list-recurring-event-instances.ts).

### Move Event to Another Calendar

Moves an existing event from one calendar to another, preserving its event ID and metadata.

| Input | What to provide | Required |
| --- | --- | --- |
| `calendar_id` | Calendar_Id | See action definition |
| `event_id` | The ID of the event to move, e.g. "abc123def456". Obtain it from Search Events Across Calendars or Get all Events. | Yes |
| `destination_calendar_id` | The calendar to move the event to. | Yes |
| `send_updates` | Who should receive notifications about the change of the event's organizer. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/move-event.ts).

### Search Events Across Calendars

Searches every calendar the account can access for events matching a keyword within a required time window.

| Input | What to provide | Required |
| --- | --- | --- |
| `query` | Free-text query matched against event fields (summary, description, location, attendee names/emails) using Google's native search. Example: "budget review". | Yes |
| `start_date` | Lower bound (inclusive) for an event's end time, as an ISO 8601 timestamp (e.g. "2026-06-01T00:00:00Z"). Required to bound the cross-calendar scan. | Yes |
| `end_date` | Upper bound (exclusive) for an event's start time, as an ISO 8601 timestamp (e.g. "2026-06-30T23:59:59Z"). Required to bound the cross-calendar scan. | Yes |
| `single_events` | When enabled, recurring events are expanded into their individual instances instead of returning the underlying recurring event. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/actions/search-events-all-calendars.ts).

## Events and recurring work

- **[Event Cancelled](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/triggers/event-cancelled.ts)** — Fires when an event is canceled or deleted.
- **[Event Ends](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/triggers/event-ends.ts)** — Fires when an event ends.
- **[New or Updated Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-calendar/src/lib/triggers/calendar-event.ts)** — Triggers when an event is added or updated

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Google Calendar to find busy/free periods in calendar. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
