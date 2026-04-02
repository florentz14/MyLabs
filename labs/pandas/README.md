# Pandas Labs

Core starter scripts in this folder use short, meaningful names. The **`basics/`** subfolder adds **55** numbered exercises; **`advanced/`** holds a smaller set of longer scripts. See **`index.md`** for a recommended path through the material.

| File / folder | Role |
|---------------|------|
| `read_people.py` | Load `people.csv` from `EXCEL_PATH` and print rows |
| `cleaning.py` | Tiny cleaning starter (`drop_duplicates`, coercion, `fillna`) |
| `features.py` | Tiny feature starter (boolean + scaled numeric) |
| `stats.py` | Tiny descriptive stats starter |
| `stock.py` | Load stock `.xlsx` from `EXCEL_PATH`, normalize and validate columns |
| `index.md` | Suggested learning route: foundation → basics → advanced |
| `basics/` | 55 numbered one-topic scripts (`01` … `55`); shared `sample_data.py` — **`basics/README.md`** |
| `advanced/` | 4 examples (groupby multi-agg, pivot, ranks/quantiles, Series arithmetic) — **`advanced/README.md`** |

## `basics/` subfolder

`basics/` is a guided set of short, one-topic scripts for beginner practice.
It covers core pandas operations step by step: selection, filtering, missing values,
sorting, grouping, indexing (`loc`/`iloc`), and exporting (`to_csv`). Later scripts use **`exam_data.csv`**.

Run from repo root:

```bash
python3 labs/pandas/read_people.py
python3 labs/pandas/stock.py
python3 labs/pandas/basics/01_head.py
PYTHONPATH=. python3 labs/pandas/advanced/01_groupby_multiagg.py
python3 labs/pandas/advanced/04_series_arithmetic.py
```
