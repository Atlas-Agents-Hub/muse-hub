---
name: service-objectives
description: "A service owner needs a correctly defined event-ratio objective, remaining error budget or burn-rate calculation from supplied measurements."
---

# Calculate an Event-Based Reliability Budget

## Use when
A service owner needs a correctly defined event-ratio objective, remaining error budget or burn-rate calculation from supplied measurements.

## Not for
Installing monitoring, treating zero traffic as perfect availability, or converting an event-ratio SLI into a time-based uptime claim.

## Inputs
- Good and total eligible event counts from the same observed window.
- A decimal reliability target, exact window length and the service-owned eligibility definition.

## Procedure
1. Identify the service, event population, good-event condition and exact observation window.
2. Validate nonnegative integer counts, good not exceeding total, and a finite target strictly between zero and one.
3. Calculate SLI, bad-event allowance, remaining budget and burn with decimal arithmetic.
4. Treat zero eligible events as no traffic with unknown SLI and burn, not a perfect score.
5. Compare the result with the existing service-owned response policy; distinguish an exhausted budget from an authorized incident action.
6. Return a dated report and retain raw count provenance so another reviewer can reproduce the result.

## Deliver
- Return the exact supplied-window SLI, bad-event count, allowed and remaining bad-event budgets, burn rate and no-traffic state. Decimal-string outputs preserve calculation meaning. Include eligibility exclusions, data freshness and target provenance in the human report. No monitor, alert or service setting is created.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Return the exact supplied-window SLI, bad-event count, allowed and remaining bad-event budgets, burn rate and no-traffic state. Decimal-string outputs preserve calculation meaning. Include eligibility exclusions, data freshness and target provenance in the human report. No monitor, alert or service setting is created.

## Example request
A window contains 1000 eligible requests, 998 good, with target 0.999.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

