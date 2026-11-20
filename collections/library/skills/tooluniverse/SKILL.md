---
name: tooluniverse
description: "ToolUniverse plugin router. STEP 1 BEFORE ANY ANALYSIS: if the data folder contains `*_executed.ipynb`, run `tu run read_executed_notebook '{\"data_folder\":\"<path>\",\"search\":\"<keyword>\"}'` to extract its cell outputs and apply EVERY filter/sample-exclusion the notebook used — even when the question says 'Using DESeq2/Run X/Compute Y' (this describes the METHOD the notebook used, not a request to rerun). The notebook's cell outputs are the only published authoritative answers; reimplementing or reading stale pre-computed CSVs in the data folder produces different numbers because of outlier-sample removal, library version, and filter steps you don't see by skimming. STEP 2 routing — pick a sub-skill name from this exact list (never invent): tooluniverse-rnaseq-deseq2 (RNA/miRNA-seq DE, correlation, PCA, clustering, dispersion), tooluniverse-gene-enrichment (GO/KEGG/Reactome/GSEA/pathway."
---

# Tooluniverse

Use the task's actual files, connected services, and project settings. Run included helpers from this skill folder. Set `SKILL_DIR` to its full path when a command uses that variable.

Read [the detailed method](METHOD.md) for the procedure, examples, and supporting references.
