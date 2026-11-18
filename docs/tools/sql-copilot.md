# SQL Copilot

**Fix a query with a small example dataset**

Debug joins, nulls, dates, duplicate rows, and aggregates using explicit expected results before optimizing the query.

**Works well with:** Data Engineering Architect, Software Engineer, Adversarial Verifier.

## What to bring

- Query and schema
- Example rows
- Expected result table

## Setup

1. Provide the SQL dialect, schema, failing query, and a small representative dataset.

**Access:** Local tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `join-cardinality` | Check whether joins multiply or drop rows |
| `null-and-time-semantics` | Review null, date, and time behavior |
| `test-sql-logic` | Compare query behavior with explicit fixtures |

## Workflow

1. Translate the request into explicit row-selection and aggregation rules.
2. Build a small dataset with duplicates, nulls, and relevant time boundaries.
3. Inspect join cardinality and intermediate row counts.
4. Correct the query and compare exact results with the expected table.

## What you get

- Corrected query
- Representative SQL fixture
- Result comparison

## Check the result

- The query returns the expected rows and totals.
- Duplicate and null cases behave intentionally.

## Try it

> Use SQL Copilot to fix a query with a small example dataset. Start from the inputs I provide, follow the setup and workflow, and return corrected query, representative sql fixture, result comparison. Verify: The query returns the expected rows and totals. Duplicate and null cases behave intentionally.

## Combine it with

- **Deliver trustworthy data and dashboards:** SQL Expert, PlanetScale, Preset API Skills, Formula Genius, WoWSQL.

## Learn more

- [tekrislabs.com](https://tekrislabs.com/)
