# Organize your day

Turn the things on your mind into a plan, useful reminders and a place to keep your notes. Start in Muse, add a Personal Companion for your routines, and choose a workspace for the records you want to keep.

## 1. Give Muse a goal

Choose one outcome and a date. Replace the brackets in this prompt with your details:

```text
Help me work toward [GOAL] by [DATE]. My main constraints are [CONSTRAINTS].
Suggest milestones and the next three actions. Show how each action moves
the goal forward and what I should review at the end of the week.
```

[Muse's goals and ongoing assistance](https://muse.ai/) can help you keep that work moving. For each milestone, agree on a useful result, a next action and a review date.

## 2. Add your Personal Companion

[Download Personal Companion](../../presets/personal-companion/INSTALL.md), extract its ZIP and open `START_HERE.md`. Follow the guide to configure its assistant and three subchats, then add your preferences, commitments and current context.

Try this first task:

```text
Use the Personal Companion guide with these notes: [NOTES]. Help me choose
today's three priorities, identify the next action for each and list what
needs follow-up. Fit the plan around [AVAILABLE TIME AND COMMITMENTS].
```

If your plans depend on a calendar or task service, find it in [work and productivity connectors](../connectors/CATALOG.md#work-and-productivity). Follow its setup guide, choose your account and try a small check:

```text
Review tomorrow's calendar. Identify overlapping events and time I should
leave for preparation. Suggest changes for me to review.
```

## 3. Set reminders and recurring check-ins in Muse

Muse can send reminders and run recurring tasks. Include the date or recurrence, time and time zone in your request, then read the schedule it confirms. [Muse's reminder guide](https://www.meta.com/help/superintelligence/1484325780075655/) explains how to manage these from your conversation and the **Upcoming** tab.

For a weekly review:

```text
Every Sunday at 6:00 p.m. in [YOUR TIME ZONE], ask me to review the past week
and choose three priorities for the next one. Confirm the schedule.
```

For one follow-up:

```text
On [DATE] at [TIME] in [YOUR TIME ZONE], remind me to [ACTION]. Confirm the
date, time and reminder text.
```

Manage the schedule as your plans change:

| What you want to do | What to ask Muse |
| --- | --- |
| Check the schedule | "Show my active reminders and recurring tasks with their times." |
| Change a time | "Update my weekly review to Mondays at 7:00 p.m. in [TIME ZONE]. Keep it weekly." |
| Change the task | "Update my weekly review to include a check of [GOAL]. Keep its current schedule." |
| Cancel it | "Cancel my weekly review reminder." |

After a change, check the confirmation and the updated list. You can also open your assistant's **Upcoming** tab. After an interrupted reply, inspect the existing schedule before creating another reminder.

## 4. Give your plan a home

For a workspace inside the Muse app, ask Muse to create a Space for your routine:

```text
Make a Space for my weekly plan with my current goal, today's priorities,
upcoming commitments and a place for review notes.
```

Muse supports custom planners, trackers and dashboards, with Spaces available in the app's sidebar or main tabs. See [Meta's Muse app description](https://apps.apple.com/us/app/muse-from-meta/id6760173601).

For a workspace on your computer, choose [Daily Desk](../spaces/DAILY_DESK.md) for tasks and notes, or [Companion Home](../COMPANION_HOME.md) for notes organized across five rooms.

Get a toolkit checkout and Python 3.12+ using the [terminal setup guide](../TERMINAL.md#run-muse-hub-tools). Run the command from the toolkit root, choosing an absolute database path in an existing private directory. Choose the workspace you want to open:

```sh
python -B examples/daily_desk.py --serve --database "$HOME/daily-desk.sqlite"
```

```sh
python -B examples/space_starter.py --serve --companion-home --database "$HOME/companion-notes.sqlite3"
```

These commands work in PowerShell, macOS Terminal and Linux shells; use `python3` where that is your interpreter name. Open the printed URL in a browser on the same computer and enter the current session token. Keep the terminal open while you work.

Muse brings you back with reminders; Daily Desk and Companion Home keep your saved records. Stop either workspace with Ctrl+C. Restart with the same database path and enter the new token to reopen your work. Daily Desk's **Download backup** button gives you a copy of its tasks and notes.

## 5. Review and adjust

At your weekly check-in, answer four questions:

- What moved the goal forward?
- What changed in my time, priorities or constraints?
- What are the next three useful actions?
- Which reminders should stay, move or finish?

Update the plan, save what matters and adjust the existing schedules. Before closing your workspace, check that your next reminder appears in **Upcoming** and that the task or note you wanted to keep appears in saved records.

[Muse Hub](../../README.md) · [Build and automate](BUILD_AND_AUTOMATE.md) · [Create something](CREATE_SOMETHING.md)
