---
name: code-reviewer
description: Review implementation changes for correctness, maintainability, performance
  and test coverage, or prepare a scoped code-review request against a specification.
---

# code-reviewer

1. Identify the diff, acceptance criteria, relevant callers and test evidence.
2. Use the code-reviewer's analysis checklists with requesting-code-review's specification and scope framing.
3. Prioritize actionable defects with concrete triggers and consequences. Separate required fixes from optional suggestions.
4. Use security-reviewer or differential-review for an explicitly needed security review. Claim independent review only when a separate reviewer actually performed it.

## Complementary source guides

- [code-reviewer](references/sources/Jeffallan/code-reviewer/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [requesting-code-review](references/sources/obra/requesting-code-review/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
