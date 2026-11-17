# Muse Hub — H00–H21 feature readiness (source-grounded)

This is the **22-item feature list** from the owner-provided Muse Hub executor graph, reconciled against the public repository baseline `08a0b652fae4385abf32a03204ae58f45f9ea6e4`. It is a **read-only evidence projection**, not a planner, dispatcher, approval issuer, runtime installation or guarantee of native Muse behavior.

## Status by feature

| ID | Original feature | Priority | Dependencies | Evidence grade | Next independent verification |
| --- | --- | --- | --- | --- | --- |
| H00 | Source and fleet preflight | P0 | — | `PARTIAL_SOURCE` | Recheck original A (offline), independent B/C and live repository main |
| H01 | Rights and source catalog | P0 | H00 | `PARTIAL_SOURCE` | Independently review every proposed mirrored item and rights ledger |
| H02 | Public discovery experience | P0 | H01 | `SOURCE_MERGED_NOT_DEPLOYED` | Hosted standalone Muse Hub domain, browser/keyboard/CSP and link tests |
| H03 | 258/402 route compatibility | P0 | H00 | `SOURCE_MERGED_CI_VERIFIED` | Any later live provider claim requires separate scoped native readback |
| H04 | Personal Muse terminal | P0 | H03 | `PROVIDER_BLOCKED` | Qualified official Muse pairing/readback; previous gateway registry 502 must be reobserved |
| H05 | Muse-to-local coding bridge | P0 | H00 | `NOT_VERIFIED` | Read original bridge code and run read-only disposable project with exact task ID |
| H06 | Browser-operated MCP fallback | P1 | H02 | `NOT_VERIFIED` | Owner-scoped browser and MCP tool-list/readback under exact profile |
| H07 | Official gadget and TypeScript SDK | P1 | H02 | `NOT_VERIFIED` | Independently qualified Gadget pairing and correct SDK pin, no token copying |
| H08 | Desktop Commander setup | P0 | H02 | `CONNECTED_TOOL_NOT_HUB_INSTALLED` | Qualify reusable Muse Hub setup with exact device, permissions and uninstall |
| H09 | CUA Driver cross-host bridge | P0 | H08 | `NOT_VERIFIED` | Device-owner OS consent, wrong window/locked screen and target proof |
| H10 | Tailscale/local shell gateway | P1 | H08 | `NOT_VERIFIED` | Container/egress tests on owner-controlled host; no public bind |
| H11 | Neutral five-door engineering workflow | P0 | H00 | `SOURCE_ONLY_NATIVE_NOT_VERIFIED` | Independently source-test current kit; original owner/recipient and production S5 still require actual authority |
| H12 | Neutral Family Link envelope | P0 | H00 | `SOURCE_MERGED_NATIVE_NOT_VERIFIED` | Independent real recipient identity, consent, transport admission, ACK and durable replay fence |
| H13 | Cross-role plan to selected transport | P1 | H04, H05, H09, H12 | `PROVIDER_BLOCKED` | One independently authenticated recipient outcome or NOT_PROVEN without dispatch |
| H14 | Neutral Companion Home rooms | P0 | H00 | `PRIVATE_DONOR_NOT_HUB` | Rights-clean neutral room UI and native/browser responsive scene QA |
| H15 | Portable animation director | P1 | H14 | `PRIVATE_DONOR_NOT_HUB` | Independent deterministic frame tests, phone render and continuity review |
| H16 | Rights-reviewed Arcade | P1 | H14 | `PRIVATE_DONOR_NOT_HUB` | Per-game license/source ledger and actual mobile gameplay smoke tests |
| H17 | Notebook persistence | P1 | H14 | `NOT_VERIFIED` | Separate notebook acceptance; existing Daily Desk alone is not this feature |
| H18 | Apple Watch/Gadget expansion | P2 | H07 | `NOT_VERIFIED` | Paired watch Wi-Fi/cellular/readability, wrong/unpaired rejection |
| H19 | Installation and recovery journeys | P1 | H02, H05, H08, H11, H12 | `SOURCE_JOURNEYS_TESTED_HOST_NOT_VERIFIED` | Host-qualified first-use and recovery route checks for each feature |
| H20 | End-to-end gate with negative cases | P0 | H13, H14, H16, H17, H19 | `NOT_VERIFIED` | Owner-authorized target, runtime identities, device and original witness across supported routes |
| H21 | Distribution and release | P0 | H20 | `RELEASE_NOT_READY` | Complete H20, independent public QA and release/deploy authorization; keep v1.1.0 draft |

