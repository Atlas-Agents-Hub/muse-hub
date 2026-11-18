# Promptfoo

**Evaluate prompts with repeatable examples**

Compare prompts or model-backed applications against representative examples and explicit pass criteria.

**Works well with:** Model Builder, Adversarial Verifier, Software Engineer, Research Evaluator, Automation Engineer.

## What to bring

- Prompt or application endpoint
- Representative and regression cases
- Expected outcomes and budget

## Setup

1. Install the Promptfoo CLI, choose a target provider, and set credentials in the environment when required.

**Access:** Local CLI; model-provider usage varies.

## Supported functions

| Function | Use it to |
| --- | --- |
| `promptfoo-provider-setup` | Connect and smoke-test the target |
| `promptfoo-evals` | Run cases and evaluate their assertions |
| `promptfoo-redteam-setup` | Select adversarial cases for the authorized target |

## Workflow

1. Connect one representative request and verify the response parser.
2. Create test cases with expected answers or source records.
3. Use deterministic assertions for exact requirements and a defined rubric for semantic quality.
4. Run the suite, inspect failures, and compare the candidate with the baseline on the same cases.

## What you get

- Evaluation configuration
- Case results
- Baseline comparison

## Check the result

- The suite catches an intentionally incorrect output.
- The candidate meets the declared thresholds without changing the expected answers.

## Try it

> Use Promptfoo to evaluate prompts with repeatable examples. Start from the inputs I provide, follow the setup and workflow, and return evaluation configuration, case results, baseline comparison. Verify: The suite catches an intentionally incorrect output. The candidate meets the declared thresholds without changing the expected answers.

## Combine it with

- **Build, review, and finish a feature:** Atlas Continuum, Atlas Omnium, Superpowers, Codex Dev Workflows, Endor Labs Agent Kit.
- **Build and evaluate a knowledge assistant:** Hugging Face, RAG & GenAI Copilot, Prompt Injection Security, DEEPBOM Artifact Evidence.
- **Choose and measure a model deployment:** Hugging Face, DEEPBOM Artifact Evidence, NVIDIA Skills, AMD, Modal.

## Learn more

- [www.promptfoo.dev](https://www.promptfoo.dev/docs/integrations/agent-skill)
- [www.promptfoo.dev](https://www.promptfoo.dev)
- [github.com](https://github.com/promptfoo/promptfoo)
