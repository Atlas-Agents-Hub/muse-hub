# Turn Real Work Into a Credible Portfolio Story — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Turn real work into a narrative of the problem, constraints, personal contribution, implementation choices, verification and observed outcome. Keep a prototype, tested local system, deployed product and independently adopted service distinct. A strong story can be ambitious without pretending unfinished work is complete.

Attribute shared work accurately and preserve evidence for quantitative claims. Personal projects can demonstrate engineering capability without being relabeled as employment or customer success. Explain tradeoffs and failures that changed the design; do not manufacture a polished linear history or unsupported business impact.

## Output contract

Deliver a case study with a concise problem statement, contribution boundaries, design rationale, screenshots or artifacts where available, test/deployment evidence and honest remaining work. Include a claim-to-proof map and a short version suitable for a portfolio page or interview.

## Choose the right action

### The project is implemented and locally tested but not deployed.
Tell the implementation and verification story with exact scope.

**Avoid:** Do not convert local tests into production usage or customer adoption.

### Several people or agents contributed.
State the author’s decisions and implemented contribution separately from others’ work.

**Avoid:** Do not claim sole ownership of a shared artifact.

### The user has real measurements.
Use their baseline, method and observed result with units and context.

**Avoid:** Do not invent a percentage improvement from an anecdote.

### The work contains private or licensed material.
Use approved redactions, synthetic examples or permitted excerpts.

**Avoid:** Do not publish credentials, personal data or unlicensed assets to strengthen the story.

### A former claim no longer matches the current state.
Update the claim and preserve the relevant historical context.

**Avoid:** Do not quietly retain an obsolete deployment or performance assertion.

## Worked example

**Input:** Claim C1 says tested and has build/test evidence; C2 says deployed but only build evidence exists.

**Method:** Review each claim against its actual evidence stage.

**Result:** Keep C1. Rewrite C2 as built or mark deployment unverified; the project remains useful portfolio evidence.

## Edge or recovery example 1 (example)

**Input:** A later deployment receipt verifies C2.

**Method:** Attach the new observation to the relevant claim without changing unrelated history.

**Result:** C2 may now be described as deployed within that environment, not automatically as widely adopted or commercially successful.

## Failure diagnosis

### The case study sounds impressive but cannot be substantiated.
**Likely cause:** Claims were written without an evidence map.

**Repair:** Link each material claim to an actual artifact or observation.

**Recheck:** Unsupported claims are removed or clearly limited.

### The narrative obscures the person’s contribution.
**Likely cause:** Team output was described as personal execution.

**Repair:** Separate authored decisions, implementation and external contributions.

**Recheck:** A reviewer can identify what the person actually did.

### A private demonstration leaks sensitive context.
**Likely cause:** Portfolio adaptation reused original data without a privacy pass.

**Repair:** Replace it with an approved neutral demonstration.

**Recheck:** The public story preserves technical meaning without exposing protected content.

## Preserve for the next turn

Preserve source and artifact revisions, personal contribution boundaries, measurement methods, privacy decisions and current claim stages. Resume by adding verified new outcomes, never by promoting planned work into accomplished history.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `portfolio-story-r4-standard`, `portfolio-story-r4-edge`, `portfolio-story-r4-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
