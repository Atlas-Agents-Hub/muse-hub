---
name: teamwork-connector
description: "Teamwork is a work and project management tool that helps teams improve collaboration, visibility, and accountability."
---

# Teamwork for Muse

Teamwork is a work and project management tool that helps teams improve collaboration, visibility, and accountability.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Teamwork**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Username** (`username`): Your Teamwork email address.
- **Password** (`password`): ProviderField
- **Subdomain** (`subdomain`): Your Teamwork site subdomain (e.g., mycompany for mycompany.teamwork.com)

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/index.ts).

## Actions

### Create Person

Create a new user/contact (name, email, invite options).

| Input | What to provide | Required |
| --- | --- | --- |
| `first-name` | The user's first name. | Yes |
| `last-name` | The user's last name. | Yes |
| `email-address` | The user's email address. | Yes |
| `user-type` | The type of user to create. | Yes |
| `company-id` | The company to associate the user with. | Optional |
| `sendInvite` | Send an invitation email to the new user. | Optional |
| `title` | The user's job title. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/create-person.ts).

### Create Stage

Add a new stage in a workflow or board.

| Input | What to provide | Required |
| --- | --- | --- |
| `workflowId` | The workflow to add the stage to. | Yes |
| `name` | The name of the stage. | Yes |
| `color` | Hex color code (e.g., #FF0000) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/create-stage.ts).

### Create Task

Add a new task under a project with description, due date, assignee, tags, etc.

| Input | What to provide | Required |
| --- | --- | --- |
| `projectId` | The project to create the task in. | Yes |
| `tasklistId` | The task list to add the task to. | Yes |
| `content` | The content of the task. | Yes |
| `responsible-party-id` | The users responsible for the task. | Optional |
| `start-date` | The start date of the task. | Optional |
| `due-date` | The due date of the task. | Optional |
| `description` | A description for the task. | Optional |
| `priority` | The priority of the task. | Optional |
| `tagIds` | Tags to associate with the task. | Optional |
| `attachment` | A file to attach to the task. | Optional |
| `customFields` | Custom fields for this task. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/create-task.ts).

### Find Company

Search for a company by name or domain.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchTerm` | The name or domain to search for. | Yes |
| `projectId` | Limit the search to a specific project. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/find-company.ts).

### Find Milestone

Find a milestone by name or due date in a project.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchTerm` | The name or due date to search for. | Yes |
| `projectId` | Limit the search to a specific project. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/find-milestone.ts).

### Find Notebook / Notebook Comment

Locate notebooks or note comments by search parameters.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchFor` | The type of item to search for. | Yes |
| `searchTerm` | The keyword to search for. | Yes |
| `projectId` | Limit the search to a specific project. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/find-notebook-or-comment.ts).

### Find Task

Search for tasks.

| Input | What to provide | Required |
| --- | --- | --- |
| `searchTerm` | The keyword to search for. | Yes |
| `projectId` | Limit the search to a specific project. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/find-task.ts).

### Update Task

Modify a task’s fields (due date, assignee, content, priority, etc.).

| Input | What to provide | Required |
| --- | --- | --- |
| `taskId` | The task to update. | Yes |
| `content` | The new content of the task. | Optional |
| `description` | The new description for the task. | Optional |
| `responsible-party-id` | The new users responsible for the task. | Optional |
| `start-date` | The new start date of the task. | Optional |
| `due-date` | The new due date of the task. | Optional |
| `priority` | The new priority of the task. | Optional |
| `tagIds` | New tags to associate with the task. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/actions/update-task.ts).

## Events and recurring work

- **[New Comment](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/triggers/new-comment.ts)** — Fires when a new comment is posted.
- **[New Expense](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/triggers/new-expense.ts)** — Fires when a new expense entry is added.
- **[New File](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/teamwork/src/lib/triggers/new-file.ts)** — Fires when a new file is added.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Teamwork to find company. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
