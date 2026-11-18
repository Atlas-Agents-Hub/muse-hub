# Prepare a Clear Appointment Summary — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Organize an appointment around the person’s actual concerns, timeline, current records and questions. Separate observed symptoms or events from interpretation and diagnosis. Preserve dates, duration, relevant context and the source of medication or treatment information without silently resolving conflicting instructions.

A concise preparation summary should help the professional understand priorities, not replace the professional’s judgment. Keep urgent safety concerns ahead of paperwork and direct them to appropriate timely help. Share only the information authorized for the intended recipient. This is a logistics and communication skill, not a diagnostic or prescribing service.

## Output contract

Deliver a brief appointment summary, dated observations, medication or record discrepancies, prioritized questions and practical visit logistics. Mark missing dates and uncertain facts. Do not invent a diagnosis, change treatment or claim that a clinician reviewed the note.

## Choose the right action

### The person provides a clear timeline.
Organize it by actual dates and preserve their descriptions.

**Avoid:** Do not add a plausible onset or symptom that was not reported.

### A date or frequency is missing.
Mark it unknown and ask only when it changes the usefulness of the visit summary.

**Avoid:** Do not turn vague memory into a precise invented history.

### Medication records conflict.
Keep both source versions and flag clarification for the appropriate clinician or pharmacist.

**Avoid:** Do not choose a dose or timing based on which note looks newer.

### An urgent safety concern is reported.
Prioritize appropriate timely human or emergency help rather than finishing the document.

**Avoid:** Do not delay help to complete a checklist or offer an unsupported diagnosis.

### The note will be shared.
Check recipient and sharing scope, then report actual delivery separately.

**Avoid:** Do not claim an appointment occurred or the care team acknowledged the note.

## Worked example

**Input:** One observation is dated Monday, another has no date, and two medication records disagree.

**Method:** Preserve known timing, mark the missing date and keep the medication discrepancy explicit.

**Result:** The appointment note includes both concerns and questions for clarification; it does not choose a treatment instruction.

## Edge or recovery example 1 (example)

**Input:** The person later supplies a date and a clinician-confirmed current record.

**Method:** Update the specific uncertainties using their actual source.

**Result:** The administrative gaps are resolved. The note still does not claim a diagnosis or that the appointment has taken place.

## Failure diagnosis

### The summary is long but the main concern is unclear.
**Likely cause:** All details were treated as equally important.

**Repair:** Lead with the person’s priorities and a short relevant timeline.

**Recheck:** The professional can identify the questions the person wants answered.

### A conflicting instruction disappears in cleanup.
**Likely cause:** Normalization selected one version without authority.

**Repair:** Restore the discrepancy and its sources.

**Recheck:** No treatment change is disguised as administrative editing.

### The note implies clinical certainty.
**Likely cause:** Interpretation was promoted to diagnosis.

**Repair:** Return to the reported observation and the unresolved question.

**Recheck:** The summary does not exceed the evidence or role.

## Preserve for the next turn

Preserve the person’s priorities, actual observation dates, current record versions, unresolved clinical questions, sharing scope and communication state. Resume from confirmed updates without importing private clinical history into generic files.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `appointment-prep-r4-standard`, `appointment-prep-r4-edge`, `appointment-prep-r4-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
