# Practice and worked examples

The collection includes 75 skills and 225 practice cases. Each skill has a procedure, decision branches, recovery steps, worked examples, and a result checklist. Start with the [skill index](../SKILL_INDEX.md), then read the selected skill's `SKILL.md` and `DEPTH.md` for the task at hand.

## Choose an exercise

| Method | What to practice |
| --- | --- |
| Daily briefing | Build a feasible day, resolve an overloaded plan, and retain travel buffers. |
| Source flashcards | Preserve the source version, units, conditions, and conflicting facts. |
| Code review | Identify a precise defect, explain its effect, and check the proposed repair. |
| Continuity review | Distinguish an unintended state change from an intentional change. |
| Model comparison | Keep the comparison conditions and eligible cases consistent. |
| Resume without replay | Reconcile an interrupted action using its original operation ID. |

Use the parts that help with your current task. A short request should not require a lengthy intake interview. Cases include ordinary use, an edge case, and recovery from a problem; the worked answers explain the expected reasoning.

## Check a practice response

A task-starter package includes its relevant `practice/CASE.json` files, worked answers under `practice/answers/`, and a checker. For example, download the Daily Planner starter, extract it into a new folder, and open a terminal there with Python 3.12+:

```sh
python -B practice/check_outputs.py check --case practice/daily-briefing-standard.json --output your-response.json
```

Create `your-response.json` in the output format described by that case. Read the case before using the worked answer. Exit 0 means the supplied response passed the case's mechanical checks; exit 2 reports a failed check or malformed input. The checker runs locally using the included data.

Then review the actual result: does it solve the task, preserve the supplied facts, explain uncertainty, and give a useful next action? Inspect visual work in its intended application. A structured response passing a fixture is one part of that review.

## Learn from a failed check

Compare the failing field with the case's inputs and requirements. Correct the response, retain the earlier version if useful, and run the same check again. Use the recovery example to understand how to handle missing information, stale evidence, or an interrupted operation in real work.

The exercises use authored example data. Textual continuity observations help practice reasoning about state; apply the method to actual images or video when assessing a production. Maintainer inventories and source history remain in the collection's technical records.

[Task starters](../CATALOG.md) · [Skills](../SKILL_INDEX.md) · [Get started](../../../docs/GETTING_STARTED.md)
