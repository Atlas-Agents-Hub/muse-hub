---
name: microsoft-excel-365-connector
description: "Spreadsheet software by Microsoft"
---

# Microsoft Excel 365 for Muse

Spreadsheet software by Microsoft

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Microsoft Excel 365**.
2. Configure **OAuth 2.0 account connection** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{cloud}/common/oauth2/v2.0/authorize>
- Token endpoint: <https://{cloud}/common/oauth2/v2.0/token>
- **Cloud** (`cloud`): ProviderField

Provider scopes: `Files.ReadWrite`, `Sites.ReadWrite.All`, `email`, `offline_access`, `openid`, `profile`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/index.ts).

## Actions

### Find Row

Locate a row by specifying a lookup column and value (e.g. find a row where “ID” = 123).

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `workbookId` | Workbook Id | See action definition |
| `worksheetId` | Worksheet Id | See action definition |
| `tableId` | Table Id | See action definition |
| `lookup_column` | The column to search in. | Yes |
| `lookup_value` | The value to find in the lookup column. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/find-row.ts).

### Find Workbook

Finds an existing workbook by name.

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `fileName` | Excel File name to search for without extension. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/find-workbooks.ts).

### Find Worksheet

Finds an existing worksheet by name.

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `workbookId` | Workbook Id | See action definition |
| `sheetName` | Worksheet Name | Yes |
| `exactMatch` | If true, only return worksheets that exactly match the name. If false, return worksheets that contain the name. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/find-worksheets.ts).

### Get Row by ID

Retrieve the entire content of a row by its row ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `workbookId` | Workbook Id | See action definition |
| `worksheetId` | Worksheet Id | See action definition |
| `tableId` | Table Id | See action definition |
| `row_id` | The zero-based index of the row to retrieve (e.g., 0 for the first row, 1 for the second). | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/get-row-by-id.ts).

### Get Table Columns

List columns of a table in a worksheet

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `workbookId` | Workbook Id | See action definition |
| `worksheetId` | Worksheet Id | See action definition |
| `tableId` | Table Id | See action definition |
| `limit` | Limit the number of columns retrieved | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/get-table-columns.ts).

### Get Table Rows

List rows of a table in a worksheet

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `workbookId` | Workbook Id | See action definition |
| `worksheetId` | Worksheet Id | See action definition |
| `tableId` | Table Id | See action definition |
| `limit` | Limit the number of rows retrieved | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/get-table-rows.ts).

### Get Workbooks

Retrieve a list of workbooks

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `limit` | Limits the number of workbooks returned, returns all workbooks if empty | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/get-workbooks.ts).

### Get Worksheets

Retrieve worksheets from a workbook

| Input | What to provide | Required |
| --- | --- | --- |
| `storageSource` | Storage Source | See action definition |
| `siteId` | Site Id | See action definition |
| `documentId` | Document Id | See action definition |
| `workbookId` | Workbook Id | See action definition |
| `returnAll` | If checked, all worksheets will be returned | Optional |
| `limit` | Limit the number of worksheets returned | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/microsoft-excel-365/src/lib/actions/get-worksheets.ts).

## Try it

> Use Microsoft Excel 365 to find row. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
