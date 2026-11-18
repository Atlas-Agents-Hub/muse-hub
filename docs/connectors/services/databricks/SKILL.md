---
name: databricks-connector
description: "Data and AI platform: query and load Unity Catalog tables, upload files to volumes and ask Genie questions."
---

# Databricks for Muse

Data and AI platform: query and load Unity Catalog tables, upload files to volumes and ask Genie questions.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Databricks**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Workspace URL** (`workspaceUrl`): Your Databricks workspace URL, e.g. https://dbc-a1b2c3d4-e5f6.cloud.databricks.com or https://adb-1234567890123456.7.azuredatabricks.net
- **Client ID** (`clientId`): The service principal's client ID (also called application ID), e.g. 6b1d5c2e-0a4f-4c3b-9f1e-2d7a8b9c0d1e.
- **Client Secret** (`clientSecret`): ProviderField

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/index.ts).

## Actions

### Ask Genie

Asks a Genie space a question in plain language and returns the answer and query results.

| Input | What to provide | Required |
| --- | --- | --- |
| `genieSpaceId` | Genie Space Id | See action definition |
| `question` | The question to ask, e.g. "What were the top 5 products by revenue last month?" | Yes |
| `conversationId` | Optional. The Conversation ID from an earlier Ask Genie step, to ask a follow-up question in the same conversation. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/ask-genie.ts).

### Find Rows

Finds rows in a Unity Catalog table where a column matches a value.

| Input | What to provide | Required |
| --- | --- | --- |
| `warehouseId` | Warehouse Id | See action definition |
| `catalogName` | Catalog Name | See action definition |
| `schemaName` | Schema Name | See action definition |
| `tableName` | Table Name | See action definition |
| `columnName` | Column Name | See action definition |
| `filterValue` | The value to match in the filter column, e.g. 1042 or jane@example.com. | Optional |
| `limit` | Maximum number of rows to return (1-10000). Defaults to 100. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/find-rows.ts).

### Insert Multiple Rows

Adds many rows to a Unity Catalog table in one statement.

| Input | What to provide | Required |
| --- | --- | --- |
| `warehouseId` | Warehouse Id | See action definition |
| `catalogName` | Catalog Name | See action definition |
| `schemaName` | Schema Name | See action definition |
| `tableName` | Table Name | See action definition |
| `batch` | Batch | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/insert-rows.ts).

### Insert Row

Adds one row to a Unity Catalog table.

| Input | What to provide | Required |
| --- | --- | --- |
| `warehouseId` | Warehouse Id | See action definition |
| `catalogName` | Catalog Name | See action definition |
| `schemaName` | Schema Name | See action definition |
| `tableName` | Table Name | See action definition |
| `rowFields` | Row Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/insert-row.ts).

### Run SQL Query

Runs any SQL statement on a SQL warehouse and returns the result rows.

| Input | What to provide | Required |
| --- | --- | --- |
| `warehouseId` | Warehouse Id | See action definition |
| `query` | The SQL statement to run. Use fully qualified table names and :name markers for values, e.g. SELECT * FROM main.sales.orders WHERE status = :status LIMIT 100 | Yes |
| `parameters` | Values for the :name markers in the query, e.g. status → shipped. Values are passed as strings; cast in SQL when needed, e.g. CAST(:amount AS DECIMAL(10,2)). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/run-query.ts).

### Update Rows

Updates the rows of a Unity Catalog table where a column matches a value.

| Input | What to provide | Required |
| --- | --- | --- |
| `warehouseId` | Warehouse Id | See action definition |
| `catalogName` | Catalog Name | See action definition |
| `schemaName` | Schema Name | See action definition |
| `tableName` | Table Name | See action definition |
| `columnName` | Column Name | See action definition |
| `matchValue` | The value to look for in the match column, e.g. 1042 or jane@example.com. | Yes |
| `rowFields` | Row Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/update-rows.ts).

### Upload File to Volume

Uploads a file to a Unity Catalog volume and, optionally, loads it into a table with COPY INTO.

| Input | What to provide | Required |
| --- | --- | --- |
| `catalogName` | Catalog Name | See action definition |
| `schemaName` | Schema Name | See action definition |
| `volumeName` | Volume Name | See action definition |
| `file` | The file to upload, e.g. a CSV or JSON file from an FTP, email or HTTP step. | Yes |
| `folder` | Optional folder inside the volume, e.g. imports/orders. It is created if it does not exist. | Optional |
| `tableName` | Table Name | See action definition |
| `warehouseId` | Warehouse Id | See action definition |
| `fileFormat` | How the file is read when it is loaded into the table. | Optional |
| `shouldMergeSchema` | When the file has columns the table does not, add them to the table instead of failing. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/upload-file-to-volume.ts).

### Upsert Row

Updates the row with a matching key, or inserts it if no row matches (MERGE).

| Input | What to provide | Required |
| --- | --- | --- |
| `warehouseId` | Warehouse Id | See action definition |
| `catalogName` | Catalog Name | See action definition |
| `schemaName` | Schema Name | See action definition |
| `tableName` | Table Name | See action definition |
| `columnName` | Column Name | See action definition |
| `rowFields` | Row Fields | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/databricks/src/lib/actions/upsert-row.ts).

## Try it

> Use Databricks to find rows. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
