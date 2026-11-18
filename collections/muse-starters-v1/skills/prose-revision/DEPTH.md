# Revise Prose Without Losing Voice or Meaning — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Editing is a constrained transformation of meaning, voice and structure. Distinguish copyediting, substantive rewriting, shortening, voice adaptation and critique-only requests. Protect exact spans such as quotations, commands, names and agreed terminology. Preserve epistemic strength: may is not does, associated with is not caused by, and a supplied number cannot be silently rounded or replaced to make prose punchier.

## Output contract

Return the complete requested revision or audit, not advice in place of text. Keep protected spans exact, preserve factual scope and audience, and explain only consequential changes. A style detector is advisory; authorship or truth cannot be inferred from a phrase score.

## Choose the right action

### The user requests critique only.
Return findings and proposed edits without replacing the source.

**Avoid:** Do not treat an audit request as permission to rewrite or save changes.

### A shorter sentence would remove a condition.
Retain the condition or choose a different compression elsewhere.

**Avoid:** Do not improve brevity by changing the claim's scope.

### A technical command or quotation is awkwardly punctuated.
Keep its exact protected bytes and edit surrounding prose.

**Avoid:** Do not normalize code or quotes under a prose-only request.

### The user asks for their voice but supplies no usable sample.
Use already confirmed preferences or state a neutral default and proceed when allowed.

**Avoid:** Do not infer personal opinions or stylistic traits from unrelated history.

### A detector flags wording that is intentionally part of the source voice.
Use editorial judgment and retain it when it serves the brief.

**Avoid:** Do not optimize a detector score at the expense of meaning or authenticity.

## Worked example

**Input:** Source: "The pilot may reduce setup time in small teams. Run `make setup --safe` to try it." Request: shorten without changing meaning.

**Method:** Protect the command and retain may plus the small-team condition.

**Result:** Revision: "The pilot may shorten setup for small teams. Try `make setup --safe`." No quantified benefit or causal certainty has been added.

## Edge or recovery example 1 (example)

**Input:** A proposed revision says "The pilot cuts setup time by 40%. Run `make setup`".

**Method:** Compare both factual scope and the literal command.

**Result:** Reject the invented 40% and certainty, restore the small-team condition and the --safe flag. A smoother sentence does not justify either change.

## Failure diagnosis

### The revision invents a percentage improvement.
**Likely cause:** Persuasive wording was mistaken for permission to add facts.

**Repair:** Remove the invented value and restore the supported scope.

**Recheck:** Every number and causal claim traces to the source or separately authorized evidence.

### A protected command no longer works.
**Likely cause:** The editor changed punctuation or spacing inside a literal span.

**Repair:** Restore the original span and compare exact bytes.

**Recheck:** Protected material is unchanged unless explicitly authorized.

### The output is polished but no longer sounds like the author.
**Likely cause:** A generic style template replaced the supplied register.

**Repair:** Restore sentence rhythm and vocabulary supported by the source.

**Recheck:** The revision meets the requested purpose without invented voice traits.

## Preserve for the next turn

Save the source version, edit mode, protected-span list, factual qualifiers and approved output. Resume from the unresolved editorial issue, not a new voice-calibration interview or an overwrite of the original.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `prose-revision-r3-standard`, `prose-revision-r3-edge`, `prose-revision-r3-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
