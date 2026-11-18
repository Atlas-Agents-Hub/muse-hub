# Customize your assistant

Make a working copy of the specialist package and adapt it to your tasks. Keep the original download for comparison when updating.

## What you can change

- **Name and identity:** choose how the assistant introduces itself and works with you.
- **Methods:** refine the playbook for your projects and expected outputs.
- **Preferences and memory:** keep your own context in the private working copy.
- **Subchats:** give each of the three focused workrooms a current task and useful files.
- **Tools:** add the connectors and local programs the work requires.

## Prepare a separate role copy

From the toolkit root with Python 3.12+:

```sh
python -B quickstart.py --role coordinator --to "$HOME/my-coordinator"
```

Read the generated `INSTALL.md`. The destination must be new, so your existing files and memory are preserved. Use the assistant's supported setup to apply the Main and subchat instructions.

## Choose skills and connections

[Select a skill](SKILLS.md) for the task at hand, or use a starter's selection. Follow the service's [connector guide](connectors/README.md) when the task needs account access. Keep credentials in the supported secure setup flow and keep private conversations and memory out of public repositories.

[Get started](GETTING_STARTED.md) · [Workrooms](handbook/subchat-workrooms.md) · [Updates and saved data](INSTALL_AND_PERSISTENCE.md)
