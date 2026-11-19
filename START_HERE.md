# Start with Muse Hub

This toolkit includes all 15 specialists, the skill and workflow collection, and the Python tools.

## Use a specialist with Muse

Open [Getting started](docs/GETTING_STARTED.md), choose a specialist, and give Muse its kit together with your current task. The [download directory](https://atlas-agents-hub.github.io/muse-ai-agent-presets/downloads.html) offers specialist kits, workflow downloads, individual starter skills, and subject packs for the expanded skill library. Every skill has its own searchable entry, guide link, and exact file path inside its download.

## Run the included tools

Open a terminal in this extracted folder. With Python 3.12 or newer, try:

```sh
python -B tools/muse_collection.py demo data-engineer
```

The [terminal guide](docs/TERMINAL.md) covers more commands, Muse chat from the command line, and your local notebook. [The README](README.md) introduces the full collection.

## Find and build your own pack

Search the included catalog for a task:

```sh
python -B tools/discover.py search "sql query"
```

Add a specialist filter such as `--role data-engineering-architect` to narrow the results. Preview selected skills and workflows with `plan`, then use `build` to create a custom ZIP with their supporting files. [Follow the find and build guide](docs/collection/FIND_AND_BUILD.md) for complete commands and examples.

## Check your download

Compare the ZIP's SHA-256 digest with `SHA256SUMS` on the [v1.6.0 release page](https://github.com/Atlas-Agents-Hub/muse-ai-agent-presets/releases/tag/v1.6.0). Keep the extracted toolkit in its own folder so updates preserve your existing work.
