# -------------------------------------------------
# ITSE-1003 — CSV CRUD with stdlib csv.DictReader / csv.DictWriter
# Schema matches data/people.csv (Id, Name, Age, Email, …).
# Output: labs/ITSE-1003/generated/people.csv — see README.md
# Use import_from_data_csv() to seed generated/ from data/people.csv.
# -------------------------------------------------

from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Mapping, Sequence

_LAB_DIR = Path(__file__).resolve().parent
_GENERATED_DIR = _LAB_DIR / "generated"
CSV_PATH = _GENERATED_DIR / "people.csv"
DATA_PEOPLE_CSV = _LAB_DIR / "data" / "people.csv"

FIELDNAMES: list[str] = [
    "Id",
    "Name",
    "Age",
    "Email",
    "City",
    "Phone",
    "Birth_Date",
    "Country",
    "Department",
]


def _ensure_generated_dir() -> None:
    _GENERATED_DIR.mkdir(parents=True, exist_ok=True)


def _normalize_row(rec: Mapping[str, object], fieldnames: Sequence[str]) -> dict[str, str]:
    """Build one dict[str, str] with exactly the keys in fieldnames (missing → "")."""
    out: dict[str, str] = {}
    for k in fieldnames:
        v = rec.get(k, "")
        out[k] = "" if v is None else str(v)
    return out


def _load(filename: Path) -> tuple[list[str], list[dict[str, str]]]:
    """READ — Header order + data rows as dicts (DictReader)."""
    with filename.open("r", newline="", encoding="utf-8") as f:
        dr = csv.DictReader(f)
        if dr.fieldnames is None:
            return [], []
        fieldnames = list(dr.fieldnames)
        records = [dict(row) for row in dr]
    return fieldnames, records


def _save(filename: Path, fieldnames: list[str], records: list[dict[str, str]]) -> None:
    """Write CSV using DictWriter (header + one dict per row)."""
    _ensure_generated_dir()
    with filename.open("w", newline="", encoding="utf-8") as f:
        dw = csv.DictWriter(f, fieldnames=fieldnames)
        dw.writeheader()
        for rec in records:
            dw.writerow({k: rec.get(k, "") for k in fieldnames})


def read_rows(filename: Path) -> tuple[list[str], list[dict[str, str]]]:
    """READ — Public alias for loading fieldnames + records."""
    return _load(filename)


def import_from_data_csv(
    src: Path | None = None,
    dest: Path | None = None,
) -> None:
    """COPY — Load rows from data/people.csv (or src) and write to generated/people.csv (or dest)."""
    path = src if src is not None else DATA_PEOPLE_CSV
    target = dest if dest is not None else CSV_PATH
    fieldnames, records = _load(path)
    _save(target, fieldnames, records)


def create_file(filename: Path, rows: Sequence[Mapping[str, object]]) -> None:
    """CREATE — Write header and initial data rows (overwrites if exists)."""
    records = [_normalize_row(r, FIELDNAMES) for r in rows]
    _save(filename, list(FIELDNAMES), records)


def append_rows(filename: Path, new_rows: Sequence[Mapping[str, object]]) -> None:
    """CREATE (append) — Add rows at the end (same fieldnames as file, or FIELDNAMES if new/missing)."""
    if not filename.is_file():
        fieldnames, records = list(FIELDNAMES), []
    else:
        fieldnames, records = _load(filename)
    if not fieldnames:
        fieldnames = list(FIELDNAMES)
    for r in new_rows:
        records.append(_normalize_row(r, fieldnames))
    _save(filename, fieldnames, records)


def update_cell(filename: Path, row_index: int, col_index: int, new_value: str | int) -> None:
    """UPDATE — One cell by data row index and column index."""
    fieldnames, records = _load(filename)
    if row_index >= len(records):
        raise IndexError(f"data row_index {row_index} out of range (have {len(records)} data rows)")
    if col_index >= len(fieldnames):
        raise IndexError(f"col_index {col_index} out of range")
    key = fieldnames[col_index]
    records[row_index][key] = str(new_value)
    _save(filename, fieldnames, records)


def update_row(filename: Path, row_index: int, new_row: Mapping[str, object]) -> None:
    """UPDATE — Replace an entire data row (keys aligned with current fieldnames; missing → "")."""
    fieldnames, records = _load(filename)
    if row_index >= len(records):
        raise IndexError(f"data row_index {row_index} out of range")
    records[row_index] = _normalize_row(new_row, fieldnames)
    _save(filename, fieldnames, records)


def update_column(filename: Path, col_index: int, new_values: list[str]) -> None:
    """UPDATE — Replace one column for all data rows."""
    fieldnames, records = _load(filename)
    if len(new_values) != len(records):
        raise ValueError(f"new_values length {len(new_values)} != data row count {len(records)}")
    if col_index >= len(fieldnames):
        raise IndexError(f"col_index {col_index} out of range")
    key = fieldnames[col_index]
    for i, value in enumerate(new_values):
        records[i][key] = str(value)
    _save(filename, fieldnames, records)


