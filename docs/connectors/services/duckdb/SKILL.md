---
name: duckdb-connector
description: "Run SQL queries on an in-memory DuckDB database."
---

# DuckDB for Muse

Run SQL queries on an in-memory DuckDB database.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **DuckDB**.
2. Configure **No account token for the listed public requests** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/duckdb/src/index.ts).

## Actions

### Create and Query DB

Create DB from data and run query

| Input | What to provide | Required |
| --- | --- | --- |
| `markdown` | Markdown | Optional |
| `tables` | List of tables to create in the database | Yes |
| `query` | Please use $1, $2, etc. for parameterized queries to avoid SQL injection. | Yes |
| `args` | Arguments to be used in the query | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/duckdb/src/lib/actions/create-and-query-db.ts).

## Try it

> Use DuckDB to create and query db. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
