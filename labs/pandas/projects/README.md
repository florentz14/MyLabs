# Projects Labs (`labs/pandas/projects`)

Small **end-to-end** pandas flows: load a shared CSV, inspect and summarize. Useful as a skeleton before adding cleaning, plots, or models.

## Requirements

- **`settings`** for paths (`EXCEL_PATH` → **`data/excel/`**).
- From the repo root: **`PYTHONPATH=.`** or **`python -m pip install -e .`**.

## Scripts

| File | Role | Description |
| --- | --- | --- |
| `basic_project.py` | ETL skeleton | Load **`people.csv`**, show load, **`head`**, and numeric summary (`select_dtypes` + **`describe`**). |

## Running

```bash
PYTHONPATH=. python3 labs/pandas/projects/basic_project.py
```

## See also

- Similar starters: [../io/read_people.py](../io/read_people.py), [../stats/people_summary.py](../stats/people_summary.py)
- Full pandas area: [../README.md](../README.md)
