# Hugging Face

**Choose a model and dataset for the actual task**

Compare candidate models, datasets, and Spaces using their documented tasks, requirements, licenses, and evaluation evidence.

**Works well with:** Model Builder, Research Evaluator, Data Engineering Architect, Adversarial Verifier.

## What to bring

- Task and evaluation examples
- Hardware and latency needs
- License constraints

## Setup

1. Define the task, hardware limit, data sensitivity, and acceptable license terms.

**Access:** Public discovery; hosted compute and inference use provider plans.

## Supported functions

| Function | Use it to |
| --- | --- |
| `model_search` | Find relevant models |
| `dataset_search` | Find relevant datasets |
| `hub_repo_details` | Read repository metadata and model or dataset cards |
| `hf_doc_search` | Find current official implementation guidance |

## Workflow

1. Search the Hub for a small set of relevant models and datasets.
2. Read repository details and model or dataset cards.
3. Record exact revisions, requirements, evaluation conditions, and any access steps.
4. Select candidates for a reproducible comparison using the same test inputs.

## What you get

- Model and dataset shortlist
- Revision-pinned evaluation inputs
- Selection rationale

## Check the result

- Every candidate has a source repository and a checked license.
- Comparison results use the same task, inputs, and metrics.

## Try it

> Use Hugging Face to choose a model and dataset for the actual task. Start from the inputs I provide, follow the setup and workflow, and return model and dataset shortlist, revision-pinned evaluation inputs, selection rationale. Verify: Every candidate has a source repository and a checked license. Comparison results use the same task, inputs, and metrics.

## Combine it with

- **Build and evaluate a knowledge assistant:** RAG & GenAI Copilot, Promptfoo, Prompt Injection Security, DEEPBOM Artifact Evidence.
- **Choose and measure a model deployment:** DEEPBOM Artifact Evidence, Promptfoo, NVIDIA Skills, AMD, Modal.

## Learn more

- [huggingface.co](https://huggingface.co/docs/hub/index)
