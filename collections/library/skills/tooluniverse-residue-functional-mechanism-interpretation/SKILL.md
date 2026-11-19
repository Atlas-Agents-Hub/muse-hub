---
name: tooluniverse-residue-functional-mechanism-interpretation
description: "Given a set of residues in a protein, explain WHY they are functionally critical by combining structural context (binding interface, ligand pocket, core, secondary structure), UniProt features (active sites, binding sites, PTM sites, disulfides), optional SAE feature evidence, and optional DMS data. Accepts residues from any source: DMS hotspots (top-K by max effect), ClinVar recurrent variants, literature-reported hot regions, evolutionarily conserved positions, or user-curated lists. Returns a per-cluster mechanism call: catalytic / ligand-binding / interface / structural-core / PTM / regulatory / unknown."
---

# Tooluniverse Residue Functional Mechanism Interpretation

Use the task's actual files, connected services, and project settings. Run included helpers from this skill folder. Set `SKILL_DIR` to its full path when a command uses that variable.

Read [the detailed method](METHOD.md) for the procedure, examples, and supporting references.
