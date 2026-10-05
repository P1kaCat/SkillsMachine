---
name: react-expert
description: Implement, review and optimize React applications, hooks, state, Server
  Components and reusable component APIs using React and Vercel engineering guidance.
---

# react-expert

1. Inspect installed React/framework versions, rendering mode and component/state boundaries.
2. Use the React implementation guide for hooks, state and forms; Vercel's performance rules for fetching, bundle size and render costs; composition patterns for flexible reusable APIs.
3. Avoid premature memoization or framework upgrades. Apply only patterns supported by the project versions.
4. Verify behavior with the project's checks and relevant component/browser tests. Use nextjs-developer for route/framework-specific work.

## Complementary source guides

- [react-expert](references/sources/Jeffallan/react-expert/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [vercel-react-best-practices](references/sources/vercel-labs/vercel-react-best-practices/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [vercel-composition-patterns](references/sources/vercel-labs/vercel-composition-patterns/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
