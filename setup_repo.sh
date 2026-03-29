#!/usr/bin/env bash
# =============================================================================
# MyLabs — preparar entorno de desarrollo local
# -----------------------------------------------------------------------------
# Ejecutar desde la raíz del repositorio (donde están pyproject.toml y settings.py):
#   chmod +x setup_repo.sh
#   ./setup_repo.sh
#   ./setup_repo.sh --lock    # usar requirements-lock.txt en lugar de requirements.txt
#
# No crea el repositorio Git ni sube a GitHub; para eso sigue el README (clone, push, PAT/SSH).
# =============================================================================
set -euo pipefail

USE_LOCK=0
for arg in "$@"; do
  case "$arg" in
    --lock) USE_LOCK=1 ;;
    -h|--help)
      echo "Uso: $0 [--lock]"
      echo "  --lock   Instalar desde requirements-lock.txt (versiones fijas)."
      exit 0
      ;;
  esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [[ ! -f "$ROOT/pyproject.toml" ]] || [[ ! -f "$ROOT/settings.py" ]]; then
  echo "Error: ejecuta este script desde la raíz del proyecto MyLabs." >&2
  exit 1
fi

PYTHON="${PYTHON:-python3}"
if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "Error: no se encontró '$PYTHON'. Instala Python 3.10+ o define PYTHON=/ruta/al/python." >&2
  exit 1
fi

if [[ ! -d .venv ]]; then
  echo "==> Creando entorno virtual .venv ..."
  "$PYTHON" -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate

echo "==> Actualizando pip ..."
python -m pip install --upgrade pip

REQ_FILE="requirements.txt"
if [[ "$USE_LOCK" -eq 1 ]]; then
  REQ_FILE="requirements-lock.txt"
fi
if [[ ! -f "$REQ_FILE" ]]; then
  echo "Error: no existe $REQ_FILE" >&2
  exit 1
fi

echo "==> Instalando dependencias ($REQ_FILE) ..."
pip install -r "$REQ_FILE"

echo "==> Instalando el paquete en modo editable (import settings / database) ..."
pip install -e .

if [[ ! -f .env ]] && [[ -f .env.example ]]; then
  cp .env.example .env
  echo "==> Creado .env desde .env.example (revísalo y ajusta SQLALCHEMY_DATABASE_URL)."
elif [[ ! -f .env ]]; then
  echo "Aviso: no hay .env ni .env.example; crea .env con SQLALCHEMY_DATABASE_URL (ver README)." >&2
fi

echo
echo "--------------------------------------------------"
echo "Listo. Activa el venv con:"
echo "  source .venv/bin/activate"
echo "Prueba: python labs/pandas/load_csv.py"
echo "--------------------------------------------------"
