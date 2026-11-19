# Infrastructure & Reliability Engineer

Turn service measurements into error budgets, capacity estimates and incident timelines you can use to prioritize reliability work.

## Run the exported kit

```sh
python run.py --demo
```

Use Python 3.10 or newer. The kit runs with the Python standard library and returns a JSON report from your supplied inputs.

For your own supplied records:

```sh
python run.py --tool service-objectives --input input.json
```

`EXAMPLE.json` contains the exact input shapes for the demo. Copy the `inputs` object for the chosen tool into `input.json`; the file must contain one object, not the entire example wrapper. Unknown fields and invalid values produce a structured error and exit code 2.

## Run from the source repository

```sh
python tools/muse_collection.py demo reliability-engineer
python tools/muse_collection.py kit reliability-engineer --to ./reliability-engineer.zip
```

The ZIP destination is create-only; use a new name rather than overwriting an existing file.

## Included capabilities

- **Calculate an Event-Based Reliability Budget**: `service-objectives`.
- **Size Capacity With Explicit Utilization and Reserve**: `capacity-planning`.
- **Reconstruct One Incident From Dated Evidence**: `incident-triage`.

## Use with an assistant

Read `PLAYBOOK.md` and the skill documents for your task. Ask Muse to inspect your supplied records, run the relevant tool, explain the result and plan the next action. Keep your assistant's existing identity, memory and working preferences.

## Use the results

Use the error budget to choose reliability priorities, the capacity estimate to review headroom, and the incident timeline to identify recovery delays. Compare those findings with your monitoring data, make the reviewed infrastructure change through your operations tools, and check the service measurements afterward.
