# Start with a useful result

[Download an assistant](../DOWNLOAD_A_SPECIALIST.md) to use its instructions in Muse, or follow this guide to run the included specialist tools.


## Run a specialist locally

Use a current source checkout and Python 3.12 or newer. These commands work from the repository root in PowerShell, macOS Terminal or a Linux shell; no `PYTHONPATH` setup is required for the collection commands.

```sh
python -B tools/muse_collection.py specialists
python -B tools/muse_collection.py demo data-engineer
python -B tools/muse_collection.py demo reliability-engineer
python -B tools/muse_collection.py demo automation-engineer
python -B tools/muse_collection.py demo product-interface-designer
```

Use `python3` in place of `python` where that is the installed interpreter name.

| Demonstration | What actually runs |
| --- | --- |
| Data engineering | Logical schema comparison, atomic versioned-event reconciliation and supplied SQLite plan classification. |
| Reliability | Event-ratio error budget, decimal capacity sizing and offset-aware incident timing. |
| Automation | Dependency/approval declaration review, locator observation selection and supplied effect-evidence consistency checks. |
| Interface design | Opaque sRGB contrast calculations and deterministic declared-state graph coverage. |

Each demonstration prints a JSON report with the skill, inputs, calculated output, and scope. Start with these worked inputs, then supply your own data using the example below.

## Take an executable kit with you

```sh
python tools/muse_collection.py kit data-engineer --to ./data-engineer.zip
```

Extract the ZIP into a new directory, then run:

```sh
python run.py --demo
```

The extracted kit needs only Python 3.10 or newer; it does not import the source repository. It includes a role contract, playbook, relevant skill guides, worked input records and the actual executable module closure. `MANIFEST.json` verifies package self-consistency before imports; it is not a publisher signature.

For your own schema input, save this as `schema.json` in the extracted kit:

```json
{
  "current": [{"name": "id", "type": "integer", "nullable": false}],
  "proposed": [
    {"name": "id", "type": "integer", "nullable": false},
    {"name": "note", "type": "text", "nullable": true}
  ],
  "row_count": 40
}
```

Then run:

```sh
python run.py --tool schema-evolution --input schema.json
```

The result identifies `note` as added and requires no backfill under this logical contract. Database locks, defaults, indexes, consumer compatibility and an actual migration remain separate questions.

## Use a starter with your existing assistant

Choose from the [starter catalog](../../collections/muse-starters-v1/CATALOG.md), inspect the selection, and export it:

```sh
python tools/muse_collection.py show data-cleaner
python tools/muse_collection.py build data-cleaner --to ./data-cleaner-starter.zip
```

A starter ZIP contains the relevant instructions and practice materials. Give your assistant the selected playbook, skills, and your current task. Keep your existing preferences and memory.

Four starters now select the new toolkits: `data-cleaner`, `operations-analyst`, `customer-support-designer` and `frontend-partner`. Their original base-role IDs remain compatible.

## Try a cross-specialist workflow

```sh
python tools/muse_collection.py workflow-demo pipeline-validation
python tools/muse_collection.py workflow-demo incident-recovery
python tools/muse_collection.py workflow-demo interface-quality
python tools/muse_collection.py workflow-demo automation-readiness
python tools/muse_collection.py workflow-demo product-to-implementation
```

These commands run the registered calculation and review stages. Each report lists completed outputs and remaining handoffs so you can continue with the tools and people needed for your project.

## Save a report without overwriting work

```sh
python tools/muse_collection.py demo reliability-engineer --to ./capacity-and-incident-report.json
```

The parent directory must already exist and the destination must be new. A collision is a refusal, not permission to replace a user's file.

## Build the complete downloadable collection

```sh
python -B examples/export_specialist_collection.py --to ./Muse_Specialist_Collection.zip
```

This builds all 100 starter archives, four executable kits, and nine worked reports. Follow the included start guide after extracting the collection.


## Common problems

**The command cannot find the tool:** run from the repository root or use the absolute path to `tools/muse_collection.py`. Older release assets may not include the new extension commands.

**The JSON input is rejected:** use one input object for the selected tool, not the whole `EXAMPLE.json` wrapper. Keep integer fields as integers and decimal measurement fields as strings. Duplicate keys, nonfinite numbers and unknown fields are refused.

**The kit says a member changed:** compare it with the original export and preserve your edits separately. Do not rewrite the manifest merely to make an unknown package pass.

**You need a connected service:** follow its [connector setup](../connectors/README.md), select the intended account and permissions, and use the report as input to your next step.

Continue with the [15-specialist catalog](SPECIALIST_CATALOG.md), [original role quickstart](../GITHUB_QUICKSTART.md) or [tools and connections guide](../handbook/source-and-host-capabilities.md).
