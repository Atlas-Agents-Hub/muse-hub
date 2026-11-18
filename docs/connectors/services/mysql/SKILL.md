---
name: mysql-connector
description: "The world's most popular open-source database"
---

# MySQL for Muse

The world's most popular open-source database

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **MySQL**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Host** (`host`): The server's hostname or IP address.
- **Port** (`port`): The port the server listens on, usually 3306.
- **Username** (`user`): The database user to sign in as.
- **Password** (`password`): ProviderField
- **Database** (`database`): The database to use. Only Run Query works without one.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/index.ts).

## Actions

### Delete Row

Deletes one or more rows from a table

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | Optional |
| `timezone` | Timezone | See action definition |
| `table` | Table | See action definition |
| `search_column` | The column to match rows on. | Yes |
| `search_value` | The value that column must equal. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/lib/actions/delete-row.ts).

### Find Rows

Reads rows from a table

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | See action definition |
| `timezone` | Timezone | See action definition |
| `table` | Table | See action definition |
| `condition` | The SQL after WHERE. Write ? where each value goes. | Yes |
| `args` | Values for each ? in the condition, in order. | Optional |
| `columns` | Leave empty to return every column. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/lib/actions/find-rows.ts).

### Get Tables

Returns a list of tables in the database

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/lib/actions/get-tables.ts).

### Insert Multiple Rows

Inserts many rows into a table in a single transaction

| Input | What to provide | Required |
| --- | --- | --- |
| `timezone` | Timezone | See action definition |
| `table` | Table | See action definition |
| `batch` | Rows | Yes |
| `keep_empty_strings` | Insert empty fields as empty strings instead of the column default. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/lib/actions/insert-rows.ts).

### Insert Row

Inserts a new row into a table

| Input | What to provide | Required |
| --- | --- | --- |
| `timezone` | Timezone | See action definition |
| `table` | Table | See action definition |
| `values` | Column names and the values to store in them. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/lib/actions/insert-row.ts).

### Run Query

Runs a SQL statement on the database and returns its results

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | See action definition |
| `timezone` | Timezone | See action definition |
| `query` | The SQL to run. Write ? where each value goes. | Yes |
| `args` | Values for each ? in the query, in order. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/lib/actions/execute-query.ts).

### Update Row

Updates one or more rows in a table

| Input | What to provide | Required |
| --- | --- | --- |
| `timezone` | Timezone | See action definition |
| `table` | Table | See action definition |
| `search_column` | The column to match rows on. | Yes |
| `search_value` | The value that column must equal. | Yes |
| `changes_info` | Changes_Info | Optional |
| `values` | Columns to change and their new values. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/mysql/src/lib/actions/update-row.ts).

## Try it

> Use MySQL to find rows. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
