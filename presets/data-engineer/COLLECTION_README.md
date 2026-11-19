# Data Engineering & Database Architect

Design safe data contracts, reconcile incremental records and review query access paths with reproducible database tools.

## Run the exported kit

```sh
python run.py --demo
```

Use Python 3.10 or newer. The kit runs with the Python standard library and returns a JSON report from your supplied inputs.

For your own supplied records:

```sh
python run.py --tool schema-evolution --input input.json
```

`EXAMPLE.json` contains the exact input shapes for the demo. Copy the `inputs` object for the chosen tool into `input.json`; the file must contain one object, not the entire example wrapper. Unknown fields and invalid values produce a structured error and exit code 2.

## Run from the source repository

```sh
python tools/muse_collection.py demo data-engineer
python tools/muse_collection.py kit data-engineer --to ./data-engineer.zip
```

The ZIP destination is create-only; use a new name rather than overwriting an existing file.

## Included capabilities

- **Review a Schema Change Before Migration**: `schema-evolution`.
- **Reconcile Versioned Events Without Resurrection**: `incremental-pipeline`.
- **Read a Query Plan Before Changing Indexes**: `query-plan-review`.

## Use with an assistant

Read `PLAYBOOK.md` and the skill documents for your task. Ask Muse to inspect your supplied records, run the relevant tool, explain the result and plan the next action. Keep your assistant's existing identity, memory and working preferences.

## Use the results

Use the schema comparison to prepare a migration, the event reconciliation to identify current records, and the query-plan review to choose the next performance investigation. Apply a reviewed change through your database tools, then compare the resulting schema, records or query plan with the expected result.
