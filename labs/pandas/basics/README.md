# Pandas basics (tiny examples)

This folder holds **55** numbered scripts (`01_*.py` … `55_*.py`), one topic per file. They are meant to be run from the **repository root** with `python3 labs/pandas/basics/<script>.py`.

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

| # | File | Idea |
|---|------|------|
| 1 | `01_head.py` | First rows |
| 2 | `02_shape.py` | `(rows, cols)` |
| 3 | `03_column.py` | One column |
| 4 | `04_subset.py` | Several columns |
| 5 | `05_filter_numeric.py` | Boolean filter on numbers |
| 6 | `06_filter_string.py` | Filter on string equality |
| 7 | `07_value_counts.py` | Frequency counts |
| 8 | `08_isnull.py` | Missing values per column |
| 9 | `09_fillna_mean.py` | Impute with mean |
| 10 | `10_describe.py` | Numeric summary |
| 11 | `11_derived_column.py` | New column (`birth_year`) |
| 12 | `12_sort_values.py` | Sort by column |
| 13 | `13_groupby_mean.py` | Group + mean |
| 14 | `14_rename.py` | Rename one column (`Name` → `User`, from `sample_data`) |
| 15 | `15_drop_column.py` | Drop a column |
| 16 | `16_iloc.py` | Index by position |
| 17 | `17_loc.py` | Index by label |
| 18 | `18_filter_and.py` | Multiple conditions with `&` |
| 19 | `19_tolist.py` | Series → `list` |
| 20 | `20_to_csv.py` | Write CSV under `EXCEL_PATH` |
| 21 | `21_from_dict.py` | DataFrame from dictionary |
| 22 | `22_from_rows.py` | DataFrame from list of dictionaries |
| 23 | `23_create_series.py` | Series with custom index |
| 24 | `24_from_numpy.py` | DataFrame from NumPy array |
| 25 | `25_from_dict_scores.py` | DataFrame from score columns (`X`, `Y`, `Z`) |
| 26 | `26_index_labels.py` | DataFrame with custom row labels (`a` to `n`) |
| 27 | `27_read_csv.py` | Read CSV, inspect columns/shape, export copy |
| 28 | `28_explore.py` | Quick DataFrame exploration (`head`, `tail`, `info`, `describe`) |
| 29 | `29_columns.py` | Create computed columns (`apply`, `map`) and rename |
| 30 | `30_first_three_rows.py` | Load `exam_data.csv` and print `head(3)` |
| 31 | `31_nulls.py` | Detect, count, drop, and fill missing values |
| 32 | `32_merge_concat.py` | `merge` (inner join) + vertical/horizontal `concat` |
| 33 | `33_drop.py` | Drop columns, rows, and duplicate rows |
| 34 | `34_statistics.py` | Mean, median, std, min/max, quantile, and correlation |
| 35 | `35_index_ops.py` | `set_index`, `reset_index`, index rename, and MultiIndex |
| 36 | `36_attempts_score_filter.py` | Filter exam rows with `attempts < 2` and `score > 15` |
| 37 | `37_counts.py` | `value_counts` as counts, percentages, and with `dropna=False` |
| 38 | `38_sum_attempts.py` | Sum the `attempts` column from `exam_data.csv` |
| 39 | `39_mean_score.py` | Mean of the `score` column from `exam_data.csv` |
| 40 | `40_series_from_list.py` | Create and print a Series from a Python list |
| 41 | `41_append_drop_row.py` | Add one row with `loc`, then remove it with `drop` |
| 42 | `42_series_from_numpy.py` | Create and print a Series from a NumPy array |
| 43 | `43_series_from_dict.py` | Create and print a Series from a Python dictionary |
| 44 | `44_sort_multi.py` | Sort by multiple columns with mixed ascending/descending |
| 45 | `45_sort_multiple_columns.py` | Same sorting example with the long original-style filename |
| 46 | `46_replace_name.py` | Replace one value in `name` (`Sergio` → `Suresh`) |
| 47 | `47_series_attrs.py` | Named Series and core attributes (`dtype`, `shape`, `size`, etc.) |
| 48 | `48_drop_attempts.py` | Drop the `attempts` column from `exam_data.csv` |
| 49 | `49_series_to_list.py` | Convert int/float/string/indexed Series to Python lists |
| 50 | `50_insert_color.py` | Insert a `color` column into `exam_data.csv` |
| 51 | `51_iterate_rows.py` | Iterate through rows with `iterrows()` |
| 52 | `52_column_headers.py` | Print column headers as a Python list |
| 53 | `53_rename_columns.py` | Rename several columns at once (`col1` → `Column1`, …) |
| 54 | `54_series_statistics.py` | Full Series stats: percentiles, IQR, skew, kurtosis, `describe`, ±σ bands |
| 55 | `55_compare_small_vs_large.py` | Compare `sample_df()` and `sample_df_large()` (shape, nulls, means) |
