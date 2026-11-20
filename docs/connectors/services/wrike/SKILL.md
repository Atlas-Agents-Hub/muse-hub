---
name: wrike-connector
description: "Wrike: add comment, create folder, create project."
---

# Wrike for Muse

Wrike: add comment, create folder, create project.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Wrike**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://login.wrike.com/oauth2/authorize/v4>
- Token endpoint: <https://login.wrike.com/oauth2/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/index.ts).

## Actions

### Add Comment

Add a comment or internal note to a task or folder

| Input | What to provide | Required |
| --- | --- | --- |
| `entityType` | Select whether you want to add the comment to a task or folder | Yes |
| `entityId` | The ID of the task or folder to add the comment to | Yes |
| `text` | The text content of the comment | Yes |
| `plainText` | Whether the comment should be treated as plain text (no HTML formatting). Default is HTML formatting. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/add-comment.ts).

### Create Folder

Create a new folder in Wrike

| Input | What to provide | Required |
| --- | --- | --- |
| `parentFolderId` | The ID of the parent folder where the new folder will be created. Leave empty to create at root level. | Optional |
| `title` | The title of the folder | Yes |
| `description` | The description of the folder | Optional |
| `shareds` | User IDs to share the folder with | Yes |
| `project` | Whether this folder should be created as a project with additional project settings | Optional |
| `projectOwnerId` | The ID of the user who will own the project (required when creating as project) | Optional |
| `projectStartDate` | The start date of the project (format: YYYY-MM-DD) | Optional |
| `projectEndDate` | The end date of the project (format: YYYY-MM-DD) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/create-folder.ts).

### Create Project

Create a new project in Wrike

| Input | What to provide | Required |
| --- | --- | --- |
| `parentFolderId` | The ID of the parent folder where the project will be created. Leave empty to create at root level. | Optional |
| `title` | The title of the project | Yes |
| `description` | The description of the project | Optional |
| `ownerIds` | User IDs who will own the project | Yes |
| `shareds` | User IDs to share the project with | Yes |
| `start_date` | Project start date (format: YYYY-MM-DD) | Optional |
| `end_date` | Project end date (format: YYYY-MM-DD) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/create-project.ts).

### Create Task

Create a new task in Wrike

| Input | What to provide | Required |
| --- | --- | --- |
| `folderId` | The ID of the folder where the task will be created | Yes |
| `title` | The title of the task | Yes |
| `description` | The description of the task | Optional |
| `status` | The status of the task | Optional |
| `importance` | The importance/priority of the task | Optional |
| `assignees` | User IDs to assign to the task | Yes |
| `start_date` | Task start date (format: YYYY-MM-DD) | Optional |
| `due_date` | Task due date (format: YYYY-MM-DD) | Optional |
| `duration` | Task duration in minutes | Optional |
| `customFields` | Custom field values for the task | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/create-task.ts).

### Find Folder / Project

Retrieve folder / project metadata by ID or name

| Input | What to provide | Required |
| --- | --- | --- |
| `folderId` | The ID of the folder/project to retrieve. If provided, other search criteria will be ignored. | Optional |
| `title` | Search for folders/projects by title (partial match) | Optional |
| `parentIds` | Search for folders/projects within specific parent folders | Yes |
| `project` | Filter to only return projects (folders marked as projects) | Optional |
| `pageSize` | Maximum number of folders/projects to return (max 1000) | Optional |
| `authors` | Filter by authors (users who created the folders) | Yes |
| `owners` | Filter by owners (users who own the projects) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/find-folder.ts).

### Find Task

Retrieve a task by its ID or lookup fields

| Input | What to provide | Required |
| --- | --- | --- |
| `taskId` | The ID of the task to retrieve. If provided, other search criteria will be ignored. | Optional |
| `title` | Search for tasks by title (partial match) | Optional |
| `folderId` | Search for tasks within a specific folder | Optional |
| `status` | Filter tasks by status | Optional |
| `importance` | Filter tasks by importance/priority | Optional |
| `assignees` | Filter tasks by assignee user IDs | Yes |
| `authors` | Filter tasks by author user IDs | Yes |
| `pageSize` | Maximum number of tasks to return (max 1000) | Optional |
| `sortField` | Field to sort tasks by | Optional |
| `sortOrder` | Sort order for results | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/find-task.ts).

### Update Task

Update fields of an existing task in Wrike

| Input | What to provide | Required |
| --- | --- | --- |
| `taskId` | The ID of the task to update | Yes |
| `title` | The new title of the task | Optional |
| `description` | The new description of the task | Optional |
| `status` | The new status of the task | Optional |
| `importance` | The new importance/priority of the task | Optional |
| `assignees` | User IDs to assign to the task (replaces existing assignees) | Yes |
| `start_date` | Task start date (format: YYYY-MM-DD) | Optional |
| `due_date` | Task due date (format: YYYY-MM-DD) | Optional |
| `duration` | Task duration in minutes | Optional |
| `customFields` | Custom field values to update for the task | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/update-task.ts).

### Upload Attachment

Upload a file and attach it to a task or folder

| Input | What to provide | Required |
| --- | --- | --- |
| `entityType` | Select whether to attach the file to a task or folder | Yes |
| `entityId` | The ID of the task or folder to attach the file to | Yes |
| `file` | The file to upload and attach | Yes |
| `fileName` | Optional custom name for the uploaded file | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/actions/upload-attachment.ts).

## Events and recurring work

- **[New Folder](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/triggers/new-folder.ts)** — Fires when a new folder (or project) is created in Wrike.
- **[New Subtask Created](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/triggers/new-subtask.ts)** — Triggers when a subtask is created.
- **[New Task](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/wrike/src/lib/triggers/new-task.ts)** — Fires when a new task is created in Wrike (optionally within a folder).

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Wrike to find folder / project. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
