# Improve Document Search

Build a retrieval pipeline whose answer context can be measured against a fixed query set.

## Bring these inputs

- Document corpus
- Representative queries and relevance judgments

## 1. Chunking Strategies

Read [the Chunking Strategies method](../skills/chunking-strategies/SKILL.md). Inspect document structure and select chunk boundaries with preserved identifiers.

**Carry forward:** Chunked documents and a corpus inspection summary.

**Check:** Chunks preserve context and point back to their exact source locations.

## 2. RAG Architect

Read [the RAG Architect method](../skills/rag-architect/SKILL.md). Configure indexing, retrieval, filtering, and reranking from the corpus and query requirements.

**Carry forward:** A retrieval design and repeatable evaluation inputs.

**Check:** The design satisfies access filters and uses the stated latency and quality targets.

## 3. Hybrid Search

Read [the Hybrid Search method](../skills/hybrid-search/SKILL.md). Compare lexical, vector, and combined retrieval on the fixed queries.

**Carry forward:** Per-query retrieval results and a selected configuration.

**Check:** The same judgments and cutoffs are used for every candidate; regressions are reviewed.

## Check the finished work

- Chunks preserve context and point back to their exact source locations.
- The design satisfies access filters and uses the stated latency and quality targets.
- The same judgments and cutoffs are used for every candidate; regressions are reviewed.

## Finish

Per-query retrieval results and a selected configuration. The same judgments and cutoffs are used for every candidate; regressions are reviewed.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
