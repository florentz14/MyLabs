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
#
# Interpreter: set PYTHON=/path/to/python to force a specific binary. Otherwise the
# script picks the first of python3.14, python3.13, python3, python that can "import ssl"
# (pip needs HTTPS). A Python built without OpenSSL will be skipped — see README
# "Python 3.14 and SSL" if your 3.14 fails this check.
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

has_ssl() {
  local bin="$1"
  command -v "$bin" >/dev/null 2>&1 && "$bin" -c "import ssl" >/dev/null 2>&1
}

resolve_python() {
  if [[ -n "${PYTHON:-}" ]]; then
    if ! command -v "$PYTHON" >/dev/null 2>&1; then
      echo "Error: PYTHON=$PYTHON not found." >&2
      exit 1
    fi
    if ! has_ssl "$PYTHON"; then
      echo "Error: $PYTHON has no working 'ssl' module (pip cannot use HTTPS)." >&2
      echo "Rebuild or reinstall Python with OpenSSL (e.g. libssl-dev + --with-openssl). See README: Python 3.14 and SSL." >&2
      exit 1
    fi
    echo "$PYTHON"
    return 0
  fi
  local c
  for c in python3.14 python3.13 python3 python; do
    if command -v "$c" >/dev/null 2>&1; then
      if has_ssl "$c"; then
        echo "$c"
        return 0
      fi
      echo "Warning: '$c' is on PATH but 'import ssl' failed — skipping (broken OpenSSL link?)." >&2
    fi
  done
  echo "Error: no python3.14 / python3.13 / python3 / python with SSL found. Install Python with OpenSSL support." >&2
  echo "See README: Python 3.14 and SSL." >&2
  exit 1
}

PYTHON="$(resolve_python)"
echo "==> Using interpreter: $($PYTHON -c "import sys; print(sys.executable)") (Python $($PYTHON -c "import sys; print(f'{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}')"))"

if [[ -d .venv ]]; then
  if ! .venv/bin/python -c "import ssl" >/dev/null 2>&1; then
    echo "==> Existing .venv has no SSL; removing .venv so we can recreate it ..."
    rm -rf .venv
  fi
fi

if [[ ! -d .venv ]]; then
  echo "==> Creating virtual environment .venv ..."
  "$PYTHON" -m venv .venv
fi

if ! .venv/bin/python -c "import ssl" >/dev/null 2>&1; then
  echo "Error: .venv Python still cannot import ssl. Remove .venv and fix the host Python build." >&2
  exit 1
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
echo "Try: python labs/pandas/io/read_people.py"
echo "--------------------------------------------------"
