---
name: zeplin-connector
description: "Zeplin: create note, find project, find screen."
---

# Zeplin for Muse

Zeplin: create note, find project, find screen.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Zeplin**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/index.ts).

## Actions

### Create Note

Create a note on a screen in Zeplin

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `screenId` | Screen Id | See action definition |
| `content` | The content of the note | Yes |
| `color` | The color of the note | Yes |
| `x` | The x coordinate position of the note on the screen | Yes |
| `y` | The y coordinate position of the note on the screen | Yes |
| `x_start` | The starting x coordinate for range selection (optional) | Optional |
| `y_start` | The starting y coordinate for range selection (optional) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/lib/actions/create-note.ts).

### Find Project

Find a project by name or retrieve all projects

| Input | What to provide | Required |
| --- | --- | --- |
| `projectName` | Optional project name to search for (partial match) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/lib/actions/find-project.ts).

### Find Screen

Find a screen by name or retrieve all screens in a project

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `screenName` | Optional screen name to search for (partial match) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/lib/actions/find-screen.ts).

### Update Project

Update a project's name and description

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `name` | The new name for the project | Optional |
| `description` | The new description for the project | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/lib/actions/update-project.ts).

### Update Screen

Update a screen's description

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | Project Id | See action definition |
| `screenId` | Screen Id | See action definition |
| `description` | The new description for the screen | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/lib/actions/update-screen.ts).

## Events and recurring work

- **[New Note](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/lib/triggers/new-note.ts)** — Triggered when a new note is created on a screen
- **[New Screen](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/zeplin/src/lib/triggers/new-screen.ts)** — Triggered when a new screen is created in a project

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Zeplin to find project. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
