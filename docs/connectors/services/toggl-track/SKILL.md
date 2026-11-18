---
name: toggl-track-connector
description: "Toggl Track is a time tracking application that allows users to track their daily activities across different platforms. Works with classic Toggl Track and Toggl 2.0 accounts."
---

# Toggl Track for Muse

Toggl Track is a time tracking application that allows users to track their daily activities across different platforms. Works with classic Toggl Track and Toggl 2.0 accounts.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Toggl Track**.
2. Configure **API key or access token; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/index.ts).

## Actions

### Find Client

Find a client by name or status in a workspace.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `name` | The name of the client to find (case-insensitive). | Optional |
| `status` | Filter clients by their status. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/find-client.ts).

### Find Project

Find a project in a workspace by its name.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `name` | The name of the project to find. | Optional |
| `active` | Return active, inactive, or both types of projects. | Optional |
| `billable` | Return only billable projects. | Optional |
| `only_me` | Get only projects assigned to the current user. | Optional |
| `only_templates` | Return only template projects. | Optional |
| `page` | Page number for pagination. | Optional |
| `per_page` | Number of items per page (max 200; Toggl 2.0: max 100). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/find-project.ts).

### Find Tag

Find a tag by name in a workspace.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `search` | Search by tag name. | Optional |
| `page` | Page number for pagination. | Optional |
| `per_page` | Number of items per page (Toggl 2.0: max 100). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/find-tag.ts).

### Find Task

Find a task by name and status.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `search` | Search by task name. | Optional |
| `project_id` | Filter by project ID. | Optional |
| `active` | Filter by active state. | Optional |
| `page` | Page number for pagination. | Optional |
| `per_page` | Number of items per page (default 50). | Optional |
| `sort_field` | Field used for sorting. | Optional |
| `sort_order` | Sort order. | Optional |
| `start_date` | Smallest boundary date (YYYY-MM-DD). | Optional |
| `end_date` | Biggest boundary date (YYYY-MM-DD). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/find-task.ts).

### Find User

Find a user in a workspace by their name or email.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `organization_id` | Organization_Id | See action definition |
| `search_term` | The name or email of the user to find. | Optional |
| `active` | Return only active users. | Optional |
| `page` | Page number for pagination. | Optional |
| `per_page` | Number of items per page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/find-user.ts).

### Get Client

Get a client by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `client_id` | Client_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/get-client.ts).

### Get Project

Get a project by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |
| `project_id` | Project_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/get-project.ts).

### Get Workspace

Get the details of a workspace.

| Input | What to provide | Required |
| --- | --- | --- |
| `workspace_id` | Workspace_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/actions/get-workspace.ts).

## Events and recurring work

- **[New Client](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/triggers/new-client.ts)** — Fires when a new client is created in a workspace.
- **[New Project](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/triggers/new-project.ts)** — Fires when a new project is added.
- **[New Tag](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/toggl-track/src/lib/triggers/new-tag.ts)** — Triggers when a new tag is created

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Toggl Track to find client. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
