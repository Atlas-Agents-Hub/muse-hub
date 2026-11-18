---
name: capacity-planning
description: "A measured workload needs a capacity estimate that includes target utilization, unavailable reserve and a reproducible rounding rule."
---

# Size Capacity With Explicit Utilization and Reserve

## Use when
A measured workload needs a capacity estimate that includes target utilization, unavailable reserve and a reproducible rounding rule.

## Not for
Purchasing infrastructure, issuing scale commands, or assuming linear scalability where shared bottlenecks or heterogeneous instances dominate.

## Inputs
- Observed demand and measured sustainable throughput per instance for the same workload.
- Target utilization, current instance count, reserve requirement and evidence for load-distribution assumptions.

## Procedure
1. Verify demand units and that the per-instance measurement represents the same endpoint mix and latency target.
2. Separate serving instances from reserve capacity and confirm whether reserve may carry normal traffic.
3. Multiply sustainable throughput by the chosen utilization target before dividing demand.
4. Round required serving instances upward, then add reserve and compare with current capacity.
5. Check non-linear bottlenecks, failure-domain requirements and measured saturation behavior before proposing changes.
6. Deliver the calculation with assumptions, a load-test plan and an explicit no-scale-action status.

## Deliver
- Return required serving instances, total including reserve, additional instances relative to the current count, effective throughput per instance and currently available throughput after reserve. Record workload identity and assumptions in the handoff. No scale action is performed and the estimate is not a price quote.
- A reproducible JSON report from the named local tool with source assumptions and limits.

## Check the result
- Recompute the decisive result from the supplied records and retain counterexamples.
- Preserve missing evidence, conflicts and unperformed external actions explicitly.
- Separate an executed local calculation from native provider behavior and broad model performance.

## Recover or narrow
Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Return required serving instances, total including reserve, additional instances relative to the current count, effective throughput per instance and currently available throughput after reserve. Record workload identity and assumptions in the handoff. No scale action is performed and the estimate is not a price quote.

## Example request
Demand is 900 requests/second, measured capacity 250, utilization target 0.6, four current instances and one reserve.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

