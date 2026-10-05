---
name: minecraft-modding
description: Build, review and debug Minecraft Fabric, NeoForge and legacy Forge mods
  with version-matched mappings, networking, mixins, registries, datagen and build
  checks.
---

# minecraft-modding

1. Read the project's Minecraft, Java, loader, Loom/Gradle and mapping versions. Preserve that version contract.
2. Use Minecraft Modding for loader selection and shared implementation workflow; use its Fabric references for Fabric-specific API, Mixin and resource review.
3. Treat examples as version-scoped. Verify current APIs before applying a legacy example; never convert Yarn to Mojang names or upgrade loaders implicitly.
4. Verify the build and relevant GameTests/runtime behavior. Route multi-loader work to minecraft-multiloader and detailed testing/releases to their dedicated skills.

## Complementary source guides

- [minecraft-modding](references/sources/Jahrome907/minecraft-modding/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
