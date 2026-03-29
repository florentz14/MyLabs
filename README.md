# MyLabs — Python lab workspace

## Overview

Personal Python lab materials: exercises under `labs/`, shared data under `data/`, and a small **SQLAlchemy** database layer (`database.py`) configured via **environment variables**. **Alembic** is included for future schema migrations.

Dependencies are listed in two ways:

- **`requirements.txt`** — direct packages only (what you would install on purpose); `pip` pulls the rest automatically.
- **`requirements-lock.txt`** — full `pip freeze` of this project’s venv for **bit-for-bit** reproducibility (optional but recommended for CI or matching a teammate’s environment).

## Prerequisites

- Python 3.10 or newer (3.13 is used in this project)
- Git
- A terminal (Terminal on macOS, your distro’s terminal on Linux, **PowerShell** or **Command Prompt** on Windows)

Commands below assume you **open a terminal**, **clone or enter the project folder**, and run steps from the **repository root** (`MyLabs/`).

---

## Setup

### 1. Create a virtual environment

The command is almost the same; use `python3` on Linux/macOS if `python` still points to Python 2.

| OS | Command |
|----|---------|
| **Linux** | `python3 -m venv .venv` |
| **macOS** | `python3 -m venv .venv` (or `python -m venv .venv` if `python` is 3.x) |
| **Windows (PowerShell or CMD)** | `py -3 -m venv .venv` or `python -m venv .venv` |

### 2. Activate the virtual environment

You must activate **once per terminal session** before `pip` or `python` use `.venv`.

| OS / shell | Command |
|------------|---------|
| **Linux** (bash, zsh, …) | `source .venv/bin/activate` |
| **macOS** (bash, zsh, …) | `source .venv/bin/activate` |
| **Windows — Command Prompt** | `.venv\Scripts\activate.bat` |
| **Windows — PowerShell** | `.venv\Scripts\Activate.ps1` |

**PowerShell note:** If execution of scripts is disabled, run once (as Administrator if needed):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

After activation, your prompt usually shows `(.venv)`.

**Deactivate** (any OS): `deactivate`

### 3. Install dependencies

With the venv **activated**, choose one approach:

| Goal | Command |
|------|---------|
| **Normal install** (direct deps; pip resolves versions) | `pip install -r requirements.txt` |
| **Reproducible install** (exact versions from the lockfile) | `pip install -r requirements-lock.txt` |
| **Project as editable package** (so `import settings` / `import database` work from any folder) | `pip install -e .` |

Run **`pip install -e .`** once from the repo root after installing dependencies. That registers the top-level modules `settings` and `database` (see `pyproject.toml`) without duplicating path logic in each script.

On Linux/macOS, if `pip` is missing, use `python3 -m pip install …`.

