# Use Muse from your terminal

Chat with your personal Muse through `muse-cli`, or run Muse Hub's specialist tools from a source checkout. Pick the section for the task you want to do.

## Chat with your personal Muse

The [muse-cli project](https://github.com/nikships/muse-cli) provides terminal chat, side-chat navigation, message history, and file commands for your personal Muse account. Its command is **`muse-cli`**; **`muse`** is used by the separate Muse Code product on many machines.

### If your connection is already set up

```sh
muse-cli --version
muse-cli status
muse-cli threads
muse-cli history --limit 5
muse-cli chat
```

`status` shows the connected identity and account information. `threads` lists Main and side chats. `history` reads recent messages. `chat` opens an interactive conversation; type `/help` for navigation commands.

To read one side chat, take its session ID from `threads` and replace `SESSION_ID` below:

```sh
muse-cli history --thread SESSION_ID --limit 5
```

### Install and connect

The CLI requires Python 3.10+ and your own signed-in Muse account. With [uv](https://docs.astral.sh/uv/) installed:

```sh
uv tool install muse-cli
```

The upstream guide also supports `pipx install muse-cli` and `pip install muse-cli`. Follow its [current installation and login instructions](https://github.com/nikships/muse-cli#quick-start) for your platform.

**macOS with Chrome, Brave, Arc, Edge, or Chromium:** sign in to [muse.ai](https://muse.ai/) in your browser, then run:

```sh
muse-cli auth export
muse-cli status
```

macOS may ask for access to the browser's Safe Storage key. Choose the browser explicitly with `muse-cli auth export --browser chrome` when needed.

**Windows or Linux:** the upstream login flow uses Node.js, `agent-browser`, and Chrome 144 or newer. Install the browser helper, open your existing Chrome profile, enable its remote-debugging option at `chrome://inspect/#remote-debugging`, and keep your signed-in `muse.ai` tab active. Then run:

```sh
muse-cli auth export --browser agent-browser
muse-cli status
```

Use the [upstream Windows/Linux setup steps](https://github.com/nikships/muse-cli#linux-windows-or-safari-agent-browser-or-by-hand) for the helper installation and browser connection. The login export saves session cookies in your private CLI configuration. Keep that file out of chats, Git repositories, and shared ZIPs. If your login expires, repeat the export for your own account.

These commands and requirements follow the [upstream README](https://github.com/nikships/muse-cli/blob/b62adbabb77abf688d26a74f93d405b6667dbc9f/README.md) and [package definition](https://github.com/nikships/muse-cli/blob/b62adbabb77abf688d26a74f93d405b6667dbc9f/pyproject.toml). Account-specific features and updated setup details are documented by that project.

## Run Muse Hub tools

Use Python 3.12+ for the repository tools. Git is needed to clone the project and for workflows that work on repositories. Commands below work in PowerShell, macOS Terminal, and Linux shells; use `python3` if that is your Python command.

```sh
git clone https://github.com/Atlas-Agents-Hub/muse-hub.git
cd muse-hub
python -B quickstart.py --all
```

The check prepares and inspects temporary packages for all 15 assistants and their 45 subchats. To keep an editable kit, choose a new absolute destination:

```sh
python -B quickstart.py --role personal-companion --to "$HOME/my-assistant-kit"
```

### Choose a starter or run a tool

Search across skills, workflows, starters, specialists, connectors and tool guides, then create a pack for your project:

```sh
python -B tools/discover.py search "sql query" --role data-engineering-architect
python -B tools/discover.py plan --skill query-plan-review --workflow pipeline-validation
python -B tools/discover.py build --skill query-plan-review --workflow pipeline-validation --to "$HOME/my-data-toolkit.zip"
```

The [finder and custom toolkit guide](collection/FIND_AND_BUILD.md) covers filters, specialist selection, supporting files and reusable exports.

```sh
python -B tools/muse_collection.py show daily-planner
python -B tools/muse_collection.py build daily-planner --to "$HOME/daily-planner.zip"
python -B tools/muse_collection.py demo data-engineer
python -B tools/muse_collection.py workflow-demo pipeline-validation
```

The starter command creates a ZIP for your assistant. The data and workflow examples print reports from the supplied sample inputs. For your own inputs and portable executable kits, follow the [specialist tool guide](collection/SPECIALIST_QUICKSTART.md).

### Open your notebook

Choose an absolute database path in an existing private directory, then run:

```sh
python -B examples/space_starter.py --serve --companion-home --database "$HOME/companion-notes.sqlite3"
```

Open the local URL printed by the command and enter its session token in Notebook. Keep the terminal running while you work. Press Ctrl+C to stop it; restarting with the same database reopens your notes. [Companion Home](COMPANION_HOME.md) covers rooms, conflicts, and recovery.

## Troubleshooting

| Problem | Next step |
| --- | --- |
| `muse-cli` is missing | Install the CLI, reopen your terminal, and check the command's location. |
| The CLI login has expired | Sign in to your own Muse account and repeat the upstream login export. |
| A feature returns an account-specific error | Check the feature's availability in your Muse account and the upstream command guide. |
| A toolkit command cannot find a file | Run it from the repository root. |
| `ModuleNotFoundError` in a lower-level example | Follow that example's `PYTHONPATH` instructions in [Workflows](WORKFLOWS.md). |
| An export destination exists | Choose a new path and keep your existing work. |
| The local notebook will not open | Use the URL from the current terminal session on the same computer. |

[Get started](GETTING_STARTED.md) · [Assistant downloads](DOWNLOAD_A_SPECIALIST.md) · [Developer quickstart](GITHUB_QUICKSTART.md)
