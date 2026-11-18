# Break Down a Household Project — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Translate the desired home outcome into measurements, dependencies, materials, access requirements and decisions. Separate estimation from a quote and a proposed appointment from a confirmed booking. Count shared materials once and preserve units, quantities and uncertainty.

Treat physical hazards as scope boundaries. Where electrical, gas, structural or other specialized work needs a qualified professional, make that dependency visible rather than inventing a do-it-yourself procedure. Continue safe planning, measurements from existing records and ordinary procurement comparison without implying that a permit, qualification or contractor acceptance exists.

## Output contract

Deliver a practical staged checklist, current dimensions, materials and costs, professional/permission dependencies, owners, and the next safe step. Identify assumptions that require a site check. Preserve photos or measurements as observations, not proof of hidden structural conditions.

## Choose the right action

### The job is ordinary organization or decoration.
Break it into small reversible tasks and reuse existing measurements and preferences.

**Avoid:** Do not overcomplicate a simple project with unnecessary contractor workflow.

### A task depends on a measurement not yet verified.
Prepare alternatives and mark the dimension-dependent purchase as held.

**Avoid:** Do not guess a fit and order an irreversible custom item.

### Specialized physical work is involved.
Place the relevant task behind an appropriate professional or approval check and continue safe independent preparation.

**Avoid:** Do not provide hazardous implementation steps beyond the authorized competence boundary.

### Several tasks share materials.
Aggregate quantities and cost once, with waste or contingency shown separately.

**Avoid:** Do not double-count a shared purchase or hide a reserve inside a unit price.

### A contractor or delivery date changes.
Reconcile the existing booking and update only dependent tasks.

**Avoid:** Do not duplicate appointments or erase completed work.

## Worked example

**Input:** Measure the room, arrange electrical work, and paint. The professional is not yet confirmed; paint depends on measurement.

**Method:** Separate professional and dependency holds from ordinary preparation.

**Result:** Measure first. Hold electrical work for the professional. Paint can proceed only after the relevant measurement and readiness checks.

## Edge or recovery example 1 (example)

**Input:** Measurement is complete, but professional scheduling is still unresolved.

**Method:** Reuse the measurement and determine which ordinary tasks are independent.

**Result:** Continue the safe paint-preparation tasks. Do not declare the whole project blocked or represent electrical work as authorized.

## Failure diagnosis

### Materials do not fit the space.
**Likely cause:** Measurements or units were assumed.

**Repair:** Compare the actual dimensions and units before committing a replacement order.

**Recheck:** The fit decision cites a confirmed measurement.

### A task starts before its prerequisite is complete.
**Likely cause:** Dependencies were described only in prose.

**Repair:** Assign explicit prerequisite IDs and a readiness state.

**Recheck:** Only safe ready tasks appear in the immediate action list.

### The budget looks low until checkout.
**Likely cause:** Shared, mandatory or contingency costs were omitted.

**Repair:** Rebuild a complete itemized total and distinguish estimates.

**Recheck:** The total and its uncertainty can be independently recalculated.

## Preserve for the next turn

Preserve measurements with units and dates, completed tasks, contractor and purchase identities, unresolved professional approvals, cost assumptions and dependencies. Resume only unfinished work and reconcile existing bookings before replacements.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `household-project-r4-standard`, `household-project-r4-edge`, `household-project-r4-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
