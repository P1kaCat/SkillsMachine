---
name: playwright-expert
description: Test and debug web applications with Playwright, browser inspection,
  stable locators, fixtures, screenshots and local-server lifecycle helpers.
---

# playwright-expert

1. Choose the project's existing Playwright language and runner; preserve TypeScript/JavaScript or Python rather than adding another runner.
2. Use Playwright Expert for suites, fixtures and locator strategy; Anthropic's webapp-testing helpers for local server startup and exploratory inspection.
3. Prefer user-observable assertions and robust locators. Verify navigation, forms and browser errors relevant to the change.
4. Execute the actual tests and inspect failures/screenshots. Never infer a passing browser test from static code alone.

## Complementary source guides

- [playwright-expert](references/sources/Jeffallan/playwright-expert/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [webapp-testing](references/sources/anthropics/webapp-testing/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
