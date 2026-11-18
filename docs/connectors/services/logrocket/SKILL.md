---
name: logrocket-connector
description: "Get AI-generated summaries of user sessions to understand customer behavior and troubleshoot issues faster."
---

# LogRocket for Muse

Get AI-generated summaries of user sessions to understand customer behavior and troubleshoot issues faster.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **LogRocket**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/logrocket/src/index.ts).

## Actions

### Identify User

Create or update user information and traits in LogRocket to contextualize user behavior.

| Input | What to provide | Required |
| --- | --- | --- |
| `orgId` | Your LogRocket organization ID (found in Settings > General Settings, or in your App ID before the slash) | Yes |
| `appId` | Your LogRocket app/project ID (found in Settings > General Settings, or in your App ID after the slash) | Yes |
| `userId` | The unique identifier for the user | Yes |
| `name` | The user's name (max 1024 characters) | Optional |
| `email` | The user's email address (max 1024 characters) | Optional |
| `timestamp` | Unix timestamp in milliseconds indicating when this data was collected (optional) | Optional |
| `traits` | User traits as key-value pairs (e.g., {"plan": "free", "age": 43}). Values will be converted to strings. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/logrocket/src/lib/actions/identify-user.ts).

### Request Highlights

Request session highlights for a user. Results will be sent to the webhook URL when ready.

| Input | What to provide | Required |
| --- | --- | --- |
| `orgId` | Your LogRocket organization ID (found in Settings > General Settings, or in your App ID before the slash) | Yes |
| `projectId` | Your LogRocket project ID (found in Settings > General Settings, or in your App ID after the slash) | Yes |
| `userEmail` | The email of the user to get highlights for | Optional |
| `userId` | The ID of the user from LogRocket.identify() calls | Optional |
| `timeRangeStart` | Start of the time range for sessions (optional) | Optional |
| `timeRangeEnd` | End of the time range for sessions (optional) | Optional |
| `webhookUrl` | URL where highlights results will be posted when ready. You can get this from the "Highlights Ready" trigger. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/logrocket/src/lib/actions/request-highlights.ts).

## Events and recurring work

- **[Highlights Ready](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/logrocket/src/lib/triggers/highlights-ready.ts)** — Trigger when session highlights are ready. Use this webhook URL when requesting highlights.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use LogRocket to identify user. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
