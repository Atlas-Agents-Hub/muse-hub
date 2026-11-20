-- Schema reference generated from the ordered migrations.
-- Install with the migration journal to retain version tracking.
CREATE TABLE calendar_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  google_event_id TEXT NOT NULL,
  calendar_name TEXT NOT NULL DEFAULT 'primary',
  title TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT,
  location TEXT, is_all_day INTEGER NOT NULL DEFAULT 0, synced_at TEXT NOT NULL
);

CREATE TABLE `calendar_sync_state` (
  `id` integer PRIMARY KEY NOT NULL,
  `last_sync_at` text,
  `status` text NOT NULL DEFAULT 'unknown',
  `error_detail` text
);

CREATE TABLE `calendar_visibility_preferences` (
  `id` integer PRIMARY KEY NOT NULL,
  `primary_visible` integer NOT NULL DEFAULT 1,
  `intent_visible` integer NOT NULL DEFAULT 1,
  `shared_visible` integer NOT NULL DEFAULT 1,
  `updated_at` text NOT NULL
);

CREATE TABLE `client_diagnostics` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `kind` text NOT NULL,
  `detail` text NOT NULL DEFAULT '',
  `client_release` text NOT NULL,
  `created_at` text NOT NULL
);

CREATE TABLE `clients` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `name` text NOT NULL,
  `relationship` text DEFAULT 'current_or_potential' NOT NULL,
  `billing_rule` text DEFAULT 'standard' NOT NULL,
  `notes` text DEFAULT '' NOT NULL,
  `created_at` integer NOT NULL,
  `updated_at` integer NOT NULL,
  CONSTRAINT `clients_name_unique` UNIQUE(`name`)
);

CREATE TABLE `daily_items` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `name` text NOT NULL,
  `position` integer NOT NULL DEFAULT 0,
  `archived_at` text
);

CREATE TABLE `daily_results` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `item_id` integer NOT NULL REFERENCES `daily_items`(`id`) ON DELETE CASCADE,
  `result_date` text NOT NULL,
  `passed` integer NOT NULL,
  `recorded_by` text NOT NULL DEFAULT ''
);

CREATE TABLE entries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  created_at INTEGER NOT NULL
);

CREATE TABLE `inbox_items` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `title` text NOT NULL,
  `notes` text DEFAULT '' NOT NULL,
  `created_at` integer NOT NULL
, `priority` text NOT NULL DEFAULT 'unprioritized', `url` text DEFAULT '' NOT NULL);

CREATE TABLE `next_actions` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `title` text NOT NULL,
  `context` text NOT NULL DEFAULT '@anywhere',
  `project_id` integer,
  `notes` text NOT NULL DEFAULT '',
  `status` text NOT NULL DEFAULT 'active',
  `created_at` integer NOT NULL,
  `completed_at` integer, `is_next` integer DEFAULT 1 NOT NULL, `priority` text NOT NULL DEFAULT 'unprioritized', `url` text DEFAULT '' NOT NULL,
  FOREIGN KEY (`project_id`) REFERENCES `projects`(`id`) ON UPDATE no action ON DELETE SET NULL
);

CREATE TABLE planner_restore_guard (id INTEGER PRIMARY KEY CHECK (id = 1), expected_revision INTEGER NOT NULL);

CREATE TABLE planner_revision (id INTEGER PRIMARY KEY CHECK (id = 1), value INTEGER NOT NULL DEFAULT 0);

CREATE TABLE `projects` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `title` text NOT NULL,
  `outcome` text NOT NULL DEFAULT '',
  `notes` text NOT NULL DEFAULT '',
  `status` text NOT NULL DEFAULT 'active',
  `created_at` integer NOT NULL,
  `updated_at` integer NOT NULL
, `client_id` integer REFERENCES clients(id) ON DELETE SET NULL, `completed_at` integer, `url` text DEFAULT '' NOT NULL);

CREATE TABLE `reference_items` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `title` text NOT NULL,
  `notes` text DEFAULT '' NOT NULL,
  `created_at` integer NOT NULL,
  `updated_at` integer NOT NULL
, `url` text DEFAULT '' NOT NULL);

CREATE TABLE `render_health_measurements` (
  `id` integer PRIMARY KEY NOT NULL,
  `render_generation` text NOT NULL,
  `request_id` text,
  `client_release` text NOT NULL,
  `server_release` text NOT NULL,
  `tab` text NOT NULL,
  `rendered_row_count` integer NOT NULL,
  `has_data` integer NOT NULL,
  `rendered_at` text NOT NULL,
  `recorded_at` text NOT NULL
);

