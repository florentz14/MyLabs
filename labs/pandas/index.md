# Pandas Study Path

Suggested order to study pandas labs in this repo.

## 1) Foundation (small starters)

Start here to warm up:

- `io/read_people.py`
- `cleaning/quick_clean.py`
- `features/derived_columns.py`
- `stats/people_summary.py`
- `io/stock.py`

## 2) Basics Track (01 to 55)

Optional warm-up (same folder): `basics/introduction.py` → `basics/analyze_data.py` (short roadmap-style scripts).

Work through the full basics sequence in order:

- `basics/01_head.py` -> ... -> `basics/55_compare_small_vs_large.py`
- Full catalog and descriptions: `basics/README.md`

Run examples from repo root:

```bash
python3 labs/pandas/basics/01_head.py
PYTHONPATH=. python3 labs/pandas/basics/52_column_headers.py
```

## 3) Analysis on `data/` (optional)

After you are comfortable with **`read_csv`** and **`groupby`**, run the EDA scripts that summarize files under the repo **`data/`** folder:

- `analysis/README.md` — catalog
- Examples: `analysis/analyze_people.py`, `analysis/analyze_exam_data.py`

```bash
PYTHONPATH=. python3 labs/pandas/analysis/analyze_people.py
```

## 4) Advanced Track (01 to 04)

Continue with:

- `advanced/01_groupby_multiagg.py`
- `advanced/02_pivot_table_report.py`
- `advanced/03_rank_and_quantiles.py`
- `advanced/04_series_arithmetic.py`

More details: `advanced/README.md`

Run from repo root:

```bash
PYTHONPATH=. python3 labs/pandas/advanced/01_groupby_multiagg.py
python3 labs/pandas/advanced/04_series_arithmetic.py
```
