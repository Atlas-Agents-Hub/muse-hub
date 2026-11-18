# Codex Dev Workflows

**Carry a feature from brief to review**

Structure feature development, bug investigation, code review, and interrupted-session recovery around the actual repository.

**Works well with:** Software Engineer, Infrastructure Reliability Engineer, Automation Engineer, Coordinator, Adversarial Verifier.

## What to bring

- Feature or defect brief
- Current repository
- Acceptance cases

## Setup

1. Open the repository in a compatible coding assistant and identify its build and test commands.

**Access:** Local tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `feature-development` | Implement a repository feature |
| `code-review` | Review a concrete change |
| `resume-interrupted-task` | Recover an interrupted development session |

## Workflow

1. Inspect the current implementation and the repository instructions.
2. Write a focused change plan with affected files and behavior checks.
3. Implement and test the change, then inspect the final diff.
4. Save a review summary and a restart note when work spans sessions.

## What you get

- Implemented change
- Targeted test results
- Review and handoff

## Check the result

- Acceptance cases map to implemented behavior.
- The handoff identifies the tested revision and remaining work.

## Try it

> Use Codex Dev Workflows to carry a feature from brief to review. Start from the inputs I provide, follow the setup and workflow, and return implemented change, targeted test results, review and handoff. Verify: Acceptance cases map to implemented behavior. The handoff identifies the tested revision and remaining work.

## Combine it with

- **Build, review, and finish a feature:** Atlas Continuum, Atlas Omnium, Superpowers, Promptfoo, Endor Labs Agent Kit.

## Learn more

- [github.com](https://github.com/srajpal/codex-dev-workflows)
