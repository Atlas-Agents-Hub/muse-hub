import { createHash, timingSafeEqual } from "node:crypto";
import { definePrivilegedHandlers, type z } from "@hatch/space-sdk";
import { CALENDAR_KEYS, type CalendarKey } from "./calendar-config";
import { calendarEventResponse, privileged } from "./calendar-contracts";
import { readCalendarSettings, publicCalendarSettings, type CalendarSettings } from "./calendar-settings";
import { CalendarAdapterError, runCalendar, type CalendarRunner } from "./calendar-runner";
export { privileged } from "./calendar-contracts";

type CalendarRow = z.infer<typeof calendarEventResponse>;
const normalizeEvent = (value: unknown, name: CalendarKey): CalendarRow | null => {
  if (!value || typeof value !== "object") return null;
  const event = value as { id?: unknown; status?: unknown; summary?: unknown; location?: unknown; start?: { dateTime?: unknown; date?: unknown }; end?: { dateTime?: unknown; date?: unknown } };
  if (event.status === "cancelled" || typeof event.id !== "string" || !event.id || event.id.length > 1024) return null;
  const start = typeof event.start?.dateTime === "string" ? event.start.dateTime : typeof event.start?.date === "string" ? event.start.date : null;
  const end = typeof event.end?.dateTime === "string" ? event.end.dateTime : typeof event.end?.date === "string" ? event.end.date : null;
  if (!start || start.length > 80 || Number.isNaN(Date.parse(start)) || (end && (end.length > 80 || Number.isNaN(Date.parse(end))))) return null;
  return {
    google_event_id: event.id, calendar_name: name,
    title: typeof event.summary === "string" && event.summary.trim() ? event.summary.trim().slice(0, 500) : "Busy",
    start_time: start, end_time: end,
    location: typeof event.location === "string" && event.location.trim() ? event.location.trim().slice(0, 500) : null,
    is_all_day: typeof event.start?.date === "string",
  };
};

const safeCalendarError = (error: unknown, writing = false) => {
  if (error instanceof CalendarAdapterError) {
    if (error.reason === "unavailable") return "Set up the Calendar adapter to connect this calendar.";
    if (error.providerStatus === 401 || error.providerStatus === 403) return "Reconnect Calendar to restore access.";
    if (writing) return "Calendar did not confirm this change. Refresh the calendar before trying again.";
    if (error.reason === "timeout") return "Calendar took too long to respond. Your saved schedule is still available.";
    if (error.reason === "output") return "This calendar window is too large. Choose a smaller window.";
  }
  return writing ? "Calendar did not confirm this change. Refresh the calendar before trying again." : "Calendar could not refresh this window. Your saved schedule is still available.";
};

export function createCalendarHandlers(runner: CalendarRunner = runCalendar, settings: () => CalendarSettings = readCalendarSettings) {
  return definePrivilegedHandlers(privileged, {
    getCalendarSettings() {
      // Invalid optional configuration must never stop a task workspace opening.
      try { return publicCalendarSettings(settings()); } catch { return publicCalendarSettings({}); }
    },
    verifyCalendarSyncToken(args) {
      const expected = Buffer.from(process.env.GTD_CALENDAR_SYNC_TOKEN ?? "");
      const provided = Buffer.from(args.token);
      return { matches: expected.length > 0 && expected.length === provided.length && timingSafeEqual(expected, provided) };
    },
    async readCalendarWindow(args) {
      try {
        const config = settings();
        const keys = CALENDAR_KEYS.filter(key => config[key]);
        const min = Date.parse(args.time_min), max = Date.parse(args.time_max);
        if (!Number.isFinite(min) || !Number.isFinite(max) || max <= min || max - min > 32 * 86_400_000) {
          return { ok: false, error: "Choose a calendar window of up to 32 days.", events: [] };
        }
        if (!keys.length) return { ok: false, error: "Connect an optional calendar with your Muse to show it here.", events: [] };
        const groups = await Promise.all(keys.map(async key => {
          const rows: CalendarRow[] = [];
          let pageToken: string | undefined;
          for (let page = 0; page < 4; page += 1) {
            const result = await runner("list", { calendarId: config[key]!.id, timeMin: args.time_min, timeMax: args.time_max, singleEvents: true, orderBy: "startTime", maxResults: 250, ...(pageToken ? { pageToken } : {}) });
            if (!Array.isArray(result.items) || result.items.length > 250) throw new CalendarAdapterError("invalid");
            for (const item of result.items) {
              const event = normalizeEvent(item, key);
              if (event) rows.push(event);
            }
            if (!result.nextPageToken) return rows;
            if (typeof result.nextPageToken !== "string" || result.nextPageToken.length > 4096) throw new CalendarAdapterError("invalid");
            pageToken = result.nextPageToken;
          }
          throw new CalendarAdapterError("output");
        }));
        return { ok: true, events: groups.flat() };
      } catch (error) { return { ok: false, error: safeCalendarError(error), events: [] }; }
    },
    async writeIntentCalendarEvent(args) {
      try {
        const calendarId = settings().intent?.id;
        if (!calendarId) return { ok: false, error: "Connect a Focus time calendar before scheduling a calendar block." };
        if (args.operation === "delete") {
          if (!args.event_id) return { ok: false, error: "Choose a saved calendar block to delete." };
          try { await runner("delete", { calendarId, eventId: args.event_id }); }
          catch (error) { if (!(error instanceof CalendarAdapterError) || ![404, 410].includes(error.providerStatus ?? 0)) throw error; }
          return { ok: true };
        }
        if (!args.title || !args.start_time || !args.end_time || Date.parse(args.end_time) <= Date.parse(args.start_time)) {
          return { ok: false, error: "Add a title and an end time later than the start time." };
        }
        if (args.operation === "create" && !args.operation_key) return { ok: false, error: "Reopen the editor to start this calendar block." };
        const eventId = args.operation === "create" ? createHash("sha256").update(args.operation_key!).digest("hex") : args.event_id;
        if (!eventId) return { ok: false, error: "Choose a saved calendar block to update." };
        const body = { summary: args.title, start: { dateTime: args.start_time }, end: { dateTime: args.end_time }, transparency: "transparent", reminders: { useDefault: true }, ...(args.operation === "create" ? { id: eventId } : {}) };
        let result: Record<string, unknown>;
        try {
          result = await runner(args.operation === "create" ? "insert" : "patch", { calendarId, ...(args.operation === "update" ? { eventId } : {}) }, body);
        } catch (error) {
          // A repeated create carries the same provider ID. Reconcile a confirmed
          // conflict by reading that ID instead of creating another event.
          if (args.operation !== "create" || !(error instanceof CalendarAdapterError) || error.providerStatus !== 409) throw error;
          result = await runner("get", { calendarId, eventId });
        }
        const event = normalizeEvent(result, "intent");
        return event ? { ok: true, event } : { ok: false, outcome_unknown: true, error: "Calendar did not return the saved block. Refresh the calendar to check its result." };
      } catch (error) {
        return { ok: false, outcome_unknown: !(error instanceof CalendarAdapterError && (error.reason === "unavailable" || [400, 401, 403].includes(error.providerStatus ?? 0))), error: safeCalendarError(error, true) };
      }
    },
  });
}

export const privilegedHandlers = createCalendarHandlers();
