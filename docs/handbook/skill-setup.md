# Select and use a skill

A skill gives your assistant a method: what to ask for, how to work through the task, and what a useful result should contain.

## Get a first useful result

Choose a skill from the [index](../../collections/muse-starters-v1/SKILL_INDEX.md) or export a task starter from the toolkit with Python 3.12+:

```sh
python -B tools/muse_collection.py show daily-planner
python -B tools/muse_collection.py build daily-planner --to "$HOME/daily-planner.zip"
```

Open `START_HERE.md` and the selected skill instructions, or attach the ZIP to your assistant. Give it your real task and ask it to keep your current preferences and memory.

For example: “I have two fixed appointments, one report, and ninety minutes of flexible time. Use this planning method to propose a realistic day.” Inspect the plan before adding events to a calendar.

## Load only what the task needs

Start with the relevant `SKILL.md`, its required inputs, and any referenced examples. Use the assistant's supported skill-import or instruction-loading route. The toolkit's 75 task skills and its 50 role/shared procedures overlap; choose by purpose rather than loading every method at once.

For a portable instruction library:

```sh
python -B examples/export_portable_skills.py --plan
python -B examples/export_portable_skills.py --to "$HOME/my-portable-skills"
```

The exporter writes standard folders in a new destination. Match the format to your host's supported import route and configure any tools the task requires.

## Check the result

Compare the output with the skill's checklist. Open the file or inspect the target service where appropriate. Keep the useful artifact and record the next step for a longer task.

## Update and recover

Export into a new directory and compare changes with your customized copy. If a connection needs setup, follow the service's guide. When an operation's result is uncertain, inspect its original state before repeating it.

[Skills](../SKILLS.md) · [Task collection](../collection/MUSE_CURATED_COLLECTION.md) · [Tools and connections](source-and-host-capabilities.md)
