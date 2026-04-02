# Pandas Study Path

Suggested order to study pandas labs in this repo.

## 1) Foundation (single-file starters)

Start here to warm up with tiny scripts:

- `read_people.py`
- `cleaning.py`
- `features.py`
- `stats.py`
- `stock.py`

## 2) Basics Track (01 to 55)

Work through the full basics sequence in order:

- `basics/01_head.py` -> ... -> `basics/55_compare_small_vs_large.py`
- Full catalog and descriptions: `basics/README.md`

Run examples from repo root:

```bash
python3 labs/pandas/basics/01_head.py
PYTHONPATH=. python3 labs/pandas/basics/52_column_headers.py
```

## 3) Advanced Track (01 to 04)

After basics, continue with:

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
