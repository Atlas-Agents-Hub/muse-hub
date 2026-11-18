# From Incident Records to a Bounded Recovery Handoff

Reconstruct the incident, calculate its service budget and size a measured capacity hypothesis while preserving original response authority.

1. **Reconstruct One Incident From Dated Evidence** — load `skills/incident-triage/SKILL.md`, then carry the previous step's output forward.
2. **Calculate an Event-Based Reliability Budget** — load `skills/service-objectives/SKILL.md`, then carry the previous step's output forward.
3. **Size Capacity With Explicit Utilization and Reserve** — load `skills/capacity-planning/SKILL.md`, then carry the previous step's output forward.
4. **Resume Work Without Duplicating Effects** — load `skills/resume-without-replay/SKILL.md`, then carry the previous step's output forward.

## Finish
Return the dated incident timeline, event-ratio budget and capacity calculation with hypotheses, observed effects and a precise next authorized action.

## Included local tools

Run the included examples from the extracted package folder:

```sh
python -B tools/run.py --demo
```

For your own JSON input: `python -B tools/run.py --tool SKILL_ID --input input.json`. Python 3.10 or newer is required for these optional tools.

- `incident-triage`: carry its returned JSON into the next relevant step.
- `service-objectives`: carry its returned JSON into the next relevant step.
- `capacity-planning`: carry its returned JSON into the next relevant step.

## Input artifacts
- Incident events
- Eligible service counts
- Measured capacity and demand

## Output artifacts
- Timeline
- Error-budget report
- Capacity estimate
