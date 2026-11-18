---
name: itinerary-plan
description: "A trip or day out needs a practical plan matched to the user’s constraints."
---

# Build a Feasible Itinerary With Contingencies

## Use when
A trip or day out needs a practical plan matched to the user’s constraints.

## Not for
Making purchases or bookings without approval, guessing current restrictions, or treating uncertain conditions as safe.

## Inputs
- Destination, dates and traveler preferences
- Budget, mobility, opening hours and travel constraints

## Procedure
1. Recover origin, destination, dates, travelers, hard constraints and any existing bookings before searching.
2. Normalize supplied times to explicit offsets or verified time-zone rules, retaining local display times and date changes.
3. Check transport, opening and admission windows for the relevant date using current sources where real planning requires them.
4. Build a feasible sequence including transfers, queues, check-in, rest and accessibility needs; do not place activities inside protected buffers.
5. Compare total cost and cancellation conditions on the same basis, distinguishing estimates from confirmed availability.
6. Deliver the plan with one practical fallback and keep booking, payment, hold and cancellation actions unperformed unless actually authorized and verified.

## Deliver
- A realistic itinerary
- A contingency and verification checklist
- Deliver a sequenced itinerary with explicit dates/time zones, travel and buffer intervals, costs and assumptions, mandatory versus optional stops, contingency and booking status. Use current official sources for live schedules, entry rules or availability; fictional fixtures must remain labeled fictional.

## Check the result
- Transit time and opening hours are compatible.
- Accessibility assumptions are explicit.
- No reservation is claimed without a booking result.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Preserve exact dates, offsets, source observation times, travel and buffer assumptions, hard constraints and original booking references. Resume the unverified leg or provider readback without duplicating reservations.

## Example request
Plan a low-walking two-day city visit with one indoor alternative each day and no bookings.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

