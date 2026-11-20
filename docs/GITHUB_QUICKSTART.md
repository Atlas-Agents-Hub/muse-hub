# Muse Hub developer quickstart

Run the specialist tools, create an editable assistant kit, or export instructions for a task. For ready-to-use assistant packages, [download a specialist](DOWNLOAD_A_SPECIALIST.md). For personal Muse chat from your shell, use the [terminal guide](TERMINAL.md).

## Get the toolkit

Use Python 3.12+ and Git. These commands work in Windows PowerShell, macOS Terminal, and Linux; use `python3` when appropriate.

```sh
git clone https://github.com/Atlas-Agents-Hub/muse-hub.git
cd muse-hub
python -B quickstart.py --all
```

The check creates and inspects temporary packages for all 15 roles. The [current release](https://github.com/Atlas-Agents-Hub/muse-hub/releases/latest) also offers downloads with included start guides.

## Create an assistant kit

```sh
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
```

Choose a new absolute output path. Read the generated `INSTALL.md`, customize `system-profile/profile/`, and use the three guides under `subchat-scopes/subchats/` when setting up your assistant. [Setup and saved data](INSTALL_AND_PERSISTENCE.md) explains the folders and updates.

## Run a specialist tool

```sh
python -B tools/muse_collection.py specialists
python -B tools/muse_collection.py demo data-engineer
python -B tools/muse_collection.py demo reliability-engineer
python -B tools/muse_collection.py workflow-demo pipeline-validation
python -B examples/daily_desk.py
```

The data and reliability commands print calculated reports. Daily Desk exercises tasks, notes, reopening, and backup restoration in a temporary database. Follow [specialist tools](collection/SPECIALIST_QUICKSTART.md) to supply your own data, or [Daily Desk](spaces/DAILY_DESK.md) to open its browser interface.

## Export a starter or skill library

```sh
python -B tools/muse_collection.py show daily-planner
python -B tools/muse_collection.py build daily-planner --to "$HOME/daily-planner.zip"
python -B examples/export_portable_skills.py --plan
python -B examples/export_portable_skills.py --to "$HOME/my-portable-skills"
python -B examples/export_portable_skills.py --inspect "$HOME/my-portable-skills"
```

The starter selects methods for one task. The portable library exports 50 role and shared procedures in `SKILL.md` folders. [Skills](SKILLS.md) explains how to choose and use them.

## Lower-level examples

Some examples import the package directly. In macOS/Linux shells use `PYTHONPATH=src python3 -B`; in PowerShell set `$env:PYTHONPATH = "src"` and use `python -B`.

```sh
PYTHONPATH=src python3 -B examples/software_engineer_workflow_demo.py
PYTHONPATH=src python3 -B examples/garden_calendar_demo.py
PYTHONPATH=src python3 -B examples/learning_session_demo.py
```

[Workflows](WORKFLOWS.md) describes the inputs and outputs. Run reviewed code in a workspace you control; repository tools use your operating-system permissions.

## Common issues

| Problem | What to do |
| --- | --- |
| `ModuleNotFoundError` | Use the repository root and the import-path instructions above. |
| Output already exists | Choose a new destination; keep the existing working copy. |
| `PATH_TRAVERSAL_REFUSED` | Use an absolute path without `..`. |
| Checksum mismatch | Download again from the release page and compare the matching checksum. |
| Connector needs an account | Follow that service's [setup guide](connectors/README.md). |

[Terminal](TERMINAL.md) · [Development](DEVELOPMENT.md) · [Security](SECURITY.md)
