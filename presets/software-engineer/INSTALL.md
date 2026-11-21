# Software Engineer | Muse Hub

Build, debug, refactor and release software. Work from reproduction and architecture decisions through implementation, regression tests, source integrity and reviewed delivery.

**[Download Software Engineer](https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/muse-software-engineer-v1.6.2.zip)** · [v1.6.2 release](https://github.com/Atlas-Agents-Hub/muse-hub/releases/tag/v1.6.2) · [Checksums](https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/SHA256SUMS)

**2517 skills · 16 workflows · 37 tool guides**. [Explore the full selection](LIBRARY.md).

## Set up or update in Muse

Paste this into your Meta Muse Personal AI Assistant. If Muse asks for the ZIP, download it on your phone and attach it to the conversation.

```text
Help me set up or update the Muse Hub specialist in this package. Use the ZIP I attach, or download this release if you can access it:
https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/muse-software-engineer-v1.6.2.zip
Release checksums: https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/SHA256SUMS

Extract the ZIP into a new staging folder. Check the ZIP against the release checksum if you can hash files. Check the package ID (software-engineer) and version (v1.6.2) in MANIFEST.json. If you cannot download or extract the ZIP, ask me to attach it or share the extracted folder. If you detect a mismatch, stop and report it.

Read START_HERE.md. Use the root skills.yaml as the portable inventory, or the skills list in MANIFEST.json for older packs. Use only the skills relevant to my task. The disabled registry in assistant/role-skills/config/skills.yaml is for host methods. Use the subchat mapping in that folder to see which method goes with each subchat.

Show a setup or update plan before making changes:
- Main: map IDENTITY.md, SOUL.md, SYSTEM_PROMPT.md, SYSTEM_INSTRUCTIONS.md, AGENTS.md, MEMORY.md, USER.md, TOOLS.md, and SUBCHATS.md in assistant/system-profile/profile/ to the supported Main instructions, settings, or reference files.
- Subchats: match the three folders under assistant/subchat-scopes/subchats/ to my existing subchats, or propose new ones. Use SUBCHAT.json to identify each scope. Map AGENTS.md, ROLE.md, CONTEXT.md, MEMORY.md, TOOLS.md, PREFERENCES.md, and HEARTBEAT.md where supported. Keep private memory within its original scope.
- For an update, compare with my current setup, keep a private backup of the files you plan to edit, preserve my identity, preferences, memory, credentials, and custom instructions, and show any conflicts for me to resolve.

Wait for me to approve the proposed changes. Apply only what the supported Muse controls allow, then reopen the affected content and tell me what you verified. When a change needs to be done by hand, give me the file to open, what to copy, and where to put it. Finish by suggesting the first task in FIRST_TASK.md.
```

## Set up by hand

Extract the ZIP into a new folder and open `START_HERE.md`. Choose a **separate Muse assistant**, add the Main instructions, and set up its **three subchats** with their included documents.

**First task to try:** Bring a failing test or bug report. Reproduce the problem, make a focused repair, and run a regression check.

Use `PROFILE.md` to choose a method and `CONNECTORS.md` to select the account and permissions for a service. Follow `START_HERE.md` for optional local tools.

[All specialists](../../docs/DOWNLOAD_A_SPECIALIST.md) · [Setup and saved data](../../docs/INSTALL_AND_PERSISTENCE.md) · [Terminal guide](../../docs/TERMINAL.md)
