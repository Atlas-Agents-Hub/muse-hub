# Plan and Check a Database Migration

Move a schema forward while preserving application behavior and data integrity.

## Bring these inputs

- Current and target schema
- Critical queries and deployment constraints

## 1. Database Designer

Read [the Database Designer method](../skills/database-designer/SKILL.md). Inspect keys, relationships, constraints, and query patterns in the current and target schemas.

**Carry forward:** A schema change plan and invariants.

**Check:** The target supports the required queries and preserves required relationships.

## 2. Migration Architect

Read [the Migration Architect method](../skills/migration-architect/SKILL.md). Turn the change plan into an expand, backfill, transition, and rollback sequence.

**Carry forward:** A migration runbook with checkpoints and recovery actions.

**Check:** The sequence maintains compatibility during deployment and bounds lock duration.

## 3. PostgreSQL Engineering

Read [the PostgreSQL Engineering method](../skills/postgres-pro/SKILL.md). Exercise the migration and critical queries on representative data.

**Carry forward:** Verified migration results, row reconciliations, and query plans.

**Check:** Rows, constraints, query behavior, and rollback match the declared invariants.

## Check the finished work

- The target supports the required queries and preserves required relationships.
- The sequence maintains compatibility during deployment and bounds lock duration.
- Rows, constraints, query behavior, and rollback match the declared invariants.

## Finish

Verified migration results, row reconciliations, and query plans. Rows, constraints, query behavior, and rollback match the declared invariants.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
