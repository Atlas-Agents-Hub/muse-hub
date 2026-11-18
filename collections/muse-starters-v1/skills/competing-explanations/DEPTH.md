# Compare Explanations With Discriminating Evidence — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Use an explanation-by-prediction matrix. Separate an observation from the hypothesis proposed to explain it, and seek evidence whose expected outcome differs across hypotheses. Record background assumptions, measurement reliability and shared causes. Prefer a low-cost, safe discriminating observation before collecting more nondiscriminating confirmation. Do not assign numerical posterior probabilities without a justified model.

## Output contract

Deliver named hypotheses, their distinct predictions, observed supporting and contradicting evidence, unresolved assumptions and the next discriminating check. State eliminated, still plausible and favored as different judgments; do not convert a favored account into certainty.

## Choose the right action

### All hypotheses predict the same proposed measurement.
Choose a different condition, timing or control that yields divergent predictions.

**Avoid:** Do not call repeated agreement a discriminating test.

### A supposedly negative observation was never measured.
Mark it unknown and identify the missing measurement.

**Avoid:** Do not treat absence of recorded evidence as evidence of absence.

### One observation contradicts a hypothesis only under an uncertain assumption.
Expose the assumption and test its relevance before elimination.

**Avoid:** Do not silently treat a disputed prerequisite as established.

### The user needs a decision before uncertainty resolves.
Recommend a reversible action robust across the remaining explanations and state the residual risk.

**Avoid:** Do not invent certainty to make the answer decisive.

### A hypothesis requires intrusive or unsafe testing.
Use passive evidence, supplied records or a safe simulation within the authorized scope.

**Avoid:** Do not extend the investigation into an unapproved target.

## Worked example

**Input:** A job runs slowly. H1 predicts slow behavior on both small and large inputs; H2 predicts only large inputs are slow. Both predict the same log message.

**Method:** A log-message check cannot distinguish H1/H2; compare a small-input control at the same version and resource settings.

**Result:** Choose the small-input timing check. A fast small control contradicts H1 under the stated model but is compatible with H2; the log message alone eliminates neither.

## Edge or recovery example 1 (example)

**Input:** No small-input timing was collected, yet a report says H1 is ruled out.

**Method:** Treat the missing observation as unknown and keep both hypotheses live.

**Result:** Neither hypothesis is eliminated. The next action remains the bounded small-input control, not a claimed diagnosis.

## Failure diagnosis

### The report favors whichever explanation was listed first.
**Likely cause:** Predictions and counterevidence were not compared symmetrically.

**Repair:** Build the same evidence columns for every hypothesis and include a contrary observation.

**Recheck:** Every hypothesis has explicit support, contradiction and unknown entries.

### A repeat measurement adds confidence but separates nothing.
**Likely cause:** The selected test has identical predicted outcomes.

**Repair:** Replace it with a condition where at least two predictions differ.

**Recheck:** The chosen test has an explicit outcome-to-hypothesis distinction.

### The conclusion jumps from plausible to proven.
**Likely cause:** Unmeasured assumptions were hidden.

**Repair:** Downgrade the claim and name the next discriminating observation.

**Recheck:** Certainty does not exceed the inspected evidence and assumptions.

## Preserve for the next turn

Carry the observation version, hypothesis definitions, prediction matrix, actual measurements, assumptions and next authorized discriminating check. Never rewrite a prior prediction after seeing its result.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `competing-explanations-r3-standard`, `competing-explanations-r3-edge`, `competing-explanations-r3-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
