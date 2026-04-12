# Data analysis with pandas (`labs/pandas/analysis/`)

EDA-style scripts over the repo **`data/`** tree using **pandas** (plus a small **pathlib** inventory). Paths come from **`settings`** (`DATA_PATH`, `EXCEL_PATH`, `JSON_PATH`).

Run from the **repository root** with an editable install or **`PYTHONPATH=.`**:

```bash
PYTHONPATH=. python3 labs/pandas/analysis/overview_data_inventory.py
PYTHONPATH=. python3 labs/pandas/analysis/analyze_people.py
PYTHONPATH=. python3 labs/pandas/analysis/analyze_students.py
PYTHONPATH=. python3 labs/pandas/analysis/analyze_exam_data.py
PYTHONPATH=. python3 labs/pandas/analysis/analyze_json_students.py
PYTHONPATH=. python3 labs/pandas/analysis/analyze_invoices_relations.py
```

## Scripts

| File | Role | Description |
| --- | --- | --- |
| `overview_data_inventory.py` | Inventory | Lists every file under **`data/`** with size and extension counts (stdlib **`pathlib`**). |
| `analyze_people.py` | EDA | **`data/excel/people.csv`** — departments, cities, salary stats. |
| `analyze_students.py` | EDA | **`data/excel/students.csv`** — majors, GPA, tuition and scholarships. |
| `analyze_exam_data.py` | EDA | **`data/excel/exam_data.csv`** — scores, regions, pass rates. |
| `analyze_json_students.py` | EDA | **`data/json/students_records.json`** — same domain as students CSV. |
| `analyze_invoices_relations.py` | Join | Merges **`invoices.csv`**, **`customers.csv`**, **`employees.csv`**. |

## Related

- Basics: [../basics/README.md](../basics/README.md)
- Advanced: [../advanced/README.md](../advanced/README.md)
- Pandas area overview: [../README.md](../README.md)
- Repo **`data/`** layout: [../../../README.md](../../../README.md) (*Repository layout*)
