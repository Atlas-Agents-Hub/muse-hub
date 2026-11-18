# PlanetScale

**Improve a slow query with production evidence**

Use schema, query insights, and workload context to prepare a focused database improvement and verify it safely.

**Works well with:** Data Engineering Architect, Infrastructure Reliability Engineer, Software Engineer.

## What to bring

- Database and branch
- Slow query or error fingerprint
- Application access pattern

## Setup

1. Connect the intended organization, database, and branch with the access needed for the task.

**Access:** PlanetScale database plan.

## Supported functions

| Function | Use it to |
| --- | --- |
| `get_branch_schema` | Read the selected branch schema |
| `get_insights` | Inspect query performance |
| `execute_read_query` | Run a query through the read-only role |
| `list_schema_recommendations` | Inspect proposed schema improvements |

## Workflow

1. Read schema, query insights, and relevant branch metrics.
2. Identify the query shape and application route responsible for the cost.
3. Prepare an index, query, or schema change with a rollback path.
4. Compare query results and query-plan or timing evidence on a representative branch before release.

## What you get

- Query diagnosis
- Reviewed change
- Before-and-after evidence

## Check the result

- Result rows and totals stay equivalent.
- Performance comparisons use the same input and workload conditions.

## Try it

> Use PlanetScale to improve a slow query with production evidence. Start from the inputs I provide, follow the setup and workflow, and return query diagnosis, reviewed change, before-and-after evidence. Verify: Result rows and totals stay equivalent. Performance comparisons use the same input and workload conditions.

## Combine it with

- **Deliver trustworthy data and dashboards:** SQL Copilot, SQL Expert, Preset API Skills, Formula Genius, WoWSQL.

## Learn more

- [planetscale.com](https://planetscale.com)
