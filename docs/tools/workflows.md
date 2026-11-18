# Workflows with your tools

Combine tools around a useful result. Start with the inputs, follow the sequence, and check the finished work.

<a id="quality-feature-delivery"></a>

## Build, review, and finish a feature

**Specialists:** Software Engineer, Automation Engineer, Infrastructure Reliability Engineer, Adversarial Verifier, Coordinator.

**Bring:** Repository and acceptance cases; Current failure or feature brief.

1. Resume the project with Atlas Continuum and select the required connection with Atlas Omnium.
2. Use Superpowers and Codex Dev Workflows to reproduce the problem or implement the bounded feature.
3. Use Promptfoo when the feature depends on model output; use Endor Labs when dependencies or security findings are affected.
4. Review the change, run its relevant tests, and save the working result and next handoff.

**You get:** Implemented feature or repair; Acceptance results; Review and handoff.

**Check the result:**

- The requested behavior works and the original failure stays fixed.
- The delivered revision matches the recorded verification.

<a id="search-ready-product"></a>

## Make a useful product easy to find

**Specialists:** Product Interface Designer, Creative Studio, Infrastructure Reliability Engineer, Coordinator.

**Bring:** Website and product brief; Audience, locale, and important user journeys.

1. Use Brand Strategist to state the product promise and useful reasons to choose it.
2. Use Keyword Tool to map relevant search intent to useful pages.
3. Use OpenSEO and AIOScan to find concrete crawl, metadata, content, and access issues.
4. Use Product Design to verify that visitors can find the feature and complete the intended journey.
5. Recheck the changed pages and retain the resulting audit links.

**You get:** Clear page messaging; Keyword-to-page map; Search and journey fixes.

**Check the result:**

- Titles and descriptions accurately describe each page.
- Both the crawler checks and the user journey succeed.

<a id="retrieval-quality"></a>

## Build and evaluate a knowledge assistant

**Specialists:** Model Builder, Data Engineering Architect, Research Evaluator, Adversarial Verifier, Claims Adjudicator.

**Bring:** Source corpus; Questions with supporting passages; Access rules and budget.

1. Use Hugging Face to select suitable model and dataset candidates.
2. Use RAG & GenAI Copilot to define ingestion, retrieval, citations, and update behavior.
3. Use Promptfoo to compare retrieval-backed answers on normal, unanswerable, and known failure cases.
4. Use Prompt Injection Security to test untrusted-document and tool-boundary cases.
5. Use DEEPBOM when the selected deployment includes an inspectable model artifact.

**You get:** Knowledge-assistant design; Evaluation suite and results; Access and injection regression cases.

**Check the result:**

- Answers cite passages that support them.
- Restricted or malicious content cannot redirect authorized behavior.

<a id="database-and-dashboard"></a>

## Deliver trustworthy data and dashboards

**Specialists:** Data Engineering Architect, Software Engineer, Adversarial Verifier.

**Bring:** Schema and business rules; Representative rows and expected totals; Viewer roles.

1. Use SQL Expert to align schema and constraints with the application.
2. Use SQL Copilot to verify joins, time boundaries, nulls, and aggregates on a small fixture.
3. Use PlanetScale or WoWSQL for the project’s actual database.
4. Use Preset to build the dashboard from the verified metrics.
5. Use Formula Genius when stakeholders also need a spreadsheet calculation or reconciliation.

**You get:** Validated queries and metrics; Dashboard or workbook; Viewer access results.

**Check the result:**

- Dashboard and workbook totals agree with the reference data.
- Each viewer can access exactly the intended records.

<a id="mobile-feature-quality"></a>

## Build and verify a mobile experience

**Specialists:** Software Engineer, Product Interface Designer, Adversarial Verifier, Infrastructure Reliability Engineer.

**Bring:** Mobile project and feature; Target devices; Acceptance cases.

1. Use Expo to implement the feature with the correct native and navigation requirements.
2. Use Testing React Native Apps for component behavior and device interaction.
3. Use Test Android Apps for the Android flow and any measured performance issue.
4. Use Product Design to inspect the complete flow, accessible controls, and screen layouts.
5. Verify the resulting build or update on the target platform.

**You get:** Working feature; Component and device results; Screenshots and build artifact.

**Check the result:**

- Loading, success, and failure states work in the component and on the device.
- The intended user journey completes on every selected platform.

<a id="creative-product-experience"></a>

## Design a coherent product experience

**Specialists:** Product Interface Designer, Creative Studio, Software Engineer.

**Bring:** Audience and product journey; Brand material; Required screens and assets.

1. Use Brand Strategist to settle the product promise and voice.
2. Use Pablooo.club to compare relevant interface patterns.
3. Use Product Design and Designly to define an original interface and consistent art direction.
4. Use MagicPath for components and Wixel for the selected visual assets.
5. Inspect the assembled experience and verify its key interaction on the intended screen sizes.

