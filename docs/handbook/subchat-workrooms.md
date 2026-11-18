# Give each subchat a useful workroom

Use Main to keep the goal, decisions, and next steps together. Give the specialist's three subchats focused tasks so each can work with the right context.

## Set up a workroom

1. Start with the subchat guide included in your specialist package.
2. Add the current task, the files it should use, and the result you need.
3. Load the selected skills and tools for that task.
4. Keep a short working note with decisions, unresolved questions, and the next action.

Use the host's supported conversation and document setup. Keep general preferences in your assistant's normal profile; share only the context needed by the subchat.

## Hand work back to Main

Return the result, the files or sources supporting it, and the next decision. For a code change, include what changed and the check that passed. For research, include the sources and uncertainty. For design, include the artifact and the interactions to review.

## Resume after an interruption

Read the latest working note and reopen the relevant files. Check whether any requested external action already completed before continuing. The [resume method](../../collections/muse-starters-v1/skills/resume-without-replay/SKILL.md) helps organize that check.

## Prepare a kit locally

With Python 3.12+ in a toolkit checkout:

```sh
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
```

The kit includes Main documents and three subchat folders with context, tools, and memory documents. Use `INSTALL.md` to apply them to your chosen assistant. Keep the working copy separate from the original package for easier updates.

[Context loading](context-loading.md) · [Skills](skill-setup.md) · [Setup and saved data](../INSTALL_AND_PERSISTENCE.md)
