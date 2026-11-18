# WoWSQL

**Explore a PostgreSQL project and validate a query**

Inspect the selected PostgreSQL schema, run a focused query, and verify results against the application’s data rules.

**Works well with:** Data Engineering Architect, Software Engineer, Automation Engineer.

## What to bring

- Project and schema
- Question or SQL query
- Expected rows or aggregate

## Setup

1. Select the intended WoWSQL project and define the query’s expected effect.

**Access:** WoWSQL project plan.

## Supported functions

| Function | Use it to |
| --- | --- |
| `get_project` | Read the selected project |
| `list_tables` | Inspect its table structure |
| `execute_sql` | Execute the requested PostgreSQL statement |

## Workflow

1. Read the selected project and table structure.
2. Write a query for the stated question using the actual schema.
3. Run a limited read and inspect row counts, nulls, and duplicate behavior.
4. For a requested data change, review the affected rows and verify the result after execution.

## What you get

- SQL query
- Result table
- Validation notes

## Check the result

- The query targets the selected project and tables.
- Returned rows or totals match the expected data rule.

## Try it

> Use WoWSQL to explore a PostgreSQL project and validate a query. Start from the inputs I provide, follow the setup and workflow, and return sql query, result table, validation notes. Verify: The query targets the selected project and tables. Returned rows or totals match the expected data rule.

## Combine it with

- **Deliver trustworthy data and dashboards:** SQL Copilot, SQL Expert, PlanetScale, Preset API Skills, Formula Genius.

## Learn more

- [wowsql.com](https://wowsql.com/database)
