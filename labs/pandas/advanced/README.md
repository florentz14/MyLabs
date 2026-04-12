# Pandas Advanced Labs (`labs/pandas/advanced`)

Short intermediate-to-advanced pandas scripts. Most use **`data/excel/exam_data.csv`** (`settings.CSV_PATH`). **`04_series_arithmetic.py`** is self-contained (Series only).

If **`import settings`** fails, run from the repo root with **`PYTHONPATH=.`** or **`python -m pip install -e .`**.

| File | Role | Description |
| --- | --- | --- |
| `01_groupby_multiagg.py` | Group | `groupby` with multiple keys and multiple aggregations |
| `02_pivot_table_report.py` | Pivot | Pivot tables with margins and multiple value columns |
| `03_rank_and_quantiles.py` | Rank / bin | Ranks and quantile bands with **`qcut`** |
| `04_series_arithmetic.py` | Series | Arithmetic between two Series (operators and `.add` / `.sub` / …) |
| `correlations.py` | Correlation | Correlation matrix of numeric columns in **`exam_data.csv`** |
| `plotting.py` | Plot | Scatter **`score`** vs **`study_hours`** → PNG under **`data/export/`** |

## Running

From the repository root:

```bash
PYTHONPATH=. python3 labs/pandas/advanced/01_groupby_multiagg.py
PYTHONPATH=. python3 labs/pandas/advanced/02_pivot_table_report.py
PYTHONPATH=. python3 labs/pandas/advanced/03_rank_and_quantiles.py
PYTHONPATH=. python3 labs/pandas/advanced/04_series_arithmetic.py
PYTHONPATH=. python3 labs/pandas/advanced/correlations.py
PYTHONPATH=. python3 labs/pandas/advanced/plotting.py
```

## See also

- Pandas area index: [../index.md](../index.md)
- Numbered basics: [../basics/README.md](../basics/README.md)
