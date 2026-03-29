# MyLabs — set up local development environment (Windows PowerShell)
# Run from the repository root (where pyproject.toml and settings.py live):
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned   # if Activate.ps1 is blocked
#   .\setup_repo.ps1
#   .\setup_repo.ps1 -Lock    # use requirements-lock.txt instead of requirements.txt
#
# Does not create a Git repo or push to GitHub; see README for clone, push, PAT/SSH.

[CmdletBinding()]
param(
    [switch]$Lock,
    [switch]$Help
)

$ErrorActionPreference = "Stop"

if ($Help) {
    Write-Host "Usage: .\setup_repo.ps1 [-Lock]"
    Write-Host "  -Lock   Install from requirements-lock.txt (pinned versions)."
    exit 0
}

$Root = $PSScriptRoot
Set-Location $Root

if (-not (Test-Path (Join-Path $Root "pyproject.toml")) -or -not (Test-Path (Join-Path $Root "settings.py"))) {
    Write-Error "Run this script from the MyLabs project root."
}

function Invoke-CreateVenv {
    if ($env:PYTHON) {
        & $env:PYTHON -m venv .venv
    }
    elseif (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3 -m venv .venv
    }
    elseif (Get-Command python -ErrorAction SilentlyContinue) {
        & python -m venv .venv
    }
    else {
        Write-Error "Python not found. Install Python 3.10+ from python.org or the Microsoft Store, or set PYTHON to your python.exe path."
    }
}

$VenvPython = Join-Path $Root ".venv\Scripts\python.exe"
if (-not (Test-Path ".venv")) {
    Write-Host "==> Creating virtual environment .venv ..."
    Invoke-CreateVenv
}

if (-not (Test-Path $VenvPython)) {
    Write-Error "Expected $VenvPython after creating venv."
}

Write-Host "==> Upgrading pip ..."
& $VenvPython -m pip install --upgrade pip | Out-Host

$ReqFile = if ($Lock) { "requirements-lock.txt" } else { "requirements.txt" }
$ReqPath = Join-Path $Root $ReqFile
if (-not (Test-Path $ReqPath)) {
    Write-Error "$ReqFile not found."
}

Write-Host "==> Installing dependencies ($ReqFile) ..."
& $VenvPython -m pip install -r $ReqPath | Out-Host

Write-Host "==> Installing package in editable mode (import settings / database) ..."
& $VenvPython -m pip install -e $Root | Out-Host

$EnvFile = Join-Path $Root ".env"
$EnvExample = Join-Path $Root ".env.example"
if (-not (Test-Path $EnvFile) -and (Test-Path $EnvExample)) {
    Copy-Item $EnvExample $EnvFile
    Write-Host "==> Created .env from .env.example (review and set SQLALCHEMY_DATABASE_URL)."
}
elseif (-not (Test-Path $EnvFile)) {
    Write-Warning "No .env or .env.example; create .env with SQLALCHEMY_DATABASE_URL (see README)."
}

Write-Host ""
Write-Host "--------------------------------------------------"
Write-Host "Done. Activate the venv with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "Try: python labs\pandas\read_people.py"
Write-Host "--------------------------------------------------"
