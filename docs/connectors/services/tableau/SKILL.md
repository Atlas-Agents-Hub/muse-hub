---
name: tableau-connector
description: "Business intelligence and analytics platform for data visualization"
---

# Tableau for Muse

Business intelligence and analytics platform for data visualization

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Tableau**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Server URL** (`serverUrl`): Your Tableau Server or Tableau Cloud URL (e.g., https://10az.online.tableau.com)
- **API Version** (`apiVersion`): Tableau REST API version (e.g., 3.19, 3.20, 3.26). Check your Tableau server documentation for supported versions. Use 3.26 for most Tableau Cloud instances.
- **Site Content URL** (`siteContentUrl`): Your Tableau site name (leave empty for default site)
- **Username** (`username`): Your Tableau username (email for Tableau Cloud, or domain\\username for Server)
- **Password** (`password`): ProviderField
- **Personal Access Token Name** (`personalAccessTokenName`): Name of your Personal Access Token
- **Personal Access Token Secret** (`personalAccessTokenSecret`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/index.ts).

## Actions

### Download View

Download a view from a workbook in the specified format

| Input | What to provide | Required |
| --- | --- | --- |
| `viewId` | Select the view to download | Yes |
| `format` | The format to download the view in | Yes |
| `maxAge` | Maximum age of cached data in minutes (default: 60) | Optional |
| `resolution` | Resolution for image format (high for maximum pixel density) | Optional |
| `vizWidth` | Width of the rendered image/PDF in pixels | Optional |
| `vizHeight` | Height of the rendered image/PDF in pixels | Optional |
| `pageType` | Page size for PDF format | Optional |
| `orientation` | Page orientation for PDF format | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/actions/download-view.ts).

### Find View

Finds a view based on name (URL name)

| Input | What to provide | Required |
| --- | --- | --- |
| `viewName` | The URL name of the view to find (e.g., Sheet1 from /views/workbook/Sheet1) | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/actions/find-view.ts).

### Find Workbook

Finds a workbook based on ID or content URL

| Input | What to provide | Required |
| --- | --- | --- |
| `searchType` | Choose whether to search by workbook ID or content URL | Yes |
| `workbookId` | The ID of the workbook to find | Optional |
| `contentUrl` | The content URL of the workbook to find (e.g., "MyWorkbook" from /workbooks/MyWorkbook) | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/actions/find-workbook.ts).

### Refresh Workbook

Refreshes the specified workbook immediately

| Input | What to provide | Required |
| --- | --- | --- |
| `workbookId` | Select the workbook to refresh | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/actions/refresh-workbook.ts).

### Run Extract Refresh Task

Runs the specified extract refresh task and returns job information

| Input | What to provide | Required |
| --- | --- | --- |
| `taskId` | Select the extract refresh task to run | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/actions/run-extract-refresh-task.ts).

## Events and recurring work

- **[Datasource Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/triggers/datasource-events.ts)** — Triggers when a datasource event occurs (created, updated, or deleted)
- **[Datasource Refresh Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/triggers/datasource-refresh-events.ts)** — Triggers when a datasource refresh event occurs (started, succeeded, or failed)
- **[Label Event](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/tableau/src/lib/triggers/label-events.ts)** — Triggers when a label event occurs (created, updated, or deleted)

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Tableau to find view. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
