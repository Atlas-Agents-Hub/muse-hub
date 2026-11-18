# Prepare an Automation Without Losing Control of Effects

Check a dependency plan, review unique observed targets and reconcile uncertain prior operations before handing off to the existing executor.

1. **Review a Bounded Automation Plan Before Execution** — load `skills/automation-contract/SKILL.md`, then carry the previous step's output forward.
2. **Choose a Locator From Actual Target Observations** — load `skills/selector-resilience/SKILL.md`, then carry the previous step's output forward.
3. **Reconcile an Uncertain Operation Without Replaying It** — load `skills/effect-reconciliation/SKILL.md`, then carry the previous step's output forward.
4. **Review Against the Actual Brief** — load `skills/bounded-review/SKILL.md`, then carry the previous step's output forward.

## Finish
Return a source-bound execution proposal and concrete blockers; do not dispatch, authenticate supplied evidence or authorize retries.

## Included local tools

Run the included examples from the extracted package folder:

```sh
python -B tools/run.py --demo
```

For your own JSON input: `python -B tools/run.py --tool SKILL_ID --input input.json`. Python 3.10 or newer is required for these optional tools.

- `automation-contract`: carry its returned JSON into the next relevant step.
- `selector-resilience`: carry its returned JSON into the next relevant step.
- `effect-reconciliation`: carry its returned JSON into the next relevant step.

## Input artifacts
- Target-scoped step graph
- Current locator observations
- Original operation evidence

## Output artifacts
- Plan review
- Target review
- Effect-reconciliation report
