# ------------------------------------------------------------ #
# File: split_excel_file.py
# Author: Florentino
# Description: Split one Excel workbook into several files (by sheet or by row chunks).
# Requires: pip install pandas openpyxl
# ------------------------------------------------------------ #

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd


def _safe_stem(name: str) -> str:
    """File-system friendly fragment from a sheet name."""
    cleaned = re.sub(r"[^\w\-]+", "_", name.strip(), flags=re.UNICODE)
    return cleaned.strip("_") or "sheet"


def split_by_sheets(input_path: Path, output_dir: Path) -> None:
    """Write one .xlsx per sheet; each file contains that sheet only."""
    input_path = input_path.resolve()
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    xl = pd.ExcelFile(input_path)
    base = input_path.stem
    print(f"Workbook has {len(xl.sheet_names)} sheet(s).")

    for sheet in xl.sheet_names:
        # Stubs may type sheet names as str | int; filenames and Excel tab names need str.
        sheet_str = str(sheet)
        df = pd.read_excel(xl, sheet_name=sheet)
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"Expected one sheet per iteration; got {type(df).__name__}")
        out = output_dir / f"{base}__{_safe_stem(sheet_str)}.xlsx"
        df.to_excel(out, index=False, sheet_name=sheet_str[:31])  # Excel sheet name limit
        print(f"  Wrote: {out.name}")

    print("Done.")


def split_by_rows(
    input_path: Path,
    output_dir: Path,
    rows_per_file: int,
    *,
    sheet_name: str | int | None = 0,
) -> None:
    """Split a single sheet into multiple workbooks with at most ``rows_per_file`` rows each."""
    if rows_per_file < 1:
        raise ValueError("rows_per_file must be >= 1")

    input_path = input_path.resolve()
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    loaded = pd.read_excel(input_path, sheet_name=sheet_name)
    if not isinstance(loaded, pd.DataFrame):
        raise TypeError(
            "read_excel returned multiple sheets; pass a single sheet index or name.",
        )
    df = loaded
    base = input_path.stem
    n = len(df)
    if n == 0:
        print("Sheet is empty; nothing to write.")
        return

    parts = range(0, n, rows_per_file)
    for i, start in enumerate(parts):
        chunk = df.iloc[start : start + rows_per_file]
        out = output_dir / f"{base}__part{i + 1:03d}.xlsx"
        chunk.to_excel(out, index=False)
        print(f"  Wrote rows {start}-{min(start + rows_per_file, n) - 1}: {out.name}")

    print("Done.")


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Split one Excel workbook into multiple .xlsx files.",
    )
    p.add_argument("input", type=Path, help="Source .xlsx file")
    p.add_argument(
        "output_dir",
        type=Path,
        help="Directory where split files will be created",
    )
    sub = p.add_subparsers(dest="mode", required=True)

    ps = sub.add_parser("sheets", help="One output file per worksheet")
    ps.set_defaults(func="sheets")

    pr = sub.add_parser("rows", help="Chunk one sheet into multiple files by row count")
    pr.add_argument(
        "--rows",
        type=int,
        required=True,
        metavar="N",
        help="Maximum rows per output file (header counted inside the chunk)",
    )
    pr.add_argument(
        "--sheet",
        default="0",
        help='Sheet index (0-based) or name (default: "0" = first sheet)',
    )
    pr.set_defaults(func="rows")

    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    if args.func == "sheets":
        split_by_sheets(args.input, args.output_dir)
    else:
        sheet_arg: str | int = args.sheet
        if isinstance(sheet_arg, str) and sheet_arg.isdigit():
            sheet_arg = int(sheet_arg)
        split_by_rows(
            args.input,
            args.output_dir,
            args.rows,
            sheet_name=sheet_arg,
        )
