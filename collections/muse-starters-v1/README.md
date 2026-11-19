# Muse Specialist Collection

**15 specialists · 5242 reusable skills · 396 workflows · 558 task starters**

Choose a specialist for your work, apply a focused method with your current assistant, or run an included Python tool. Each package brings together instructions, examples, and a start guide.

## Start with a useful task

1. [Choose an assistant](../../docs/DOWNLOAD_A_SPECIALIST.md), a [task starter](CATALOG.md), or a [skill](SKILL_INDEX.md).
2. Download its ZIP from [Muse Hub](https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html).
3. Extract it into its own folder, open `START_HERE.md`, and give Muse your task and source material.
4. Follow the result checklist and keep the output in your working folder.

Assistant instructions need no Python. The [getting-started guide](../../docs/GETTING_STARTED.md) explains specialist setup, Main, and the three focused subchats.

## What is included

| Component | Use it for |
| --- | --- |
| 15 specialists | Engineering, research, data, creative work, design, planning, and everyday tasks. |
| 5242 skills | A focused procedure with inputs, decisions, examples, and an output checklist. |
| 396 workflows | A sequence of methods with clear inputs, handoffs, and expected results. |
| 558 task starters | A useful selection of methods and context for a specific task. |
| 225 practice cases | Worked exercises for trying the methods and checking recovery from common problems. |
| Python tools | Reproducible calculations, data checks, local records, and package exports. |

## Run a tool or create a package

From the toolkit root with Python 3.12+:

```sh
python -B tools/muse_collection.py demo data-engineer
python -B tools/muse_collection.py show frontend-partner
python -B tools/muse_collection.py build frontend-partner --to "$HOME/frontend-partner.zip"
python -B tools/muse_collection.py kit product-interface-designer --to "$HOME/interface-kit.zip"
```

Use `python3` if that is your Python command. Choose a new export destination and keep the original download separate from your customized copy. [The tool quickstart](../../docs/collection/SPECIALIST_QUICKSTART.md) covers package contents and your own input records.

## Try a workflow

```sh
python -B tools/muse_collection.py workflow-demo pipeline-validation
python -B tools/muse_collection.py workflow-demo incident-recovery
python -B tools/muse_collection.py workflow-demo interface-quality
```

Read the report to see which calculations ran and which handoffs need your next tool or decision. Connect services through their supported account setup when your task needs live data or an external action.

## Keep your work

Preserve your assistant's preferences, memory, and project files. Keep personal data outside the toolkit directory. Updates are easier to compare when you retain the original package and your working copy. [Setup and saved data](../../docs/INSTALL_AND_PERSISTENCE.md) covers backup and recovery.

## Development

[Development](../../docs/DEVELOPMENT.md) explains repository checks and contributions. License notices accompany the relevant skill files. Browse [skills and tools by specialist](../../docs/collection/SPECIALIST_LIBRARY.md) to choose a focused collection.

[All specialists](../../docs/DOWNLOAD_A_SPECIALIST.md) · [Skills](SKILL_INDEX.md) · [Task starters](CATALOG.md) · [Terminal](../../docs/TERMINAL.md)
