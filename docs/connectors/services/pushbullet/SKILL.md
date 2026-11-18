---
name: pushbullet-connector
description: "Cross-device notification service"
---

# Pushbullet for Muse

Cross-device notification service

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Pushbullet**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushbullet/src/index.ts).

## Actions

### Send a Link

Sends a clickable link notification to your devices, one device or an email address.

| Input | What to provide | Required |
| --- | --- | --- |
| `url` | The link that opens when the notification is clicked, e.g. https://example.com. | Yes |
| `title` | The headline of the notification. | Optional |
| `body` | Optional text shown under the title. | Optional |
| `device` | Device | See action definition |
| `email` | Email | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushbullet/src/lib/actions/send-a-link.ts).

### Send a Note

Sends a text notification to your devices, one device or an email address.

| Input | What to provide | Required |
| --- | --- | --- |
| `title` | The headline of the notification. | Yes |
| `body` | The text shown under the title. | Yes |
| `device` | Device | See action definition |
| `email` | Email | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushbullet/src/lib/actions/send-a-note.ts).

## Events and recurring work

- **[New Push](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/pushbullet/src/lib/triggers/new-push.ts)** — Triggers when a new push (note, link or file) appears on your Pushbullet account.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Pushbullet to send a link. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
