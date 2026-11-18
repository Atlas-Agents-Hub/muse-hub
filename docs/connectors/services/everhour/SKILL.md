---
name: everhour-connector
description: "Time tracking software that integrates into project management tools to track billable hours, set budgets, and monitor spending."
---

# Everhour for Muse

Time tracking software that integrates into project management tools to track billable hours, set budgets, and monitor spending.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Everhour**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/everhour/src/index.ts).

## Actions

### Create Task

Creates a new task in a project.

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | The ID of the project to create the task in. | Yes |
| `name` | The name of the task. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/everhour/src/lib/actions/create-task.ts).

### Start Timer

Starts a timer for a specific task.

| Input | What to provide | Required |
| --- | --- | --- |
| `taskId` | The ID of the task to start the timer for. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/everhour/src/lib/actions/start-timer.ts).

### Stop Timer

Stops the currently running timer. Fails if no timer is currently active.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/everhour/src/lib/actions/stop-timer.ts).

## Try it

> Use Everhour to create task. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
