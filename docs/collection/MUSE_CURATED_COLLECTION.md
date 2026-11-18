# Specialist collection

Explore **15 specialist packages, 75 skills, 25 workflows, and 100 task starters**. Start with [an assistant download](../DOWNLOAD_A_SPECIALIST.md), a [task starter](../../collections/muse-starters-v1/CATALOG.md), or the [tool quickstart](SPECIALIST_QUICKSTART.md).

## Choose a method for your task

A specialist package brings together the role's instructions and a useful selection of skills, workflows, and examples. A task starter narrows that selection for a specific job. Give your assistant the relevant instructions and your current task while keeping your preferences and memory.

The [skill index](../../collections/muse-starters-v1/SKILL_INDEX.md) covers the full task collection. The toolkit also provides 50 role/shared procedures through the [portable exporter](../SKILLS.md#portable-instruction-library); the two libraries overlap.

## Run and export tools

From the toolkit root with Python 3.12+:

```sh
python -B tools/muse_collection.py check
python -B tools/muse_collection.py specialists
python -B tools/muse_collection.py demo data-engineer
python -B tools/muse_collection.py kit data-engineer --to ./data-engineer.zip
python -B tools/muse_collection.py workflow-demo pipeline-validation
```

The data, reliability, automation, and interface kits include their Python tools, worked inputs, and guides. Export into a new path, extract, and follow the included runner instructions. Each report identifies its outputs and the remaining workflow handoffs.

## Keep your customizations

Keep the original package and your working copy separately. Export a new version before comparing and applying changes. Preserve your task files, preferences, and memory.

## Developer references

The [compatibility map](../../collections/muse-starters-v1/PUBLIC_COMPATIBILITY.json) maps existing procedure IDs and the `data-engineer` and `reliability-engineer` toolkit aliases. `python -B tools/collection_compatibility.py` checks those relationships and preserved source records. The collection's historical evaluation records remain with its engineering data.

[Get started](../GETTING_STARTED.md) · [Skills](../SKILLS.md) · [Workflows](../WORKFLOWS.md) · [Operating handbook](../handbook/README.md)
