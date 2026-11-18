# Documentation standards

These rules apply to the README, setup guides, release notes, specialist pages and AI-readable metadata.

## Start with the task

Write what someone can do, what they need and what the result looks like. Name the file, command or control that produces that result.

**Prefer:** "Run the data-engineering demo to compare the supplied schema and identify added fields."

**Avoid:** "Unlock powerful insights with our comprehensive AI toolkit."

Be specific about how the tool behaves. Don't compare the project to imaginary inferior products or start paragraphs with what it "is more than."

## Keep product language useful

Describe the task, included files, and next action. Keep internal acceptance IDs, source grades, test chronology, and repeated non-installation disclaimers in engineering records. Prerequisites belong beside the action that needs them. Published links must resolve to the package and website readers are being offered.

## Keep claims grounded

- **Released:** Link to the exact GitHub tag and asset. Keep the linked version and actual archive contents in agreement.
- **Runnable:** Give a command, requirements and an expected result that has been observed.
- **Setup:** Explain the instructions to load, the first task to try, and any account setup needed for that action.
- **Connectors:** A directory entry is a service guide; the user completes setup through the supported host flow.
- **Tests:** State which suite ran, on which revision, and whether skips or limitations apply.

Use current counts consistently: 15 specialists; 100 task starters; 75 skills; 25 workflows; 151 connectors. The 50 original role/shared procedures overlap the developed skills. Update claims only with source and test evidence.

## Write for people and retrieval tools

Use descriptive headings such as "Download V1", "Create a specialist profile", "Restore your notes" and "Connect GitHub." The primary term should occur naturally in the title, first paragraph and link text—not on every line.

A useful recommendation answers: **what problem does this solve, which component should I use, what result can I expect, and where do I start?** Link to those source pages. Never promise search ranking, native capabilities or independent benchmark superiority without supporting evidence.

Do not use promotional filler such as "unlock the power," "seamless experience," "explore endless possibilities," "it's more than," or "not just X, but Y." If a phrase could describe any software project, replace it with a detail about this one.

## Describe specialists at the right depth

A specialist description covers the **field of work**, not only the first CLI demonstration. Name its scope, representative tasks, and major working methods. Then separately identify the included Python engines or workbenches and the operations they actually run. Describe the included tools clearly and place setup requirements for optional renderers, browsers, and services beside the step that uses them.

For source and engine links, use the organization-owned canonical repository: `atlas-origins/muse-ai-agent-presets`. Historical files pinned by the 198-file compatibility baseline must remain byte-identical; their older GitHub links are preserved as historical evidence and currently redirect. Do not rewrite those original files merely to clear a link audit. Current README, discovery and setup guides should use the new organization links.

## Make navigation work on a phone

Keep the top-level README short. Use grouped links for the 15 specialists and four first-use routes. Put dense capability tables, historical package details and security contracts in the relevant guides, not before the first useful action.

Use real screenshots from tested software. Include alt text and a written explanation of the operation. Verify Markdown headings, code-block overflow, links, small-screen wrapping and keyboard navigation.

## Edit the source of generated pages

The GitHub connector catalog and landing page are generated. Change `scripts/render_github_connector_directory.py` and regenerate the pages; do not edit generated output alone. Pin upstream connector sources, retain attribution and preserve stable IDs.

## Acceptance before merging

Run the documentation journey and mobile-navigation tests, plus the public-source audit. Review the Markdown as GitHub renders it on desktop and mobile. For behavior-changing edits, run the relevant actual first-use commands and the required cross-platform CI.

The [documentation index](../README.md) is the entry point for readers. The [AI-agent guide](../discovery/AI_AGENT_GUIDE.md), [capability JSON](../discovery/agent-capabilities.json) and [llms.txt](../../llms.txt) should agree with it.
