# Review a Schema Change Before Migration — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Separate logical compatibility from operational migration safety. Compare column identity, type and nullability before considering a deployment strategy. A nullable addition can be logically additive while still requiring engine-specific lock and application review. For nonempty tables, a new required value needs an explicit backfill contract. Expand, backfill, validate and contract are separate checkpoints; defaults and indexes are not inferred from column names.

## Output contract

Produce added, removed, retyped and nullability-tightened columns; list required backfills; state the observed row count and the limits of a logical-only review. Include a migration sequence, validation queries to be reviewed by the owner, consumer compatibility notes and a rollback boundary. The tool returns a comparison, not executed DDL.

## Choose the right action

### A nullable column is added without changing existing columns.
Classify the logical contract as additive, then review engine locks and client decoders.

**Avoid:** Do not infer an online migration guarantee from a compatible column diff.

### A required column is added to a populated table.
Require a source-grounded backfill and validation before enforcing the requirement.

**Avoid:** Do not invent a default that changes record meaning.

### A column disappears or changes type.
Treat the change as migration-required and trace all affected consumers.

**Avoid:** Do not interpret a removal as an automatically safe rename.

### The table is observed to contain zero rows.
Omit unnecessary backfill while still reviewing consumer and deployment ordering.

**Avoid:** Do not reuse a stale zero-row observation after writes resume.

### A rollback would discard data written under the new schema.
Preserve those writes and require an explicit forward-repair or reversible transformation.

**Avoid:** Do not offer destructive down-migration as a harmless rollback.

## Worked example

**Input:** A populated customer table has integer id; add nullable text note.

**Method:** Compare identities and nullability, then keep lock and consumer checks separately pending.

**Result:** The logical report lists note as added, requires no backfill, and does not claim a database write.

## Edge or recovery example 1 (example)

**Input:** Replace nullable legacy_code with required integer customer_id on 40 existing rows.

**Method:** Report removal plus required backfill; do not invent a mapping between unrelated identifiers.

**Result:** The result is migration-required with legacy_code removed and customer_id requiring a backfill.

## Failure diagnosis

### Existing records violate the new non-null constraint.
**Likely cause:** The required-column change was applied before a complete backfill.

**Repair:** Reopen the source-pinned backfill plan, account for every affected row and validate on a disposable copy.

**Recheck:** No existing row lacks the required value before the constraint is proposed.

### A previously working client cannot decode the new response.
**Likely cause:** Logical database compatibility was mistaken for client compatibility.

**Repair:** Replay the actual client decoder against the proposed response and retain its failure.

**Recheck:** Old and new consumers behave according to the declared compatibility policy.

### The deployment stalls despite a small logical diff.
**Likely cause:** The review omitted database-version-specific locks or table rewrite behavior.

**Repair:** Inspect the actual engine documentation and measured rehearsal; revise the sequence.

**Recheck:** The operational claim has a measured environment, duration and rollback limit.

## Preserve for the next turn

Preserve the exact supplied input and tool version, the returned report, any unresolved source assumptions and the next authorized check. Produce added, removed, retyped and nullability-tightened columns; list required backfills; state the observed row count and the limits of a logical-only review. Include a migration sequence, validation queries to be reviewed by the owner, consumer compatibility notes and a rollback boundary. The tool returns a comparison, not executed DDL.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `schema-evolution-r5-standard`, `schema-evolution-r5-edge`, `schema-evolution-r5-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
