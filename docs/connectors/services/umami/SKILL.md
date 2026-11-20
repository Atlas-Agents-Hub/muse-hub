---
name: umami-connector
description: "Privacy-focused, open-source web analytics."
---

# Umami for Muse

Privacy-focused, open-source web analytics.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Umami**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Instance URL** (`baseUrl`): Base URL of your Umami instance (e.g. `https://umami.example.com`). Do not include a trailing slash.
- **Username** (`username`): Your Umami login username.
- **Password** (`password`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/index.ts).

## Actions

### Get Active Visitors

Returns the number of people currently browsing a website in real time.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/actions/get-active-visitors.ts).

### Get Pageviews

Returns pageview and session counts over time, broken down by hour, day, week, month, or year.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `startDate` | Start Date | See action definition |
| `endDate` | End Date | See action definition |
| `unit` | How to bucket the results over time. | Optional |
| `timezone` | Timezone for date grouping, e.g. Europe/Paris or America/New_York. Defaults to UTC. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/actions/get-pageviews.ts).

### Get Website Metrics

Returns a ranked list for a chosen metric category (e.g. top pages, browsers, or countries) over a date range.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `startDate` | Start Date | See action definition |
| `endDate` | End Date | See action definition |
| `type` | Which metric to rank results by. | Yes |
| `limit` | Maximum number of results to return. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/actions/get-website-metrics.ts).

### Get Website Stats

Returns a summary of visitors, pageviews, bounce rate, and average visit duration for a date range.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `startDate` | Start Date | See action definition |
| `endDate` | End Date | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/actions/get-website-stats.ts).

### List Websites

Returns all websites tracked in your Umami account.

| Input | What to provide | Required |
| --- | --- | --- |
| `limit` | Maximum number of websites to return. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/actions/list-websites.ts).

### Send Event

Records a custom event or pageview on a website. Leave the event name blank to track a plain pageview.

| Input | What to provide | Required |
| --- | --- | --- |
| `websiteId` | Website Id | See action definition |
| `url` | Path of the page to record, e.g. /pricing. | Yes |
| `eventName` | Name of the custom event, e.g. signup-button-click. Leave blank to record a pageview. | Optional |
| `eventData` | Extra key-value pairs to attach to the event. | Optional |
| `referrer` | URL the visitor came from. | Optional |
| `title` | Title of the page being recorded. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/actions/send-event.ts).

## Events and recurring work

- **[New Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/triggers/new-event.ts)** — Triggers when a new custom event is recorded on a website.
- **[New Session](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/umami/src/lib/triggers/new-session.ts)** — Triggers when a new visitor session is detected on a website.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Umami to get active visitors. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

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
python connector.py inspect umami
```

Available HTTP reads: `read-v1-websites`.

[Prepare and run a request](../../RUN_CONNECTORS.md) using the inputs in [http.json](http.json).
