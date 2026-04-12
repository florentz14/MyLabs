# Pandas Labs (`labs/pandas/`)

Scripts are grouped by topic: **`basics/`** (**55** numbered exercises and **7** roadmap-style scripts), **`advanced/`**, **`io/`**, **`cleaning/`**, **`viz/`**, ITSE-style folders (`inspect/`, `select/`, …), and more. Only **`README.md`** and **`index.md`** live at this root. Suggested study route: **`index.md`**.

**Imports:** Anything that uses **`from settings import …`** must be run from the repo root with **`PYTHONPATH=.`** or after **`python -m pip install -e .`**.

| File | Role | Description |
| --- | --- | --- |
| `io/` | Subfolder | Read/write starters: `read_people.py`, `stock.py`, ITSE `load_csv.py` / `to_csv_updated.py` |
| `cleaning/` | Subfolder | `quick_clean.py`, `basic_cleaning.py` (`people.csv`), step-by-step hospital CSV cleanup — notes in **`README_starter.md`** |
| `stats/` | Subfolder | `people_summary.py` — mean, median, `value_counts` on `people.csv` |
| `features/` | Subfolder | `derived_columns.py`, `basic_features.py` — **`README_starter.md`** |
| `viz/` | Subfolder | Matplotlib (+ pandas where needed) — **`viz/README.md`** |
| `projects/` | Subfolder | End-to-end skeletons — **`projects/README.md`** |
| `analysis/` | Subfolder | Pandas EDA on root **`data/`** — **`analysis/README.md`** |
| `inspect/`, `select/`, `filter/`, `transform/`, `sort/`, `group/`, `aggregate/` | Subfolders | Small ITSE-style demos (`settings.load_students()`, `ITSE_STUDENTS_*`) |
| `basics/` | Subfolder | Numbered `01` … `55` scripts, roadmap files, `sample_data.py` — **`basics/README.md`** |
| `advanced/` | Subfolder | Groupby, pivot, ranks, Series arithmetic, correlations, plotting — **`advanced/README.md`** |
| `index.md` | Index | Suggested learning route |

## `basics/` subfolder

`basics/` is a guided set of short, one-topic scripts for beginner practice (numbered series plus roadmap files such as `introduction.py` and `read_json.py`).
It covers core pandas operations step by step: selection, filtering, missing values,
sorting, grouping, indexing (`loc`/`iloc`), and exporting (`to_csv`). Later scripts use **`exam_data.csv`**.

Run from repo root:

```bash
python3 labs/pandas/io/read_people.py
python3 labs/pandas/io/stock.py
python3 labs/pandas/basics/01_head.py
PYTHONPATH=. python3 labs/pandas/advanced/01_groupby_multiagg.py
python3 labs/pandas/advanced/04_series_arithmetic.py
PYTHONPATH=. python3 labs/pandas/analysis/analyze_people.py
```
