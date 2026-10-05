param([string]$Destination, [switch]$List, [switch]$DryRun)
$ErrorActionPreference = 'Stop'
$installer = Join-Path $PSScriptRoot 'install.py'
$installArgs = @($installer)
if ($Destination) { $installArgs += @('--dest', $Destination) }
if ($List) { $installArgs += '--list' }
if ($DryRun) { $installArgs += '--dry-run' }
if (Get-Command py -ErrorAction SilentlyContinue) { & py -3 @installArgs }
elseif (Get-Command python -ErrorAction SilentlyContinue) { & python @installArgs }
else { throw 'Install Python 3, then run this installer again.' }
if ($LASTEXITCODE -ne 0) { throw "Installer failed with exit code $LASTEXITCODE" }
