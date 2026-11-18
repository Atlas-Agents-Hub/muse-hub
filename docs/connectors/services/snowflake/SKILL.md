---
name: snowflake-connector
description: "Data warehouse built for the cloud"
---

# Snowflake for Muse

Data warehouse built for the cloud

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Snowflake**.
2. Configure **OAuth 2.0 account connection; Provider connection fields; API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://{account}.snowflakecomputing.com/oauth/authorize>
- Token endpoint: <https://{account}.snowflakecomputing.com/oauth/token-request>
- **Account Identifier** (`account`): Account icon (bottom-left) → **View account details** → copy the **Account Identifier**. Examples: `xy12345.us-east-1`, `orgname-accountname`.
- **Default Database** (`database`): Optional. Default database for queries. Find names under **Data → Databases**.
- **Default Warehouse** (`warehouse`): Optional. Default virtual warehouse. Find names under **Admin → Warehouses**.
- **Default Role** (`role`): Optional. Default security role. Find names under **Admin → Users & Roles → Roles**.

Provider scopes: `refresh_token`.

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/index.ts).

## Actions

### Delete Row

Delete one or more rows from a Snowflake table that match a WHERE condition.

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `schema` | Schema | See action definition |
| `table` | Table | See action definition |
| `where_clause` | WHERE Condition | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/delete-row.ts).

### Get Row by ID

Retrieve a single row from a Snowflake table by matching a column value.

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `schema` | Schema | See action definition |
| `table` | Table | See action definition |
| `id_column` | The column to search in (e.g. the primary key or unique identifier column). | Yes |
| `id_value` | The value to look up in the ID column. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/get-row-by-id.ts).

### Get Table Schema

Retrieve the column definitions (name, data type, nullability, default) for a Snowflake table.

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `schema` | Schema | See action definition |
| `table` | Table | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/get-table-schema.ts).

### Insert Row

Insert a row into a table.

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `schema` | Schema | See action definition |
| `table` | Table | See action definition |
| `table_column_values` | Table_Column_Values | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/insert-row.ts).

### List Tables

List all tables in a Snowflake schema.

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `schema` | Schema | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/list-tables.ts).

### Run Query

Execute a SQL query against your Snowflake database and return the results as rows.

| Input | What to provide | Required |
| --- | --- | --- |
| `sqlText` | The SQL statement to execute. Use `:1`, `:2`… or `?` as placeholders for the **Parameters** values below to safely pass dynamic values without SQL injection risk. | Yes |
| `binds` | Values to bind to the placeholders (`:1`, `:2`…, or `?`) in the SQL query. Provide them in the same order they appear in the query. Using parameters is the safe way to pass dynamic values — never concatenate user input directly into the SQL. | Optional |
| `timeout` | Maximum time in milliseconds the query may run before Snowflake cancels it (applied as STATEMENT_TIMEOUT_IN_SECONDS, capped at 540 seconds). Defaults to 30 000 ms (30 seconds). | Optional |
| `application` | An optional label sent to Snowflake to identify this client. Visible in query history under **Monitoring → Query History → Client Application**. Useful for auditing which automation triggered a query. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/run-query.ts).

### Search Rows

Search for rows in a Snowflake table using an optional WHERE condition, ordering, and row limit.

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `schema` | Schema | See action definition |
| `table` | Table | See action definition |
| `where_clause` | Filter Condition | Optional |
| `order_by` | Sort By | Optional |
| `limit` | Maximum number of rows to return (1–10 000). Defaults to 100. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/search-rows.ts).

### Update Row

Update one or more rows in a Snowflake table that match a WHERE condition.

| Input | What to provide | Required |
| --- | --- | --- |
| `database` | Database | See action definition |
| `schema` | Schema | See action definition |
| `table` | Table | See action definition |
| `table_update_values` | Table_Update_Values | See action definition |
| `where_clause` | WHERE Condition | Optional |
| `update_all_rows` | Confirm that an empty WHERE condition should update every row in the table. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/actions/update-row.ts).

## Events and recurring work

- **[New Column](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/triggers/new-column.ts)** — Triggers when a new column is added to the selected table. Checked by polling every few minutes.
- **[New or Updated Row](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/triggers/new-or-updated-row.ts)** — Triggers when a row is inserted or updated in the selected table. Uses an "updated at" timestamp column you choose — any row whose timestamp is newer than the last check will fire the trigger.
- **[New Row](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/snowflake/src/lib/triggers/new-row.ts)** — Triggers when a new row is inserted into the selected table. Uses a timestamp column you choose to detect rows added since the last check.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Snowflake to get row by id. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
