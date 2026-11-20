# Product & Interface Designer

Specify coherent interface states and measure real design-token contrast before handing off implementation and rendered-product review.

## Run the exported kit

```sh
python run.py --demo
```

Use Python 3.10 or newer. The kit runs with the Python standard library and returns a JSON report from your supplied inputs.

For your own supplied records:

```sh
python run.py --tool design-token-audit --input input.json
```

`EXAMPLE.json` contains the exact input shapes for the demo. Copy the `inputs` object for the chosen tool into `input.json`; the file must contain one object, not the entire example wrapper. Unknown fields and invalid values produce a structured error and exit code 2.

## Run from the source repository

```sh
python tools/muse_collection.py demo product-interface-designer
python tools/muse_collection.py kit product-interface-designer --to ./product-interface-designer.zip
```

The ZIP destination is create-only; use a new name rather than overwriting an existing file.

## Included capabilities

- **Check Real Color Tokens Before Interface Handoff**: `design-token-audit`.
- **Review Interface States and Recovery Paths**: `interaction-state-coverage`.

## Use with an assistant

Read `PLAYBOOK.md` and the skill documents for your task. Ask Muse to inspect your supplied records, run the relevant tool, explain the result and plan the next action. Keep your assistant's existing identity, memory and working preferences.

## Use the results

Use the contrast results to refine color tokens and the state-coverage report to fill gaps in loading, empty, error and recovery flows. Apply the changes in your design or application, then review the rendered screens with keyboard navigation, zoom and the viewport sizes your users need.