**You get:** Original interface design; Working components; Coherent visual assets.

**Check the result:**

- The primary action is obvious and usable.
- Layout, typography, and brand treatment remain consistent across the finished experience.

<a id="model-performance"></a>

## Choose and measure a model deployment

**Specialists:** Model Builder, Infrastructure Reliability Engineer, Data Engineering Architect.

**Bring:** Model task and evaluation cases; Target hardware; Latency, memory, and quality limits.

1. Use Hugging Face to choose candidates and record their exact revisions.
2. Use DEEPBOM to inspect available deployment artifacts.
3. Use Promptfoo to establish a quality baseline.
4. Use NVIDIA or AMD workflows for the actual hardware and Modal when the chosen workload needs cloud compute.
5. Compare the same quality and performance cases after each focused change.

**You get:** Model selection; Artifact inspection; Quality and performance comparison.

**Check the result:**

- Performance gains preserve the required output quality.
- Results record the model, hardware, runtime, and workload.

<a id="security-review"></a>

## Review access, dependencies, and agent boundaries

**Specialists:** Adversarial Verifier, Software Engineer, Reverse Engineering Researcher, Infrastructure Reliability Engineer.

**Bring:** Authorized application or organization; Repository and roles; Threat questions.

1. Use Descope to examine sign-in, permissions, and tenant boundaries.
2. Use Endor Labs to inspect dependency and code findings.
3. Use Prompt Injection Security for assistant and retrieval boundaries.
4. Use Authorised OSINT Toolkit for relevant public exposure and reverse engineering anything for supplied software artifacts.
5. Fix confirmed issues and repeat the affected normal and negative test cases.

**You get:** Prioritized findings; Verified repairs; Repeatable security checks.

**Check the result:**

- Every finding has a specific target and reproducible evidence.
- The remediation closes the failure while retaining intended access and behavior.

<a id="research-and-explanation"></a>

## Research a question and explain the result

**Specialists:** Research Evaluator, Claims Adjudicator, Learning Coach, Model Builder.

**Bring:** Research question; Source requirements; Audience and output format.

1. Use TinyFish to find and read relevant primary material.
2. Use nDot Physics Research for a question about its published physics work.
3. Use Wolfram to check the quantitative part with explicit assumptions and units.
4. Use Gum for precise figures and MindMap for a navigable conceptual outline.
5. Use KaTeX Error Fixer when equations need to appear in a rendered learning page.

**You get:** Cited explanation; Reproducible calculation; Readable figure or learning page.

**Check the result:**

- Each substantive claim can be traced to its source or calculation.
- The rendered equations and figures preserve the verified content.

<a id="game-production"></a>

## Create and test a game feature

**Specialists:** Creative Studio, Software Engineer, Product Interface Designer, Adversarial Verifier.

**Bring:** Game feature or asset brief; Unity project; Target performance budget.

1. Use Game Development Studio to create or select and validate the asset.
2. Use Wixel for any requested visual reference or supporting graphic.
3. Use Unity Essentials to implement the feature in a reproducible scene.
4. Use the relevant NVIDIA or AMD workflow when the task specifically depends on that hardware.
5. Run the scene and intended build and compare both appearance and measured performance.

**You get:** Playable feature; Validated asset package; Scene and build evidence.

**Check the result:**

- Assets load correctly and the feature works after reopening the project.
- The scene meets the declared visual and performance target.

<a id="personal-projects"></a>

## Organize personal projects and learning

**Specialists:** Personal Companion, Learning Coach, Garden Companion, Coordinator.

**Bring:** Personal project or study goal; Dates and constraints; Reference information.

1. Use MindMap to organize the goal into useful topics and next actions.
2. Use TinyFish to gather any current facts needed to make a decision.
3. Use Formula Genius for a tracker or calculation with explicit example rows.
4. Use Flowchart Maker for a recurring decision or process.
5. Use Windowisp for an optional Windows focus-session companion.

**You get:** Project or study outline; Useful tracker; Clear next actions.

**Check the result:**

- Every immediate action has the information needed to begin.
- Tracker calculations match the supplied examples.

<a id="explain-architecture"></a>

## Turn architecture into an editable visual

**Specialists:** Software Engineer, Data Engineering Architect, Coordinator, Product Interface Designer, Research Evaluator.

**Bring:** Source code, schema, or process; Question the diagram must answer; Audience.

1. Choose the view with Diagram Maker: structure, sequence, data, or process.
2. Use Flowchart Maker for a decision process and Lucid for a shared editable architecture document.
3. Use Gum when the deliverable needs a precise figure or reproducible export.
4. Compare every displayed entity and relationship with the actual source.
5. Review the exported diagram at its intended viewing size.

**You get:** Editable diagram; Readable export; Source relationship notes.

**Check the result:**

- The diagram answers the stated question without invented relationships.
- Labels and connections remain readable in the final export.

