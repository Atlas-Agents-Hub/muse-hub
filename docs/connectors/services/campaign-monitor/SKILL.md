---
name: campaign-monitor-connector
description: "Email marketing platform for delivering exceptional email campaigns."
---

# Campaign Monitor for Muse

Email marketing platform for delivering exceptional email campaigns.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Campaign Monitor**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/index.ts).

## Actions

### Find Subscriber

Find a subscriber by email in a specific list.

| Input | What to provide | Required |
| --- | --- | --- |
| `clientId` | Client Id | See action definition |
| `listId` | List Id | See action definition |
| `email` | The email address of the subscriber to find | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/find-subscriber.ts).

### Get Campaign Summary

Returns the reporting summary of a sent campaign.

| Input | What to provide | Required |
| --- | --- | --- |
| `clientId` | Client Id | See action definition |
| `campaignId` | Campaign Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/get-campaign-summary.ts).

### Get List Stats

Returns subscriber growth and totals for a list.

| Input | What to provide | Required |
| --- | --- | --- |
| `clientId` | Client Id | See action definition |
| `listId` | List Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/get-list-stats.ts).

### Get List Subscribers

Returns one page of subscribers in a list, filtered by state.

| Input | What to provide | Required |
| --- | --- | --- |
| `clientId` | Client Id | See action definition |
| `listId` | List Id | See action definition |
| `state` | State | Yes |
| `page` | Page number to return, starting at 1. | Optional |
| `pageSize` | Subscribers per page, between 10 and 1000. | Optional |
| `orderField` | Order By | Optional |
| `orderDirection` | Order Direction | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/get-list-subscribers.ts).

### List Clients

Returns all clients in your Campaign Monitor account.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/list-clients.ts).

### List Lists

Returns all subscriber lists of a client.

| Input | What to provide | Required |
| --- | --- | --- |
| `clientId` | Client Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/list-lists.ts).

### List Sent Campaigns

Returns one page of campaigns a client has sent.

| Input | What to provide | Required |
| --- | --- | --- |
| `clientId` | Client Id | See action definition |
| `sentFromDate` | Only campaigns sent on or after this date. | Optional |
| `sentToDate` | Only campaigns sent before this date (the date itself is excluded). | Optional |
| `tags` | Only campaigns with these tags, as a comma-separated list. | Optional |
| `page` | Page number to return, starting at 1. | Optional |
| `pageSize` | Campaigns per page, between 10 and 1000. | Optional |
| `orderDirection` | Order Direction | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/list-sent-campaigns.ts).

### List Smart Emails

Returns the smart transactional emails of a client.

| Input | What to provide | Required |
| --- | --- | --- |
| `clientId` | Client Id | See action definition |
| `status` | Status | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/actions/list-smart-emails.ts).

## Events and recurring work

- **[New Campaign Sent](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/triggers/new-campaign-sent.ts)** — Triggers when a client sends a new campaign.
- **[New Client](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/triggers/new-client.ts)** — Triggered when a new client is added to Campaign Monitor.
- **[New Subscriber Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/campaign-monitor/src/lib/triggers/new-subscriber-added.ts)** — Triggered when a new subscriber is added to a list.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Campaign Monitor to find subscriber. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
