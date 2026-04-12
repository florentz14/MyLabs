# Model Evaluation Labs (`labs/eval`)

Introductory exercises on **evaluation metrics** with **scikit-learn**: regression errors and classification accuracy.

## Requirements

- Repo dependencies: `requirements.txt` (includes **scikit-learn**).
- If a script imports **`settings`**, from the repo root use **`python -m pip install -e .`** or **`PYTHONPATH=.`** when you run it.

## How to run

From the repository root:

```bash
PYTHONPATH=. python3 labs/eval/basic_metrics.py
```

## Scripts

| File | Role | Description |
| --- | --- | --- |
| `basic_metrics.py` | Metrics demo | **MAE**, **MSE** (regression) and **accuracy** (classification) via **`sklearn.metrics`**. |

## Related

- Simple ML: [../ml/README.md](../ml/README.md)
- Pandas / projects: [../pandas/README.md](../pandas/README.md)