## What has landed versus what is still missing

- **Public source:** H03 historical CLI route comparator was merged after protected CI; H12 offline Family Link contract/ZIP was merged after protected CI. H02's public explorer and initial website source exist in Git, but the separate Muse Hub property has **not** been deployed. H11 adds a *source-only* 25-route contract and a real disposable RED→GREEN→local S5 review demonstration; this cannot authenticate an original donor worker or alter a live controller.
- **Source rights:** H01 includes a source/rights research ledger, but a donor link alone does not grant code/media redistribution. The private original agents, ROMs and owner credentials stay out of public output.
- **H12 remains operationally incomplete:** It validates role/receiver **shape** and blocks synthetic replay; it does **not** establish independently authenticated sender/receiver, consent, delivery, a durable replay fence or original recipient acknowledgment.
- **Original `T12` remains OPEN:** The private original TaskGuard release-before-terminal and retention independent witness problems require their owner's actual mutating controller fix and independent runtime acceptance, or a production policy disabling destructive prune. A hash chain on the same owner-writable storage is insufficient.
- **Native Muse auth:** Previous Gadget gateway registry lookup returned `fail_ip_registry_not_found`; current owner-app known-chat and recipient readback are **NOT VERIFIED**. A healthy local shell or Desktop Commander device is not native Muse authentication.
- **Site and release:** The standalone Hub site is code under `hub/site/`, not a deployed public URL. Published v1.0.0 remains distinct from the unpublished v1.1.0 draft. H20 seven-scenario runtime acceptance and H21 final distribution acceptance are not complete.

## Production holds — do not bypass

**`T12_TASKGUARD_TERMINAL` — OPEN.** Original donor mutating TaskGuard can release claim without verified terminal and skip corrupt receipt. Required closure: Owner-authorized mutating repair, fail-closed claim/release under corruption, fenced terminal, independent recipient readback.

**`T12_RETENTION_WITNESS` — OPEN.** Local owner-writable ledger and checksum anchor can disappear or be rewritten together. Required closure: Host-owned durable tombstone or recipient idempotency with monotonic fence; otherwise production PRUNE_DISABLED.

**`NATIVE_MUSE_AUTH` — OPEN.** Previous paired Gadget provider websocket upgrade failed with fail_ip_registry_not_found; no qualified current known-chat readback. Required closure: Original owner paired Muse app/provider transport read-only qualification, independent wrong account rejection.

**`H12_REAL_RECIPIENT` — OPEN.** Offline envelope and distinct local processes do not authenticate actual cross-account recipients. Required closure: Independent sender+recipient identity, actor-specific consent, original transport and ACK plus durable replay prevention.

## Verification contract

Each row's `minimum_acceptance`, `next_verification`, `source_paths`, and separate native/runtime flags are in the [machine-readable companion](discovery/hub-feature-status.json). A source file's existence can qualify that file's presence only; it cannot promote a native, provider, device or release result. Preserved source/test receipts may support a narrower grade, not blanket completion. Maintain the original owner and original security authority for effects and claims.

For H11 see the [five-door contract](../kits/engineering-doors/README.md); for H12 see the [Family Link offline contract](../kits/family-handoff/README.md). The site remains an [offline source preview](../hub/site/index.html). Read [public release status](RELEASES.md) before advertising download availability.
