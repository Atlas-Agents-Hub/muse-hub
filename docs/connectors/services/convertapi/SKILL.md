---
name: convertapi-connector
description: "Convert, merge and split documents, images and PDFs with 300+ file converters."
---

# ConvertAPI for Muse

Convert, merge and split documents, images and PDFs with 300+ file converters.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **ConvertAPI**.
2. Configure **API key or access token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.


[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/convertapi/src/index.ts).

## Actions

### Convert File

Convert a file to another format with any of ConvertAPI's converters, such as Word to PDF or PDF to JPG. Extra file inputs (like a template or overlay file) are not supported here; use Custom API Call for those.

| Input | What to provide | Required |
| --- | --- | --- |
| `from` | The format of the file you are converting. | Yes |
| `to` | What to convert the file into. | Yes |
| `file` | The file to convert. | Yes |
| `additionalFiles` | Files to add after the main one, for converters that combine files. | Yes |
| `options` | Options of the chosen converter. Leave empty for the defaults. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/convertapi/src/lib/actions/convert-file.ts).

### Merge PDF Files

Combine several PDF files into one PDF, in the order you list them.

| Input | What to provide | Required |
| --- | --- | --- |
| `files` | Add the PDFs in the order they should appear. At least two are needed. | Yes |
| `fileName` | Merged file name, without the extension. Leave empty for a default. | Optional |
| `password` | Only needed if the PDFs are password-protected. Used for every file. | Optional |
| `bookmarksTableOfContents` | Add a top-level bookmark for each merged file. | Optional |
| `pageSize` | Scale every page to this size, or keep the original size. | Optional |
| `pageOrientation` | Rotate every page to this orientation, or keep the original. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/convertapi/src/lib/actions/merge-pdf.ts).

### Split PDF File

Split a PDF into several PDFs by page count, page ranges, single pages, matching text or bookmarks.

| Input | What to provide | Required |
| --- | --- | --- |
| `file` | The PDF to split. | Yes |
| `mode` | How the PDF is cut into parts. | Yes |
| `valueHelp` | Value Help | Optional |
| `value` | What to split on. The format depends on the Split By mode. | Optional |
| `mergeOutput` | Join the parts back into one PDF, e.g. to extract selected pages. | Optional |
| `password` | Only needed if the PDF is password-protected. | Optional |
| `fileName` | Base name for the parts, without extension. Each part gets a number. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/convertapi/src/lib/actions/split-pdf.ts).

## Try it

> Use ConvertAPI to convert file. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
