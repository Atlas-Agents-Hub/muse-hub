# Connect your assistant and tools

Use the setup route supported by the assistant or tool you are working with. Muse Hub provides role instructions, skills, and local programs; your chosen host manages its account, available tools, and service permissions.

## Assistant instructions

Open a specialist's `START_HERE.md` and follow its guide for Main and three subchats. Attach or load the supplied instructions through your host's supported flow. Try the included first task and check that the result uses the context you supplied.

## Personal Muse in the terminal

Use [muse-cli setup](TERMINAL.md#chat-with-your-personal-muse) for personal Muse chat, side chats, and history. The executable is `muse-cli`. Muse Code uses a different command and setup guide, so choose the one that matches your task.

## Connect a service

Find the service in the [connector directory](connectors/README.md), follow its setup guide, and select the intended account and permissions. Start with a small read or harmless example before using it for a larger workflow. Check the result in the original service when the action changes something.

## Diagnose a local host

From the toolkit root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B -m muse_presets.cli host-doctor --host personal-hatch
```

Use `--host muse-code` for that environment. In PowerShell, set `$env:PYTHONPATH = "src"` and use `python`.

This diagnostic lists candidate executables, process names, skill directories, and available package metadata. It reads local configuration. `HOST_UNVERIFIED` or exit code 2 means the inspection could not establish the requested host connection; continue with the actual application's setup and status command. An executable being present is useful inventory, while the host's own status confirms your account connection.

## Inspect a skill configuration

For an existing installation, provide paths from your own setup:

```sh
PYTHONPATH=src python3 -B -m muse_presets.cli skill-binding-doctor   --host personal-hatch   --custom-root /owner-approved/custom-skills   --registry /owner-approved/config/skills.yaml   --skill local_claim_gate
```

The inspector checks the selected descriptor, instructions, entrypoints, and catalog fields. `LOCAL_CATALOG_GAP` identifies a missing local entry. Apply any proposed change through the host's supported configuration flow, then try the skill on a small task.

## Choose the right skill format

The [portable exporter](SKILLS.md#portable-instruction-library) creates 50 standard `SKILL.md` folders. Role packages also include registry descriptors for their supported configuration. Keep your live registry and memory separate from downloaded packages, and follow the format accepted by your host.

[Get started](GETTING_STARTED.md) · [Setup and saved data](INSTALL_AND_PERSISTENCE.md) · [Terminal](TERMINAL.md)
