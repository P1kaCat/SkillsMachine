---
name: roblox-ui-implementation
description: Build and fix Roblox HUDs, ScreenGui components, responsive mobile layouts,
  UI controllers and Fusion 0.3 components while preserving the existing framework.
---

# roblox-ui-implementation

1. Inspect current UI framework, theme and screen hierarchy. Use roblox-game-ux for gameplay/onboarding design decisions.
2. Combine ScreenGui/state-controller patterns with engine layout/input primitives. Load Fusion references only if the project uses Fusion.
3. Check safe areas, resizing, touch, keyboard/gamepad focus, respawn lifecycle and cleanup of reactive state.
4. Verify the UI in Studio's available device simulations; report untested devices clearly.

## Complementary source guides

- [roblox-ui-implementation](references/sources/AshExplained/roblox-ui-implementation/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [roblox-ui](references/sources/afrxo/roblox-ui/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
