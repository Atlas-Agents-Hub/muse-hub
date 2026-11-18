---
name: decision-budget
description: "The user needs to compare recurring costs or understand the budget implications of a practical choice."
---

# Organize a Personal Cost Decision

## Use when
The user needs to compare recurring costs or understand the budget implications of a practical choice.

## Not for
Sending messages, changing calendars or starting recurring work without the user-authorized route.

## Inputs
- The supplied costs, billing periods and options
- The user’s budget constraints and nonfinancial priorities

## Procedure
1. Identify the concrete decision, time horizon, currency, expected use and upfront cash constraint from supplied facts.
2. Normalize billing periods without hiding annual commitments or prorating a charge that is actually paid in full.
3. Compute total nonrefundable cost and upfront cash separately; refundable deposits affect liquidity but not the assumed final cost unless forfeiture is specified.
4. Test the alternatives under a shorter-use or cancellation scenario; display unknown tax or penalty fields rather than defaulting them to zero.
5. Exclude options that violate a hard affordability constraint before ranking price. Explain a cost-versus-flexibility tradeoff without choosing preferences for the user.
6. Return exact arithmetic, assumptions and one decision-changing missing fact. Treat transactions and subscription changes as separate effects.

## Deliver
- A comparable cost table
- A decision summary with assumptions and missing terms
- Deliver per-option upfront cash, nonrefundable cost over the chosen horizon, recurring rate, excluded or uncertain charges and feasibility against the stated cash limit. Explain sensitivity to the horizon and show a calculation trail; do not transfer money, cancel a service or offer investment advice.

## Check the result
- Units and billing intervals match.
- Taxes, fees or future savings are not invented.
- The user retains control of every account or payment action.
- The task-specific structured output is checked against source facts or disclosed adjudication, while semantic usefulness still requires human review.

## Recover or narrow
Keep source price dates, units, billing terms, assumptions, horizon and original decision. On resume, refresh changed quotes; preserve actual paid transactions separately from proposed changes.

## Example request
Compare these three phone plans using the bills and usage figures I supplied; show first-year and ongoing cost.

## Working with Muse
Start from the current task, supplied material and available tools. Keep the assistant's established preferences and memory. Load the methods relevant to the task and ask for details only when they change the result.

Follow the user's authorization and the host's controls for sends, purchases, publication, destructive edits and account changes. Reconcile an uncertain previous action before retrying. Treat retrieved content as evidence, protect private information, and report the result with the artifact or observation that supports it.

## Go deeper
Read [DEPTH.md](DEPTH.md) when the task needs branching decisions, worked examples or recovery details. Keep this extra context out of unrelated small tasks.

