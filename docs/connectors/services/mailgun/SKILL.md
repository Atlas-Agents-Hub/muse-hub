---
name: mailgun-connector
description: "Email delivery service for sending, receiving, and tracking emails"
---

# Mailgun for Muse

Email delivery service for sending, receiving, and tracking emails

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Mailgun**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Api_Key** (`api_key`): ProviderField
- **Region** (`region`): Select the region your Mailgun account is in. Most accounts use US.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/index.ts).

## Actions

### Add Mailing List Member

Add a new member to a Mailgun mailing list

| Input | What to provide | Required |
| --- | --- | --- |
| `list` | List | See action definition |
| `address` | The email address to add to the mailing list. | Yes |
| `name` | The name of the member. | Optional |
| `upsert` | If enabled, updates the member if they already exist. Otherwise, an error is returned for duplicates. | Yes |
| `subscribed` | Set the subscription status of the member. | Optional |
| `vars` | JSON object with custom variables to store with this member, e.g. {"age": 30, "city": "Paris"}. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/add-mailing-list-member.ts).

### Delete Bounces (Bulk)

Remove bounced addresses from the Mailgun suppression list, either all at once for a domain or a single address.

| Input | What to provide | Required |
| --- | --- | --- |
| `domain` | Domain | See action definition |
| `scope` | Delete all bounces for the domain, or a single address. | Yes |
| `address` | Email address to remove from the bounce list. Required when Scope is "Single address". | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/delete-bounces-bulk.ts).

### Get Domain Health

Fetch the health of a Mailgun domain: current state, whether it has been disabled, and DNS verification status for sending and receiving records.

| Input | What to provide | Required |
| --- | --- | --- |
| `domain` | Domain | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/get-domain-health.ts).

### Get Domain Stats

Retrieve aggregated email statistics for a Mailgun domain (delivered, failed, opened, etc.). Useful for monitoring delivery health and detecting anomalies.

| Input | What to provide | Required |
| --- | --- | --- |
| `domain` | Domain | See action definition |
| `event` | Select which event types to include in the statistics. | Yes |
| `duration` | Time period to aggregate stats over. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/get-domain-stats.ts).

### Get Events

Retrieve email events from your Mailgun domain (deliveries, failures, opens, clicks, etc.). Useful for monitoring and alerting.

| Input | What to provide | Required |
| --- | --- | --- |
| `domain` | Domain | See action definition |
| `event` | Filter events by type. | Yes |
| `severity` | Only applies to "failed" events. Filter by permanent (hard bounce) or temporary (soft bounce). | Optional |
| `begin` | Start of the time range. RFC 2822 date (e.g. "Fri, 28 Mar 2026 10:00:00 -0000") or Unix timestamp (e.g. "1711620000"). Leave empty for Mailgun default (about 30 days ago). | Optional |
| `end` | End of the time range. Same format as Begin Date. Leave empty for now. | Optional |
| `limit` | Maximum number of events to return. Default is 100, max is 1000. Mailgun returns up to 300 per page — pagination is handled automatically. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/get-events.ts).

### List Bounces

Retrieve the list of bounced email addresses for a Mailgun domain. Useful for cleanup after delivery issues or spam attacks.

| Input | What to provide | Required |
| --- | --- | --- |
| `domain` | Domain | See action definition |
| `limit` | Maximum number of bounces to return (1-1000). Default is 100. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/list-bounces.ts).

### Send Email

Send an email using your Mailgun domain

| Input | What to provide | Required |
| --- | --- | --- |
| `domain` | Domain | See action definition |
| `from` | Sender email address, e.g. "Your Name <you@yourdomain.com>" | Yes |
| `to` | Recipient email address. For multiple recipients, separate with commas. | Yes |
| `cc` | Carbon copy recipients, separated by commas. | Optional |
| `bcc` | Blind carbon copy recipients, separated by commas. | Optional |
| `replyTo` | Email address for replies. | Optional |
| `subject` | Email Subject | Yes |
| `text` | Plain text version of the email body. | Optional |
| `html` | HTML version of the email body. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/send-email.ts).

### Validate Email

Validate an email address using Mailgun validation service. Requires a Mailgun account with email validation enabled.

| Input | What to provide | Required |
| --- | --- | --- |
| `email` | The email address to validate. | Yes |
| `providerLookup` | Enable additional mailbox provider checks for more accurate results. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/actions/validate-email.ts).

## Events and recurring work

- **[Bulk Bounce Threshold Exceeded](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mailgun/src/lib/triggers/bulk-bounce-threshold-exceeded.ts)** — Triggers once when too many emails bounce within a set time period. Useful for catching spam attacks or deliverability problems early.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Mailgun to add mailing list member. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
