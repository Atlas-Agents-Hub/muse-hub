# Evaluate an AI System’s Defenses

Test prompt injection and unsafe tool behavior against an explicit threat model.

## Bring these inputs

- Authorized test environment and tool inventory
- Trust boundaries and allowed evaluation cases

## 1. Prompt Injection Defense

Read [the Prompt Injection Defense method](../skills/prompt-injection-defense/SKILL.md). Identify untrusted inputs and the actions they could influence.

**Carry forward:** A trust-boundary map and defense requirements.

**Check:** The map distinguishes user intent, retrieved content, tool results, and privileged actions.

## 2. Red Teaming Language Models

Read [the Red Teaming Language Models method](../skills/red-teaming-llms/SKILL.md). Run bounded adversarial cases against the mapped boundaries.

**Carry forward:** A case-level result set and reproducible failures.

**Check:** Each failure demonstrates an actual boundary violation within the authorized scope.

## 3. Agent Regression Evaluation

Read [the Agent Regression Evaluation method](../skills/agent-regression-evals/SKILL.md). Retest the fixes against attack and normal-use cases.

**Carry forward:** A regression report covering both protection and task success.

**Check:** The fixes block the demonstrated failure without unacceptable normal-task regressions.

## Check the finished work

- The map distinguishes user intent, retrieved content, tool results, and privileged actions.
- Each failure demonstrates an actual boundary violation within the authorized scope.
- The fixes block the demonstrated failure without unacceptable normal-task regressions.

## Finish

A regression report covering both protection and task success. The fixes block the demonstrated failure without unacceptable normal-task regressions.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
