---
name: postgres-connector
description: "The world's most advanced open-source relational database"
---

# Postgres for Muse

The world's most advanced open-source relational database

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Postgres**.
2. Configure **Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **Host** (`host`): The server's hostname or IP address.
- **Port** (`port`): The port the server listens on, usually 5432.
- **User** (`user`): The database user to sign in as.
- **Password** (`password`): ProviderField
- **Database** (`database`): The name of the database to connect to.
- **Enable SSL** (`enable_ssl`): Encrypt the connection. Most hosted databases require it.
- **Verify Server Certificate** (`reject_unauthorized`): Check the server's certificate. Self-signed servers need a CA below.
- **Certificate** (`certificate`): The CA certificate (PEM) to trust when verifying the server.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/index.ts).

## Actions

### Delete Row

Deletes one or more rows from a table

| Input | What to provide | Required |
| --- | --- | --- |
| `delete_warning` | Delete_Warning | Optional |
| `table` | Table | See action definition |
| `search_column` | Search_Column | See action definition |
| `search_value` | Rows whose search column equals this value are deleted. | Yes |
| `return_rows` | Return every deleted row. The row count is always returned. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/actions/delete-row.ts).

### Find Rows

Reads rows from a table

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | See action definition |
| `table` | Table | See action definition |
| `condition` | The SQL after WHERE. Leave empty to read every row. | Optional |
| `args` | Values for $1, $2 and so on in the condition, in order. | Optional |
| `columns` | Columns | See action definition |
| `limit` | Maximum rows to return. Clear it to return every matching row. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/actions/find-rows.ts).

### Get Tables

Returns the tables in the database

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/actions/get-tables.ts).

### Insert Multiple Rows

Inserts many rows into a table in a single transaction

| Input | What to provide | Required |
| --- | --- | --- |
| `table` | Table | See action definition |
| `batch` | Rows | Yes |
| `keep_empty_strings` | Insert empty fields as empty strings instead of the column default. | Optional |
| `return_rows` | Return inserted rows with generated ids. Needs SELECT permission too. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/actions/insert-rows.ts).

### Insert Row

Inserts a new row into a table

| Input | What to provide | Required |
| --- | --- | --- |
| `table` | Table | See action definition |
| `values` | Column names mapped to the values to insert. | Yes |
| `return_row` | Return the stored row with generated ids. Needs SELECT permission too. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/actions/insert-row.ts).

### Run Query

Runs a SQL statement on the database

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | Optional |
| `query` | The SQL to run. Write $1, $2 where each value goes. | Yes |
| `args` | Values for $1, $2 and so on in the query, in order. | Optional |
| `query_timeout` | Milliseconds to wait for the query before it fails. | Optional |
| `connection_timeout_ms` | Milliseconds to wait for the connection before it fails. | Optional |
| `application_name` | A name that identifies this step in the server's activity list. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/actions/run-query.ts).

### Update Row

Updates one or more rows in a table

| Input | What to provide | Required |
| --- | --- | --- |
| `table` | Table | See action definition |
| `changes_info` | Changes_Info | Optional |
| `values` | Column names mapped to their new values. | Yes |
| `search_column` | Search_Column | See action definition |
| `search_value` | Rows whose search column equals this value are updated. | Yes |
| `return_rows` | Return every updated row. The row count is always returned. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/actions/update-row.ts).

## Events and recurring work

- **[New Row](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/postgres/src/lib/triggers/new-row.ts)** — Triggers when a new row is added to a table

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Postgres to find rows. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
