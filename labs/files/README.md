# Text and CSV I/O (`labs/files`)

Exercises for **reading and writing files** with the standard library: plain text, **CSV** (`csv.reader` / `writer`), **DictReader** / **DictWriter**, tab-separated values, **append** mode, and small **interactive** programs.

Scripts are **numbered `01`–`18`** in suggested learning order (simple I/O first, then structured text, filesystem helpers, CSV APIs, interactive last)—same idea as `labs/pandas/basics/`.

All paths go through **`settings`** (`FILES_PATH` → `data/text/`, `CSV_PATH` → `data/excel/`). From the repo root, use an **editable install** so imports work:

```bash
python -m pip install -e .
```

Alternatively, prefix runs with `PYTHONPATH=.` (same as other labs that import `settings`).

Run examples:

```bash
python3 labs/files/01_read_test.py
python3 labs/files/12_csv_read_write.py
```

## Scripts

| # | File | Description | Role |
| --- | ------ | ------------- | ------ |
| 1 | `01_read_test.py` | Read an entire text file into memory and print it. | Reads `test.txt` from **`FILES_PATH`**. |
| 2 | `02_write_test.py` | Create or overwrite a simple text file. | Writes `test.txt` under **`FILES_PATH`**. |
| 3 | `03_read_fruits.py` | Load a line-oriented list from disk. | Reads `test2.txt`. |
| 4 | `04_write_fruits.py` | Save a list of lines to a file. | Writes `test2.txt`. |
| 5 | `05_read_student.py` | Parse CSV-like rows stored in a `.txt` file. | Reads `student.txt`. |
| 6 | `06_write_student.py` | Write student records as text rows. | Writes `student.txt`. |
| 7 | `07_append_student.py` | Add new rows without rewriting the whole file. | Appends to `student.txt`. |
| 8 | `08_update_student.py` | Change one record in place by identifier. | Upserts a row in `student.txt` by `id`. |
| 9 | `09_exist_folder.py` | Create missing directories safely before writing. | `mkdir` with parents. |
| 10 | `10_replace_file.py` | Combine path setup with writing a single output file. | Ensures folder, then writes/replaces a file (e.g. avatar path). |
| 11 | `11_append_log.py` | Grow a log file over time using append mode. | Appends to `birdwatch.txt` under **`FILES_PATH`**. |
| 12 | `12_csv_read_write.py` | Use list-based CSV rows with the standard `csv` module. | `csv.writer` / `csv.reader`; output under **`CSV_PATH`**. |
| 13 | `13_csv_dict_reader.py` | Access columns by header name while reading. | **`csv.DictReader`**. |
| 14 | `14_csv_dict_write.py` | Emit CSV from dictionaries with fieldnames. | **`csv.DictWriter`**. |
| 15 | `15_csv_tab_delimited.py` | Use a tab delimiter instead of commas. | Tab-separated **`.tsv`** under **`CSV_PATH`**. |
| 16 | `16_phone_directory.py` | Interactive loop: load, search, and save contacts. | Uses `phone_directory.txt`. |
| 18 | `18_password_secret_check.py` | Read `SecretPasswordFile.txt`, compare with `input()`; `if` / `elif` / `else`. | **`FILES_PATH`**; joke branch for wrong password `12345`. |

## Where data lives

| Setting                   | Resolves to   | Typical use in these scripts                          |
| ------------------------- | ------------- | ----------------------------------------------------- |
| **`settings.FILES_PATH`** | `data/text/`  | `.txt` practice files (`test.txt`, `student.txt`, …). |
| **`settings.CSV_PATH`**   | `data/excel/` | `.csv` / `.tsv` produced or read by the CSV modules.  |

Generated files may be listed in **`.gitignore`** (e.g. lab-specific CSV names); that is expected.

## Suggested order

Same as the numeric prefixes:

1. **01–04:** text basics (`01_read_test` → `02_write_test` → `03_read_fruits` → `04_write_fruits`).  
2. **05–08:** structured text (`05_read_student` → … → `08_update_student`).  
3. **09–11:** filesystem helpers (`09_exist_folder`, `10_replace_file`, `11_append_log`).  
4. **12–15:** CSV API (`12_csv_read_write` → … → `15_csv_tab_delimited`).  
5. **16:** interactive (`16_phone_directory`).  
6. **18:** password compare from file (`18_password_secret_check`).

## Concepts checklist

| Topic | Scripts |
| ----- | ------- |
| `open()`, `read()`, `write()`, context managers | `01_read_test.py`, `02_write_test.py`, …, `18_password_secret_check.py` |
| Append mode (`"a"`) | `07_append_student.py`, `11_append_log.py` |
| CSV rows as lists | `12_csv_read_write.py` |
| CSV rows as dicts | `13_csv_dict_reader.py`, `14_csv_dict_write.py` |
| TSV / delimiters | `15_csv_tab_delimited.py` |
| Paths with `pathlib` + `settings` | All |

## Related

- Root project layout and **`FILES_PATH`**: [README.md](../../README.md) (section *Repository layout* / *Running lab scripts*).  
- For **pandas** on CSV/Excel at scale, see **`labs/pandas/`** and **`labs/pandas/basics/`**.
