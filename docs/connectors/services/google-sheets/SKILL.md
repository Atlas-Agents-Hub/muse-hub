---
name: google-sheets-connector
description: "Create, edit, and collaborate on spreadsheets online"
---

# Google Sheets for Muse

Create, edit, and collaborate on spreadsheets online

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Sheets**.
2. Configure **OAuth 2.0 account connection; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/index.ts).

## Actions

### Find or Create Row

Look up a row by column value; if no match is found, create a new row with the provided values.

| Input | What to provide | Required |
| --- | --- | --- |
| `columnName` | Column Name | See action definition |
| `searchValue` | The value to look for in the selected column. | Yes |
| `matchCase` | Only treat exact matches as found. | Yes |
| `headerRow` | The row that contains the column names. | Yes |
| `useHeaderNames` | Key each row by column name instead of A, B, C. | Optional |
| `first_row_headers` | First_Row_Headers | See action definition |
| `as_string` | Store dates and formulas as plain text instead of evaluating them. | Optional |
| `values` | Values | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/find-or-create-row.ts).

### Find Rows

Look up rows in a worksheet based on a column value.

| Input | What to provide | Required |
| --- | --- | --- |
| `columnName` | Column Name | See action definition |
| `searchValue` | The value to look for. Leave empty to return all rows. | Optional |
| `matchCase` | Only return rows whose cell matches the value exactly. | Yes |
| `startingRow` | Start searching from this row number. | Optional |
| `numberOfRows` | How many matching rows to return. | Optional |
| `headerRow` | The row that contains the column names. | Yes |
| `useHeaderNames` | Key each row by column name instead of A, B, C. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/find-rows.ts).

### Find Spreadsheet(s)

Find spreadsheet(s) by name.

| Input | What to provide | Required |
| --- | --- | --- |
| `includeTeamDrives` | Include Team Drives | See action definition |
| `spreadsheet_name` | Enter the name of the spreadsheet to search for | Yes |
| `exact_match` | Only return spreadsheets whose name matches exactly. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/find-spreadsheets.ts).

### Find Worksheet(s)

Find worksheets in a spreadsheet by title.

| Input | What to provide | Required |
| --- | --- | --- |
| `includeTeamDrives` | Include Team Drives | See action definition |
| `spreadsheetId` | Spreadsheet Id | See action definition |
| `title` | The worksheet title to search for. | Yes |
| `exact_match` | Only return worksheets whose title matches exactly. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/find-worksheet.ts).

### Get All Rows

Read every row from a worksheet.

| Input | What to provide | Required |
| --- | --- | --- |
| `first_row_headers` | First_Row_Headers | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/get-many-rows.ts).

### Get Next Rows

Read the next batch of rows from a worksheet, continuing where the last run left off. A batch of only blank rows returns an empty list mid-sheet, so do not stop at the first empty result.

| Input | What to provide | Required |
| --- | --- | --- |
| `startRow` | The row to start reading from on the first run. | Yes |
| `headerRow` | The row that contains the column names. | Yes |
| `useHeaderNames` | Key each row by column name instead of A, B, C. | Optional |
| `markdown` | Markdown | Optional |
| `memKey` | The key used to store the current row number in memory | Yes |
| `groupSize` | The number of rows to get | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/get-rows.ts).

### Get Row by Number

Retrieve one row by its row number.

| Input | What to provide | Required |
| --- | --- | --- |
| `rowNumber` | The row to retrieve, counting from 1. | Yes |
| `headerRow` | The row that contains the column names. | Yes |
| `useHeaderNames` | Key each row by column name instead of A, B, C. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/find-row-by-num.ts).

### Read Data Range

Read cells from a range using A1 notation (e.g. A1:D10). Returns rows and the resolved range.

| Input | What to provide | Required |
| --- | --- | --- |
| `range` | The cells to read. Leave empty to read the whole worksheet. | Optional |
| `majorDimension` | Group the results one array per row, or one array per column. | Yes |
| `valueRenderOption` | Return values as displayed, as raw values, or as formulas. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/actions/read-data-range.ts).

## Events and recurring work

- **[New or Updated Row](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/triggers/new-or-updated-row.trigger.ts)** — Triggers when a new row is added or modified in a spreadsheet.
- **[New Row Added](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-sheets/src/lib/triggers/new-row-added-webhook.ts)** — Triggers when a new row is added to the bottom of a worksheet.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Google Sheets to find or create row. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
