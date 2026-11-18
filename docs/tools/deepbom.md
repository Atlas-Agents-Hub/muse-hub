# DEEPBOM Artifact Evidence

**Inspect a model artifact before deployment**

Inspect model structure, operators, tensor metadata, and findings in a serialized deployment artifact.

**Works well with:** Model Builder, Adversarial Verifier, Reverse Engineering Researcher, Infrastructure Reliability Engineer.

## What to bring

- Model artifact
- Format and intended runtime
- Inspection question

## Setup

1. Prepare a supported TFLite, ONNX, GGUF, SafeTensors, Core ML, or ExecuTorch artifact and select the required inspection depth.

**Access:** Provider access.

## Supported functions

| Function | Use it to |
| --- | --- |
| `deepbom_capabilities` | Check supported artifact formats and analysis options |
| `deepbom_analyze_file` | Inspect the attached deployment artifact |
| `deepbom_query_file` | Explore its layers, findings, or requested tensor analysis |

## Workflow

1. Confirm supported format and begin structural analysis.
2. Retain the artifact hash and model representation.
3. Query the relevant layers, findings, or tensor payloads for the specific question.
4. Export the evidence and use the findings to choose a separate runtime test.

## What you get

- Model structure report
- Artifact findings
- Model BOM or visualization

## Check the result

- The report identifies the exact analyzed artifact.
- Each finding references a specific layer, operator, or tensor.

## Try it

> Use DEEPBOM Artifact Evidence to inspect a model artifact before deployment. Start from the inputs I provide, follow the setup and workflow, and return model structure report, artifact findings, model bom or visualization. Verify: The report identifies the exact analyzed artifact. Each finding references a specific layer, operator, or tensor.

## Combine it with

- **Build and evaluate a knowledge assistant:** Hugging Face, RAG & GenAI Copilot, Promptfoo, Prompt Injection Security.
- **Choose and measure a model deployment:** Hugging Face, Promptfoo, NVIDIA Skills, AMD, Modal.

## Learn more

- [deepbom.org](https://deepbom.org/)
