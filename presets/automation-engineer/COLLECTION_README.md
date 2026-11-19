# Automation Engineer

Turn a repeated task into a clear workflow, choose controls from observed application state, and recover interrupted actions without duplicating work.

## Run the exported kit

```sh
python run.py --demo
```

Use Python 3.10 or newer. The kit runs with the Python standard library and returns a JSON report from your supplied inputs.

For your own supplied records:

```sh
python run.py --tool automation-contract --input input.json
```

`EXAMPLE.json` contains the exact input shapes for the demo. Copy the `inputs` object for the chosen tool into `input.json`; the file must contain one object, not the entire example wrapper. Unknown fields and invalid values produce a structured error and exit code 2.

## Run from the source repository

```sh
python tools/muse_collection.py demo automation-engineer
python tools/muse_collection.py kit automation-engineer --to ./automation-engineer.zip
```

The ZIP destination is create-only; use a new name rather than overwriting an existing file.

## Included capabilities

- **Review a Bounded Automation Plan Before Execution**: `automation-contract`.
- **Choose a Locator From Actual Target Observations**: `selector-resilience`.
- **Reconcile an Uncertain Operation Without Replaying It**: `effect-reconciliation`.

## Use with an assistant

Read `PLAYBOOK.md` and the skill documents for your task. Ask Muse to inspect your supplied records, run the relevant tool, explain the result and plan the next action. Keep your assistant's existing identity, memory and working preferences.

## Use the results

Use the dependency report to order the work, the locator review to select the intended control, and the reconciliation result to decide whether an interrupted action needs a status check or a retry. Carry the reviewed plan into your connected service, confirm its target account and permissions, and save the operation result with the plan.
