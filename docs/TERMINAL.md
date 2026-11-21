# Use Muse Hub from your terminal

Build a specialist kit, search the skill library, or run a local Muse Hub tool. For conversations and assistant setup, [open the Muse Personal AI Assistant](https://muse.ai/). For Meta’s terminal coding agent, see the [official Muse Code guide](https://dev.meta.ai/docs/muse-code).

## Run Muse Hub tools

Use Python 3.12+ for the repository tools. Git is needed to clone the project and for workflows that work on repositories. Commands below work in PowerShell, macOS Terminal, and Linux shells; use `python3` if that is your Python command.

```sh
git clone https://github.com/Atlas-Agents-Hub/muse-hub.git
cd muse-hub
python -B quickstart.py --all
```

The check prepares and inspects temporary packages for all 15 assistants and their 45 subchats. To keep an editable kit, choose a new absolute destination:

```sh
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
```

### Choose a starter or run a tool

Search across skills, workflows, starters, specialists, connectors and tool guides, then create a pack for your project:

```sh
python -B tools/discover.py search "sql query" --role data-engineering-architect
python -B tools/discover.py plan --skill query-plan-review --workflow pipeline-validation
python -B tools/discover.py build --skill query-plan-review --workflow pipeline-validation --to "$HOME/my-data-toolkit.zip"
```

The [finder and custom toolkit guide](collection/FIND_AND_BUILD.md) covers filters, specialist selection, supporting files and reusable exports.

```sh
python -B tools/muse_collection.py show daily-planner
python -B tools/muse_collection.py build daily-planner --to "$HOME/daily-planner.zip"
python -B tools/muse_collection.py demo data-engineer
python -B tools/muse_collection.py workflow-demo pipeline-validation
```

The starter command creates a ZIP for your assistant. The data and workflow examples print reports from the supplied sample inputs. For your own inputs and portable executable kits, follow the [specialist tool guide](collection/SPECIALIST_QUICKSTART.md).

### Open your notebook

Choose an absolute database path in an existing private directory, then run:

```sh
python -B examples/space_starter.py --serve --companion-home --database "$HOME/companion-notes.sqlite3"
```

Open the local URL printed by the command and enter its session token in Notebook. Keep the terminal running while you work. Press Ctrl+C to stop it; restarting with the same database reopens your notes. [Companion Home](COMPANION_HOME.md) covers rooms, conflicts, and recovery.

## Troubleshooting

| Problem | Next step |
| --- | --- |
| A toolkit command cannot find a file | Run it from the repository root. |
| `ModuleNotFoundError` in a lower-level example | Follow that example's `PYTHONPATH` instructions in [Workflows](WORKFLOWS.md). |
| An export destination exists | Choose a new path and keep your existing work. |
| The local notebook will not open | Use the URL from the current terminal session on the same computer. |

[Get started](GETTING_STARTED.md) · [Assistant downloads](DOWNLOAD_A_SPECIALIST.md) · [Developer quickstart](GITHUB_QUICKSTART.md)
