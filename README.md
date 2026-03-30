# MyLabs — Python lab workspace

## Contents

- **[Overview](#overview)** — what this repo contains; `requirements.txt` vs lockfile  
- **[Prerequisites](#prerequisites)** — Python, Git, terminal  
- **[Setup](#setup)** — **virtual environment** (create, **activate on Linux/macOS/Windows/WSL/fish…**), **`python -m pip install`**, editable install, optional setup scripts, **`.env`**  
- **[Database (`database.py`)](#database-databasepy)** — SQLAlchemy engine and sessions  
- **[Alembic](#alembic)** — migrations (initialize when needed)  
- **[Repository layout](#repository-layout)** — main folders and files  
- **[Running lab scripts](#running-lab-scripts)** — `labs/files`, `pandas`, `matplotlib`, `sql/`  
- **[Tests](#tests)**  
- **[Git](#git)** — branch tips, push to GitHub  
- **[Get the project (clone or download)](#get-the-project-clone-or-download)**  
- **[Use this project (quick path)](#use-this-project-quick-path)**  
- **[Contributing](#contributing)**

## Overview

Personal Python lab materials: exercises under `labs/`, shared data under `data/`, and a small **SQLAlchemy** database layer (`database.py`) configured via **environment variables**. **Alembic** is included for future schema migrations.

Dependencies are listed in two ways:

- **`requirements.txt`** — direct packages only (what you would install on purpose); `pip` pulls the rest automatically.
- **`requirements-lock.txt`** — full `pip freeze` of this project’s venv for **bit-for-bit** reproducibility (optional but recommended for CI or matching a teammate’s environment).

## Prerequisites

- **Python** `3.10` or newer (`3.13` is used in this project)
- **Git**
- A terminal (Terminal on macOS, your distro’s terminal on Linux, **PowerShell** or **Command Prompt** on Windows)

Commands below assume you **open a terminal**, **clone or enter the project folder**, and run steps from the **repository root** (`MyLabs/`).

---

## Setup

Typical order: **create venv → activate → upgrade pip → install dependencies → `python -m pip install -e .` → copy `.env.example` to `.env`**. All `pip` / `python` commands below assume the **repository root** as the current directory unless noted.

### 1. Create a virtual environment

This project keeps the environment in **`.venv/`** at the repo root (ignored by Git). Use `python3` on Linux/macOS if `python` still points to Python 2.

| OS | Command |
|----|---------|
| **Linux** | `python3 -m venv .venv` |
| **macOS** | `python3 -m venv .venv` (or `python -m venv .venv` if `python` is 3.x) |
| **Windows — PowerShell or CMD** | `py -3 -m venv .venv` or `python -m venv .venv` |
| **WSL** (Windows Subsystem for Linux) | Same as Linux: `python3 -m venv .venv` |

### 2. Activate the virtual environment

Activate **once per terminal session**. Until you do, **`python -m pip install`** may target your **system** Python instead of **`.venv`**.

| OS / shell | Command |
|------------|---------|
| **Linux** — bash, zsh, … | `source .venv/bin/activate` |
| **Linux / macOS** — **fish** | `source .venv/bin/activate.fish` |
| **Linux / macOS** — **csh/tcsh** | `source .venv/bin/activate.csh` |
| **macOS** — bash, zsh, … | `source .venv/bin/activate` |
| **WSL** | Same as Linux: `source .venv/bin/activate` |
| **Windows — Command Prompt** | `.venv\Scripts\activate.bat` |
| **Windows — PowerShell** | `.\.venv\Scripts\Activate.ps1` |
| **Windows — Git Bash** | `source .venv/Scripts/activate` (if that fails, open **CMD** or **PowerShell** and use the rows above) |

**PowerShell note:** If script execution is disabled, run once (as Administrator only if your policy requires it):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Check that activation worked** (optional):

| OS | Command | Expected |
|----|---------|----------|
| **Linux / macOS / WSL** | `which python` | Path ending in `.venv/bin/python` |
| **Windows — CMD** | `where python` | `.venv\Scripts\python.exe` first |
| **Windows — PowerShell** | `Get-Command python` | Under `.venv\Scripts\` |

After activation, your prompt usually shows **`(.venv)`**.

**Deactivate** (any OS): `deactivate`

### 3. Install dependencies

With the venv **activated**, always prefer **`python -m pip`** so the same interpreter runs `pip`:

```bash
python -m pip install --upgrade pip
```

Then install this project’s dependencies (from the repo root).

| Goal | Command |
|------|---------|
| **Normal install** (direct deps in `requirements.txt`; pip resolves versions) | `python -m pip install -r requirements.txt` |
| **Reproducible install** (exact versions from `requirements-lock.txt`) | `python -m pip install -r requirements-lock.txt` |
| **Editable install** (so `import settings` / `import database` work without `PYTHONPATH`) | `python -m pip install -e .` |

Run **`python -m pip install -e .`** once after the requirements install. That registers the top-level packages from `pyproject.toml` so lab scripts can import `settings` and `database`.

**Install, upgrade, or remove a single package** (examples):

| Action | Command |
|--------|---------|
| Install one package | `python -m pip install requests` |
| Pin a version | `python -m pip install "pandas>=2.0,<3"` |
| Upgrade a package | `python -m pip install -U httpx` |
| Uninstall | `python -m pip uninstall httpx` |
| Show what is installed | `python -m pip list` or `python -m pip show pandas` |

If you add a dependency for the whole project, edit **`requirements.txt`**, reinstall, and regenerate **`requirements-lock.txt`** when you use the lockfile workflow (`python -m pip freeze > requirements-lock.txt`).

On Linux/macOS, if the `pip` command is missing, **`python3 -m pip`** is the reliable form.

**PyTorch / GPU (Linux):** This stack pins **PyTorch 2.11** with **CUDA 13** wheels on Linux. You need a recent **NVIDIA driver** compatible with CUDA 13. Installs can be large. On macOS or CPU-only machines, you may need a different `torch` build (see [PyTorch get started](https://pytorch.org/get-started/locally/)).

**Refresh the lockfile** after you change packages (so CI and others stay in sync):

```bash
python -m pip freeze > requirements-lock.txt
```

#### Optional setup scripts

| OS / environment | Command |
|------------------|---------|
| **Linux** / **macOS** | `./setup_repo.sh` or `./setup_repo.sh --lock` (run `chmod +x setup_repo.sh` once) |
| **Windows — PowerShell** | `.\setup_repo.ps1` or `.\setup_repo.ps1 -Lock` (if `Activate.ps1` is blocked, see [Setup §2](#2-activate-the-virtual-environment)) |
| **Windows — Git Bash** | Same as Linux: `./setup_repo.sh` |

These scripts create `.venv`, install dependencies, run **`python -m pip install -e .`**, and copy `.env.example` to `.env` when missing.

Plain **cmd.exe** does not run `.sh` or `.ps1` by default; use **PowerShell**, **Git Bash**, or **WSL**, or follow the manual `pip` commands in the table above.

### 4. Configure the environment

Create `.env` at the project root from the example file:

| OS / shell | Command |
|------------|---------|
| **Linux** / **macOS** | `cp .env.example .env` |
| **Windows — CMD** | `copy .env.example .env` |
| **Windows — PowerShell** | `Copy-Item .env.example .env` |

Then edit **`.env`** and ensure **`SQLALCHEMY_DATABASE_URL`** is set — it is **required**. The app loads **`.env`** from the project directory (next to **`database.py`**), not from the shell’s current working directory.

Example for the school SQLite file (same value on every OS). Create or refresh the file with **`python labs/sql/init_school_db.py`** before using SQLAlchemy; the path matches **`settings.SCHOOL_DB_PATH`** (**`data/sql_files/school.db`**):

```bash
SQLALCHEMY_DATABASE_URL=sqlite:///./data/sql_files/school.db
```

Relative SQLite paths are resolved against the project root, so the database file stays in the right place even if you run scripts from another directory.

Optional keys (see `.env.example` for the full list) include `SQLALCHEMY_ECHO`, pool settings, and `ENVIRONMENT` / `DEBUG`.

---

## Database (`database.py`)

- **`engine`** / **`SessionLocal`** — SQLAlchemy engine and session factory.
- **`Base`** — declarative base for ORM models.
- **`get_db()`** — generator suitable for dependency injection (for example **`FastAPI`**): yields a session and closes it in a **`finally`** block.

Import only after **`.env`** exists with **`SQLALCHEMY_DATABASE_URL`** set.

---

## Alembic

Alembic is installed with the project. There is no `alembic/` folder in the repo until you initialize it (same command everywhere; run with the venv activated):

```bash
alembic init alembic
```

Then point **`sqlalchemy.url`** in **`alembic.ini`** (or **`env.py`**) at the same URL as **`SQLALCHEMY_DATABASE_URL`**, or import it from your **`settings`** module.

---

## Repository layout

| Path | Purpose |
|------|---------|
| `database.py` | SQLAlchemy engine, session, `Base`, `get_db()` |
| `settings.py` | Project `BASE_PATH` and subpaths under `data/` and `labs/` |
| `data/` | CSV, exports, JSON, PDFs, text files, SQL snippets, etc. (see `settings.py`) |
| `data/text_files/` | Sample `.txt` files for `labs/files/` (`settings.FILES_PATH` / `TEXT_PATH`) |
| `data/sql_files/` | School demo SQLite: versioned files are `school_schema.sql` and `school_seed.sql`. **`school.db` is not committed** (`*.db` is in `.gitignore`); create it locally with `python labs/sql/init_school_db.py` → `settings.SCHOOL_DB_PATH` |
| `labs/` | Lab code: `classes/`, `files/`, `pandas/`, `sql/`, etc. |
| `labs/files/` | Text I/O exercises (read/write, append, upsert, folders, replace file) |
| `labs/pandas/` | Pandas exercises (e.g. load CSV via `settings.CSV_PATH`) |
| `labs/matplotlib/` | Small plots (e.g. `plot_people.py` from `people.csv`) |
| `requirements.txt` | Direct dependencies (SQLAlchemy, Alembic, torch stack, Jupyter, etc.) |
| `requirements-lock.txt` | Full pinned environment (`python -m pip freeze`) for reproducible installs |
| `pyproject.toml` | Local package metadata; `python -m pip install -e .` exposes `settings` and `database` |
| `setup_repo.sh` | Optional setup (Linux/macOS/Git Bash): venv, deps, editable install, `.env` from example |
| `setup_repo.ps1` | Same automation for **Windows PowerShell** |
| `.env` | Local secrets and config — **not committed** (see `.gitignore`) |
| `.env.example` | Template for required variables (copy to `.env`) |

---

## Running lab scripts

From the repository root, with the venv activated and **`python -m pip install -e .`** run once so `import settings` works.

| OS | Typical command |
|----|-----------------|
| **Linux** / **macOS** | `python3 labs/files/read_test.py` or `python labs/pandas/read_people.py` |
| **Windows** | `python labs\files\read_test.py` or `py labs\pandas\read_people.py` |

Forward slashes work on Windows in current Python versions (`labs/files/read_test.py`).

### `labs/files/` (text files under `data/text_files/`)

Scripts use **`settings.FILES_PATH`**. Naming follows **action + topic** (e.g. `read_test`, `write_student`, `read_fruits`) so similar exercises stay easy to tell apart.

| Script | Role |
|--------|------|
| `read_test.py` / `write_test.py` | Read/write `test.txt` |
| `read_fruits.py` / `write_fruits.py` | Read/write `test2.txt` (line list) |
| `read_student.py` / `write_student.py` | Read/write `student.txt` (CSV-style rows) |
| `append_student.py` | Append rows to `student.txt` |
| `update_student.py` | Upsert a row in `student.txt` by `id` |
| `exist_folder.py` | Ensure a folder exists (`mkdir` with parents) |
| `replace_file.py` | Ensure folder, replace or create a file (e.g. avatar path) |

### `labs/pandas/`

| Script | Role |
|--------|------|
| `read_people.py` | Load `people.csv` from **`settings.CSV_PATH`** into a DataFrame and print it |

### `labs/matplotlib/`

| Script | Role |
|--------|------|
| `plot_people.py` | Bar chart of ages from **`people.csv`** (requires a display backend for `plt.show()`) |

### `labs/sql/`

| Script | Role |
|--------|------|
| `init_school_db.py` | Create or overwrite **`data/sql_files/school.db`** from `school_schema.sql` + `school_seed.sql` (departments, rooms, teachers, students, guardians, courses, prerequisites, offerings, enrollments) |

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

### Push this project to GitHub

Target remote: [https://github.com/florentz14/MyLabs](https://github.com/florentz14/MyLabs).

1. **Stage and commit** (from the repo root):

   ```bash
   git add -A
   git status
   git commit -m "Describe your change in a short message"
   ```

2. **Set the remote** (only once; skip if `git remote -v` already shows `origin`):

   ```bash
   git remote add origin https://github.com/florentz14/MyLabs.git
   # or SSH:
   # git remote add origin git@github.com:florentz14/MyLabs.git
   ```

3. **Push** the `main` branch:

   ```bash
   git push -u origin main
   ```

4. **Authentication** — GitHub does **not** accept your account password for Git over HTTPS. You must use one of:

   - **HTTPS + Personal Access Token (classic):** [Create a token](https://github.com/settings/tokens) with the **`repo`** scope. When Git asks for a password, paste the **token** (username = your GitHub login).
   - **SSH:** [Add an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) to your GitHub account, then use the remote URL `git@github.com:florentz14/MyLabs.git` and run **`ssh -T git@github.com`** to verify.

If **`git push`** fails with **`401`** or “invalid credentials”, use a PAT or switch to SSH. If you see **`Permission denied (publickey)`**, your SSH key is missing or not loaded on GitHub.

After the first successful push, the repository page will show your code instead of an empty repo.

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
   - **Linux** / **macOS**: unzip in the terminal or with the file manager; then **`cd`** into the extracted folder (often **`MyLabs-main`** if downloaded from GitHub — you may rename it to **`MyLabs`**).
   - **Windows**: right-click the ZIP → **Extract All…**, then open **PowerShell** or **CMD** and **`cd`** into that folder.

ZIP downloads **do not** include Git history; use **clone** if you plan to contribute with branches and pull requests.

---

## Use this project (quick path)

1. **Obtain** the code: [clone](#clone-with-git-recommended) or [download ZIP](#download-as-a-zip-no-git-required).
2. **Follow [Setup](#setup)** above: create and activate **`.venv`**, install with **`requirements.txt`** or **`requirements-lock.txt`**, run **`python -m pip install -e .`**, copy **`.env.example`** to **`.env`**, set **`SQLALCHEMY_DATABASE_URL`**. Or use the **[optional setup scripts](#optional-setup-scripts)** (`./setup_repo.sh` on Linux/macOS/Git Bash, **`.\setup_repo.ps1`** on Windows PowerShell).
3. **Run** what you need: e.g. [Running lab scripts](#running-lab-scripts), or import `database` / `settings` from the project root (or with `PYTHONPATH` set to the repo root if you run from elsewhere).

If anything imports **`database.py`**, **`.env` must exist** with a valid **`SQLALCHEMY_DATABASE_URL`**.

---

## Contributing

Contributions are welcome: fixes, docs, exercises, or small refactors. Typical flow:

1. **Fork** the repository on the hosting site (GitHub/GitLab), or ask for **collaborator** access if it is a private course repo.
2. **Clone your fork** (or the shared remote) and create a **branch** off the default branch (`main` or `master`):

   ```bash
   git checkout -b feature/short-description
   ```

3. **Make changes** in small, focused commits with **clear messages** (what changed and why).
4. **Run tests** if the project has them (**`pytest -q`**) and ensure new code matches existing style (formatting, naming).
5. **Do not commit** `.env`, local `.db` files, or `.venv/` — they are listed in `.gitignore`.
6. If you change dependencies, update **`requirements.txt`** as needed and regenerate **`requirements-lock.txt`** (`python -m pip freeze > requirements-lock.txt`) so others and CI stay aligned.
7. **Push** your branch and open a **pull request** / **merge request** against the upstream default branch. Describe the change and link any related issue.

If there is no public remote yet, you can still use branches locally and share patches or zips; once a remote exists, the same Git workflow applies on Linux, macOS, and Windows.

For course-style work, the instructor may ask for a branch named `lab/<your-name>` instead of `feature/…` — follow their guidelines when they differ from the above.

---

Good luck and happy coding.
