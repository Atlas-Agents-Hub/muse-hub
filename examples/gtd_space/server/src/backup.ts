import { defineAction, z } from "@hatch/space-sdk";
import { getTableConfig } from "drizzle-orm/sqlite-core";
import { sql } from "drizzle-orm";
import * as schema from "./schema";

const tables = [schema.clients, schema.projects, schema.nextActions, schema.ticklers,
  schema.inboxItems, schema.referenceItems, schema.somedayItems, schema.scheduledItems,
  schema.dailyItems, schema.dailyResults, schema.weeklyItems, schema.weeklyResults,
  schema.calendarVisibilityPreferences] as const;
export const BACKUP_TABLES = tables.map(table => getTableConfig(table));
type Cell = string | number | null;
const tableSchemas = Object.fromEntries(BACKUP_TABLES.map(table => [table.name, z.array(z.object(Object.fromEntries(table.columns.map(column => {
  let validator: z.ZodType = column.dataType === "number" || column.dataType === "date" || column.dataType === "boolean"
    ? z.number().int().safe() : z.string().max(12000);
  if (column.dataType === "boolean") validator = z.union([z.literal(0), z.literal(1)]);
  if (column.name === "id" || column.name.endsWith("_id")) validator = z.number().int().positive().safe();
  if (column.enumValues?.length) validator = z.enum(column.enumValues as [string, ...string[]]);
  if (column.name === "url") validator = z.string().max(2048).refine(value => !value || /^https?:\/\//i.test(value), "Use an http or https URL.");
  if (!column.notNull) validator = validator.nullable();
  return [column.name, validator];
}))).strict()).max(10000)]));
export const backupSchema = z.object({
  format: z.literal("muse-planner-backup"), version: z.literal(1), created_at: z.string().datetime(),
  tables: z.object(tableSchemas).strict(),
}).strict().superRefine((backup, ctx) => {
  if (Object.values(backup.tables).reduce((count, rows) => count + rows.length, 0) > 10000) ctx.addIssue({ code: "custom", message: "A backup supports up to 10,000 rows." });
  if (new TextEncoder().encode(JSON.stringify(backup)).length > 4 * 1024 * 1024) ctx.addIssue({ code: "custom", message: "A backup supports up to 4 MiB." });
  for (const table of BACKUP_TABLES) {
    const rows = backup.tables[table.name] ?? [];
    const ids = new Set<unknown>();
    for (const row of rows) {
      if (ids.has(row.id)) ctx.addIssue({ code: "custom", message: `Duplicate ID in ${table.name}.` });
      ids.add(row.id);
    }
  }
});

export const BackupActions = {
  exportWorkspace: defineAction({
    description: "Export projects, tasks, notes, schedules, and routine history as a portable JSON backup.",
    request: z.object({}), response: z.object({ revision: z.number().int().nonnegative(), backup: backupSchema }),
    async handler(ctx) {
      const db = ctx.db();
      const queries: Parameters<typeof db.batch>[0] = [db.all(sql`SELECT value FROM planner_revision WHERE id = 1`), ...BACKUP_TABLES.map(table => db.all(sql.raw(`SELECT * FROM "${table.name}" ORDER BY id`)))];
      const results = await db.batch(queries);
      const revisionRows = results[0] as { value: number }[];
      const backup = backupSchema.parse({ format: "muse-planner-backup", version: 1, created_at: new Date().toISOString(), tables: Object.fromEntries(BACKUP_TABLES.map((table, index) => [table.name, results[index + 1]])) });
      return { revision: revisionRows[0]?.value ?? 0, backup };
    },
  }),
  restoreWorkspace: defineAction({
    description: "Restore a JSON backup atomically, rejecting a stale workspace revision.",
    request: z.object({ expected_revision: z.number().int().nonnegative(), backup: backupSchema }),
    response: z.object({ ok: z.boolean(), error: z.string().optional() }),
    async handler(ctx, args) {
      const db = ctx.db();
      const queries: [ReturnType<typeof db.run>, ...ReturnType<typeof db.run>[]] = [db.run(sql`INSERT INTO planner_restore_guard (id, expected_revision) VALUES (1, ${args.expected_revision})`)];
      for (const table of [...BACKUP_TABLES].reverse()) queries.push(db.run(sql.raw(`DELETE FROM "${table.name}"`)));
      for (const table of BACKUP_TABLES) {
        for (const row of args.backup.tables[table.name] ?? []) {
          const columns = table.columns.map(column => column.name);
          const values = columns.map(name => sql`${row[name] as Cell}`);
          queries.push(db.run(sql`INSERT INTO ${sql.identifier(table.name)} (${sql.join(columns.map(name => sql.identifier(name)), sql`, `)}) VALUES (${sql.join(values, sql`, `)})`));
        }
      }
      queries.push(db.run(sql`DELETE FROM planner_restore_guard WHERE id = 1`));
      try {
        // libSQL batch is one write transaction. The guard and all data changes
        // either commit together or roll back, including foreign-key failures.
        await db.batch(queries);
        ctx.invalidateQueries();
        return { ok: true };
      } catch (error) {
        const message = error instanceof Error ? error.message : "";
        return { ok: false, error: /workspace changed/i.test(message)
          ? "Your workspace changed while the backup was open. Export the latest work, then review the restore again."
          : "The backup could not be restored. Check its records and project links. Your workspace is unchanged." };
      }
    },
  }),
};
