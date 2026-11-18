# Review a Software Supply Chain

Connect dependency, license, and security evidence to release decisions.

## Bring these inputs

- Dependency manifests and lockfiles
- Distribution requirements and release candidate

## 1. Dependency Auditor

Read [the Dependency Auditor method](../skills/dependency-auditor/SKILL.md). Inventory direct and transitive dependencies from the actual lockfiles.

**Carry forward:** A versioned dependency inventory with risk findings.

**Check:** The inventory reflects the built application rather than uninstalled candidates.

## 2. License Auditor

Read [the License Auditor method](../skills/license-auditor/SKILL.md). Inspect the relevant licenses and redistribution obligations.

**Carry forward:** A license inventory and required notice set.

**Check:** Every distributed component has a reviewed license and the necessary notices.

## 3. Adversarial Reviewer

Read [the Adversarial Reviewer method](../skills/adversarial-reviewer/SKILL.md). Review unresolved findings against the planned release behavior.

**Carry forward:** A prioritized remediation list and release recommendation.

**Check:** Critical findings have a concrete fix or a documented release decision with an owner.

## Check the finished work

- The inventory reflects the built application rather than uninstalled candidates.
- Every distributed component has a reviewed license and the necessary notices.
- Critical findings have a concrete fix or a documented release decision with an owner.

## Finish

A prioritized remediation list and release recommendation. Critical findings have a concrete fix or a documented release decision with an owner.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
