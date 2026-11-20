---
name: baserow-connector
description: "Open-source online database tool, alternative to Airtable"
---

# Baserow for Muse

Open-source online database tool, alternative to Airtable

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Baserow**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Authentication Method** (`authType`): Choose **Database Token** (recommended) for scoped, per-table access compatible with 2FA. Choose **Email & Password** only if you need automatic webhook registration on triggers — 2FA accounts are not supported.
- **API URL** (`apiUrl`): Your Baserow instance URL. Leave the default for Baserow Cloud.
- **Md_Token** (`md_token`): MarkDown
- **Token** (`token`): ProviderField
- **Md_Jwt** (`md_jwt`): MarkDown
- **Email** (`email`): Your Baserow account email. Leave blank when using Database Token.
- **Password** (`password`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/index.ts).

## Actions

### Find Row

Finds a row by matching a field value. Returns the first match.

| Input | What to provide | Required |
| --- | --- | --- |
| `table_id` | Table_Id | See action definition |
| `field_name` | The column to look in. | Yes |
| `field_value` | Returns the first row whose value equals this exactly. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/find-row.ts).

### Find Row

Finds the first row whose field equals a value.

| Input | What to provide | Required |
| --- | --- | --- |
| `table_id` | Table_Id | See action definition |
| `field_name` | Exact name of the field to match on. Resolve with Get Table Fields. | Yes |
| `value` | The value the field must equal. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/find-row-ai.ts).

### Get Row

Gets a single row by its ID from a table.

| Input | What to provide | Required |
| --- | --- | --- |
| `table_id` | Table_Id | See action definition |
| `row_id` | Row_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/get-row.ts).

### Get Row

Gets a single row by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `table_id` | Table_Id | See action definition |
| `row_id` | Row_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/get-row-ai.ts).

### Get Table

Gets a table by its ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `table_id` | Table_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/get-table.ts).

### List Rows

Lists rows from a table with optional search, sorting, and filtering.

| Input | What to provide | Required |
| --- | --- | --- |
| `table_id` | Table_Id | See action definition |
| `page` | Which page of results to return, starting at 1. | Optional |
| `limit` | Rows per page, up to 200. | Optional |
| `search` | Returns rows with this text in any cell. | Optional |
| `order_by` | Column name to sort by. Start it with - to sort in reverse. | Optional |
| `filter_type` | Whether rows must match every filter or just one. | Optional |
| `filter_instructions` | Filter_Instructions | Optional |
| `filters` | One JSON filter per entry. Empty returns all rows. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/list-rows.ts).

### List Tables

Lists the tables the connection can access.

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/list-tables.ts).

### List Views

Lists the views of a table.

| Input | What to provide | Required |
| --- | --- | --- |
| `table_id` | Table_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/actions/list-views.ts).

## Events and recurring work

- **[Any Row Change](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/triggers/row-event.ts)** — Triggers when a row is created, updated or deleted in a table.
- **[Deleted Row](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/triggers/row-deleted.ts)** — Triggers when a row is deleted from a Baserow table.
- **[New Row](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/baserow/src/lib/triggers/row-created.ts)** — Triggers when a new row is created in a Baserow table.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Baserow to find row. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
