# Compare Purchases by Fit and Total Cost — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Compare purchases against the user’s actual use case and hard constraints before optimizing price. Separate must-have features, preferences, compatibility and unknown specifications. Keep exact product variants and evidence dates, because a similar name or old review may describe a different item.

Compute complete comparable costs over a stated horizon: price, shipping, mandatory fees, subscriptions and necessary accessories where relevant. Refundable deposits affect cash required now without necessarily being economic cost. Unknown mandatory charges make a total incomplete, not zero. A low price is not a recommendation if the product does not fit the task.

## Output contract

Deliver a small comparison table with fit decisions, supported specifications, complete or incomplete totals, cash requirements and meaningful tradeoffs. State the observation date and source for real prices. Do not place an order, endorse a counterfeit, or promise a return or warranty term that was not verified.

## Choose the right action

### A product fails a stated must-have requirement.
Exclude it from the eligible shortlist and explain the specific mismatch.

**Avoid:** Do not let a low price override the hard constraint.

### A mandatory cost or specification is unknown.
Mark that comparison incomplete and identify the missing fact.

**Avoid:** Do not substitute zero cost or an assumed feature.

### Different options include subscriptions or accessories.
Normalize the horizon and included components before ranking.

**Avoid:** Do not compare an upfront-only price with a complete multi-period cost.

### A refundable deposit is required.
Show it as cash tied up separately from nonrefundable cost.

**Avoid:** Do not double-count it as permanent expense or hide the liquidity requirement.

### The user chooses an option.
Recheck the exact variant, seller, total and terms before any separately authorized order.

**Avoid:** Do not report a purchase from a recommendation or cart.

## Worked example

**Input:** A meets the offline requirement and costs 100 plus 20 shipping. B meets it but has an unknown mandatory fee; C lacks offline use.

**Method:** Filter by fit and distinguish complete from incomplete totals.

**Result:** A has a complete total of 120. B remains unresolved; C is rejected for fit. B is not declared cheapest by assuming its fee is zero.

## Edge or recovery example 1 (example)

**Input:** B’s fee is later verified as 10 on a price of 90.

**Method:** Update B’s complete total without changing the hard requirement.

**Result:** B has a complete total of 100 and is the lower-cost eligible option. No purchase is claimed.

## Failure diagnosis

### The cheapest option does not solve the user’s problem.
**Likely cause:** Ranking happened before fit filtering.

**Repair:** Apply hard constraints first and rerank the eligible set.

**Recheck:** Every shortlisted option meets the supported must-haves.

### The checkout total exceeds the comparison.
**Likely cause:** A mandatory fee or recurring charge was omitted.

**Repair:** Recompute a complete comparable total with dates and horizon.

**Recheck:** Unknown charges remain explicit until verified.

### A review describes a different variant.
**Likely cause:** Product identity was matched only by a broad name.

**Repair:** Bind evidence to the exact model and configuration.

**Recheck:** The recommendation uses the item actually available.

## Preserve for the next turn

Preserve the exact product variants, source timestamps, hard constraints, cost horizon, nonrefundable totals, refundable cash requirements and actual order state. Resume by refreshing changed prices or missing terms, not by assuming old availability.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `purchase-compare-r4-standard`, `purchase-compare-r4-edge`, `purchase-compare-r4-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
