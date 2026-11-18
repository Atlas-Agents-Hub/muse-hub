# Build a Reliable Data Pipeline

Define a repeatable pipeline with measurable data quality and recovery behavior.

## Bring these inputs

- Input schemas and sample records
- Destination model and freshness requirement

## 1. Data Pipeline Engineering

Read [the Data Pipeline Engineering method](../skills/senior-data-engineer/SKILL.md). Design the ingestion and transformation boundaries, keys, and retry behavior.

**Carry forward:** A pipeline specification and representative transformations.

**Check:** Each transformation has an input schema, output schema, and update rule.

## 2. Data Quality Auditor

Read [the Data Quality Auditor method](../skills/data-quality-auditor/SKILL.md). Check source and transformed data against the specification.

**Carry forward:** A quality report covering nulls, uniqueness, types, and reconciliation.

**Check:** Quality failures are tied to specific records and cannot silently pass.

## 3. Spark Engineer

Read [the Spark Engineer method](../skills/spark-engineer/SKILL.md). Implement or tune the distributed stages using the quality checks.

**Carry forward:** A pipeline run with partitioning, resource use, and recovery results.

**Check:** The output reconciles and rerunning a bounded batch preserves the intended data.

## Check the finished work

- Each transformation has an input schema, output schema, and update rule.
- Quality failures are tied to specific records and cannot silently pass.
- The output reconciles and rerunning a bounded batch preserves the intended data.

## Finish

A pipeline run with partitioning, resource use, and recovery results. The output reconciles and rerunning a bounded batch preserves the intended data.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
