# Pandas basics (tiny examples)

This folder holds **55** numbered scripts (`01_*.py` … `55_*.py`) plus **7** roadmap-style scripts (`introduction.py`, `getting_started.py`, `pandas_series.py`, `dataframes.py`, `read_csv.py`, `read_json.py`, `analyze_data.py`), one topic per file. They are meant to be run from the **repository root** with `python3 labs/pandas/basics/<script>.py`.

## Shared data

- **`sample_data.py`** — in-memory practice tables:
  - `sample_df()` — small default dataset (`Name`, `Age`, `City`, `Score`).
  - `sample_df_large()` — larger variant for comparisons (see `55_compare_small_vs_large.py`).
- **`exam_data.csv`** — under `data/excel/` (via `settings.CSV_PATH`); used from about **`30_first_three_rows.py`** onward for realistic rows. Scripts that import `settings` expect **`python -m pip install -e .`** from the repo root, or **`PYTHONPATH=.`** when you run them.

## Related docs

- Parent overview: [`../README.md`](../README.md)
- Suggested study order: [`../index.md`](../index.md)
- Longer or heavier examples: [`../advanced/`](../advanced/)

## Quick start

```bash
python3 labs/pandas/basics/01_head.py
```

Scripts that use **`settings`** (for example `20_to_csv.py`, `52_column_headers.py`) need the editable install or `PYTHONPATH=.` from the repo root.

| File | Role | Description |
| --- | --- | --- |
| `01_head.py` | Inspect | First rows |
| `02_shape.py` | Structure | `(rows, cols)` |
| `03_column.py` | Select | One column |
| `04_subset.py` | Select | Several columns |
| `05_filter_numeric.py` | Filter | Boolean filter on numbers |
| `06_filter_string.py` | Filter | Filter on string equality |
| `07_value_counts.py` | Count | Frequency counts |
| `08_isnull.py` | Missing data | Missing values per column |
| `09_fillna_mean.py` | Missing data | Impute with mean |
| `10_describe.py` | Statistics | Numeric summary |
| `11_derived_column.py` | Transform | New column (`birth_year`) |
| `12_sort_values.py` | Sort | Sort by column |
| `13_groupby_mean.py` | Group | Group + mean |
| `14_rename.py` | Rename / replace | Rename one column (`Name` → `User`, from `sample_data`) |
| `15_drop_column.py` | Drop | Drop a column |
| `16_iloc.py` | Select | Index by position |
| `17_loc.py` | Select | Index by label |
| `18_filter_and.py` | Filter | Multiple conditions with `&` |
| `19_tolist.py` | Convert | Series → `list` |
| `20_to_csv.py` | I/O | Write CSV under `EXCEL_PATH` |
| `21_from_dict.py` | Create | DataFrame from dictionary |
| `22_from_rows.py` | Create | DataFrame from list of dictionaries |
| `23_create_series.py` | Create | Series with custom index |
| `24_from_numpy.py` | Create | DataFrame from NumPy array |
| `25_from_dict_scores.py` | Create | DataFrame from score columns (`X`, `Y`, `Z`) |
| `26_index_labels.py` | Index | DataFrame with custom row labels (`a` to `n`) |
| `27_read_csv.py` | I/O | Read CSV, inspect columns/shape, export copy |
| `28_explore.py` | Inspect | Quick DataFrame exploration (`head`, `tail`, `info`, `describe`) |
| `29_columns.py` | Select | Create computed columns (`apply`, `map`) and rename |
| `30_first_three_rows.py` | Inspect | Load `exam_data.csv` and print `head(3)` |
| `31_nulls.py` | Missing data | Detect, count, drop, and fill missing values |
| `32_merge_concat.py` | Combine | `merge` (inner join) + vertical/horizontal `concat` |
| `33_drop.py` | Drop | Drop columns, rows, and duplicate rows |
| `34_statistics.py` | Statistics | Mean, median, std, min/max, quantile, and correlation |
| `35_index_ops.py` | Index | `set_index`, `reset_index`, index rename, and MultiIndex |
| `36_attempts_score_filter.py` | Filter | Filter exam rows with `attempts < 2` and `score > 15` |
| `37_counts.py` | Count | `value_counts` as counts, percentages, and with `dropna=False` |
| `38_sum_attempts.py` | Statistics | Sum the `attempts` column from `exam_data.csv` |
| `39_mean_score.py` | Statistics | Mean of the `score` column from `exam_data.csv` |
| `40_series_from_list.py` | Create | Create and print a Series from a Python list |
| `41_append_drop_row.py` | Drop | Add one row with `loc`, then remove it with `drop` |
| `42_series_from_numpy.py` | Create | Create and print a Series from a NumPy array |
| `43_series_from_dict.py` | Create | Create and print a Series from a Python dictionary |
| `44_sort_multi.py` | Sort | Sort by multiple columns with mixed ascending/descending |
| `45_sort_multiple_columns.py` | Select | Same sorting example with the long original-style filename |
| `46_replace_name.py` | Rename / replace | Replace one value in `name` (`Sergio` → `Suresh`) |
| `47_series_attrs.py` | Create | Named Series and core attributes (`dtype`, `shape`, `size`, etc.) |
| `48_drop_attempts.py` | Drop | Drop the `attempts` column from `exam_data.csv` |
| `49_series_to_list.py` | Create | Convert int/float/string/indexed Series to Python lists |
| `50_insert_color.py` | Transform | Insert a `color` column into `exam_data.csv` |
| `51_iterate_rows.py` | Iterate | Iterate through rows with `iterrows()` |
| `52_column_headers.py` | Inspect | Print column headers as a Python list |
| `53_rename_columns.py` | Rename / replace | Rename several columns at once (`col1` → `Column1`, …) |
| `54_series_statistics.py` | Statistics | Full Series stats: percentiles, IQR, skew, kurtosis, `describe`, ±σ bands |
| `55_compare_small_vs_large.py` | Compare | Compare `sample_df()` and `sample_df_large()` (shape, nulls, means) |

### Roadmap-style scripts

| File | Role | Description |
| --- | --- | --- |
| `introduction.py` | Overview | What pandas is and print the installed version. |
| `getting_started.py` | Overview | Minimal `Series` and `DataFrame` from literals. |
| `pandas_series.py` | Create | Series index, dtype, and element-wise operations. |
| `dataframes.py` | Create | Small `DataFrame`: columns, dtypes, selection. |
| `read_csv.py` | I/O | Load `customers.csv` from `CSV_PATH`. |
| `read_json.py` | I/O | Load `students_records.json` from `JSON_PATH`. |
| `analyze_data.py` | Inspect | `head`, `info`, `describe`, and `value_counts` on `exam_data.csv`. |

---

## Related READMEs (pandas)

- Parent folder: [../README.md](../README.md)
- Advanced (groupby, pivot, correlations, plots): [../advanced/README.md](../advanced/README.md)
- Visualization: [../viz/README.md](../viz/README.md)
- Cleaning / feature starters on disk: [../cleaning/README_starter.md](../cleaning/README_starter.md), [../features/README_starter.md](../features/README_starter.md)
