---
name: clockify-connector
description: "Clockify: create task, create time entry, find running timer."
---

# Clockify for Muse

Clockify: create task, create time entry, find running timer.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Clockify**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/index.ts).

## Actions

### Create Task

Creates a new in a specific project.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `projectId` | Project Id | See action definition |
| `name` | Task Name | Yes |
| `status` | Status | Optional |
| `assigneeIds` | Assignee Ids | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/actions/create-task.ts).

### Create Time Entry

Creates a new time entry.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `start` | Start Datetime | Yes |
| `end` | End Datetime | Yes |
| `description` | Entry Description | Optional |
| `projectId` | Project Id | See action definition |
| `taskId` | Task Id | See action definition |
| `billable` | Billable | Optional |
| `tagIds` | Tag Ids | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/actions/create-time-entry.ts).

### Find Running Timer

Finds currently running timer on specified workspace.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/actions/find-running-timer.ts).

### Find Task

Finds an existing task in a specific project.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `projectId` | Project Id | See action definition |
| `name` | Task Name | Yes |
| `exactMatch` | Exact Match ? | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/actions/find-task.ts).

### Find Time Entry

Finds a time entry by description, start datetime or end datetime.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `start` | Start Datetime | Optional |
| `end` | End Datetime | Optional |
| `description` | Entry Description | Optional |
| `projectId` | Project Id | See action definition |
| `taskId` | Task Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/actions/find-time-entry.ts).

### Start Timer

Starts a new time entry.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |
| `description` | Entry Description | Optional |
| `projectId` | Project Id | See action definition |
| `taskId` | Task Id | See action definition |
| `billable` | Billable | Optional |
| `tagIds` | Tag Ids | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/actions/start-timer.ts).

### Stop Timer

Stops currently running timer on specified workspace.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspaceId` | Workspace Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/actions/stop-timer.ts).

## Events and recurring work

- **[New Task](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/triggers/new-task.ts)** — Triggers when a new task is created in specified project.
- **[New Time Entry](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/triggers/new-time-entry.ts)** — Triggers when a new time entry is created.
- **[New Timer Started](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/clockify/src/lib/triggers/new-timer-started.ts)** — Triggers when a new entry is started and running.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Clockify to find running timer. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
