# Companion Home — neutral five-room source (H14–H17)

This is an **independent, source-only** Muse Hub product demo. It is **not a native Muse room**, an authenticated Muse account, a room-local chat transport, or a service running in the background.

## Five configurable rooms (H14)

The reviewed catalog in `examples/companion_home/rooms.json` defines five neutral rooms:

| Room | Feature surface | What actually works |
| --- | --- | --- |
| Focus Room | Local checklist | Marks one visual focus in this browser tab; does **not** schedule a real task |
| Notebook | Owner/Space-scoped notes | Static preview links to the reference; the explicit local Notebook mode creates, edits and deletes real SQLite notes |
| Garden | Calm original scene | CSS-only geometric landscape; no donor art or external assets |
| Arcade | Original Signal Trail | Keyboard/touch tiles, Back navigation, locally saved score |
| Studio | Neutral pose director | Four deterministic geometric poses, pause/resume and reduced-motion support |

`rooms.js` is deterministically generated from `rooms.json`; run `python -B scripts/build_companion_rooms.py --check` to detect drift. Labels, room IDs, theme choices and feature IDs are source-reviewed rather than pulled from an untrusted network feed.

## Run the UI locally

From a checked-out Muse Hub repository:

```sh
python -B scripts/build_companion_rooms.py --check
python -B -m http.server 8766 --bind 127.0.0.1 --directory .
```

Then browse **http://127.0.0.1:8766/examples/companion_home/** from that same authorized computer. Stop the manually started server to end the preview; this command binds only to localhost, not to a public interface. Opening `examples/companion_home/index.html` directly can also work, but browser storage under `file://` varies.

The page has a Content Security Policy blocking network fetches and remote scripts. Its global Muse assistant remains **external**; no `ConversationTransport`, `ROOM_CHAT` or `RoomChatWelcome` is installed or included. The five rooms are self-contained source UI, not provider-issued room identities.

## Use the real local Notebook

The interactive mode is **default OFF**, reuses `space_server.make_server`, and is separate from the network-disabled static preview. It keeps all five rooms, the original game and the motion controls. It does not start another daemon, install a Muse agent or connect a provider.

Create an owner-controlled directory **outside the source checkout**. From the repository root, use Python 3.12+:

```sh
python -B examples/space_starter.py --serve --companion-home --database "/absolute/owner-controlled/notes.sqlite3"
```

Replace the database path with a real absolute path whose parent directory exists. On Windows, an absolute path such as a file within your private user directory is supported. The existing launcher adds `src` to its import path; no new package installation is required.

Open the **127.0.0.1 URL printed by that launch**, select Notebook, and enter its temporary local session token. Never paste that token into chat, screenshots or source files. The launcher prints it only to its local console. The token remains in the page's memory, not in a URL, localStorage or sessionStorage. This is an OS-user-controlled development session, **not Muse authentication**.

Select the room in which to keep a note, type your text and choose **Save note**. The interface confirms saving only after a server readback. Select a saved note to edit it; the expected revision prevents an older editor from overwriting newer content. Deletion asks for confirmation and preserves a revision tombstone. It is not secure erasure.

**Recovery:** if a request times out or its reply is lost, the page preserves the draft and blocks another write. Choose **Refresh saved notes** to inspect original state. It never automatically retries a save or deletion. A stale-edit conflict also preserves the draft: read the saved revision before explicitly opening it or starting a new note. Navigating away clears page memory, and late replies cannot refill the locked view.

**Stop and restart:** press Ctrl+C in the terminal that started this server. This closes its listener and revokes that server's token. Start the same command with the same database path to reopen notes; use the newly printed token. **Lock Notebook** clears this page's notes/draft/token but does not revoke another already-open tab or erase the database. An inaccessible server requires stopping only that original run-owned process, not all Python processes.

**Uninstall:** stop the owned server first. Keep or back up the database under the owner's storage policy; removing application source does not delete notes. Do not delete unknown databases or overwrite an existing store to restore a snapshot. The original Python snapshot/restore demonstration below restores into a new empty store, not through an unrestricted browser upload.