def delete_row(filename: Path, row_index: int) -> None:
    """DELETE — Remove one data row by index."""
    fieldnames, records = _load(filename)
    if row_index >= len(records):
        raise IndexError(f"data row_index {row_index} out of range")
    del records[row_index]
    _save(filename, fieldnames, records)


def delete_column(filename: Path, col_index: int) -> None:
    """DELETE — Remove a column (header + values) from every row."""
    fieldnames, records = _load(filename)
    if not fieldnames or col_index >= len(fieldnames):
        raise IndexError(f"col_index {col_index} out of range")
    new_fieldnames = [f for i, f in enumerate(fieldnames) if i != col_index]
    new_records = [{k: rec.get(k, "") for k in new_fieldnames} for rec in records]
    _save(filename, new_fieldnames, new_records)


def delete_cell(filename: Path, row_index: int, col_index: int) -> None:
    """DELETE — Clear one cell (empty string)."""
    fieldnames, records = _load(filename)
    if row_index >= len(records):
        raise IndexError(f"data row_index {row_index} out of range")
    if col_index >= len(fieldnames):
        raise IndexError(f"col_index {col_index} out of range")
    records[row_index][fieldnames[col_index]] = ""
    _save(filename, fieldnames, records)


def print_table(label: str, filename: Path) -> None:
    """READ — Pretty-print using dict rows from DictReader."""
    fieldnames, records = _load(filename)
    print(f"\n--- {label} ---")
    print(fieldnames)
    for rec in records:
        print([rec.get(k, "") for k in fieldnames])


def _prompt_line(prompt: str, default: str = "") -> str:
    raw = input(f"{prompt}" + (f" [{default}]" if default else "") + ": ").strip()
    return raw if raw else default


def _prompt_int(prompt: str, *, min_v: int | None = None, max_v: int | None = None) -> int:
    while True:
        raw = input(f"{prompt}: ").strip()
        try:
            n = int(raw)
        except ValueError:
            print("  Enter an integer.")
            continue
        if min_v is not None and n < min_v:
            print(f"  Must be >= {min_v}.")
            continue
        if max_v is not None and n > max_v:
            print(f"  Must be <= {max_v}.")
            continue
        return n


def _prompt_row_dict(fieldnames: Sequence[str], defaults: Mapping[str, str] | None = None) -> dict[str, str]:
    """Ask for each column; use defaults[key] when user presses Enter."""
    d: dict[str, str] = {}
    base = dict(defaults) if defaults else {}
    print("  (Enter keeps the suggested value, if any; empty string clears to blank.)")
    for k in fieldnames:
        cur = base.get(k, "")
        v = _prompt_line(f"  {k}", cur)
        d[k] = v
    return d


