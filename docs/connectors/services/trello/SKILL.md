---
name: trello-connector
description: "Project management tool for teams"
---

# Trello for Muse

Project management tool for teams

## Start a task

Tell Muse the result you want, the account or workspace to use, and the records or files involved.
Use the actions below to choose a concrete operation. Resolve names to service IDs before preparing a change.

## Connect your account

1. Open the service connection in your Muse setup and choose **Trello**.
2. Configure **Service username and password or token** using the provider fields below.
3. Store credentials in the connection manager or your local secret store. Select the account and permissions for this task.
4. Start with a lookup or list operation. Keep the returned record IDs for the next step.

- **API Key** (`username`): Trello API Key
- **Token** (`password`): Trello Token

[Provider connection definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/index.ts).

## Actions

### Add Card Attachment

Adds an attachment to a card.

| Input | What to provide | Required |
| --- | --- | --- |
| `card_id` | From an earlier step, or the code after /c/ in the card's URL. | Yes |
| `attachment` | A file from an earlier step, or a public URL. | Yes |
| `name` | Shown on the card. Empty uses the file's own name. | Optional |
| `mime_type` | The MIME type. Empty lets Trello detect it. | Optional |
| `set_cover` | Only images can be card covers. | Optional |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card-attachment/add-card-attachment.ts).

### Create Card

Create a new card in Trello

| Input | What to provide | Required |
| --- | --- | --- |
| `board_id` | Board_Id | See action definition |
| `list_id` | List_Id | See action definition |
| `name` | Card Name | Yes |
| `description` | Markdown formatting is supported. | Optional |
| `position` | Empty adds the card at the bottom of the list. | Optional |
| `labels` | Labels | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card/create-card.ts).

### Delete Card

Deletes an existing card.

| Input | What to provide | Required |
| --- | --- | --- |
| `card_id` | From an earlier step, or the code after /c/ in the card's URL. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card/delete-card.ts).

### Delete Card Attachment

Deletes an attachment from a card.

| Input | What to provide | Required |
| --- | --- | --- |
| `card_id` | From an earlier step, or the code after /c/ in the card's URL. | Yes |
| `attachment_id` | From Get All Card Attachments or an earlier step. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card-attachment/delete-card-attachment.ts).

### Get All Card Attachments

Gets all attachments on a card.

| Input | What to provide | Required |
| --- | --- | --- |
| `card_id` | From an earlier step, or the code after /c/ in the card's URL. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card-attachment/get-card-attachments.ts).

### Get Card

Gets a card by ID.

| Input | What to provide | Required |
| --- | --- | --- |
| `cardId` | From an earlier step, or the code after /c/ in the card's URL. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card/get-card.ts).

### Get Card Attachment

Gets a specific attachment on a card.

| Input | What to provide | Required |
| --- | --- | --- |
| `card_id` | From an earlier step, or the code after /c/ in the card's URL. | Yes |
| `attachment_id` | From Get All Card Attachments or an earlier step. | Yes |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card-attachment/get-card-attachment.ts).

### Update Card

Updates an existing card.

| Input | What to provide | Required |
| --- | --- | --- |
| `card_id` | From an earlier step, or the code after /c/ in the card's URL. | Yes |
| `board_id` | Board_Id | See action definition |
| `changes_info` | Changes_Info | Optional |
| `name` | Card Name | Optional |
| `description` | Markdown formatting is supported. | Optional |
| `due` | Due Date | Optional |
| `closed` | On archives the card. Off keeps it open or restores it. | Optional |
| `position` | Empty keeps the card where it is in its list. | Optional |
| `labels` | Labels | See action definition |
| `list_id` | List_Id | See action definition |

[Request and response definition](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/actions/card/update-card.ts).

## Events and recurring work

- **[Card Deadline](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/triggers/deadline.ts)** — Fires a set time before each card's due date.
- **[Card Moved to List](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/triggers/cardMoved.ts)** — Fires when a card is moved into the chosen list.
- **[New Card](https://github.com/activepieces/activepieces/blob/5110199059649227b42a805020ab03ef429103aa/packages/pieces/community/trello/src/lib/triggers/newCard.ts)** — Fires when a card is created on the board or in the list.

Choose the event source, polling interval or webhook connection supported by your automation setup. Save event IDs to avoid processing the same event twice.

## Try it

> Use Trello to get all card attachments. Ask for any required account, workspace or record ID, then return the useful fields and a saved result I can reuse.

## Complete the task

- Match each input to the selected action in `adapter.json`; use its linked request definition for the HTTP method, endpoint and payload.
- For paginated results, retain the cursor and requested limit. Include the count and selected record IDs in the result.
- Before a create, update, delete, send or publish operation, show the target and proposed change for approval.
- On a validation error, correct the named input. On a rate limit, respect the provider retry interval. Reconcile an ambiguous write before retrying.
- Save the result with the service, operation, timestamp and resource identifiers so the next workflow can continue.

[Connector configuration](adapter.json) · [All connectors](../../CATALOG.md)
