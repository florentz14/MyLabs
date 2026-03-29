#!/usr/bin/env bash
# =============================================================================
# MyLabs — set up local development environment
# -----------------------------------------------------------------------------
# Run from the repository root (where pyproject.toml and settings.py live):
#   chmod +x setup_repo.sh
#   ./setup_repo.sh
#   ./setup_repo.sh --lock    # use requirements-lock.txt instead of requirements.txt
#
# Does not create a Git repo or push to GitHub; see README for clone, push, PAT/SSH.
# On Windows (PowerShell), use setup_repo.ps1 instead.
# =============================================================================
set -euo pipefail

USE_LOCK=0
for arg in "$@"; do
  case "$arg" in
    --lock) USE_LOCK=1 ;;
    -h|--help)
      echo "Usage: $0 [--lock]"
      echo "  --lock   Install from requirements-lock.txt (pinned versions)."
      exit 0
      ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [[ ! -f "$ROOT/pyproject.toml" ]] || [[ ! -f "$ROOT/settings.py" ]]; then
  echo "Error: run this script from the MyLabs project root." >&2
  exit 1
fi

PYTHON="${PYTHON:-python3}"
if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "Error: '$PYTHON' not found. Install Python 3.10+ or set PYTHON=/path/to/python." >&2
  exit 1
fi

if [[ ! -d .venv ]]; then
  echo "==> Creating virtual environment .venv ..."
  "$PYTHON" -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate

echo "==> Upgrading pip ..."
python -m pip install --upgrade pip

REQ_FILE="requirements.txt"
if [[ "$USE_LOCK" -eq 1 ]]; then
  REQ_FILE="requirements-lock.txt"
fi
if [[ ! -f "$REQ_FILE" ]]; then
  echo "Error: $REQ_FILE not found." >&2
  exit 1
fi

echo "==> Installing dependencies ($REQ_FILE) ..."
pip install -r "$REQ_FILE"

echo "==> Installing package in editable mode (import settings / database) ..."
pip install -e .

if [[ ! -f .env ]] && [[ -f .env.example ]]; then
  cp .env.example .env
  echo "==> Created .env from .env.example (review and set SQLALCHEMY_DATABASE_URL)."
elif [[ ! -f .env ]]; then
  echo "Warning: no .env or .env.example; create .env with SQLALCHEMY_DATABASE_URL (see README)." >&2
fi

echo
echo "--------------------------------------------------"
echo "Done. Activate the venv with:"
echo "  source .venv/bin/activate"
echo "Try: python labs/pandas/read_people.py"
echo "--------------------------------------------------"
