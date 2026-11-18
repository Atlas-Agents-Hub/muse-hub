# Reconcile a Data Pipeline Before Delivery

Review schema evolution, reconcile a versioned batch and inspect a supplied query plan without modifying a production database.

1. **Review a Schema Change Before Migration** — load `skills/schema-evolution/SKILL.md`, then carry the previous step's output forward.
2. **Reconcile Versioned Events Without Resurrection** — load `skills/incremental-pipeline/SKILL.md`, then carry the previous step's output forward.
3. **Read a Query Plan Before Changing Indexes** — load `skills/query-plan-review/SKILL.md`, then carry the previous step's output forward.
4. **Test Data Transformations Against Explicit Invariants** — load `skills/data-quality-review/SKILL.md`, then carry the previous step's output forward.

## Finish
Return the schema decision, reconciled candidate state, conflict ledger and query-plan evidence; retain production transaction and retention obligations.

## Included local tools

Run the included examples from the extracted package folder:

```sh
python -B tools/run.py --demo
```

For your own JSON input: `python -B tools/run.py --tool SKILL_ID --input input.json`. Python 3.10 or newer is required for these optional tools.

- `schema-evolution`: carry its returned JSON into the next relevant step.
- `incremental-pipeline`: carry its returned JSON into the next relevant step.
- `query-plan-review`: carry its returned JSON into the next relevant step.

## Input artifacts
- Current/proposed schema
- Prior state and source event batch
- Original query plan

## Output artifacts
- Schema report
- Candidate state
- Query-plan review
