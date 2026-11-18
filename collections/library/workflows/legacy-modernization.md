# Modernize a Legacy Component

Replace a bounded component while preserving the behavior users rely on.

## Bring these inputs

- Legacy component and observed behavior
- Target stack and compatibility constraints

## 1. Legacy Modernizer

Read [the Legacy Modernizer method](../skills/legacy-modernizer/SKILL.md). Identify the replacement boundary and the behavior that must remain stable.

**Carry forward:** A staged migration plan with compatibility cases.

**Check:** The boundary can be migrated independently and rollback is defined.

## 2. Tdd Guide

Read [the Tdd Guide method](../skills/tdd-guide/SKILL.md). Capture the compatibility cases and implement the replacement incrementally.

**Carry forward:** A replacement with regression tests and a migration adapter.

**Check:** Tests preserve required behavior and expose the intended changes.

## 3. Dependency Auditor

Read [the Dependency Auditor method](../skills/dependency-auditor/SKILL.md). Inspect the replacement dependencies and their compatibility.

**Carry forward:** A dependency report and resolved upgrade or license issues.

**Check:** The final dependency set builds, is supported, and satisfies the project constraints.

## Check the finished work

- The boundary can be migrated independently and rollback is defined.
- Tests preserve required behavior and expose the intended changes.
- The final dependency set builds, is supported, and satisfies the project constraints.

## Finish

A dependency report and resolved upgrade or license issues. The final dependency set builds, is supported, and satisfies the project constraints.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
