---
name: acuity-scheduling-connector
description: "Acuity Scheduling: add blocked off time, create appointment, create client."
---

# Acuity Scheduling for Muse

Acuity Scheduling: add blocked off time, create appointment, create client.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Acuity Scheduling**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://acuityscheduling.com/oauth2/authorize>
- Token endpoint: <https://acuityscheduling.com/oauth2/token>

Provider scopes: `api-v1`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/index.ts).

## Actions

### Add Blocked Off Time

Block off a specific time range on a calendar.

| Input | What to provide | Required |
| --- | --- | --- |
| `start` | The start date and time for the block (ISO 8601 format). | Yes |
| `end` | The end date and time for the block (ISO 8601 format). | Yes |
| `calendarID` | Calendar Id | See action definition |
| `notes` | Optional notes for the blocked off time. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/actions/add-blocked-time.ts).

### Create Appointment

Creates a new appointment.

| Input | What to provide | Required |
| --- | --- | --- |
| `datetime` | Date and time of the appointment. | Yes |
| `appointmentTypeID` | Appointment Type Id | See action definition |
| `firstName` | Client's first name. | Yes |
| `lastName` | Client's last name. | Yes |
| `email` | Client's email address. (Optional if booking as admin). | Optional |
| `phone` | Client's phone number. | Optional |
| `timezone` | Client's timezone (e.g., America/New_York). Required for accurate availability checking. | Yes |
| `adminBooking` | Set to true to book as an admin. Disables availability/attribute validations, allows setting notes, and makes Calendar ID required. | Optional |
| `calendarID` | Calendar Id | See action definition |
| `noEmail` | If true, confirmation emails or SMS will not be sent. | Optional |
| `certificate` | Package or coupon certificate code. | Optional |
| `notes` | Appointment notes. Only settable if booking as admin. | Optional |
| `smsOptIn` | Indicates whether the client has explicitly given permission to receive SMS messages. | Optional |
| `addonIDs` | Addon Ids | See action definition |
| `labelId` | Label Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/actions/create-appointment.ts).

### Create Client

Creates a new client.

| Input | What to provide | Required |
| --- | --- | --- |
| `firstName` | Client's first name. | Yes |
| `lastName` | Client's last name. | Yes |
| `phone` | Client's phone number. | Optional |
| `email` | Client's email address. | Optional |
| `notes` | Notes about the client. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/actions/create-client.ts).

### Find Appointment(s)

Find appointments based on various criteria, including client information.

| Input | What to provide | Required |
| --- | --- | --- |
| `firstName` | Filter appointments by client first name. | Optional |
| `lastName` | Filter appointments by client last name. | Optional |
| `email` | Filter appointments by client e-mail address. | Optional |
| `phone` | Filter appointments by client phone number. URL encode '+' if using country codes (e.g., %2B1234567890). | Optional |
| `minDate` | Only get appointments on or after this date. | Optional |
| `maxDate` | Only get appointments on or before this date. | Optional |
| `calendarID` | Calendar Id | See action definition |
| `appointmentTypeID` | Appointment Type Id | See action definition |
| `status` | Filter by appointment status. | Optional |
| `maxResults` | Maximum number of results to return (default 100). | Optional |
| `direction` | Sort direction for the results. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/actions/find-appointments.ts).

### Find Client

Finds client based on seach term.

| Input | What to provide | Required |
| --- | --- | --- |
| `search` | Filter client list by first name, last name, or phone number. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/actions/find-client.ts).

### Reschedule Appointment

Reschedules an existing appointment to a new date/time.

| Input | What to provide | Required |
| --- | --- | --- |
| `id` | The ID of the appointment to reschedule. | Yes |
| `appointmentTypeID` | Appointment Type Id | See action definition |
| `datetime` | New Date and time of the appointment. | Yes |
| `timezone` | Client's timezone (e.g., America/New_York). | Yes |
| `calendarID` | Calendar Id | See action definition |
| `adminReschedule` | Set to true to reschedule as an admin. Disables availability validations. | Optional |
| `noEmail` | If true, rescheduling emails or SMS will not be sent. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/actions/reschedule-appointment.ts).

### Update Client

Updates an existing client.

| Input | What to provide | Required |
| --- | --- | --- |
| `currentFirstName` | The current first name of the client to update. | Yes |
| `currentLastName` | The current last name of the client to update. | Yes |
| `currentPhone` | The current phone number of the client to update. Helps identify the client if names are not unique. | Optional |
| `newFirstName` | Client's new first name. Leave blank to keep current. | Optional |
| `newLastName` | Client's new last name. Leave blank to keep current. | Optional |
| `newEmail` | Client's new email address. Leave blank to keep current. | Optional |
| `newPhone` | Client's new phone number. Leave blank to keep current. | Optional |
| `newNotes` | New notes about the client. Leave blank to keep current. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/actions/update-client.ts).

## Events and recurring work

- **[Appointment Canceled](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/triggers/appointment-canceled.ts)** — Triggers when an appointment is canceled.
- **[New Appointment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/acuity-scheduling/src/lib/triggers/appointment-scheduled.ts)** — Triggers when a new appointment is scheduled.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Acuity Scheduling to find appointment(s). Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
