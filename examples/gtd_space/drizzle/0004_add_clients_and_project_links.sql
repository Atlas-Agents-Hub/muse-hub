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
--> statement-breakpoint
ALTER TABLE `projects` ADD `client_id` integer REFERENCES clients(id) ON DELETE SET NULL;
