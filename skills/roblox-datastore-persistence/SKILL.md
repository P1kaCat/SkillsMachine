---
name: roblox-datastore-persistence
description: Build and debug Roblox persistence, DataStores, MemoryStores, autosave,
  profile locking, migrations and cross-server data coordination.
---

# roblox-datastore-persistence

1. Record the schema, storage services, failure modes and current persistence library.
2. Combine save/load and profile-locking workflows with service-specific limits, caching, versioning, MemoryStores and cross-server messaging.
3. Design retries, idempotence, shutdown handling and migration recovery without changing production data unprompted.
4. Verify failed saves, overlapping sessions and rejoin behavior using an authorized test environment.

## Complementary source guides

- [roblox-datastore-persistence](references/sources/AshExplained/roblox-datastore-persistence/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [roblox-data](references/sources/luumenlabs/roblox-data/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
