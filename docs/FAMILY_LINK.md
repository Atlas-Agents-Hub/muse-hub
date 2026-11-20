# Family Link

Link two Muse personal assistants so they can communicate through a connection you configure. One assistant can send a request with the relevant context, and the other can return a result. Each assistant keeps its own notes, preferences, and memory.

For example, one Personal Companion can ask another to coordinate a family event. Share the date options and what you need confirmed, then bring the answer back to the requesting assistant.

## Link two personal assistants

1. Set up a [Personal Companion](../presets/personal-companion/INSTALL.md) for each person or workspace.
2. Choose a [connection](CONNECTORS.md) both sides can use and configure the accounts and permissions it needs.
3. Use Family Link to prepare and review a request for the other assistant. Send it through that connection and return the reply to the requesting assistant.

The same handoff format works when a Personal Companion needs help from a specialist.

## Prepare a useful handoff

1. Choose the receiving specialist and the capability needed for the task.
2. Include a concise request, the relevant source material, and a result the recipient can check.
3. Keep the recipient's own preferences and memory in place.
4. Review the handoff, then share it through the service or account connection you have chosen.
5. Read the returned result and confirm the task's outcome before continuing.

The role packages include suggested receiving roles. Configure the connection when you need to send work, using the account and permissions for that service. [Connector setup](CONNECTORS.md) covers the available routes.

## Try the handoff tool

From the repository root with Python 3.12+:

```sh
PYTHONPATH=src python3 -B examples/family_offline_handoff_demo.py
```

In Windows PowerShell, set `$env:PYTHONPATH = "src"` and use `python -B`.

The example prepares a handoff and reviews it in a separate process. It checks role compatibility, request identifiers, replay declarations, and recipient context using supplied data. Its result is a proposal for review; use your chosen connection for delivery.

The [portable handoff kit](kits/FAMILY_LINK_SOURCEKIT.md) includes the example and role policies. Developers can inspect `muse_presets.family.propose_handoff` and the [envelope contract](../kits/family-handoff/envelope-contract.json) for exact fields.

## Recover an interrupted handoff

Keep the request ID, expected recipient, and latest result. Check the original service's message or task status before resending work whose outcome is unclear. Confirm the recipient and current scope before continuing after a permission change.

[Coordinator](../presets/coordinator/INSTALL.md) · [Workflows](WORKFLOWS.md) · [Connectors](connectors/README.md)
