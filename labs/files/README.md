# Text and CSV I/O (`labs/files`)

Exercises for **reading and writing files** with the standard library: plain text, **CSV** (`csv.reader` / `writer`), **DictReader** / **DictWriter**, tab-separated values, **append** mode, and small **interactive** programs.

Scripts are **numbered `01`–`18`** in suggested learning order (simple I/O first, then structured text, filesystem helpers, CSV APIs, interactive last)—same idea as **`labs/pandas/basics/`** ([README](../pandas/basics/README.md)).

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

| File | Role | Description |
| --- | --- | --- |
| `01_read_test.py` | Read | **1.** Read an entire text file into memory and print it. Uses `test.txt` under **`FILES_PATH`**. |
| `02_write_test.py` | Write | **2.** Create or overwrite a simple text file. Writes `test.txt` under **`FILES_PATH`**. |
| `03_read_fruits.py` | Read | **3.** Load a line-oriented list from disk. Reads `test2.txt`. |
| `04_write_fruits.py` | Write | **4.** Save a list of lines to a file. Writes `test2.txt`. |
| `05_read_student.py` | Read | **5.** Parse CSV-like rows stored in a `.txt` file. Reads `student.txt`. |
| `06_write_student.py` | Write | **6.** Write student records as text rows. Writes `student.txt`. |
| `07_append_student.py` | Append | **7.** Add new rows without rewriting the whole file. Appends to `student.txt`. |
| `08_update_student.py` | Update | **8.** Change one record in place by identifier. Upserts a row in `student.txt` by `id`. |
| `09_exist_folder.py` | Filesystem | **9.** Create missing directories safely before writing. `mkdir` with parents. |
| `10_replace_file.py` | Write | **10.** Combine path setup with writing a single output file. Ensures folder, then writes/replaces a file (e.g. avatar path). |
| `11_append_log.py` | Append | **11.** Grow a log file over time using append mode. Appends to `birdwatch.txt` under **`FILES_PATH`**. |
| `12_csv_read_write.py` | CSV | **12.** List-based CSV rows with the standard `csv` module. `csv.writer` / `csv.reader`; output under **`CSV_PATH`**. |
| `13_csv_dict_reader.py` | CSV | **13.** Access columns by header name while reading. **`csv.DictReader`**. |
| `14_csv_dict_write.py` | CSV | **14.** Emit CSV from dictionaries with fieldnames. **`csv.DictWriter`**. |
| `15_csv_tab_delimited.py` | CSV | **15.** Tab delimiter instead of commas. Tab-separated **`.tsv`** under **`CSV_PATH`**. |
| `16_phone_directory.py` | Interactive | **16.** Load, search, and save contacts in a loop. Uses `phone_directory.txt`. |
| `18_password_secret_check.py` | Interactive | **18.** Read `SecretPasswordFile.txt`, compare with `input()`; `if` / `elif` / `else`. **`FILES_PATH`**; joke branch for wrong password `12345`. |

## Where data lives

| File | Role | Description |
| --- | --- | --- |
| **`settings.FILES_PATH`** | Path constant | Resolves to `data/text/` — `.txt` practice files (`test.txt`, `student.txt`, …). |
| **`settings.CSV_PATH`** | Path constant | Resolves to `data/excel/` — `.csv` / `.tsv` read or written by the CSV scripts. |

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

| File | Role | Description |
| --- | --- | --- |
| `open()`, `read()`, `write()`, context managers | Concept | Covered across `01_read_test.py`, `02_write_test.py`, …, `18_password_secret_check.py` |
| Append mode (`"a"`) | Concept | `07_append_student.py`, `11_append_log.py` |
| CSV rows as lists | Concept | `12_csv_read_write.py` |
| CSV rows as dicts | Concept | `13_csv_dict_reader.py`, `14_csv_dict_write.py` |
| TSV / delimiters | Concept | `15_csv_tab_delimited.py` |
| Paths with `pathlib` + `settings` | Concept | All scripts |

## Related

- Repo root and **`FILES_PATH`**: [README.md](../../README.md) (*Repository layout* / *Running lab scripts*).
- **Pandas** for CSV/Excel: [../pandas/README.md](../pandas/README.md), [../pandas/basics/README.md](../pandas/basics/README.md).
