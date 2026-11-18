# Muse Hub — H19 installation and recovery journeys

**Source-only onboarding, not native Muse installation.** The H19 journey tool reads the public **H00–H21** readiness register and the **15 independent specialist guides**. It provides a conservative seven-phase first-use/recovery checklist without connecting accounts, starting a model, installing a Muse agent, changing credentials, running commands or writing files.

## Run from the checked-out public source

Python 3.12+ is sufficient. No additional packages or API credentials are needed.

    python -B tools/hub_journeys.py --verify
    python -B tools/hub_journeys.py --all --format markdown
    python -B tools/hub_journeys.py --feature H19 --role learning-coach
    python -B tools/hub_journeys.py --feature H11 --role software-engineer

The `--verify` command checks the 22-feature register, dependency graph, source paths and 15 role-specific `INSTALL.md` guides. It **does not** verify installed Muse runtime behavior. `--all` produces JSON journeys for every feature; `--format markdown` prints a readable table. A forged role, unknown feature, missing source, duplicate ID, dependency cycle, unsafe source path or unsupported native claim is refused. No command changes the checkout.

## Seven phases for each feature

1. **install:** inspect existing source or report `BLOCKED_NO_PUBLIC_SOURCE`; this is never a native install.
2. **configure:** read `presets/<role>/INSTALL.md` and [host compatibility](../HOST_COMPATIBILITY.md). Main and three subchats require separate supported host setup.
3. **health:** verify reviewed source files exist locally; this does not imply a working provider/device connection.
4. **named_test:** run the named source regression where available. Without a qualified test, report `NOT_VERIFIED` rather than inventing a receipt.
5. **failure:** preserve an ambiguous outcome as `HOLD_UNKNOWN`; never blindly retry an unknown external effect.
6. **stop:** the journey starts no background worker. Stop only an owned process after reconciling identity and side effects.
7. **uninstall:** remove only verified disposable local output. Remote jobs, accounts and host registrations require owner-authorized revocation.

The tool is a **read-only source planner**, not a second installer, Claim Gate, transport selector or execution authority. For disposable source packaging, use the existing `python -B quickstart.py --role learning-coach` command. For create-only staging, see [Installation and saved data](../INSTALL_AND_PERSISTENCE.md).

## Feature-specific boundaries

- **H02:** standalone Muse Hub website source exists, but the site is **not deployed**. Source browser checks do not prove hosted Pages behavior.
- **H03/H11/H12:** offline route, five-door and Family Link contracts exist; source tests do not authenticate original Muse identities or authorize external actions.
- **H04–H10/H13:** provider, device and bridge acceptance requires the original authorized host. Desktop Commander availability alone does not prove Muse authentication.
- **H14–H17:** Companion Home, animation, Arcade and notebook require separate rights, persistence and gameplay acceptance; no private donor assets or unlicensed ROMs may be published.
- **H18:** paired Apple Watch/Gadget behavior is not established by static source.
- **H19:** this index covers 22 feature IDs and 15 role guides; host-qualified first-use and recovery remain outstanding.
- **H20:** seven-scenario end-to-end acceptance, independent recipients, wrong-target refusals and original device witnesses remain outstanding.
- **H21:** the standalone site, release acceptance and v1.1.0 individual ZIPs are not deployed/published. Published v1.0.0 assets are separate.

The original TaskGuard terminal/retention durable-witness holds and H12 real-recipient authentication remain open. A local hash or fixture is not native exactly-once evidence.

## Local Companion Notebook path

The [Companion Home guide](../COMPANION_HOME.md#use-the-real-local-notebook) now gives an explicit local launch, session entry, saved-note health check, revision-conflict recovery, stop/restart and database-preserving uninstall path. Use `examples/space_starter.py --serve --companion-home` with an owner-controlled absolute database path. This is one usable **local** journey, not completion of the CLI, coding bridge, desktop, five-door or authenticated Family Link setup paths.

H03 and H14?H17 now expose their existing named source tests through the journey tool. `SOURCE_TEST_AVAILABLE_NOT_RUN` means exactly that: displaying a test command does not execute it or prove native acceptance. The interactive Notebook's additional real HTTP tests are named in its guide.

## Failure and restart policy

Keep original packages, customization, memory, credentials and generated outputs separate. On recovery, inspect source and the original host before acting. Preserve unknown-effect evidence rather than replaying it. If source rights or integrity are uncertain, stop distribution. Do not modify the Atlas Origins website as part of Muse Hub deployment.

**Acceptance grade:** H19 source journey index and negative controls only. Host-qualified install, first-run, stop, uninstall and restart checks must be independently performed for each relevant provider/device route before H19 can be marked complete.
