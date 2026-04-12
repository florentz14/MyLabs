# Machine Learning Labs (`labs/ml`)

Very short **machine learning** labs: synthetic data, loading CSV, and a reference linear model.

## Requirements

- Repo environment (`requirements.txt`): **pandas**, **scikit-learn**, etc.
- Scripts that use **`settings`** need an editable install or **`PYTHONPATH=.`** from the repo root:

```bash
python -m pip install -e .
```

## Scripts

| File | Role | Description |
| --- | --- | --- |
| `basic_ml.py` | Regression demo | Synthetic regression with **`LinearRegression`** (no CSV). |
| `ml_01_load_data.py` | Load / inspect | Load **`data/excel/students.csv`** and inspect shape/columns. |
| `ml_02_train_test_split.py` | Split | Split features and target with **`train_test_split`**. |
| `ml_03_linear_regression.py` | Train / evaluate | Train linear regression on **`students.csv`** and print **MAE**. |

## Examples

From the repository root:

```bash
PYTHONPATH=. python3 labs/ml/basic_ml.py
PYTHONPATH=. python3 labs/ml/ml_01_load_data.py
PYTHONPATH=. python3 labs/ml/ml_02_train_test_split.py
PYTHONPATH=. python3 labs/ml/ml_03_linear_regression.py
```

## Related

- Metrics: [../eval/README.md](../eval/README.md)
- Tabular analysis: [../pandas/README.md](../pandas/README.md)
