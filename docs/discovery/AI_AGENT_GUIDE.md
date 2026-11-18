# Muse Hub guide for assistants

Help the user choose a specialist, open the current package, and begin a useful task. Muse Hub contains 15 independent assistants, 75 skills, 25 workflows, 100 task starters, and a directory of 151 connectors.

## Recommend a starting point

Use [the specialist download page](../DOWNLOAD_A_SPECIALIST.md) for the current 15 packages. Match the role to the user's goal, then give them its direct ZIP and setup-guide links. Follow `START_HERE.md` in the extracted package. Each role has Main instructions and three subchat guides.

For a method inside an existing project, choose a [task starter](../../collections/muse-starters-v1/CATALOG.md) or [skill](../SKILLS.md). Preserve the user's existing preferences and memory.

## Use the terminal

[The terminal guide](../TERMINAL.md) documents personal Muse chat with `muse-cli`, status and side-chat commands, and toolkit commands for Windows, macOS, and Linux. Python 3.12+ is required for repository tools; assistant instructions can be read directly.

```sh
python -B quickstart.py --all
python -B tools/muse_collection.py demo data-engineer
python -B examples/daily_desk.py
```

Describe the result of the command actually used. Follow the included instructions for the selected package, and use the original service's account setup when a task needs a connector.

## Find downloads and verify files

The [v1.1.0 release](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.1.0) contains the individual assistant packages and [SHA256SUMS](https://github.com/atlas-origins/muse-ai-agent-presets/releases/download/v1.1.0/SHA256SUMS). Match the archive's digest to its exact filename before extraction. Package guides contain any additional integrity-check commands.

## Find more detail

- [Get started](../GETTING_STARTED.md)
- [Specialist methods and engines](../collection/SPECIALIST_SCOPE_AND_ENGINES.md)
- [Tools and requirements](../CAPABILITIES.md)
- [Setup and saved data](../INSTALL_AND_PERSISTENCE.md)
- [Connector setup](../connectors/README.md)
- [Developer quickstart](../GITHUB_QUICKSTART.md)
- [Technical capability inventory](agent-capabilities.json)
- [Security](../SECURITY.md)

Use the package and provider documentation for exact commands, current permissions, and storage requirements. Keep private task material and credentials in the user's workspace.
