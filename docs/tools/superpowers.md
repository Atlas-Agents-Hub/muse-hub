# Superpowers

**Repair a bug and prove the behavior changed**

Use a focused reproduce, fix, and review cycle for implementation work, with checks tied to the requested behavior.

**Works well with:** All specialists.

## What to bring

- Expected behavior
- Failing example
- Relevant source and test command

## Setup

1. Open the relevant project and choose the debugging, implementation, or review skill that matches the work.

**Access:** Local tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `systematic-debugging` | Reproduce and isolate a defect |
| `test-driven-development` | Use a regression case to guide a repair |
| `verification-before-completion` | Verify the final behavior before reporting completion |

## Workflow

1. Reproduce the failure and identify the component responsible.
2. Add a focused regression check when the failure warrants one.
3. Implement the smallest maintainable correction and run the relevant checks.
4. Review the diff and report the observed result with the exact verification command.

## What you get

- Focused repair
- Regression evidence
- Review notes

## Check the result

- The original failing case succeeds.
- The check tests user-visible behavior and catches the original defect.

## Try it

> Use Superpowers to repair a bug and prove the behavior changed. Start from the inputs I provide, follow the setup and workflow, and return focused repair, regression evidence, review notes. Verify: The original failing case succeeds. The check tests user-visible behavior and catches the original defect.

## Combine it with

- **Build, review, and finish a feature:** Atlas Continuum, Atlas Omnium, Codex Dev Workflows, Promptfoo, Endor Labs Agent Kit.

## Learn more

- [github.com](https://github.com/obra/superpowers)
