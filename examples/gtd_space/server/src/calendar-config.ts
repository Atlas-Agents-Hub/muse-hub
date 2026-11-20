/** Portable calendar names. Account identifiers stay in privileged settings. */
export const CALENDAR_KEYS = ["primary", "intent", "shared"] as const;
export type CalendarKey = (typeof CALENDAR_KEYS)[number];
export const DEFAULT_CALENDAR_LABELS: Record<CalendarKey, string> = {
  primary: "My calendar", intent: "Focus time", shared: "Shared calendar",
};
export const calendarKeyFor = (name: string): CalendarKey => {
  const key = name.trim().toLowerCase();
  return CALENDAR_KEYS.find(candidate => candidate === key) ?? "primary";
};
