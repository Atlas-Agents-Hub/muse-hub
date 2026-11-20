---
name: datadog-connector
description: "Cloud monitoring and analytics platform"
---

# Datadog for Muse

Cloud monitoring and analytics platform

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Datadog**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Api Key** (`apiKey`): ProviderField
- **App Key** (`appKey`): ProviderField
- **Site** (`site`): StaticDropdown

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/datadog/src/index.ts).

## Actions

### Send Multiple logs

Send your logs to your Datadog platform over HTTP.

| Input | What to provide | Required |
| --- | --- | --- |
| `body` | Logs to send to Datadog, must contain a \`logs\` key with an array of objects. Documentation: https://docs.datadoghq.com/api/latest/logs/#send-logs | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/datadog/src/lib/actions/send-multiple-logs.ts).

### Send One log

Send one log to your Datadog platform over HTTP.

| Input | What to provide | Required |
| --- | --- | --- |
| `message` | The message to send to Datadog | Yes |
| `ddsource` | The DD source to send to Datadog | Optional |
| `ddtags` | The DD tags to send to Datadog, comma separated | Optional |
| `hostname` | The hostname to send to Datadog | Optional |
| `service` | The service to send to Datadog | Optional |
| `additionalProperties` | Additional properties to send to Datadog, in key-value pairs like status, level, etc. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/datadog/src/lib/actions/send-one-log.ts).

## Try it

> Use Datadog to send multiple logs. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
