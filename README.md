# SkillsMachine

Private collection of development and finance skills for Codex, including Roblox/Luau, Minecraft, interface design, architecture, testing, security and code review.

**166 installable skills**, including the 153 development skills (12 complementary merges) 9 finance skills and 4 Apache-licensed system skills. [The complete catalog](CATALOG.md) inventories **231 skills**; the remaining 65 are installed through official plugins or supplied by the host. Copying a skill does not connect accounts or provide plugin APIs.

## Install

Your GitHub account must have access to this private repository. Install Git and Python 3, then:

```powershell
git clone https://github.com/P1kaCat/SkillsMachine.git
cd SkillsMachine
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

This uses a process-local execution-policy override. Existing skill directories are skipped, not overwritten. Restart Codex after installation.

On macOS/Linux: `python3 install.py`. The destination is `$CODEX_HOME/skills`, or `~/.codex/skills` when CODEX_HOME is unset.

```powershell
python install.py --list
python install.py --dry-run
python install.py --only minecraft-modding roblox-ui-implementation
python install.py --dest C:\path\to\project\.agents\skills
```

The installer copies all bundled guides, scripts and resources. Individual scripts may require additional tools or dependencies documented in their guides.

## Official plugins

Install the plugins listed in [CATALOG.md](CATALOG.md) through the official ChatGPT/Codex plugin directory: https://chatgpt.com/plugins. Availability depends on your host and account. The host-provided review-agent is not separately packaged.

## Sources and licensing

[catalog.json](catalog.json) records provenance and availability. Read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and each skill's license before reuse or redistribution. Private sharing also requires redistribution permission. The unlicensed Fabric supplement is excluded; the licensed Minecraft modding guide still covers Fabric. No proprietary plugin source is bundled.

## Finance skills

Bundled: `zero-based-budget`, `subscription-audit`, `financial-goals`, `cash-flow-forecast`, `break-even-calc`, `pricing-optimizer`, `yfinance-data`, `company-valuation`, `earnings-recap`.

Budget and business skills support CSV/manual input without Wilson. Market research skills require Python and yfinance, installed when used. Examples may use US conventions; use the user's currency and jurisdiction for actual analyses.
