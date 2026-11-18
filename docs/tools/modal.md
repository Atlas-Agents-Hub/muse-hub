# Modal

**Move a defined Python workload to cloud compute**

Package a Python task for an explicitly sized compute environment and retain its inputs, logs, outputs, and usage.

**Works well with:** Model Builder, Data Engineering Architect, Infrastructure Reliability Engineer, Automation Engineer.

## What to bring

- Python workload
- Dependencies and input fixture
- Resource and time limits

## Setup

1. Set up and authenticate the Modal SDK through the supported host workflow.
2. Select the compute type, timeout, and budget for the task.

**Access:** Metered cloud compute.

## Supported functions

| Function | Use it to |
| --- | --- |
| `onboard-modal` | Prepare the supported local Modal SDK and authentication workflow |

## Workflow

1. Reproduce the task with a small input and record its expected output.
2. Define the cloud image, dependencies, resources, and timeout.
3. Run the configured job and retain the job identifier and logs.
4. Download the output and compare it with the fixture or declared metric.

## What you get

- Packaged workload
- Job logs
- Result artifact
- Usage record

## Check the result

- The job uses the declared resources and completes within its limit.
- The output passes the same check as the local fixture.

## Try it

> Use Modal to move a defined Python workload to cloud compute. Start from the inputs I provide, follow the setup and workflow, and return packaged workload, job logs, result artifact, usage record. Verify: The job uses the declared resources and completes within its limit. The output passes the same check as the local fixture.

## Combine it with

- **Choose and measure a model deployment:** Hugging Face, DEEPBOM Artifact Evidence, Promptfoo, NVIDIA Skills, AMD.

## Learn more

- [modal.com](https://modal.com/docs)
- [modal.com](https://modal.com)
- [github.com](https://github.com/modal-labs/modal-client)
