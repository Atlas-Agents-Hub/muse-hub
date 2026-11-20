import { definePrivilegedContracts, z } from "@hatch/space-sdk";
import { CALENDAR_KEYS } from "./calendar-config";

export const publicCalendarSettingsSchema = z.object({
  enabled: z.array(z.enum(CALENDAR_KEYS)).max(3),
  labels: z.object({ primary: z.string().max(80), intent: z.string().max(80), shared: z.string().max(80) }),
});
export const calendarEventResponse = z.object({
  google_event_id: z.string().max(1024), calendar_name: z.enum(CALENDAR_KEYS),
  title: z.string().max(500), start_time: z.string().max(80), end_time: z.string().max(80).nullable(),
  location: z.string().max(500).nullable(), is_all_day: z.boolean(),
});
export const privileged = definePrivilegedContracts({
  getCalendarSettings: { request: z.object({}), response: publicCalendarSettingsSchema, timeoutMs: 5_000 },
  verifyCalendarSyncToken: {
    request: z.object({ token: z.string().min(1).max(500) }), response: z.object({ matches: z.boolean() }), timeoutMs: 5_000,
  },
  readCalendarWindow: {
    request: z.object({ time_min: z.string().datetime({ offset: true }), time_max: z.string().datetime({ offset: true }) }),
    response: z.object({ ok: z.boolean(), error: z.string().optional(), events: z.array(calendarEventResponse).max(3000) }),
    timeoutMs: 30_000,
  },
  writeIntentCalendarEvent: {
    request: z.object({
      operation: z.enum(["create", "update", "delete"]), operation_key: z.string().uuid().optional(),
      event_id: z.string().max(1024).optional(), title: z.string().trim().min(1).max(500).optional(),
      start_time: z.string().datetime({ offset: true }).optional(), end_time: z.string().datetime({ offset: true }).optional(),
    }),
    response: z.object({ ok: z.boolean(), error: z.string().optional(), outcome_unknown: z.boolean().optional(), event: calendarEventResponse.optional() }),
    timeoutMs: 30_000,
  },
});
