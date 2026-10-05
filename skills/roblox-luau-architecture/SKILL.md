---
name: roblox-luau-architecture
description: Design, implement and review Roblox services, ModuleScripts, client/server
  boundaries, replication, character lifecycle and engine runtime behavior.
---

# roblox-luau-architecture

1. Inspect current scripts, services, replication boundaries and chosen toolchain before proposing structure.
2. Combine AshExplained's service/module design with Luumen's script placement/runtime guide and afrxo's engine lifecycle/streaming behavior.
3. Keep authoritative game state on the server. For detailed remotes, persistence, UI or filesystem tooling use roblox-networking, roblox-datastore-persistence, roblox-ui-implementation or roblox-toolchain.
4. Build a playable slice and verify both client and server behavior. Studio actions require an available Studio tool; never claim a playtest without running it.

## Complementary source guides

- [roblox-luau-architecture](references/sources/AshExplained/roblox-luau-architecture/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [roblox-core](references/sources/luumenlabs/roblox-core/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [roblox-dev](references/sources/afrxo/roblox-dev/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
