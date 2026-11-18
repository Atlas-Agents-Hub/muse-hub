# Make the right context available

Give your assistant the brief, files, and constraints it needs for the current task. Start with a short source list and add detail as the work requires it.

## First useful result

Save this sample brief in your workspace or attach it to a conversation:

```text
Project: North Window
Goal: turn three rough notes into an outline.
Constraint: keep the original uncertainty; do not send or publish anything.
Source marker: context-demo-v1
Notes: prototype exists; testing is incomplete; next review is unscheduled.
```

Ask: **Read this brief and produce a three-part outline. Include the source marker, keep the uncertainty in the notes, and suggest the next review step.**

The result should use the supplied notes, retain the incomplete testing, and identify the unscheduled review as a next step.

## Choose a manageable context packet

For repeated work, include the current goal, source names/versions, important constraints, selected methods, existing output location, unresolved questions and one next action. Point to large references rather than copying them into every message. Use a short index to show which source answers each question.

Keep task context separate from your lasting preferences. An experiment's temporary output format should not become a permanent personality rule. If the assistant has a supported read tool, ask it to read the exact reference it needs. Otherwise, supply the relevant material through a supported attachment or paste route. Follow the host's documented file and attachment controls.

## Verify

Compare the output with the supplied brief. Ask for a short paraphrase and a location in the source, then check whether that passage supports the conclusion. Use the host's activity records when you need to confirm which documents were read.

To start with existing source guidance, read [Scope a Useful Next Result](../../collections/muse-starters-v1/skills/scope-and-route/SKILL.md) and [Keep Sources and Changes Traceable](../../collections/muse-starters-v1/skills/source-and-custody/SKILL.md). Choose the methods relevant to the current task.

## Failure and recovery

If the answer misses the brief, first check the exact attachment, path and version. Then narrow the request and explicitly supply the missing section. If the assistant cannot access a file, it should say which source is unavailable and continue any useful work supported by the supplied text. Use the host's supported attachment or instruction-loading route to make the material available.

Before changing a long-running workflow, preserve the previous packet and output. Reopen the selected source after an edit and compare the relevant lines. Repeat the check in each conversation or scheduled workflow that depends on the changed source.

## Continue

Keep the current task and its essential sources easy to reopen. For durable state, continue with [Documents that remain recoverable](durable-documents.md).
