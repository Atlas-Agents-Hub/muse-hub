# Personal Companion | Muse Hub

Support daily life with personal planning, routines, accessible interactions and privacy-aware assistance shaped to the owner's preferences.

**[Download Personal Companion](https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/muse-personal-companion-v1.6.2.zip)** · [v1.6.2 release](https://github.com/Atlas-Agents-Hub/muse-hub/releases/tag/v1.6.2) · [Checksums](https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/SHA256SUMS)

**115 skills · 15 workflows · 9 tool guides**. [Explore the full selection](LIBRARY.md).

## Set up or update in Muse

Paste this into your Meta Muse Personal AI Assistant. If Muse asks for the ZIP, download it on your phone and attach it to the conversation.

```text
Help me set up or update the Muse Hub specialist in this package. Use the ZIP I attach, or download this release if you can access it:
https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/muse-personal-companion-v1.6.2.zip
Release checksums: https://github.com/Atlas-Agents-Hub/muse-hub/releases/download/v1.6.2/SHA256SUMS

Extract the ZIP into a new staging folder. Check the ZIP against the release checksum if you can hash files. Check the package ID (personal-companion) and version (v1.6.2) in MANIFEST.json. If you cannot download or extract the ZIP, ask me to attach it or share the extracted folder. If you detect a mismatch, stop and report it.

Read START_HERE.md. Use the root skills.yaml as the portable inventory, or the skills list in MANIFEST.json for older packs. Use only the skills relevant to my task. The disabled registry in assistant/role-skills/config/skills.yaml is for host methods. Use the subchat mapping in that folder to see which method goes with each subchat.

Show a setup or update plan before making changes:
- Main: map IDENTITY.md, SOUL.md, SYSTEM_PROMPT.md, SYSTEM_INSTRUCTIONS.md, AGENTS.md, MEMORY.md, USER.md, TOOLS.md, and SUBCHATS.md in assistant/system-profile/profile/ to the supported Main instructions, settings, or reference files.
- Subchats: match the three folders under assistant/subchat-scopes/subchats/ to my existing subchats, or propose new ones. Use SUBCHAT.json to identify each scope. Map AGENTS.md, ROLE.md, CONTEXT.md, MEMORY.md, TOOLS.md, PREFERENCES.md, and HEARTBEAT.md where supported. Keep private memory within its original scope.
- For an update, compare with my current setup, keep a private backup of the files you plan to edit, preserve my identity, preferences, memory, credentials, and custom instructions, and show any conflicts for me to resolve.

Wait for me to approve the proposed changes. Apply only what the supported Muse controls allow, then reopen the affected content and tell me what you verified. When a change needs to be done by hand, give me the file to open, what to copy, and where to put it. Finish by suggesting the first task in FIRST_TASK.md.
```

## Set up by hand

1. Extract the ZIP into its own folder and open `START_HERE.md`. You can also give Muse the ZIP with your current task.
2. Choose a **separate Muse assistant** for Personal Companion and add the supplied Main instructions.
3. Set up its **three subchats** using their included instructions, context, tools and memory documents.
4. Personalize the assistant's working preferences. Open `PROFILE.md` to choose the methods for your task.
5. Try the first task below, check the result against the method's expected outputs, and save your work.

**First task to try:** Bring today's commitments and unfinished tasks. Make a workable plan, capture your notes and choose the next three actions.

No Python is needed for the assistant instructions. Optional local tools include their commands and requirements in `START_HERE.md`. Use `CONNECTORS.md` for the included service guides and select the account and permissions for each connection you add.

## Use a skill or workflow

Start with [this specialist's library](LIBRARY.md). A skill describes a focused method and includes its reference files. A workflow connects several methods with named inputs, expected results and checks. Load the method that fits the current task; the complete selection remains available in the download.

[Find and build your own pack](../../docs/collection/FIND_AND_BUILD.md) to search this specialist's methods, preview the included files and create a ZIP for your task. Add `--role personal-companion` to the toolkit's search command to focus on this specialist.

Explore the [working methods and included engines](../../docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md). For terminal tools, follow the [terminal guide](../../docs/TERMINAL.md). Keep the original download and your personalized working copy separately when updating.

## Review email with saved preferences

Use the [inbox workspace](../../collections/muse-starters-v1/skills/inbox-triage/INBOX_WORKSPACE.md) to prepare reply preferences, resume from the last completed review and check the action log. The download includes three Python helpers, an example workspace and Inbox Setup for personalizing it.

## Plan in a Muse Space

Your download includes [Muse Planner](../../docs/spaces/MUSE_PLANNER.md), a complete Space for projects, next actions, daily routines, weekly reviews, notes and calendars. Open `spaces/planner/README.md` in the ZIP to create your Space and save your first project.

Role ID: `personal-companion`. Package: `muse-personal-companion-v1.6.2.zip`.

[All specialists](../../docs/DOWNLOAD_A_SPECIALIST.md) · [Setup and saved data](../../docs/INSTALL_AND_PERSISTENCE.md) · [Get started](../../docs/GETTING_STARTED.md)