The local API exposes only `POST /api/room/list`, `/api/room/put` and `/api/room/forget` in this mode. It rejects extra identity/path fields, wrong Host/Origin, missing session authorization, changed owner/Space and invalid revisions. Browser requests cannot access claim/callback/native dispatch routes. Existing Space and Daily Desk modes remain unchanged.

## Portable neutral animation (H15)

`home.js` composes a pure four-pose sequence of original CSS shapes. The Studio provides Pause, Resume and Next pose controls, with visible `aria-pressed` and live status. An operating-system `prefers-reduced-motion: reduce` setting prevents autoplay. A hidden tab pauses the animation; no character skin, video, sprite sheet or third-party media is redistributed.

This is a local director, not a private original animation engine or a native Muse scene renderer.

## Original rights-clean Arcade (H16)

Signal Trail is new original source code in `examples/companion_home/home.js`, distributed under the repository MIT license. Its individual rights statement is recorded in `examples/companion_home/arcade-rights.json`.

It uses four numbered tiles. Click/touch or keys **1–4** to select the highlighted tile; Escape or Back to Focus exits. The game stores only numeric `seed`, `turn` and `score` in that browser's `localStorage` (when allowed), never names, notes, chat content or credentials. It does **not** sync between devices, contain commercial ROMs or import third-party gameplay assets.

No broader game catalog is licensed by this one original title. Additional games require their own rights/source review and mobile gameplay tests.

## Notebook and recovery (H17)

The existing `PersonalCompanion` backend remains the sole owner/Space-scoped SQLite writer. The `RoomNotebook` adapter in `src/muse_presets/room_notebook.py` adds room prefixes and validates a versioned local snapshot, then delegates **atomic new-store restoration** to the existing SQLite transaction.

```sh
PYTHONPATH=src python -B examples/companion_home_notebook_demo.py
PYTHONPATH=src python -B -m unittest discover -s tests -p test_companion_home_h14_h17.py -v
```

On Windows PowerShell, set `$env:PYTHONPATH = "src"` before invoking Python.

The demo uses fictional data and a temporary real SQLite database. It verifies owner/Space isolation, note revision update, restart recovery, restoration to a **new empty store** preserving revisions, and refusal of duplicate or wrong-scope restoration. Malformed, duplicate, stale or cross-room records are rejected before mutations. Snapshots are in memory; exporting user notes to a file requires an explicit owner-controlled destination and separate privacy review.

The scope fingerprint and SHA-256 detect accidental corruption and mixups; **they are not authentication or encryption**. Real ownership must be authenticated by the hosting app at every call. SQLite is local and unencrypted; logical deletion does not prove secure physical erasure. No actual provider callback, cloud sync, native Muse login or background reminder is established.

## Test and release gates

- `python -B scripts/build_companion_rooms.py --check`: canonical room config parity.
- `PYTHONPATH=src python -B -m unittest discover -s tests -p test_companion_home_h14_h17.py -v`: room, notebook and source-contract negatives.
- `PYTHONPATH=src python -B -m unittest discover -s tests -p test_companion_room_http.py -v`: real HTTP/SQLite lifecycle, restart, scope, conflict and malformed-input tests.
- `PYTHONPATH=src python -B -m unittest discover -s tests -p test_companion_room_launcher.py -v`: explicit launcher mode and default-mode compatibility.
- `python -B scripts/check_public.py`: public source privacy/export gate.
- `tests/browser_companion_notebook.mjs` is an explicit Chromium CDP acceptance driver for an already-owned **synthetic** loopback fixture. It takes that fixture's connection JSON and a new output prefix; it does not launch a provider or attach to a personal browser. Its response-stage fault test verifies lost-acknowledgment recovery without a second write.
- Browser QA: room switching at 320 / 390 / 768 / 1440px, keyboard navigation, reduced-motion, Pause/Resume/Next pose, Arcade touch/keys/Back/save/reload and no unexpected external requests.
- Full repository tests on supported hosts, then new protected GitHub PR and required CI **before** describing this source as merged.
- Separate native Muse host identity, authorized room transport, OS accessibility and actual end-to-end effects remain **NOT VERIFIED**.

Do not describe this as a completed native H14–H17 installation or hosted service. The standalone Muse Hub marketing site, v1.1.0 draft release, original `T12` hold and Atlas Agents ownership migration are separate workstreams.