**PyTorch / GPU (Linux):** This stack pins **PyTorch 2.11** with **CUDA 13** wheels on Linux. You need a recent **NVIDIA driver** compatible with CUDA 13. Installs can be large. On macOS or CPU-only machines, you may need a different `torch` build (see [PyTorch get started](https://pytorch.org/get-started/locally/)).

**Refresh the lockfile** after you change packages (so CI and others stay in sync):

```bash
pip freeze > requirements-lock.txt
```

### 4. Configure the environment

Create `.env` at the project root from the example file:

| OS / shell | Command |
|------------|---------|
| **Linux** / **macOS** | `cp .env.example .env` |
| **Windows — CMD** | `copy .env.example .env` |
| **Windows — PowerShell** | `Copy-Item .env.example .env` |

Then edit `.env` and ensure **`SQLALCHEMY_DATABASE_URL`** is set — it is **required**. The app loads `.env` from the project directory (next to `database.py`), not from the shell’s current working directory.

Example for the default SQLite file under `data/` (same value on every OS):

```bash
SQLALCHEMY_DATABASE_URL=sqlite:///./data/students.db
```

Relative SQLite paths are resolved against the project root, so the database file stays in the right place even if you run scripts from another directory.

Optional keys (see `.env.example` for the full list) include `SQLALCHEMY_ECHO`, pool settings, and `ENVIRONMENT` / `DEBUG`.

---

## Database (`database.py`)

- **`engine`** / **`SessionLocal`** — SQLAlchemy engine and session factory.
- **`Base`** — declarative base for ORM models.
- **`get_db()`** — generator suitable for dependency injection (for example FastAPI): yields a session and closes it in a `finally` block.

Import only after `.env` exists with `SQLALCHEMY_DATABASE_URL` set.

---

## Alembic

Alembic is installed with the project. There is no `alembic/` folder in the repo until you initialize it (same command everywhere; run with the venv activated):

```bash
alembic init alembic
```

Then point `sqlalchemy.url` in `alembic.ini` (or `env.py`) at the same URL as `SQLALCHEMY_DATABASE_URL`, or import it from your settings module.

---

## Repository layout

| Path | Purpose |
|------|---------|
| `database.py` | SQLAlchemy engine, session, `Base`, `get_db()` |
| `settings.py` | Project `BASE_PATH` and subpaths under `data/` and `labs/` |
| `data/` | CSV, exports, JSON, PDFs, SQL snippets, etc. (see `settings.py`) |
| `labs/` | Lab code (e.g. `classes/`, scripts) |
| `requirements.txt` | Direct dependencies (SQLAlchemy, Alembic, torch stack, Jupyter, etc.) |
| `requirements-lock.txt` | Full pinned environment (`pip freeze`) for reproducible installs |
| `pyproject.toml` | Local package metadata; `pip install -e .` exposes `settings` and `database` |
| `.env` | Local secrets and config — **not committed** (see `.gitignore`) |
| `.env.example` | Template for required variables (copy to `.env`) |

---

## Running lab scripts

From the repository root, with the venv activated:

| OS | Typical command |
|----|-----------------|
| **Linux** / **macOS** | `python3 labs/main.py` or `python labs/main.py` |
| **Windows** | `python labs\main.py` or `py labs\main.py` |

Forward slashes (`labs/main.py`) also work on Windows in current Python versions.

Example (pandas + `settings.CSV_PATH`): `python labs/pandas/load_csv.py` (requires `pip install -e .`).

Adjust paths if you add other entry points.

---

## Tests

If you add tests under `tests/`, run (venv activated):

```bash
pytest -q
```

On Linux/macOS, if needed: `python3 -m pytest -q`

---

## Git

Use a branch such as `lab/<your-name>` for coursework-style workflows, or follow your own branching rules. Git commands are the same on Linux, macOS, and Windows.

---

## Get the project (clone or download)

### Clone with Git (recommended)

You get full history and can pull updates easily. Install [Git](https://git-scm.com/downloads) first, then in a folder where you keep projects:

```bash
git clone https://github.com/florentz14/MyLabs.git
cd MyLabs
```

If the repository name or host differs (fork, GitLab, etc.), adjust the URL. For SSH:

```bash
git clone git@github.com:florentz14/MyLabs.git
cd MyLabs
```

**Update** an existing clone later:

```bash
cd MyLabs
git pull
```

### Download as a ZIP (no Git required)

1. Open the repository page in the browser (GitHub, GitLab, …).
2. Use **Code** → **Download ZIP** (or the site’s equivalent).
3. Extract the archive:
   - **Linux** / **macOS**: unzip in the terminal or with the file manager; then `cd` into the extracted folder (often `MyLabs-main` if downloaded from GitHub — you may rename it to `MyLabs`).
   - **Windows**: right-click the ZIP → **Extract All…**, then open **PowerShell** or **CMD** and `cd` into that folder.

ZIP downloads **do not** include Git history; use **clone** if you plan to contribute with branches and pull requests.

---

## Use this project (quick path)

1. **Obtain** the code: [clone](#clone-with-git-recommended) or [download ZIP](#download-as-a-zip-no-git-required).
2. **Follow [Setup](#setup)** above: create and activate `.venv`, install with `requirements.txt` or `requirements-lock.txt`, run **`pip install -e .`**, copy `.env.example` to `.env`, set `SQLALCHEMY_DATABASE_URL`.
3. **Run** what you need: e.g. [Running lab scripts](#running-lab-scripts), or import `database` / `settings` from the project root (or with `PYTHONPATH` set to the repo root if you run from elsewhere).

If anything imports `database.py`, **`.env` must exist** with a valid `SQLALCHEMY_DATABASE_URL`.

---

## Contributing

Contributions are welcome: fixes, docs, exercises, or small refactors. Typical flow:

1. **Fork** the repository on the hosting site (GitHub/GitLab), or ask for **collaborator** access if it is a private course repo.
2. **Clone your fork** (or the shared remote) and create a **branch** off the default branch (`main` or `master`):

   ```bash
   git checkout -b feature/short-description
   ```

3. **Make changes** in small, focused commits with **clear messages** (what changed and why).
4. **Run tests** if the project has them (`pytest -q`) and ensure new code matches existing style (formatting, naming).
5. **Do not commit** `.env`, local `.db` files, or `.venv/` — they are listed in `.gitignore`.
6. If you change dependencies, update **`requirements.txt`** as needed and regenerate **`requirements-lock.txt`** (`pip freeze > requirements-lock.txt`) so others and CI stay aligned.
7. **Push** your branch and open a **pull request** / **merge request** against the upstream default branch. Describe the change and link any related issue.

If there is no public remote yet, you can still use branches locally and share patches or zips; once a remote exists, the same Git workflow applies on Linux, macOS, and Windows.

For course-style work, the instructor may ask for a branch named `lab/<your-name>` instead of `feature/…` — follow their guidelines when they differ from the above.

---

Good luck and happy coding.
