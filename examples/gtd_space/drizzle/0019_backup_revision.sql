CREATE TABLE planner_revision (id INTEGER PRIMARY KEY CHECK (id = 1), value INTEGER NOT NULL DEFAULT 0);
INSERT INTO planner_revision (id, value) VALUES (1, 0);
CREATE TABLE planner_restore_guard (id INTEGER PRIMARY KEY CHECK (id = 1), expected_revision INTEGER NOT NULL);
CREATE TRIGGER planner_restore_revision BEFORE INSERT ON planner_restore_guard
WHEN NEW.expected_revision <> (SELECT value FROM planner_revision WHERE id = 1)
BEGIN SELECT RAISE(ABORT, 'workspace changed'); END;
CREATE TRIGGER planner_revision_clients_insert AFTER INSERT ON clients
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_clients_update AFTER UPDATE ON clients
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_clients_delete AFTER DELETE ON clients
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_projects_insert AFTER INSERT ON projects
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_projects_update AFTER UPDATE ON projects
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_projects_delete AFTER DELETE ON projects
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_next_actions_insert AFTER INSERT ON next_actions
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_next_actions_update AFTER UPDATE ON next_actions
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_next_actions_delete AFTER DELETE ON next_actions
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_ticklers_insert AFTER INSERT ON ticklers
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_ticklers_update AFTER UPDATE ON ticklers
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_ticklers_delete AFTER DELETE ON ticklers
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_inbox_items_insert AFTER INSERT ON inbox_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_inbox_items_update AFTER UPDATE ON inbox_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_inbox_items_delete AFTER DELETE ON inbox_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_reference_items_insert AFTER INSERT ON reference_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_reference_items_update AFTER UPDATE ON reference_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_reference_items_delete AFTER DELETE ON reference_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_someday_items_insert AFTER INSERT ON someday_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_someday_items_update AFTER UPDATE ON someday_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_someday_items_delete AFTER DELETE ON someday_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_scheduled_items_insert AFTER INSERT ON scheduled_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_scheduled_items_update AFTER UPDATE ON scheduled_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_scheduled_items_delete AFTER DELETE ON scheduled_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_daily_items_insert AFTER INSERT ON daily_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_daily_items_update AFTER UPDATE ON daily_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_daily_items_delete AFTER DELETE ON daily_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_daily_results_insert AFTER INSERT ON daily_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_daily_results_update AFTER UPDATE ON daily_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_daily_results_delete AFTER DELETE ON daily_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_weekly_items_insert AFTER INSERT ON weekly_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_weekly_items_update AFTER UPDATE ON weekly_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_weekly_items_delete AFTER DELETE ON weekly_items
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_weekly_results_insert AFTER INSERT ON weekly_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_weekly_results_update AFTER UPDATE ON weekly_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_weekly_results_delete AFTER DELETE ON weekly_results
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_calendar_visibility_preferences_insert AFTER INSERT ON calendar_visibility_preferences
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_calendar_visibility_preferences_update AFTER UPDATE ON calendar_visibility_preferences
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
CREATE TRIGGER planner_revision_calendar_visibility_preferences_delete AFTER DELETE ON calendar_visibility_preferences
BEGIN UPDATE planner_revision SET value = value + 1 WHERE id = 1; END;