def _file_ready(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0


def run_crud_menu(csv_path: Path | None = None) -> None:
    """Interactive CRUD: numbered options, stdin prompts, writes to csv_path (default CSV_PATH)."""
    path = csv_path if csv_path is not None else CSV_PATH
    print(f"CSV people CRUD — file: {path}")
    while True:
        print(
            """
Opciones:
  1  Importar desde data/people.csv (copia a generated/)
  2  Ver todas las filas
  3  Crear archivo nuevo (solo cabecera, sin filas; confirma)
  4  Añadir una fila
  5  Actualizar una celda (fila, columna, valor)
  6  Actualizar una fila completa
  7  Actualizar una columna entera
  8  Borrar una fila
  9  Borrar una columna
 10  Vaciar una celda
  0  Salir"""
        )
        choice = input("Elige opción: ").strip()
        if choice in ("0", "q", "Q", "salir"):
            print("Adiós.")
            return
        try:
            if choice == "1":
                import_from_data_csv(dest=path)
                print("Importación hecha.")
            elif choice == "2":
                if not _file_ready(path):
                    print("No hay datos. Usa 1 o 3 primero.")
                else:
                    print_table("Contenido", path)
            elif choice == "3":
                if _prompt_line("¿Sobrescribir el archivo? (s/N)", "n").lower() not in ("s", "si", "sí", "y", "yes"):
                    print("Cancelado.")
                else:
                    create_file(path, [])
                    print("Archivo creado (solo cabecera).")
            elif choice == "4":
                if not path.parent.is_dir():
                    _ensure_generated_dir()
                fnames = list(FIELDNAMES)
                if _file_ready(path):
                    fnames, _ = _load(path)
                print("Nueva fila:")
                row = _prompt_row_dict(fnames)
                append_rows(path, [row])
                print("Fila añadida.")
            elif choice == "5":
                if not _file_ready(path):
                    print("No hay datos.")
                    continue
                fnames, recs = _load(path)
                print("Columnas:", list(enumerate(fnames)))
                ri = _prompt_int("Índice de fila (0 = primera)", min_v=0, max_v=len(recs) - 1)
                ci = _prompt_int("Índice de columna", min_v=0, max_v=len(fnames) - 1)
                val = _prompt_line("Nuevo valor")
                update_cell(path, ri, ci, val)
                print("Celda actualizada.")
            elif choice == "6":
                if not _file_ready(path):
                    print("No hay datos.")
                    continue
                fnames, recs = _load(path)
                ri = _prompt_int("Índice de fila a reemplazar", min_v=0, max_v=len(recs) - 1)
                print("Fila actual:", recs[ri])
                print("Nueva fila:")
                row = _prompt_row_dict(fnames, defaults=recs[ri])
                update_row(path, ri, row)
                print("Fila actualizada.")
            elif choice == "7":
                if not _file_ready(path):
                    print("No hay datos.")
                    continue
                fnames, recs = _load(path)
                print("Columnas:", list(enumerate(fnames)))
                ci = _prompt_int("Índice de columna", min_v=0, max_v=len(fnames) - 1)
                key = fnames[ci]
                vals: list[str] = []
                for i in range(len(recs)):
                    vals.append(_prompt_line(f"  Valor fila {i} ({key})", recs[i].get(key, "")))
                update_column(path, ci, vals)
                print("Columna actualizada.")
            elif choice == "8":
                if not _file_ready(path):
                    print("No hay datos.")
                    continue
                _, recs = _load(path)
                ri = _prompt_int("Índice de fila a borrar", min_v=0, max_v=len(recs) - 1)
                delete_row(path, ri)
                print("Fila borrada.")
            elif choice == "9":
                if not _file_ready(path):
                    print("No hay datos.")
                    continue
                fnames, _ = _load(path)
                print("Columnas:", list(enumerate(fnames)))
                ci = _prompt_int("Índice de columna a borrar", min_v=0, max_v=len(fnames) - 1)
                delete_column(path, ci)
                print("Columna borrada.")
            elif choice == "10":
                if not _file_ready(path):
                    print("No hay datos.")
                    continue
                fnames, recs = _load(path)
                print("Columnas:", list(enumerate(fnames)))
                ri = _prompt_int("Índice de fila", min_v=0, max_v=len(recs) - 1)
                ci = _prompt_int("Índice de columna a vaciar", min_v=0, max_v=len(fnames) - 1)
                delete_cell(path, ri, ci)
                print("Celda vaciada.")
            else:
                print("Opción no válida.")
        except (OSError, ValueError, IndexError) as e:
            print(f"Error: {e}")


def _row(
    pid: str,
    name: str,
    age: str,
    email: str,
    city: str,
    phone: str,
    birth: str,
    country: str,
    department: str,
) -> dict[str, str]:
    return {
        "Id": pid,
        "Name": name,
        "Age": age,
        "Email": email,
        "City": city,
        "Phone": phone,
        "Birth_Date": birth,
        "Country": country,
        "Department": department,
    }


def demo() -> None:
    """Create → append → updates → deletes (same lesson flow, full people schema)."""
    data = (
        _row("1", "Balaji", "23", "b@example.com", "Chennai", "555-0001", "2001-01-10", "IN", "Engineering"),
        _row("2", "Gokul", "24", "g@example.com", "Madurai", "555-0002", "2000-06-15", "IN", "Engineering"),
        _row("3", "Lakshman", "29", "l@example.com", "Coimbatore", "555-0003", "1995-03-20", "IN", "Sales"),
    )
    create_file(CSV_PATH, data)
    print("CREATE: file written to", CSV_PATH)
    print_table("After CREATE", CSV_PATH)

    append_rows(
        CSV_PATH,
        [
            _row("4", "Arjun", "31", "a@example.com", "Bengaluru", "555-0004", "1993-11-01", "IN", "Marketing"),
            _row("5", "Priya", "27", "p@example.com", "Mumbai", "555-0005", "1997-08-22", "IN", "HR"),
        ],
    )
    print("\nAPPEND: two rows added")
    print_table("After APPEND", CSV_PATH)

    # Age column is index 2; row 0 first person
    update_cell(CSV_PATH, 0, 2, 25)
    update_row(
        CSV_PATH,
        1,
        _row("2", "Gokul", "26", "g@example.com", "Madurai", "555-0002", "2000-06-15", "IN", "Engineering"),
    )
    # Last Name analog: overwrite Name with placeholder for all rows
    update_column(CSV_PATH, 1, ["X", "X", "X", "X", "X"])
    print("\nUPDATE: cell (Age), row, column (Name)")
    print_table("After UPDATE", CSV_PATH)

    delete_row(CSV_PATH, 4)
    delete_column(CSV_PATH, 8)
    delete_cell(CSV_PATH, 0, 4)
    print("\nDELETE: row, column (Department), clear cell (City)")
    print_table("Final", CSV_PATH)
    print("\nDone.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        run_crud_menu()
