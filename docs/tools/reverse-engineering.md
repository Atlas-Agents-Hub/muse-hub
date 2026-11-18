# reverse engineering anything

**Explain how an authorized software artifact works**

Choose an appropriate inspection workflow for a binary, application package, JavaScript bundle, firmware image, or recorded trace.

**Works well with:** Reverse Engineering Researcher, Adversarial Verifier, Software Engineer, Research Evaluator.

## What to bring

- Artifact and hash
- Investigation scope
- Expected platform or format

## Setup

1. Identify the authorized artifact, the question to answer, and the available REA analysis tools.

**Access:** Local tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `rea-target-routing` | Select the inspection workflow for an artifact |
| `rea-javascript-electron` | Inspect a JavaScript or Electron application |
| `rea-mobile-and-firmware` | Plan an authorized APK or firmware inspection |
| `rea-evidence-and-reporting` | Explain findings with reproducible evidence |

## Workflow

1. Classify the artifact and select the relevant static or recorded-trace inspection.
2. Inspect package structure, metadata, and the code paths relevant to the question.
3. Trace specific findings to offsets, files, functions, or recorded events.
4. Write a concise explanation with reproduction steps and clearly identified unresolved questions.

## What you get

- Artifact analysis
- Evidence references
- Reproduction notes

## Check the result

- Findings reference the exact artifact and location.
- The explanation separates direct observations from inferred behavior.

## Try it

> Use reverse engineering anything to explain how an authorized software artifact works. Start from the inputs I provide, follow the setup and workflow, and return artifact analysis, evidence references, reproduction notes. Verify: Findings reference the exact artifact and location. The explanation separates direct observations from inferred behavior.

## Combine it with

- **Review access, dependencies, and agent boundaries:** Descope, Endor Labs Agent Kit, Prompt Injection Security, Authorised OSINT Toolkit.

## Learn more

- [github.com](https://github.com/morluto/rea)
- [thedoersfirm.com](https://thedoersfirm.com/)
