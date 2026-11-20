# Muse Hub — Visual Identity

The Muse Hub identity is a controlled part of the product, not a replaceable theme. Every page, new Space catalogue view, marketing asset and social image uses the same shared palette and typography.

## Design tokens

| Token | Hex | Use |
| --- | --- | --- |
| Black | `#151515` | Dark canvases, site header, hero, primary text |
| Ink | `#161616` | Text on paper, black detail work |
| Warm paper | `#F8F6E9` | Alternating light sections, page backgrounds |
| Paper strong | `#FFFCF1` | Cards, fields, editorial surfaces |
| Muse Electric | `#F4FF52` | Signature M mark, primary CTA, signal labels, selected accents, focus indicator |
| Dark border | `#43433F` | Lines on black |
| Paper border | `#C9C7BD` | Lines on cream |

The canonical CSS variables live at the top of `hub/site/site.css`. The homepage `.muse-premium` class may set the same values for page isolation but must never establish a divergent palette.

## Type and mark

Display headings use `Georgia, "Iowan Old Style", Baskerville, serif`, regular weight, generous size and restrained letter spacing. Interface labels, actions, body content, form controls and small metadata use `Inter, "Helvetica Neue", Arial, system-ui, sans-serif`. Preserve the existing two-path **M** symbol and spaced **MUSE HUB** wordmark from the site header; do not substitute a different logo or invent a new product name.

## Application rules

- Black hero with large cream serif headline and yellow accent/CTA, not gradients or a generic pastel SaaS hero
- Cream information sections alternating with charcoal functional sections
- Crisp strokes, rectangular controls, editorial grid alignment, purposeful negative space
- Yellow used deliberately for actionable priority and signal, not as an overwhelming fill everywhere
- Mobile navigation in one row, large touch targets and visible keyboard focus
- Respect `prefers-reduced-motion`, no horizontal page overflow at 320px and 390px
- Preserve information architecture and working product links when iterating on the visual design

## Authentic product showcase

The first screen must establish product value by displaying a **real working Muse Space** rather than a decorative mock interface. The two reviewed browser captures are `hub/site/planner-desktop.png` (980 × 745) and `planner-mobile.png` (390 × 490). Their bytes and hashes remain sealed in `hub/site/INTEGRITY.json`. On desktop, the main screenshot is paired with a smaller phone-capture inset; on phones, the responsive `<picture>` displays the mobile capture directly. Both have links to inspect the full-size originals. Label these as **app screenshots**: a static preview must never imply that visitors are manipulating the actual running Space.

- Keep actual app data, controls, and states legible at desktop and phone widths; images must be responsive and provide useful alt text.
- Every showcase should link to the matching app's setup guide and source, not an unrelated generic directory.
- Keep mobile evidence visible in the first-screen journey. Never hide the only product demonstration on phones.
- Specialist discovery starts with visible search and an accessible results count, then expands the full directory on input, focus, or in-page navigation. Without JavaScript, the native directory disclosure still exposes all 15 kits.
- Four outcome-first shortcuts resolve only reviewed specialist identifiers (software engineer, claims adjudicator, product interface designer, coordinator). Shortcuts update the real filter, count and selection state, open the real kit directory and move keyboard focus to the matching card. The directory summary must reflect the filtered count.
- Maintain real links, browser tested keyboard/deep-link behavior, no horizontal overflow, and a clear primary action. Do not imply a static illustration is an interactive application.
- Preserve deterministic image inventory and fail-closed source distribution controls when adding screenshots; a new image needs explicit asset review and tests.

## Verification

Run the source-level brand gate and browser interaction gates after any design change:

```powershell
$env:PYTHONPATH = "src"
python -B -m unittest discover -s tests -p "test_hub_brand_identity.py" -v
python -B -m unittest discover -s tests -p "test_hub_home_product_journey.py" -v
python -B -m unittest discover -s tests -p "test_hub_showcase_visual_acceptance.py" -v
python -B scripts/render_downloads.py --check
```

The branded social preview lives at `hub/site/social-card.png`; its checksum and byte count are recorded in `hub/site/INTEGRITY.json`. The exact image is included through the strict public-source admission path.
