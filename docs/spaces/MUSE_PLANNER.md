# Muse Planner: projects, routines and your next action

Turn a loose idea into a project you can move forward. Muse Planner brings your inbox, projects, daily routines, weekly review, reference notes and calendar into one Muse Space with persistent SQLite storage.

**[Download Muse Planner](https://github.com/Atlas-Agents-Hub/muse-ai-agent-presets/releases/download/v1.6.0/muse-space-planner-v1.6.0.zip)** · [v1.6.0 release](https://github.com/Atlas-Agents-Hub/muse-ai-agent-presets/releases/tag/v1.6.0) · [Complete setup guide](../../examples/gtd_space/README.md)

The same complete app is included in the [Coordinator](../../presets/coordinator/INSTALL.md) and [Personal Companion](../../presets/personal-companion/INSTALL.md) downloads. In any of those ZIPs, open `spaces/planner/README.md`.

## Make a useful workspace

| View | What you can do |
| --- | --- |
| Today | Choose your next actions, priorities and scheduled work. |
| Inbox | Capture ideas, then clarify and route them into the right project. |
| Projects | Define an outcome and keep its next actions together. |
| Future | Build daily and weekly routines, reminders and scheduled items. |
| Week | View connected calendars and reserve focus blocks. |
| Someday and Reference | Keep future ideas, notes and useful links easy to find. |
| Done | Review completed work and reopen an item when you need it. |

## Create your Space

1. Extract the download into a new folder and give Muse the complete `spaces/planner/` app folder.
2. Ask Muse to create a **TypeScript Space** named **Muse Planner**. Follow the app's README to prepare the Muse host's SDK and install the locked dependencies with Bun.
3. Apply the included SQL migrations in journal order and build through Muse's Space builder.
4. Capture an inbox item, create a project with a next action, and add a daily routine. Reopen the Space to continue from the saved workspace.
5. Choose **Export** to keep a portable JSON backup.

The [app guide](../../examples/gtd_space/README.md) includes the exact commands, local preview, calendar settings, backup and restore. Start with your projects and routines; add the calendars you want when you are ready.

## Plan with your specialist

Ask **Coordinator** to turn a project outcome into next actions, dependencies and a weekly plan. Ask **Personal Companion** to shape routines and reminders around your priorities. Copy an item's reference into the conversation so your assistant can discuss the same work.

> Set up my current projects in Muse Planner. Help me capture loose tasks, define each project's outcome, choose a small next action and create a weekly review routine.

Use **Export** before an update or move. **Import** validates a backup and asks you to confirm replacing the current workspace, then restores it as one transaction.

[All workspaces](../README.md#open-a-workspace) · [Setup and saved data](../INSTALL_AND_PERSISTENCE.md) · [Specialist library](../collection/SPECIALIST_LIBRARY.md)
