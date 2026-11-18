# From Tokens and States to Interface QA

Measure supplied color pairs, find missing interaction states and review target observations before actual rendered-interface acceptance.

1. **Check Real Color Tokens Before Interface Handoff** — load `skills/design-token-audit/SKILL.md`, then carry the previous step's output forward.
2. **Review Interface States and Recovery Paths** — load `skills/interaction-state-coverage/SKILL.md`, then carry the previous step's output forward.
3. **Choose a Locator From Actual Target Observations** — load `skills/selector-resilience/SKILL.md`, then carry the previous step's output forward.
4. **Inspect a Real Interface for Access Barriers** — load `skills/accessible-ui/SKILL.md`, then carry the previous step's output forward.

## Finish
Return contrast calculations, graph gaps and eligible locator candidates; report browser, keyboard and visual checks only when they actually ran.

## Included local tools

Run the included examples from the extracted package folder:

```sh
python -B tools/run.py --demo
```

For your own JSON input: `python -B tools/run.py --tool SKILL_ID --input input.json`. Python 3.10 or newer is required for these optional tools.

- `design-token-audit`: carry its returned JSON into the next relevant step.
- `interaction-state-coverage`: carry its returned JSON into the next relevant step.
- `selector-resilience`: carry its returned JSON into the next relevant step.

## Input artifacts
- Color tokens and actual pairs
- Required interaction states
- Locator observations

## Output artifacts
- Contrast report
- State coverage report
- Locator review
