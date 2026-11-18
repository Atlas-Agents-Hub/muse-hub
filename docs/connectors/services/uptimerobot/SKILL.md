---
name: uptimerobot-connector
description: "Monitor your websites, APIs, and servers. Get alerted when things go down."
---

# UptimeRobot for Muse

Monitor your websites, APIs, and servers. Get alerted when things go down.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **UptimeRobot**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/uptimerobot/src/index.ts).

## Actions

### Create HTTP Monitor

Create a new HTTP uptime monitor in UptimeRobot

| Input | What to provide | Required |
| --- | --- | --- |
| `friendly_name` | A name for this monitor (e.g. 'Company Website' or 'API Server') | Yes |
| `url` | The full URL to monitor, including the protocol (e.g. 'https://example.com'). | Yes |
| `interval` | How often UptimeRobot checks this URL, in seconds. Minimum 300s (5 min) on the Free plan, 60s on Solo/Team, 30s on Enterprise. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/uptimerobot/src/lib/actions/create-monitor.ts).

### Delete Monitor

Permanently delete a monitor from UptimeRobot. This cannot be undone.

| Input | What to provide | Required |
| --- | --- | --- |
| `monitor` | Monitor | See action definition |
| `monitor_id_override` | Use this to pass a dynamic Monitor ID from a previous step. If set, this overrides the dropdown selection above. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/uptimerobot/src/lib/actions/delete-monitor.ts).

### Edit Monitor

Update the settings of an existing UptimeRobot monitor

| Input | What to provide | Required |
| --- | --- | --- |
| `monitor` | Monitor | See action definition |
| `monitor_id_override` | Use this to pass a dynamic Monitor ID from a previous step (e.g. {{create_monitor.id}}). If set, this overrides the dropdown selection above. | Optional |
| `friendly_name` | Update the monitor's name. Leave empty to keep the current name. | Optional |
| `url` | Update the URL or IP being monitored. Leave empty to keep the current value. | Optional |
| `interval` | Minimum 300s (5 min) on the Free plan, 60s on Solo/Team, 30s on Enterprise. Values below the plan minimum are rejected by UptimeRobot. Leave empty to keep the current interval. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/uptimerobot/src/lib/actions/edit-monitor.ts).

### Get Monitors

List and search your UptimeRobot monitors with optional filters. Leave the Monitors / Monitor IDs fields empty to return all monitors.

| Input | What to provide | Required |
| --- | --- | --- |
| `monitor_ids` | Monitor_Ids | See action definition |
| `monitor_ids_csv` | Use this to pass dynamic Monitor IDs from a previous step (e.g. "123, 456"). Merged with any selections above. | Optional |
| `type` | Only HTTP monitors are supported at the moment. Other UptimeRobot types (Keyword, Ping, Port, Heartbeat) will be added in a future release. Leave empty to return monitors of all types. | Optional |
| `status` | Only return monitors with this status. Leave empty for all statuses. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/uptimerobot/src/lib/actions/get-monitors.ts).

### Pause or Resume Monitor

Temporarily pause or resume monitoring for a specific monitor.

| Input | What to provide | Required |
| --- | --- | --- |
| `monitor` | Monitor | See action definition |
| `monitor_id_override` | Use this to pass a dynamic Monitor ID from a previous step. If set, this overrides the dropdown selection above. | Optional |
| `action` | Pause stops all checks and alerts. Resume restarts monitoring. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/uptimerobot/src/lib/actions/pause-resume-monitor.ts).

## Try it

> Use UptimeRobot to get monitors. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
