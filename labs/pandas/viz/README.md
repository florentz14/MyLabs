# Data Visualization Labs (`labs/pandas/viz`)

Chart examples with **Matplotlib**; several combine **pandas** to read CSVs or prepare data.

## Requirements

- **`matplotlib`** (listed in the repo `requirements.txt`).
- Data paths via **`settings`** → use **`PYTHONPATH=.`** or **`pip install -e .`** from the repo root.

## Scripts

| File | Role | Description |
| --- | --- | --- |
| `basic_viz.py` | Line plot | Simple lines; saves **`data/gen/basic_viz.png`** (**Agg** backend, no window). |
| `viz_line_basic.py` | Line plot | Minimal line with **`plt.show()`** (needs a display backend for a window). |
| `viz_bar_people_basic.py` | Bar chart | Age bars from **`data/excel/people.csv`**. |
| `viz_bar_age_mean_by_city.py` | Bar chart | In-memory CSV → mean age by city → horizontal bar; writes **`people_city_sample.csv`** under **`data/excel/`** and **`data/gen/viz_age_mean_by_city.png`**. |

## Running

From the repository root:

```bash
PYTHONPATH=. python3 labs/pandas/viz/basic_viz.py
PYTHONPATH=. python3 labs/pandas/viz/viz_bar_people_basic.py
```

## See also

- Pandas “advanced” scatter (exam): [../advanced/README.md](../advanced/README.md) (`plotting.py`)
- Pandas index: [../index.md](../index.md)
