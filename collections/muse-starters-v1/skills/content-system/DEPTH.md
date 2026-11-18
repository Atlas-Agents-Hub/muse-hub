# Plan Content From Reusable Source Material — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Build a content system around reusable, verified source material and an audience need rather than a calendar full of invented claims. Treat each content item as a transformation of identified facts, examples or owned creative material. Separate evergreen material, time-sensitive claims and private source context.

Repurposing should preserve meaning while adapting format, depth and channel. A short post must not turn a qualified finding into certainty, and a case study must not silently expose a private client. Draft approval, scheduling and publication are distinct states. Keep source refresh and withdrawal paths so stale claims can be found without redoing unrelated work.

## Output contract

Deliver content pillars, a source-to-item map, practical drafts or outlines, channel-specific acceptance checks and a refresh queue. Identify stale, unlicensed or private source dependencies. Record scheduling or publication only when an actual supported service returns evidence.

## Choose the right action

### The user has a substantial source artifact.
Extract reusable claims and examples and assign source IDs before choosing channels.

**Avoid:** Do not produce a pile of generic posts detached from the source.

### A source is outdated or withdrawn.
Hold affected claims and continue content based on still-valid sources.

**Avoid:** Do not refresh a date without rechecking the underlying fact.

### The same idea is adapted to several formats.
Keep the core claim and its qualification stable while changing presentation.

**Avoid:** Do not count aliases or channel variants as new evidence.

### The source contains personal or client details.
Minimize, redact or obtain the appropriate permission for the intended audience.

**Avoid:** Do not treat access to a document as authority to publish it.

### The user requests scheduling or publication.
Prepare the exact content and channel, then use the actual authorized provider and inspect its result.

**Avoid:** Do not claim a draft exists online or promise a background schedule without execution.

## Worked example

**Input:** A blog draft uses current source S1; a social post uses stale source S2.

**Method:** Check source currency and reuse scope per item.

**Result:** The blog is ready to draft. Hold the post for source refresh. Neither item is marked published.

## Edge or recovery example 1 (example)

**Input:** S2 is refreshed and approved for reuse.

**Method:** Recheck the affected claim and update the item without rebuilding the blog.

**Result:** Both drafts can proceed; scheduling and publication remain separate authorized actions.

## Failure diagnosis

### A polished post contains a claim absent from the source.
**Likely cause:** The writing process filled a gap with a plausible statement.

**Repair:** Remove or qualify it and trace the remaining claims.

**Recheck:** Every material factual assertion has support.

### Repurposed content contradicts the original.
**Likely cause:** Compression removed conditions or uncertainty.

**Repair:** Restore the key qualification and check the channel version.

**Recheck:** The shorter format preserves the original meaning.

### Old content keeps circulating after a correction.
**Likely cause:** Source dependencies were not recorded.

**Repair:** Use the source-to-item map to identify affected drafts and publications.

**Recheck:** The correction scope is explicit and does not erase unrelated content.

## Preserve for the next turn

Preserve source revisions, claim IDs, audience, draft versions, approvals and actual provider publication identifiers. Resume by refreshing only affected claims and reconciling ambiguous prior publishing actions.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `content-system-r4-standard`, `content-system-r4-edge`, `content-system-r4-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
