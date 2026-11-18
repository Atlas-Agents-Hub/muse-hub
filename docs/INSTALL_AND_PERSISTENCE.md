# Setup and saved data

## Set up a specialist

[Download a specialist](DOWNLOAD_A_SPECIALIST.md), extract it into a new folder, and open `START_HERE.md`. Give Muse the guide or ZIP with your current task. Follow its instructions for one separate Muse assistant, Main, and three focused subchats.

No Python is needed for these instructions. When you add a connector, choose its account and permissions through the service's setup flow. Keep credentials and personal memory in your private workspace.

## Customize your working copy

Start with the supplied identity, role instructions, and first-task prompt. Add your preferences, project context, relevant files, and desired outputs. Use Main for shared goals and decisions, and the subchats for focused work. [Workrooms](handbook/subchat-workrooms.md) explains the handoff between them.

Keep the downloaded package as a reference and make a separate working copy. Store generated reports and personal data outside the application files so an update is easy to compare.

## Prepare a kit from the terminal

From a source checkout with Python 3.12+ on Windows, macOS, or Linux:

```sh
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
```

Use `python3` where appropriate and choose a new absolute destination. The command preserves existing folders by refusing to replace them.

| Folder | What it contains |
| --- | --- |
| `system-profile/profile/` | Identity, instructions, preferences, tools, and memory documents for Main. |
| `subchat-scopes/subchats/` | Three focused subchat guides, each with context, tools, and memory. |
| `role-skills/` | Three role-specific methods and five shared methods. |

Use the generated `INSTALL.md` to apply the documents through your assistant's supported setup route. Enable only the tools you intend to use; the generated skill registry starts disabled until configured.

## Run optional local tools

Follow each package's included command guide. Repository tools use Python 3.12+; engineering workflows also use Git. The [terminal guide](TERMINAL.md) covers personal Muse chat and the local toolkit, while [Workflows](WORKFLOWS.md) lists example inputs and outputs.

Local programs use your operating-system permissions. Run reviewed code in a workspace you control and provide only the files needed for the task.

## Save tasks and notes

[Daily Desk](spaces/DAILY_DESK.md) and [Companion Home](COMPANION_HOME.md) store notes in the SQLite database you choose. Put the database outside the application folder, keep its directory private, and reuse the same path after restarting. Their guides explain session tokens, conflicting edits, backup, and restoration.

SQLite files and exported archives contain readable personal data. Use your normal private storage and backup protections. Locking the browser view clears the current page; deleting application code leaves the database in place.

## Update without losing customization

1. Keep the original download, your working copy, and the new package separately.
2. Compare instructions and settings before bringing in changes.
3. Preserve your identity, preferences, memory, credentials, and task outputs.
4. Reopen the assistant or tool and check a small task after the update.

For generated profiles, `muse_presets.cli inspect --path PATH` reports `LOCAL_MATCH`, `OWNER_CUSTOMIZED`, `REVIEW_REQUIRED`, or `LEGACY_UNVERIFIABLE`. These results help identify changed or missing files; keep your edits when reconciling them.

## Recover or remove a setup

Save the current result and inspect the original target before repeating an interrupted external action. For local servers, stop the terminal process you started with Ctrl+C. Back up the database before moving or removing it. Remove only the package files you chose to install, and manage connected accounts or scheduled jobs through their original service.

[Get started](GETTING_STARTED.md) · [Host setup](HOST_COMPATIBILITY.md) · [Downloads](RELEASES.md)
