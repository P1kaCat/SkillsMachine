---
name: systematic-debugging
description: Investigate reproducible software failures, stack traces, regressions
  and runtime bugs through evidence, falsifiable hypotheses and verified fixes.
---

# systematic-debugging

1. Capture a minimal reproduction, expected behavior, logs and relevant recent changes before editing.
2. Use systematic-debugging's root-cause sequence and debugging-wizard's language/framework diagnostics to rank hypotheses.
3. Change one causal factor at a time. Fix the root cause and retain a meaningful regression check.
4. Rerun the reproduction and relevant checks; report remaining uncertainty. Specialized Roblox or Minecraft guides supply engine-specific mechanics.

## Complementary source guides

- [systematic-debugging](references/sources/obra/systematic-debugging/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [debugging-wizard](references/sources/Jeffallan/debugging-wizard/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
