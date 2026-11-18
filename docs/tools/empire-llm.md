# Empire LLM for Codex

**Get a focused second opinion on a change**

Request an independent model review of a small diff or compare model choices against a defined workload.

**Works well with:** Software Engineer, Adversarial Verifier, Model Builder, Research Evaluator.

## What to bring

- Review objective
- Small diff or selected files
- Model constraints and budget

## Setup

1. Use an installed Empire environment with its supported host, configured provider, and an explicit review budget.

**Access:** Provider inference credits.

## Supported functions

| Function | Use it to |
| --- | --- |
| `empire-review` | Request a bounded partner-model code review |
| `empire-benchmarks` | Compare model candidates using current benchmark metadata |
| `empire-cost-policy` | Apply the chosen spending policy |

## Workflow

1. Select only the files needed to answer the review question.
2. Choose the review profile and spending limit.
3. Run one focused review and retain the provider result.
4. Reproduce each actionable finding before changing the implementation.

## What you get

- Second-opinion report
- Confirmed findings
- Review cost record

## Check the result

- Every accepted finding names a file and reproducible behavior.
- The review stays within the selected evidence and budget.

## Try it

> Use Empire LLM for Codex to get a focused second opinion on a change. Start from the inputs I provide, follow the setup and workflow, and return second-opinion report, confirmed findings, review cost record. Verify: Every accepted finding names a file and reproducible behavior. The review stays within the selected evidence and budget.

## Learn more

- [empirellm.com](https://empirellm.com/)
- [github.com](https://github.com/web5labs/empire-llm-codex)
