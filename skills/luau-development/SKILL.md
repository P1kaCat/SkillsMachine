---
name: luau-development
description: Write, review and debug Luau language code, strict types, generics, modules
  and metatables. Use for language correctness and typing; use Roblox specialists
  for engine APIs and networking.
---

# luau-development

1. Identify the project's strictness and Luau version. Combine language correctness with types rather than treating typing as an afterthought.
2. Use luau-core for syntax and standard-library behavior, luau-types for advanced typing, and luau-expert for typed module patterns and practical idioms.
3. Preserve existing module APIs and strictness. Validate with the project's analyzer and runnable examples; use luau-performance only for measured performance problems.

## Complementary source guides

- [luau-core](references/sources/luumenlabs/luau-core/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [luau-types](references/sources/luumenlabs/luau-types/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [luau-expert](references/sources/afrxo/luau-expert/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
