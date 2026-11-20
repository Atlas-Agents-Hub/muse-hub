---
name: azure-devops-connector
description: "Track work, code, and ship software with Azure Boards, Repos, and Pipelines."
---

# Azure DevOps for Muse

Track work, code, and ship software with Azure Boards, Repos, and Pipelines.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Azure DevOps**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Organization URL** (`organizationUrl`): Your Azure DevOps organization URL (e.g. https://dev.azure.com/mycompany)
- **Pat** (`pat`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/index.ts).

## Actions

### Add Comment

Adds a comment to an existing work item in Azure DevOps

| Input | What to provide | Required |
| --- | --- | --- |
| `project` | Project | See action definition |
| `work_item_id` | Numeric ID of the work item (e.g. 123). To pass it dynamically, reference the ID from a previous step (e.g. `{{trigger.id}}`), not the title. | Yes |
| `comment` | The comment text to add (supports HTML) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/lib/actions/add-comment.ts).

### Create Work Item

Creates a new work item (Bug, Task, User Story, etc.) in Azure DevOps

| Input | What to provide | Required |
| --- | --- | --- |
| `project` | Project | See action definition |
| `work_item_type` | Work_Item_Type | See action definition |
| `title` | The title of the work item | Yes |
| `description` | Detailed description of the work item (supports HTML) | Optional |
| `assigned_to` | Assigned_To | See action definition |
| `priority` | Priority | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/lib/actions/create-work-item.ts).

### Get Work Item

Retrieves a work item by ID from Azure DevOps

| Input | What to provide | Required |
| --- | --- | --- |
| `project` | Project | See action definition |
| `work_item_id` | Numeric ID of the work item (e.g. 123). To pass it dynamically, reference the ID from a previous step (e.g. `{{trigger.id}}`), not the title. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/lib/actions/get-work-item.ts).

### List Work Items

Lists work items from Azure DevOps using a WIQL query

| Input | What to provide | Required |
| --- | --- | --- |
| `project` | Project | See action definition |
| `wiql_query` | The WIQL query to execute. Default: SELECT [System.Id] FROM WorkItems WHERE [System.TeamProject] = @project ORDER BY [System.ChangedDate] DESC | Optional |
| `limit` | Maximum number of work items to return (default: 50, max: 200) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/lib/actions/list-work-items.ts).

### Update Work Item

Updates an existing work item in Azure DevOps

| Input | What to provide | Required |
| --- | --- | --- |
| `project` | Project | See action definition |
| `work_item_type` | Work_Item_Type | See action definition |
| `work_item_id` | Numeric ID of the work item (e.g. 123). To pass it dynamically from a previous step, use a reference like `{{trigger.id}}` or the output of a Get/List step — not the title. | Yes |
| `title` | New title for the work item | Optional |
| `description` | New description for the work item (supports HTML) | Optional |
| `state` | State | See action definition |
| `assigned_to` | Assigned_To | See action definition |
| `priority` | Priority | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/lib/actions/update-work-item.ts).

## Events and recurring work

- **[New or Updated Work Item (Instant)](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/lib/triggers/new-updated-work-item-webhook.ts)** — Fires instantly when a work item is created, updated, or commented on in Azure DevOps via a Service Hooks subscription. Requires a public webhook URL reachable from Azure DevOps.
- **[New or Updated Work Item (Polling)](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/azure-devops/src/lib/triggers/new-updated-work-item.ts)** — Polls Azure DevOps every few minutes and fires when a work item is created or updated. Use this when your Muse instance is not reachable from the public internet; otherwise prefer the Instant trigger. Pick a work item type to unlock the state filter.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Azure DevOps to get work item. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
