---
name: pagerduty-connector
description: "Incident management workflows for PagerDuty REST API v2."
---

# PagerDuty for Muse

Incident management workflows for PagerDuty REST API v2.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **PagerDuty**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/index.ts).

## Actions

### Acknowledge Incident

Acknowledge an existing PagerDuty incident.

| Input | What to provide | Required |
| --- | --- | --- |
| `incidentId` | Incident Id | See action definition |
| `fromEmail` | From Email | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/actions/acknowledge-incident.ts).

### Create Incident

Create a new PagerDuty incident using the REST API.

| Input | What to provide | Required |
| --- | --- | --- |
| `fromEmail` | From Email | See action definition |
| `serviceId` | Service Id | See action definition |
| `title` | Incident title / summary. | Yes |
| `urgency` | Urgency | See action definition |
| `details` | Additional incident body text. | Optional |
| `incidentKey` | A string that identifies the incident. Duplicate requests with the same key and open incident on the same service will be rejected (de-duplication). | Optional |
| `assigneeIds` | Comma-separated list of PagerDuty user IDs to assign the incident to. Cannot be used together with Escalation Policy ID. | Optional |
| `priorityId` | The ID of the priority to assign to this incident. | Optional |
| `conferenceNumber` | Phone number of the conference bridge. | Optional |
| `conferenceUrl` | URL for the conference bridge. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/actions/create-incident.ts).

### Get Incident

Retrieve a PagerDuty incident by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `incidentId` | Incident Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/actions/get-incident.ts).

### List Incidents

List PagerDuty incidents with optional filters and pagination.

| Input | What to provide | Required |
| --- | --- | --- |
| `statuses` | Statuses | See action definition |
| `urgency` | Urgency | See action definition |
| `since` | Optional start of the search window. | Optional |
| `until` | Optional end of the search window. | Optional |
| `limit` | Maximum number of incidents to return (1–100). | Optional |
| `offset` | Pagination offset (number of records to skip). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/actions/list-incidents.ts).

### Resolve Incident

Resolve an existing PagerDuty incident.

| Input | What to provide | Required |
| --- | --- | --- |
| `incidentId` | Incident Id | See action definition |
| `fromEmail` | From Email | See action definition |
| `resolution` | Optional resolution note. PagerDuty adds this to the resolve log entry. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/actions/resolve-incident.ts).

## Events and recurring work

- **[Incident Acknowledged](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/triggers/incident-acknowledged.ts)** — Triggers when an incident is acknowledged.
- **[Incident Resolved](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/triggers/incident-resolved.ts)** — Triggers when an incident is resolved.
- **[New Incident](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pagerduty/src/lib/triggers/new-incident.ts)** — Triggers when a new incident is created

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use PagerDuty to get incident. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
