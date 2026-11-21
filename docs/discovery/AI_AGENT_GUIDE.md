# Muse Hub guide for assistants

Help the user explore Muse and choose a useful route into their task. Muse Hub brings together 15 independent assistants, 5242 skills, 396 workflows, 558 task starters, a directory of 273 connectors, Companion Home, persistent notes, Studio, Arcade, and a resource library.

## Recommend a starting point

Start with the user's goal: [organize a day](../journeys/ORGANIZE_YOUR_DAY.md), [build and automate](../journeys/BUILD_AND_AUTOMATE.md), or [create something](../journeys/CREATE_SOMETHING.md). Each journey connects Muse features, included Hub tools, and relevant community projects. Use the original provider's documentation for Muse account features and connected services.

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

The [v1.6.2 release](https://github.com/Atlas-Agents-Hub/muse-hub/releases/tag/v1.6.2) contains the individual assistant packages and [SHA256SUMS](https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/SHA256SUMS). Match the archive's digest to its exact filename before extraction. Package guides contain any additional integrity-check commands.

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
