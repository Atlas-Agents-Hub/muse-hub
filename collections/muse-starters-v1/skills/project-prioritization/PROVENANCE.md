# Prioritization calculator sources

The included `tools/prioritize.py` is a new Muse Hub implementation, distributed under the project's MIT license. It implements exact RICE ranking and a deterministic, dependency-aware selection of work within separate resource capacities.

## RICE framework

Sean McBride's [RICE: Simple prioritization for product managers](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/), published by Intercom on January 5, 2018, explains the reach, impact, confidence and effort formula, its impact scale and the need to consider dependencies when choosing an execution order. Muse Hub uses that framework with explicitly declared effort units and a separate capacity check.

## Implementation reference reviewed

The review considered Alireza Rezvani's [Product Manager Toolkit RICE script](https://github.com/alirezarezvani/claude-skills/blob/f8593c4941210a621a6629ce1da9e07897976d5f/product-team/skills/product-manager-toolkit/scripts/rice_prioritizer.py) at revision `f8593c4941210a621a6629ce1da9e07897976d5f`, Git blob `5e6f2574ce7f798ef409f48bfc417c1cd0b53f54`. Its [MIT license](https://github.com/alirezarezvani/claude-skills/blob/f8593c4941210a621a6629ce1da9e07897976d5f/LICENSE) credits Alireza Rezvani, 2025.

That script was a comparison source; its code and prose are not included in this package. Muse Hub's implementation, examples and tests were written for this input contract. Exact arithmetic, stable tie-breaking, prerequisite closure, separate resource budgets, strict validation, CSV quoting and exclusive output creation are implemented and tested here.

[Calculator guide](PRIORITIZE.md) · [Skill procedure](SKILL.md)
