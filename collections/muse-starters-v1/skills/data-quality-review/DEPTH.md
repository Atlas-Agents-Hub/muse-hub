# Test Data Transformations Against Explicit Invariants — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

A transformation must preserve declared invariants across source identity, business version, payload and aggregation scope. Arrival time is not necessarily business order. Define what may change and what must remain conserved: row membership, keys, units, totals, null meanings and unaffected partitions. Handle conflicting same-key/same-version payloads explicitly; do not invent an order to make a pipeline succeed.

## Output contract

Deliver the transformation contract, before/after invariant results, exact discrepant keys or partitions, accepted replays, quarantined conflicts and a bounded repair. Distinguish a fixture check from production pipeline guarantees such as exactly-once delivery.

## Choose the right action

### An older event arrives after a newer one.
Use the source-owned business version and retain the newer state.

**Avoid:** Do not roll back state based on arrival order.

### Same key and version have different payloads.
Hold or quarantine the conflict before any write under the stated policy.

**Avoid:** Do not choose a winner by filename, timestamp or arbitrary row order.

### An identical event is replayed.
Treat it as an idempotent repeat under the exact key/version/payload contract.

**Avoid:** Do not create another output record or count it as new activity.

### A refreshed window contains no eligible rows.
Clear stale aggregate values within that authorized window and preserve outside data.

**Avoid:** Do not skip the refresh and leave obsolete totals behind.

### The requested check concerns a local fixture only.
Report the precise invariants exercised and remaining production assumptions.

**Avoid:** Do not claim distributed exactly-once behavior from a single-process example.

## Worked example

**Input:** Key A has version 2 payload20; a late version 1 payload10 arrives, then an identical version 2 payload20 replay.

**Method:** Order by source version and compare same-version payload identity.

**Result:** Final A remains version 2 with payload 20; the older event is ignored and the identical replay adds no record.

## Edge or recovery example 1 (example)

**Input:** Another version 2 event carries payload 25.

**Method:** Detect a same-key/same-version conflict before applying it.

**Result:** Hold the conflicting batch under the fixture's fail-closed policy and preserve the existing state; do not invent version 3 or choose the latest arrival.

## Failure diagnosis

### A late event restores obsolete data.
**Likely cause:** Ingestion time was used as business version.

**Repair:** Restore source-version ordering and test a late older event.

**Recheck:** The maximum valid business version remains authoritative.

### A conflict disappears after deduplication.
**Likely cause:** Keep-last logic erased a contradictory same-version payload.

**Repair:** Preserve both records and apply the declared quarantine policy.

**Recheck:** No conflicting payload is silently admitted.

### An empty sales day retains yesterday's stale aggregate.
**Likely cause:** The refresh skipped empty outputs.

**Repair:** Replace the complete authorized window, including deletion of stale aggregate rows.

**Recheck:** Inside-window totals reflect current source and outside-window rows are unchanged.

## Preserve for the next turn

Preserve input and output digests, key/version semantics, transformation version, authorized window, conflicts and invariant results. Resume the specific failed boundary without silently changing the source contract.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `data-quality-review-r3-standard`, `data-quality-review-r3-edge`, `data-quality-review-r3-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
