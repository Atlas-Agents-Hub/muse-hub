ALTER TABLE calendar_events RENAME TO calendar_events_previous;
CREATE TABLE calendar_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  google_event_id TEXT NOT NULL,
  calendar_name TEXT NOT NULL DEFAULT 'primary',
  title TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT,
  location TEXT, is_all_day INTEGER NOT NULL DEFAULT 0, synced_at TEXT NOT NULL
);
INSERT INTO calendar_events SELECT * FROM calendar_events_previous;
DROP TABLE calendar_events_previous;
CREATE UNIQUE INDEX calendar_events_source_id_unique ON calendar_events (calendar_name, google_event_id);
