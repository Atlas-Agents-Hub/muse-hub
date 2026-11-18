# Prompt Injection Security

**Test whether untrusted content can redirect an assistant**

Examine documents, retrieved passages, tool results, and memory for paths that could change an assistant’s authorized behavior.

**Works well with:** Adversarial Verifier, Model Builder, Software Engineer, Research Evaluator, Automation Engineer.

## What to bring

- Assistant workflow
- Untrusted content channels
- Expected tool boundaries

## Setup

1. Use a test environment with a defined task, tool permissions, and synthetic sensitive values.

**Access:** Local tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `indirect-injection-review` | Inspect untrusted documents and retrieval inputs |
| `agent-tool-boundaries` | Review tool arguments, permissions, and action boundaries |
| `mitigation-regression-tests` | Turn confirmed findings into repeatable checks |

## Workflow

1. Map where untrusted text enters the workflow and which actions it could influence.
2. Create controlled cases that attempt to override the task or misuse a tool.
3. Record whether each case changes the output or triggers an unauthorized operation.
4. Apply input handling or action-boundary fixes and repeat both normal and adversarial cases.

## What you get

- Injection test cases
- Boundary findings
- Mitigation regression results

## Check the result

- Untrusted content cannot authorize a new destination or action.
- Normal tasks still succeed after the mitigation.

## Try it

> Use Prompt Injection Security to test whether untrusted content can redirect an assistant. Start from the inputs I provide, follow the setup and workflow, and return injection test cases, boundary findings, mitigation regression results. Verify: Untrusted content cannot authorize a new destination or action. Normal tasks still succeed after the mitigation.

## Combine it with

- **Build and evaluate a knowledge assistant:** Hugging Face, RAG & GenAI Copilot, Promptfoo, DEEPBOM Artifact Evidence.
- **Review access, dependencies, and agent boundaries:** Descope, Endor Labs Agent Kit, Authorised OSINT Toolkit, reverse engineering anything.

## Learn more

- [thedoersfirm.com](https://thedoersfirm.com/)
- [thedoersfirm.com](https://thedoersfirm.com/gpts)
