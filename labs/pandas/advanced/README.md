# Pandas Advanced Labs

Short, focused scripts for intermediate/advanced pandas practice.
Most use `data/excel/exam_data.csv`; `04_series_arithmetic.py` is standalone.

If `settings` import fails, run from repo root with `PYTHONPATH=.`.

| # | File | Description |
|---|------|-------------|
| 1 | `01_groupby_multiagg.py` | Group by multiple keys and apply several aggregations |
| 2 | `02_pivot_table_report.py` | Build pivot tables with totals and multiple value columns |
| 3 | `03_rank_and_quantiles.py` | Rank students and split scores into quartile bands (`qcut`) |
| 4 | `04_series_arithmetic.py` | Arithmetic between two Series (operators, summary table, `.add`/`.sub`/…) |

Run from repo root:

```bash
PYTHONPATH=. python3 labs/pandas/advanced/01_groupby_multiagg.py
PYTHONPATH=. python3 labs/pandas/advanced/02_pivot_table_report.py
PYTHONPATH=. python3 labs/pandas/advanced/03_rank_and_quantiles.py
python3 labs/pandas/advanced/04_series_arithmetic.py
```
