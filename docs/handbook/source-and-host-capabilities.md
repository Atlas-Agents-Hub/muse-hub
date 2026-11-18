# Choose tools for your task

Start with the result you need, then choose the method, local program, or service that produces it.

| Your task | Useful starting point |
| --- | --- |
| Follow a repeatable method | Choose a skill and give your assistant its instructions and inputs. |
| Calculate or inspect supplied data | Run a specialist tool and open its report. |
| Work with a service | Configure its connector, choose the account, and run a small check. |
| Work in a browser or on a desktop | Use the available browser or desktop tool for the intended application. |
| Carry work between specialists | Prepare a Family Link handoff and share it through your chosen connection. |

## Try the local tools

From the toolkit root with Python 3.12+:

```sh
python -B tools/muse_collection.py demo automation-engineer
python -B tools/muse_collection.py workflow-demo pipeline-validation
```

Read the report to see the stages that ran, their outputs, and the remaining handoffs. Supply your own reviewed inputs using the [specialist tool guide](../collection/SPECIALIST_QUICKSTART.md).

## Check the intended result

Open the generated file or read the result from the original service. For a change, confirm the intended account, target, and outcome. Keep the request or operation ID if you may need to resume later.

If a response is lost, inspect the original status before repeating the action. If access changes, use the service's setup process to reconnect the correct account and scope.

## Add a connection when needed

The [connector directory](../connectors/README.md) links to each service's setup guide. Use secure account setup and choose the permissions your task needs. [Host setup](../HOST_COMPATIBILITY.md) covers tool configuration; [Terminal](../TERMINAL.md) covers personal Muse chat and toolkit commands.

[Skills](../SKILLS.md) · [Tools](../CAPABILITIES.md) · [Family Link](../FAMILY_LINK.md)