CREATE TABLE `scheduled_items` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `title` text NOT NULL,
  `scheduled_date` text NOT NULL,
  `start_time` text,
  `end_time` text,
  `source_label` text DEFAULT '' NOT NULL,
  `is_blocking` integer DEFAULT 1 NOT NULL,
  `notes` text DEFAULT '' NOT NULL,
  `created_at` integer NOT NULL,
  `updated_at` integer NOT NULL
, `url` text DEFAULT '' NOT NULL);

CREATE TABLE `someday_items` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `title` text NOT NULL,
  `notes` text DEFAULT '' NOT NULL,
  `created_at` integer NOT NULL,
  `updated_at` integer NOT NULL
, `url` text DEFAULT '' NOT NULL);

CREATE TABLE `ticklers` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `title` text NOT NULL,
  `remind_on` text NOT NULL,
  `notes` text NOT NULL DEFAULT '',
  `status` text NOT NULL DEFAULT 'pending',
  `created_at` integer NOT NULL
, `completed_at` integer, `url` text DEFAULT '' NOT NULL);

CREATE TABLE `weekly_items` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `name` text NOT NULL,
  `position` integer NOT NULL DEFAULT 0,
  `archived_at` text
);

CREATE TABLE `weekly_results` (
  `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  `item_id` integer NOT NULL REFERENCES `weekly_items`(`id`) ON DELETE CASCADE,
  `result_week` text NOT NULL,
  `passed` integer NOT NULL,
  `recorded_by` text NOT NULL DEFAULT ''
);

CREATE UNIQUE INDEX calendar_events_source_id_unique ON calendar_events (calendar_name, google_event_id);

CREATE UNIQUE INDEX `daily_results_item_date_unique` ON `daily_results` (`item_id`, `result_date`);

CREATE UNIQUE INDEX `weekly_results_item_week_unique` ON `weekly_results` (`item_id`, `result_week`);

CREATE TRIGGER planner_restore_revision BEFORE INSERT ON planner_restore_guard
WHEN NEW.expected_revision <> (SELECT value FROM planner_revision WHERE id = 1)
BEGIN SELECT RAISE(ABORT, 'workspace changed'); END;

CREATE TRIGGER planner_revision_calendar_visibility_preferences_delete AFTER DELETE ON calendar_visibility_preferences
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_calendar_visibility_preferences_insert AFTER INSERT ON calendar_visibility_preferences
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_calendar_visibility_preferences_update AFTER UPDATE ON calendar_visibility_preferences
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_clients_delete AFTER DELETE ON clients
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_clients_insert AFTER INSERT ON clients
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_clients_update AFTER UPDATE ON clients
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_daily_items_delete AFTER DELETE ON daily_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_daily_items_insert AFTER INSERT ON daily_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_daily_items_update AFTER UPDATE ON daily_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_daily_results_delete AFTER DELETE ON daily_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_daily_results_insert AFTER INSERT ON daily_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_daily_results_update AFTER UPDATE ON daily_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_inbox_items_delete AFTER DELETE ON inbox_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_inbox_items_insert AFTER INSERT ON inbox_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_inbox_items_update AFTER UPDATE ON inbox_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_next_actions_delete AFTER DELETE ON next_actions
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_next_actions_insert AFTER INSERT ON next_actions
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_next_actions_update AFTER UPDATE ON next_actions
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_projects_delete AFTER DELETE ON projects
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_projects_insert AFTER INSERT ON projects
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_projects_update AFTER UPDATE ON projects
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_reference_items_delete AFTER DELETE ON reference_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_reference_items_insert AFTER INSERT ON reference_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_reference_items_update AFTER UPDATE ON reference_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_scheduled_items_delete AFTER DELETE ON scheduled_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_scheduled_items_insert AFTER INSERT ON scheduled_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_scheduled_items_update AFTER UPDATE ON scheduled_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_someday_items_delete AFTER DELETE ON someday_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_someday_items_insert AFTER INSERT ON someday_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_someday_items_update AFTER UPDATE ON someday_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_ticklers_delete AFTER DELETE ON ticklers
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_ticklers_insert AFTER INSERT ON ticklers
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_ticklers_update AFTER UPDATE ON ticklers
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_weekly_items_delete AFTER DELETE ON weekly_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_weekly_items_insert AFTER INSERT ON weekly_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_weekly_items_update AFTER UPDATE ON weekly_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_weekly_results_delete AFTER DELETE ON weekly_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_weekly_results_insert AFTER INSERT ON weekly_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;

CREATE TRIGGER planner_revision_weekly_results_update AFTER UPDATE ON weekly_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
