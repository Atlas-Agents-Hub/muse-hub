# RAG & GenAI Copilot

**Build answers that stay connected to their sources**

Design and evaluate retrieval, ingestion, citations, and operational checks for a knowledge assistant.

**Works well with:** Model Builder, Data Engineering Architect, Research Evaluator, Adversarial Verifier, Claims Adjudicator.

## What to bring

- Source corpus
- Question-and-answer examples
- Access and latency requirements

## Setup

1. Identify the corpus, update cadence, access rules, and representative user questions.

**Access:** Chosen model, embedding, and storage services.

## Supported functions

| Function | Use it to |
| --- | --- |
| `design-ingestion-indexing` | Plan document ingestion and updates |
| `design-retrieval` | Choose retrieval and ranking behavior |
| `evaluate-rag` | Measure retrieval and answer quality |
| `audit-citations` | Check whether citations support the answer |

## Workflow

1. Define document identity, chunking, metadata, and update behavior.
2. Evaluate retrieval on questions with known supporting passages.
3. Evaluate answer accuracy, citation support, and unanswerable questions.
4. Add monitoring for retrieval failures, stale content, latency, and access violations.

## What you get

- Retrieval design
- Evaluation dataset
- Cited answer results
- Operational checks

## Check the result

- Citations support the answer they accompany.
- Restricted documents stay outside unauthorized queries and unsupported questions are handled correctly.

## Try it

> Use RAG & GenAI Copilot to build answers that stay connected to their sources. Start from the inputs I provide, follow the setup and workflow, and return retrieval design, evaluation dataset, cited answer results, operational checks. Verify: Citations support the answer they accompany. Restricted documents stay outside unauthorized queries and unsupported questions are handled correctly.

## Combine it with

- **Build and evaluate a knowledge assistant:** Hugging Face, Promptfoo, Prompt Injection Security, DEEPBOM Artifact Evidence.

## Learn more

- [tekrislabs.com](https://tekrislabs.com/)
