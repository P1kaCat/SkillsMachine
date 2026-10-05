---
name: writing-skills
description: Create, review and improve reusable agent skills, with precise triggers,
  progressive references and realistic validation.
---

# writing-skills

1. Define the actual task and triggering boundary. Avoid broad instructions that capture unrelated work.
2. Combine Superpowers' behavioral validation guidance with AshExplained's concise skill-authoring structure.
3. Keep substantial details in task-specific references and retain necessary scripts/assets. Match the target host's skill format and available tools.
4. Validate frontmatter, references and runnable helpers; use independent behavioral evaluation when warranted and authorized.

## Complementary source guides

- [writing-skills](references/sources/obra/writing-skills/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.
- [write-a-skill](references/sources/AshExplained/write-a-skill/GUIDE.md): read when its specialist scope applies; resolve its supporting files relative to this guide folder.

Read the guides needed for the task, not every guide automatically. Scripts and assets remain beside their source guide. Run helpers by their absolute installed path; use the source-guide directory as the working directory when a helper relies on relative resources. Source-specific CLAUDE_PLUGIN_ROOT examples must be adapted to this installed location.

Apply these guides within the user request and existing project conventions. Their setup actions and external integrations require the corresponding tools and authorization. Do not migrate frameworks or versions merely to match an example. When guides disagree, prefer verified project-version behavior and this scoped workflow.
