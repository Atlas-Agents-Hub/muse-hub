# Review a calendar change

Use this sheet to make room for a useful task while protecting the commitments around it. Start with the current calendar entry and choose whether the change affects one occurrence or the whole series.

## Your calendar review

```text
Account and calendar:
Event title and ID or link:
Recurring series ID, if available:
Occurrence being reviewed, using its original date and time:
Change scope: this occurrence / the series
Attendees and any intended invitation update:

Current start and end, with time zone:
Proposed start and end, with time zone:
Reason for the change:
Fixed commitments before and after:
Preparation, travel and recovery time needed:
Remaining free time after those buffers:

Chosen action:
Result returned by the calendar:
Updated event start, end and time zone:
Series or adjacent occurrences checked:
Last checked at:
```

Read the relevant day before choosing a new slot. Count overlapping busy periods once, retain each event's identity and convert times to the same time zone for comparison. Leave the original event and the proposed change visible until the calendar confirms the result.

## Filled example: move one weekly project review

This example uses a personal calendar block with no other attendees.

| Field | Example |
| --- | --- |
| Calendar and event | Work · Project review · series `project-review` |
| Occurrence | November 27, 2026, originally 15:00–15:30, Europe/London |
| Change scope | This occurrence only |
| Proposed time | November 27, 16:00–16:30, Europe/London |
| Reason | A fixed client call runs from 15:00 to 15:45. |
| Preparation | 15 minutes immediately before the review: 15:45–16:00. |
| Next commitment | A 17:00 appointment, with 20 minutes of travel needed after the review. |
| Fit | Review ends at 16:30; travel ends at 16:50; ten minutes remain before the appointment. |
| Chosen action | Move the November 27 occurrence to 16:00 and keep its 30-minute duration. |
| Readback to save | The changed occurrence at 16:00–16:30 and the December 4 occurrence still at 15:00–15:30. |

Give Muse the request with the actual calendar entry:

```text
Move only the November 27 Project review on my Work calendar from
15:00–15:30 to 16:00–16:30, Europe/London. Keep the other weekly occurrences
at their current time. Show the updated November 27 entry and the next
occurrence after the change.
```

Save the resulting event details in the worksheet. For an event with other attendees, include the intended invitation update in the request before changing it.

## If the calendar changed while you were planning

Refresh the target event and its neighboring commitments. Recheck the duration and buffers against the current day. If a new conflict occupies the proposed slot, choose another slot or retain the current event and explain the remaining conflict.

After an interrupted change, open the same event before retrying. Use its series identity and original occurrence time to find a moved instance. If it is already at the chosen time, save that result. Check an adjacent occurrence when the change was meant for only one date.

[Daily Briefing](SKILL.md) · [Reminders](REMINDERS.md)
