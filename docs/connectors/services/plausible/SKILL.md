---
name: plausible-connector
description: "Privacy-friendly website analytics"
---

# Plausible Analytics for Muse

Privacy-friendly website analytics

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Plausible Analytics**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/index.ts).

## Actions

### Get Aggregate Stats

Get aggregated analytics metrics for a time period

| Input | What to provide | Required |
| --- | --- | --- |
| `site_id` | Site_Id | See action definition |
| `period` | Period | Yes |
| `metrics` | Metrics | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/get-aggregate-stats.action.ts).

### Get Site

Get details of a site including tracker script configuration

| Input | What to provide | Required |
| --- | --- | --- |
| `site_id` | Site_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/get-site.ts).

### Get Traffic Breakdown

Break down traffic by page, source, country, or other dimensions

| Input | What to provide | Required |
| --- | --- | --- |
| `site_id` | Site_Id | See action definition |
| `period` | Period | Yes |
| `property` | Breakdown By | Yes |
| `limit` | Limit | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/get-breakdown.action.ts).

### List Custom Properties

Get a list of custom properties for a site

| Input | What to provide | Required |
| --- | --- | --- |
| `site_id` | Site_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/list-custom-properties.ts).

### List Goals

Get a list of goals for a site

| Input | What to provide | Required |
| --- | --- | --- |
| `site_id` | Site_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/list-goals.ts).

### List Guests

Get a list of guests for a site

| Input | What to provide | Required |
| --- | --- | --- |
| `site_id` | Site_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/list-guests.ts).

### List Sites

Get a list of sites your Plausible account can access

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/list-sites.ts).

### List Teams

Get a list of teams your Plausible account can access

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/actions/list-teams.ts).

## Events and recurring work

- **[Traffic Spike](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/plausible/src/lib/triggers/traffic-spike.trigger.ts)** — Triggers once when current visitors exceed a threshold, then resets when they drop below it

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Plausible Analytics to get aggregate stats. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
