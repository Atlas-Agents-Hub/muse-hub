# Darling Runtime

**Try a macOS command-line utility on Linux**

Inspect a Mach-O command-line tool and test a defined compiler or utility workflow with Darling on a compatible Linux host.

**Works well with:** Software Engineer, Reverse Engineering Researcher, Infrastructure Reliability Engineer.

## What to bring

- Authorized Mach-O utility
- Arguments and fixture
- Host architecture

## Setup

1. Use a compatible Linux host and follow the Darling package setup for the target architecture.
2. Keep a representative input and expected command-line output.

**Access:** Local tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `darling-runtime` | Set up and investigate a Mach-O command-line workflow on Linux |

## Workflow

1. Inspect the binary architecture and linked dependencies.
2. Select the matching Darling components and record their versions.
3. Run a small fixture in the compatibility environment.
4. Compare exit status and output with the expected result and retain diagnostic logs.

## What you get

- Compatibility result
- Reproduction command
- Diagnostic log

## Check the result

- The tested command produces the expected output for the fixture.
- Host, runtime, binary, and invocation are recorded together.

## Try it

> Use Darling Runtime to try a macOS command-line utility on Linux. Start from the inputs I provide, follow the setup and workflow, and return compatibility result, reproduction command, diagnostic log. Verify: The tested command produces the expected output for the fixture. Host, runtime, binary, and invocation are recorded together.

## Learn more

- [tarekwasfy01.github.io](https://tarekwasfy01.github.io/Darling-MacOS-for-ChatGPT-Plugin/)
