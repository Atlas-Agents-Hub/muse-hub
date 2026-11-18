# From Product Contract to Verified Handoff

Turn a bounded product request into interface, data and automation contracts that an existing implementation owner can execute.

1. **Review a Bounded Automation Plan Before Execution** — load `skills/automation-contract/SKILL.md`, then carry the previous step's output forward.
2. **Review Interface States and Recovery Paths** — load `skills/interaction-state-coverage/SKILL.md`, then carry the previous step's output forward.
3. **Review a Schema Change Before Migration** — load `skills/schema-evolution/SKILL.md`, then carry the previous step's output forward.
4. **Check a Release Without Confusing Build and Delivery** — load `skills/release-readiness/SKILL.md`, then carry the previous step's output forward.

## Finish
Deliver the inert dependency review, declared state graph, schema-risk report and exact remaining implementation/release checks; never claim deployment.

## Included local tools

Run the included examples from the extracted package folder:

```sh
python -B tools/run.py --demo
```

For your own JSON input: `python -B tools/run.py --tool SKILL_ID --input input.json`. Python 3.10 or newer is required for these optional tools.

- `automation-contract`: carry its returned JSON into the next relevant step.
- `interaction-state-coverage`: carry its returned JSON into the next relevant step.
- `schema-evolution`: carry its returned JSON into the next relevant step.

## Input artifacts
- Approved product scope
- Current interface and data contracts

## Output artifacts
- Step review
- State coverage report
- Schema compatibility report
- Implementation handoff
