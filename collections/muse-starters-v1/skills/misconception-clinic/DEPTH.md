# Repair a Specific Misunderstanding — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Diagnose a specific wrong rule rather than treating every error as ignorance. Distinguish an incorrect concept, a reversed relationship, a missing condition, an arithmetic slip and a vocabulary mismatch. Test the suspected rule with a discriminating counterexample and a new transfer problem, not a repeated explanation.

## Output contract

Deliver the learner's proposed rule, the source-supported correction, a minimal contrast or counterexample, one diagnostic response and a separate transfer check. Record understanding as untested when no fresh response exists.

## Choose the right action

### The final answer is wrong but the reasoning is sound.
Check arithmetic, units or transcription before reteaching the concept.

**Avoid:** Do not diagnose a conceptual misunderstanding from one numeric slip.

### The learner applied a true rule outside its conditions.
Make the condition explicit, then compare one case satisfying it with one that does not.

**Avoid:** Do not replace a qualified rule with another absolute slogan.

### Two terms are being used interchangeably.
Define both in the source's language and ask the learner to classify a new example.

**Avoid:** Do not invent a distinction absent from the actual teaching context.

### A correction is repeated back immediately.
Record coached reproduction and ask a different transfer question before concluding the misconception is repaired.

**Avoid:** Do not equate repetition with independently demonstrated understanding.

### The source itself is ambiguous or contradictory.
Present the competing readings with exact locations and hold the contested grade.

**Avoid:** Do not resolve a course-specific conflict from unsupported memory.

## Worked example

**Input:** The learner says a larger denominator always makes a fraction larger, because 1/8 looks larger than 1/4.

**Method:** Hold the numerator fixed and compare equal wholes split into four versus eight pieces; ask a new 1/3 versus 1/6 comparison.

**Result:** Correction: for positive fractions with equal positive numerator, increasing the denominator reduces the value. The original rule is rejected; transfer remains untested until the new comparison is answered.

## Edge or recovery example 1 (example)

**Input:** The learner instead writes 3/4=0.75 correctly but accidentally copies 0.57 into the answer.

**Method:** Preserve the sound conversion and diagnose transcription, not fraction magnitude.

**Result:** No concept reteaching is needed from this evidence. Correct the copied value and use one new conversion as a check; do not label a global arithmetic deficit.

## Failure diagnosis

### The explanation becomes longer but the same error returns.
**Likely cause:** The intervention never tested the learner's actual wrong rule.

**Repair:** Reduce to a discriminating contrast and ask for the reasoning.

**Recheck:** The next prompt differentiates the original rule from the corrected one.

### The learner receives a correct answer but no actionable correction.
**Likely cause:** Feedback names the result, not the causal mistake.

**Repair:** Identify the exact erroneous step and a minimal fix.

**Recheck:** The learner can locate what changed in the reasoning.

### The record says repaired without a new response.
**Likely cause:** Coached performance was promoted to transfer.

**Repair:** Change the status to transfer untested and preserve the completed explanation.

**Recheck:** Only a fresh independent response can support a transfer observation.

## Preserve for the next turn

Keep the original reasoning, diagnosis alternatives, counterexample, assistance given, source conditions and unanswered transfer item. Do not restart an explanation already understood or silently reclassify a coached response as independent.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `misconception-clinic-r3-standard`, `misconception-clinic-r3-edge`, `misconception-clinic-r3-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
