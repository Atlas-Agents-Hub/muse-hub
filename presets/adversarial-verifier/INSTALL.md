# Adversarial Verifier | Muse Hub

Challenge authorized releases with negative controls and reproducible evidence.

**Current published source:** [v1.0.0](https://github.com/atlas-origins/muse-ai-agent-presets/releases/tag/v1.0.0) · **Individual assistant ZIP:** `muse-adversarial-verifier-v1.1.0.zip` (v1.1.0 draft; not yet a public download).

## Set up this assistant

1. Choose a **separate Muse assistant** for Adversarial Verifier. Don't combine multiple specialists in one account.
2. When v1.1.0 is published, download the individual ZIP and open its `START_HERE.md`.
3. Start in **Main** with the supplied identity and instruction documents.
4. Set up its **three subchats** inside this same assistant. Each subchat has its own instructions, user context, tools, and memory files.
5. Keep credentials and personal memory outside public GitHub. Any service connection must be authorized separately.

**First task to try:** "Review this proposed release for failure modes, unsafe effects, and missing tests."

No Python is needed to set up the assistant. For the **current published v1.0.0 source release**, follow [the source setup guide](../../docs/GITHUB_QUICKSTART.md) instead of assuming the draft ZIP is already available.

## Optional source tools

For a development copy, use the reviewed [source generator](../../examples/github_quickstart.py) (`examples/github_quickstart.py`) and the [developer setup guide](../../docs/GITHUB_QUICKSTART.md). These require a trusted source checkout, not a preconfigured Muse account.

See [this specialist's capability scope](../../docs/collection/SPECIALIST_SCOPE_AND_ENGINES.md) and [the local tool guide](../../docs/CAPABILITIES.md). Local scripts run under the computer's permissions; they are not native Muse registrations.

Source role ID: `adversarial-verifier`.

## More help

[Choose another specialist](../../docs/DOWNLOAD_A_SPECIALIST.md) · [Saved data and updates](../../docs/INSTALL_AND_PERSISTENCE.md) · [Muse Hub product scope](../../hub/README.md)

Downloading a ZIP or copying a profile does **not automatically** create a Muse account or subchat, grant tool access, or connect external services.
