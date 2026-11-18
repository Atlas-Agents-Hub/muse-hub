---
name: google-tasks-connector
description: "Task list management application"
---

# Google Tasks for Muse

Task list management application

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Tasks**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

Provider scopes: `email`, `https://www.googleapis.com/auth/tasks`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/index.ts).

## Actions

### Add Task

Add a new task to a specified task list

| Input | What to provide | Required |
| --- | --- | --- |
| `tasks_list` | Tasks_List | See action definition |
| `title` | Title | See action definition |
| `notes` | Notes | See action definition |
| `due` | Due | See action definition |
| `completed` | Completed | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/new-task.ts).

### Create Task

Create a new task in a task list, optionally as a subtask and/or positioned after a sibling.

| Input | What to provide | Required |
| --- | --- | --- |
| `tasks_list` | Tasks_List | See action definition |
| `title` | Title | See action definition |
| `notes` | Notes | See action definition |
| `due_date` | Due_Date | See action definition |
| `parent_task_id` | Make this a subtask of the task with this id (must be in the same list). Obtain the id from Find Tasks. Omit to create a top-level task. | Optional |
| `previous_task_id` | Place the new task immediately after the sibling with this id. Obtain the id from Find Tasks. Omit to place it first among its siblings. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/create-task.ts).

### Delete Task

Permanently delete a task by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `tasks_list` | Tasks_List | See action definition |
| `task_id` | The ID of the task to delete. Obtain the id from Find Tasks. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/delete-task.ts).

### Find Tasks

Search and list tasks in a task list with optional date-range and status filters.

| Input | What to provide | Required |
| --- | --- | --- |
| `tasks_list` | Tasks_List | See action definition |
| `show_completed` | Include completed tasks in results. Defaults to true. | Optional |
| `show_hidden` | Include hidden tasks (tasks that have been completed and a day has passed). Defaults to false. | Optional |
| `due_min` | Return tasks due on or after this date. RFC 3339 timestamp, e.g. 2026-06-01T00:00:00Z. | Optional |
| `due_max` | Return tasks due before this date (exclusive). RFC 3339 timestamp, e.g. 2026-07-01T00:00:00Z. | Optional |
| `completed_min` | Return tasks completed on or after this date. RFC 3339 timestamp. | Optional |
| `completed_max` | Return tasks completed before this date (exclusive). RFC 3339 timestamp. | Optional |
| `updated_min` | Return tasks last modified on or after this date. Useful for "since last run" incremental reads. RFC 3339 timestamp. | Optional |
| `max_results` | Maximum number of tasks to return (1–100). Defaults to 20 when omitted. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/find-tasks.ts).

### Get Task

Fetch a single task by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `tasks_list` | Tasks_List | See action definition |
| `task_id` | The ID of the task to fetch. Obtain the id from Find Tasks. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/get-task.ts).

### List Task Lists

List the authenticated user's task lists (id and title).

| Input | What to provide | Required |
| --- | --- | --- |
| `max_results` | Maximum number of task lists to return (1–100). Defaults to 20 when omitted. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/list-task-lists.ts).

### Move Task

Reposition or reparent a task within its list, or move it to another list.

| Input | What to provide | Required |
| --- | --- | --- |
| `tasks_list` | Tasks_List | See action definition |
| `task_id` | The ID of the task to move. Obtain the id from Find Tasks. | Yes |
| `parent_task_id` | Reparent the task under the task with this id (must be in the destination list). Obtain the id from Find Tasks. Omit to move it to the top level. | Optional |
| `previous_task_id` | Place the task immediately after the sibling with this id (must be in the destination list). Obtain the id from Find Tasks. Omit to place it first among its siblings; to move it to the end, pass the last sibling's id (read the current order with Find Tasks). | Optional |
| `destination_tasklist_id` | Move the task to this task list. Omit to keep it in the current list. Recurring tasks cannot be moved between lists. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/move-task.ts).

### Update Task

Edit an existing task — title, notes, due date, or status.

| Input | What to provide | Required |
| --- | --- | --- |
| `tasks_list` | Tasks_List | See action definition |
| `task_id` | The ID of the task to update. Obtain the id from Find Tasks. | Yes |
| `title` | New title for the task. | Optional |
| `notes` | New notes / description for the task. | Optional |
| `due` | New due date for the task. RFC 3339 timestamp, e.g. 2026-07-15T00:00:00Z. | Optional |
| `status` | Task status. To simply complete a task prefer Mark Task Complete; set needsAction here to reopen a completed task. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/actions/update-task.ts).

## Events and recurring work

- **[New Task](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-tasks/src/lib/triggers/new-task.ts)** — Triggers when a task is added to a list, or also when one is edited if you choose New and edited tasks.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Google Tasks to find tasks. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
