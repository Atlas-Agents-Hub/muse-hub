---
name: freshdesk-connector
description: "Customer support software"
---

# Freshdesk for Muse

Customer support software

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Freshdesk**.
2. Configure **Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Base URL** (`base_url`): Enter the base URL
- **API Token** (`access_token`): Enter the API token

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshdesk/src/index.ts).

## Actions

### Get All Tickets By Status

Get All Tickets by selected status from Freshdesk.

| Input | What to provide | Required |
| --- | --- | --- |
| `status_filter` | Select one or status values | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshdesk/src/lib/actions/get-all-tickets-by-status.ts).

### Get Contact from ID

Get contacts details from Freshdesk using ID number.

| Input | What to provide | Required |
| --- | --- | --- |
| `contactid` | The ID number of the contact | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshdesk/src/lib/actions/get-contact-from-id.ts).

### Get Freshdesk Contacts

Get contact details from Freshdesk for all (optional filtered) contacts.

| Input | What to provide | Required |
| --- | --- | --- |
| `filter_type` | Select one and provide the value. | Optional |
| `filter_value` | Provide value if previous option selected! | Optional |
| `filter_status` | Can filter by state: blocked, deleted, unverified or verified. | Optional |
| `per_page` | Freshdesk calls this per_page - set to 0 for all, if specified maximum is 100 | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshdesk/src/lib/actions/get-contacts.ts).

### Get Ticket Status

Get Ticket status from Freshdesk. Returns ticket_status, assigned_status, assigned_id

| Input | What to provide | Required |
| --- | --- | --- |
| `ticketid` | The Ticket ID to return status | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshdesk/src/lib/actions/get-ticket-status.ts).

### Get Tickets

Get Ticket instances from Freshdesk.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/freshdesk/src/lib/actions/get-tickets.ts).

## Try it

> Use Freshdesk to get all tickets by status. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
