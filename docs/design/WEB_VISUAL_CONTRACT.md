# Muse Hub — Shared Visual Contract

## Scope and authority

This contract applies to the 38 published HTML page routes: the homepage, Downloads, 35 generated Library subject pages, and the Setup Guide Directory. It governs the shared header, navigation, brand mark, type hierarchy, horizontal gutters, colors, cards, controls, focus states, and responsive spacing. No dependency on an external font CDN, framework, remote assets, or user account is introduced.

**Single point of ownership:** `hub/site/experience.css` defines the `--muse-*` visual tokens and the final cross-family component contract. Earlier `hub/site/site.css` and `hub/site/public/styles.css` remain page-specific foundations. Do not introduce new page-specific header styling or reintroduce the removed guide-only navigation component.

**Header markup:** the authored `hub/site/index.html` header is the reference. `hub/site/downloads.html` and `hub/site/public/index.html` share the same component. The subject-page generator reuses the homepage header and resolves links relative to `library/`. Guide Directory links are relative to `public/`. All four families must use `site-header r7-header muse-header` and the same `mobile-navigation` disclosure.

## Visual tokens

| Domain | Contract |
| --- | --- |
| Main background | `--muse-bg: #151515` |
| Card surface / hover | `--muse-panel: #21231e`; `--muse-panel-hover: #2a2c25` |
| Text / secondary text | `--muse-text: #f6f4eb`; `--muse-muted: #c9cbbd` |
| Border / interaction | `--muse-border: #575b4e`; `--muse-accent: #eaff43` |
| Typography | `--muse-sans` for UI; `--muse-serif` for editorial headings |
| Content | `--muse-content: 1260px`; `--muse-gutter` from 16–36px |
| Main card radius/gap | `--muse-card-radius: 4px`; `--muse-gap: 12–16px` |
| Section rhythm | 8, 12, 20, 32, 48, 72 px scale (context-dependent) |

Hero headlines may be larger than interior page titles. Content types (task card, resource card, specialist card) may have different minimum heights where needed, but they must share the same content gutters, border/color hierarchy, font family, and focus affordances.

## Cross-device behavior

- **Desktop / 1440px:** primary navigation and search are visible; header has 76px baseline, 56px logo and single-row controls.
- **Tablet / 768px:** navigation collapses to native `details`, no hover-only behavior; subject cards have two columns where space permits.
- **Phone / 320–393px:** full-width accessible menu targets, 16–20px side gutters, cards in one column, no horizontal page overflow; one task entry visible at the earliest reasonable point.
- Phone-width multi-page subject pagination presents Prev / current / Next in one row. Direct numbered links remain on desktop; full page count remains in the mobile subject summary.
- No-JavaScript navigation and static subject links must remain navigable.
- Real data must not be deleted or moved to invisible-only storage to make cards shorter. On generated subject cards a concise description is a presentation excerpt, while the underlying catalog and actual method remain unchanged. Pack paths are disclosed through accessible `<details>` before primary action links.
- Respect focus-visible and reduced-motion preferences. Do not weaken contrast or pointer targets to fit copy.

## Regression and evidence gates

1. `python scripts/render_downloads.py --check`: generated pages match source.
2. `python -B -m unittest tests.test_hub_sitewide_experience -q`: all routes, shared header, tokens, asset links, readable pack paths, release version.
3. `node tests/hub_experience_browser.cjs . "<CHROME>" "<UNIQUE_OUTSIDE_REPO_DIR>" --require-journeys`: real Chrome CDP; 8 widths, 35 subjects, stateful search, keyboard/menu, fallback, source-hash guard and visual contract.
4. `python scripts/check_public.py`: public-source integrity after refreshing hashes on the final *frozen* source.
5. GitHub Actions must pass on the exact commit; independently review browser captures at 390px and 1440px.
6. Native iPhone Safari and VoiceOver remain an explicit unverified release gate unless actual device evidence is provided. Chrome viewport emulation is not equivalent.

A green test suite does not by itself establish visual quality. Review homepage, Downloads, subject index, and Guide Directory screenshots both above and below the fold. Reject misleading counts, broken links, clipped text, obscured focus rings, unexpected scrollbars, inaccessible menus, or inconsistent headers.
