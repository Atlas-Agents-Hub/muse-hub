# Skills and workflows

Choose a method for your current task. Muse Hub includes **461 skills**, **58 workflows**, and **100 task starters** covering engineering, research, data, design, creative work, and everyday planning.

[Browse every skill](../collections/muse-starters-v1/SKILL_INDEX.md) · [Find skills by specialist](collection/SPECIALIST_LIBRARY.md) · [Tool guides](tools/README.md)

## Choose and use a skill

1. Browse the [skill index](../collections/muse-starters-v1/SKILL_INDEX.md) or pick a [task starter](../collections/muse-starters-v1/CATALOG.md).
2. Read its `SKILL.md` for inputs, steps, and expected output.
3. Give your assistant the selected instructions and your task material.
4. Check the result against the skill's output checklist and keep the useful artifact.

You can ask: “Use this method for my current task. Keep my existing preferences and memory, and use the files I supplied.” The [skill setup guide](handbook/skill-setup.md) covers longer projects and host-specific skill discovery.

## Start with a bundle

Each [specialist package](DOWNLOAD_A_SPECIALIST.md) includes a relevant selection of skills and workflows. For a smaller task, export a starter from the toolkit with Python 3.12+:

```sh
python -B tools/muse_collection.py show daily-planner
python -B tools/muse_collection.py build daily-planner --to "$HOME/daily-planner.zip"
```

Choose a new destination, then open the ZIP's `START_HERE.md`. No Python is needed to use the exported instructions with your assistant.

## Connect steps with a workflow

The [workflow guide](WORKFLOWS.md) covers research checks, engineering repair, planning, and saved-data recovery. Each workflow names the inputs, outputs, and handoffs between steps. Add the tools or service connections needed by the task through your host's supported setup.

## Portable instruction library

The toolkit also provides 50 role and shared procedures. These overlap the task collection and can be exported as standard `SKILL.md` folders:

```sh
python -B examples/export_portable_skills.py --plan
python -B examples/export_portable_skills.py --to "$HOME/my-portable-skills"
python -B examples/export_portable_skills.py --inspect "$HOME/my-portable-skills"
```

The export contains 50 folders with matching names, descriptions, and license information. It creates a new destination and preserves existing work. Use the import or instruction-loading flow supported by your assistant.

Five shared procedures support work across roles: [Evidence Audit](../skills/shared/evidence-audit/SKILL.md), [Safe Resume](../skills/shared/safe-resume/SKILL.md), [Research Verification](../skills/shared/research-verification/SKILL.md), [Consent and Effects](../skills/shared/consent-and-effects/SKILL.md), and [Quality Handoff](../skills/shared/quality-handoff/SKILL.md).

[Specialists by task](handbook/specialists-by-task.md) · [Workflows](WORKFLOWS.md) · [Connectors](connectors/README.md) · [Customize](CUSTOMIZE.md)
