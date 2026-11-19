# Find the right skills and build your own toolkit

Search Muse Hub from your terminal, choose the methods that fit your task, and export a focused ZIP for Muse. The finder searches skills, workflows, task starters, specialists, connectors and tool guides together. Every result includes its guide and the specialists who can use it.

Use Python 3.12 or newer from the extracted toolkit or repository folder. On macOS or Linux, use `python3` if that is your Python command.

## Find a useful starting point

```sh
python -B tools/discover.py search "sql query" --kind skill --role data-engineering-architect --limit 8
python -B tools/discover.py search "study" --role learning-coach --limit 8
python -B tools/discover.py search "calendar" --kind connector --kind workflow
python -B tools/discover.py search "python testing" --match all
```

An exact title or skill identifier appears first. Other matches rank by words in the title, identifier, description and category. `--match all` requires every meaningful query word; the default includes resources matching any query word. Search works with your local catalogs and needs no service account.

| Option | Use it to |
| --- | --- |
| `--kind skill` | Search one resource type. Repeat it to combine types. |
| `--role learning-coach` | Find resources assigned to a specialist. All 15 specialist identifiers are supported. |
| `--category software-engineering` | Choose an exact category; spaces and hyphens are treated alike. |
| `--limit 8` | Choose how many results to show, from 1 to 100. |
| `--offset 20` | Continue through the same ranked results. The finder prints the next offset. |
| `--json` | Return structured results with match reasons, totals and specialist guide paths. |

Find the available specialist identifiers or inspect a particular method:

```sh
python -B tools/discover.py search --kind specialist
python -B tools/discover.py show skill query-plan-review
python -B tools/discover.py show specialist data-engineering-architect
```

The `show` command returns the resource's purpose, guide, example, setup requirements and specialist routes. Use the guide to see the complete method and its supporting files.

## Choose your toolkit

Start with one skill or combine it with a workflow. Preview the complete selection before creating the ZIP:

```sh
python -B tools/discover.py plan --skill query-plan-review --workflow pipeline-validation
```

The preview lists every included skill, the workflows, and the supporting file count. Workflow and starter dependencies are added automatically. For this selection, the toolkit includes the query-plan method, the pipeline's other required skills, the workflow guide, and the local tools used by the pipeline examples.

Use a task starter when you want a prepared first task and expected result:

```sh
python -B tools/discover.py plan --starter daily-planner
python -B tools/discover.py plan --starter daily-planner --skill weekly-reset --json
```

Repeat `--skill`, `--workflow` or `--starter` to combine your choices. `plan --json` returns the exact file list, sizes and checksums so scripts can inspect the package before export. A toolkit can contain up to 64 resolved skills and 160 MB of supporting files; use separate toolkits for larger projects.

## Export and use it with Muse

Choose a new ZIP filename inside an existing folder:

```sh
python -B tools/discover.py build --skill query-plan-review --workflow pipeline-validation --to "$HOME/my-data-toolkit.zip"
```

In PowerShell, `$HOME` points to your user folder as well. You can also supply a full local path. If the filename already exists, choose another name to keep both versions.

The ZIP contains `START_HERE.md`, the selected methods, their scripts and references, workflow resources, starter prompts, and a checksum manifest. Each skill's files stay together in its own folder. Repeating the same selection against the same source produces the same package bytes.

Give Muse the ZIP and a concrete task, such as:

> Read START_HERE.md. Review the supplied query and execution plan, identify the bottleneck, and use the included pipeline checks where they fit. Return the proposed change, the comparison and the resulting report.

Open each included guide for the inputs it needs and the local commands it supplies. Keep working files and outputs in your project folder. After an update, create a new toolkit from the current catalog.

[Specialist library](SPECIALIST_LIBRARY.md) · [Developer quickstart](../GITHUB_QUICKSTART.md) · [Skills](../SKILLS.md) · [All downloads](https://atlas-origins.github.io/muse-ai-agent-presets/downloads.html)
