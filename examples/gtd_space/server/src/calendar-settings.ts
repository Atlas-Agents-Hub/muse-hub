import { CALENDAR_KEYS, DEFAULT_CALENDAR_LABELS, type CalendarKey } from "./calendar-config";

export type CalendarSettings = Partial<Record<CalendarKey, { id: string; label: string }>>;

/** Called only by the privileged server. An absent setting enables no service. */
export function readCalendarSettings(raw = process.env.GTD_CALENDARS_JSON): CalendarSettings {
  if (!raw?.trim()) return {};
  if (raw.length > 8192) throw new Error("Calendar configuration exceeds 8 KiB.");
  let value: unknown;
  try { value = JSON.parse(raw); } catch { throw new Error("Calendar configuration must be a JSON object."); }
  if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error("Calendar configuration must be a JSON object.");
  const settings: CalendarSettings = {};
  for (const [key, item] of Object.entries(value)) {
    if (!CALENDAR_KEYS.includes(key as CalendarKey) || !item || typeof item !== "object" || Array.isArray(item)) {
      throw new Error("Use primary, intent, or shared calendar settings.");
    }
    const { id, label, ...extra } = item as Record<string, unknown>;
    if (Object.keys(extra).length || typeof id !== "string" || !id.trim() || id.length > 1024 || /[\u0000-\u001f\u007f]/.test(id)) {
      throw new Error("Each enabled calendar requires an account calendar ID.");
    }
    if (label !== undefined && (typeof label !== "string" || !label.trim() || label.length > 80 || /[\u0000-\u001f\u007f]/.test(label))) {
      throw new Error("Calendar labels must contain 1–80 visible characters.");
    }
    settings[key as CalendarKey] = { id: id.trim(), label: typeof label === "string" ? label.trim() : DEFAULT_CALENDAR_LABELS[key as CalendarKey] };
  }
  return settings;
}

export function publicCalendarSettings(settings: CalendarSettings) {
  return {
    enabled: CALENDAR_KEYS.filter(key => settings[key]),
    labels: Object.fromEntries(CALENDAR_KEYS.map(key => [key, settings[key]?.label ?? DEFAULT_CALENDAR_LABELS[key]])) as Record<CalendarKey, string>,
  };
}
