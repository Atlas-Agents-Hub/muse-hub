---
name: google-slides-connector
description: "Google Slides: add slide, find presentations, get presentation."
---

# Google Slides for Muse

Google Slides: add slide, find presentations, get presentation.

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Google Slides**.
2. Configure **OAuth 2.0 account connection; Provider connection fields** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- Authorize account: <https://accounts.google.com/o/oauth2/auth>
- Token endpoint: <https://oauth2.googleapis.com/token>

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/index.ts).

## Actions

### Add Slide

Add a new slide with a layout, and optionally fill its title and body.

| Input | What to provide | Required |
| --- | --- | --- |
| `presentation_id` | Presentation_Id | See action definition |
| `layout` | Layout of the new slide, from the presentation's theme. | Yes |
| `position` | Where to put the slide, starting at 1 for the first slide. Leave empty to add it at the end. | Optional |
| `title` | Text for the slide title. Leave empty to keep the placeholder empty. | Optional |
| `body` | Text for the body (or the subtitle, on the Title slide layout). New lines start new paragraphs. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/add-slide.ts).

### Find Presentations

Search Google Drive for presentations by name and/or folder.

| Input | What to provide | Required |
| --- | --- | --- |
| `name_contains` | Return presentations whose name contains this text (case-insensitive). Leave empty to list all. | Optional |
| `folder_id` | Folder_Id | See action definition |
| `limit` | Maximum number of presentations to return (1-${MAX_LIMIT}). Default 50. | Optional |
| `page_token` | The nextPageToken of a previous call, to get the next results. Leave empty for the first page. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/find-presentations.ts).

### Get Presentation

Get all slides from a presentation

| Input | What to provide | Required |
| --- | --- | --- |
| `presentation_id` | The presentation ID (between /d/ and /edit in its URL), or the full URL. | Yes |
| `fields` | Optional Google field mask to return only part of the presentation, e.g. presentationId,title,slides(objectId). Leave empty for the full presentation. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/get-presentation.ts).

### Get Presentation Outline

Get each slide's number, object ID, title, text and speaker notes.

| Input | What to provide | Required |
| --- | --- | --- |
| `presentation_id` | Presentation_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/get-presentation-outline.ts).

### Get Slide

Get one slide with all of its elements.

| Input | What to provide | Required |
| --- | --- | --- |
| `presentation_id` | Presentation_Id | See action definition |
| `slide_number` | Slide_Number | See action definition |
| `slide_object_id` | Slide_Object_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/get-slide.ts).

### Get Slide Thumbnail

Get a PNG image of a slide, as a link and optionally as a file.

| Input | What to provide | Required |
| --- | --- | --- |
| `presentation_id` | Presentation_Id | See action definition |
| `slide_number` | Slide_Number | See action definition |
| `slide_object_id` | Slide_Object_Id | See action definition |
| `size` | Width of the image. | Optional |
| `save_as_file` | Also download the image and return it as a file (the image link expires after about 30 minutes). | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/get-slide-thumbnail.ts).

### List Slide Elements

List the elements on one slide with their position, size and text, in points.

| Input | What to provide | Required |
| --- | --- | --- |
| `presentation_id` | Presentation_Id | See action definition |
| `slide_number` | Slide_Number | See action definition |
| `slide_object_id` | Slide_Object_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/list-slide-elements.ts).

### Move Slide

Move a slide to a new position in the presentation.

| Input | What to provide | Required |
| --- | --- | --- |
| `presentation_id` | Presentation_Id | See action definition |
| `slide_number` | Slide_Number | See action definition |
| `slide_object_id` | Slide_Object_Id | See action definition |
| `position` | Position the slide should end up at, starting at 1 for the first slide. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/google-slides/src/lib/actions/move-slide.ts).

## Try it

> Use Google Slides to find presentations. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
