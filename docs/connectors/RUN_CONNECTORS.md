# Use a connector with Muse

Choose a service in the [connector directory](CATALOG.md), open its guide, and give Muse the task you want to complete. The guide brings together account setup, service actions, inputs, useful events and a starting prompt.

## Inspect actions and inputs

From this directory, use Python 3.10 or later:

```console
python connector.py inspect trello
```

The result includes action IDs, input names, required fields, account settings and the provider request definitions. Choose the action that fits your task. Keep service IDs returned by lookups so the next step can use the exact record.

## Prepare a task

Save action inputs as a JSON object. For example, a file lookup might need a folder ID, file name and result limit. Use the exact input names shown by `inspect`.

```console
python connector.py plan trello ACTION_ID --inputs /absolute/path/inputs.json
```

The helper lists missing required inputs and provider fields that need to be resolved. It returns the action's request definition alongside the prepared values. Follow that definition to perform the operation through your connected service or automation setup.

## Make a direct HTTP read

Services with an included `http.json` also provide exact HTTP read requests. Their IDs appear under `http_reads` in the inspection result. Each request includes its URL template, input parameters and authentication header.

First prepare the request:

```console
python connector.py read gmail read-gmail-v1-users-me-profile
```

To run it, make an access token available through an environment variable supplied by your connection manager or local secret store. Pass the variable's **name** and a new absolute output path:

```console
python connector.py read gmail read-gmail-v1-users-me-profile --execute --token-env MUSE_GMAIL_TOKEN --output /absolute/path/gmail-profile.json
```

The result file contains the service, request ID, HTTP status and response. The command prints the saved file location and response size. For a request with path parameters, supply `--inputs /absolute/path/inputs.json`; the parameter names are listed in `http.json`.

## Continue a workflow

- Pass selected record IDs and useful result fields to the next specialist or workflow.
- For a create, update, send or publish task, review the target and proposed change before applying it.
- Keep page tokens when collecting additional results, and respect the service's rate-limit response.
- Save the result with its task so Muse can resume from the completed operation.

[Browse connectors](CATALOG.md) · [Muse Hub](../../README.md)
