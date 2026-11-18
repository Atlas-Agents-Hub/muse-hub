# uniwire

**Turn an electrical plan into a reviewable diagram**

Create a structured electrical diagram, inspect rule findings, and export a drawing and materials list for professional review.

**Works well with:** Research Evaluator, Creative Studio, Garden Companion.

## What to bring

- Electrical specification
- Circuit and cable data
- Drawing requirements

## Setup

1. Provide the supply, circuits, loads, cable details, and applicable rule profile from the project specification.

**Access:** Provider access or self-hosted tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `get_reference_card` | Read the diagram format and node definitions |
| `check` | Validate the diagram and apply the chosen rule profile |
| `render` | Render single-line or multi-line drawings |
| `bom` | Create a materials list from specified products |

## Workflow

1. Read the relevant format types and start from the closest example.
2. Build the document with stable circuit and device identifiers.
3. Validate the structure and run the selected rule checks.
4. Resolve missing input or findings with the project designer, then render the diagram and materials list.

## What you get

- Single-line or multi-line drawing
- Rule findings
- Materials and wiring lists

## Check the result

- All references and circuit identifiers resolve.
- Ratings and cable details match the approved project specification.

## Try it

> Use uniwire to turn an electrical plan into a reviewable diagram. Start from the inputs I provide, follow the setup and workflow, and return single-line or multi-line drawing, rule findings, materials and wiring lists. Verify: All references and circuit identifiers resolve. Ratings and cable details match the approved project specification.

## Learn more

- [uniwire.sh](https://uniwire.sh)
- [github.com](https://github.com/uniwire-dev/uniwire)
