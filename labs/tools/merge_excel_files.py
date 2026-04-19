# ------------------------------------------------------------ #
# File: merge_excel_files.py
# Author: Florentino
# Description: Merge all Excel (.xlsx) files in a folder into one workbook.
# Requires: pip install pandas openpyxl
# ------------------------------------------------------------ #

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def merge_excel_files(
    folder_path: Path,
    output_path: Path,
    *,
    pattern: str = "*.xlsx",
    add_source_column: bool = True,
    skip_output_if_inside_folder: bool = True,
) -> None:
    """
    Read all Excel files matching ``pattern`` under ``folder_path``,
    optionally tag rows with ``Source_File``, drop all-empty rows, and
    write a single ``output_path`` workbook.
    """
    folder_path = folder_path.resolve()
    output_path = output_path.resolve()

    files = sorted(folder_path.glob(pattern))
    if skip_output_if_inside_folder and output_path.parent == folder_path:
        files = [f for f in files if f.resolve() != output_path]

    if not files:
        print("No Excel files found for the given folder and pattern.")
        return

    print(f"Found {len(files)} file(s). Merging…")

    frames: list[pd.DataFrame] = []
    for path in files:
        try:
            current = pd.read_excel(path)
            if add_source_column:
                current = current.copy()
                current["Source_File"] = path.name
            frames.append(current)
            print(f"  OK: {path.name}")
        except Exception as exc:  # noqa: BLE001 — surface read errors per file
            print(f"  Error reading {path.name}: {exc}")

    if not frames:
        print("No frames loaded; nothing to write.")
        return

    combined = pd.concat(frames, ignore_index=True)
    before = len(combined)
    combined = combined.dropna(how="all")
    removed = before - len(combined)
    if removed:
        print(f"Dropped {removed} all-empty row(s).")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined.to_excel(output_path, index=False)
    print("Done.")
    print(f"Merged workbook: {output_path}")


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=merge_excel_files.__doc__)
    p.add_argument(
        "folder",
        type=Path,
        help="Directory containing .xlsx files (e.g. ./data or an absolute path)",
    )
    p.add_argument(
        "output",
        type=Path,
        help="Output .xlsx path (e.g. ./merged_report.xlsx)",
    )
    p.add_argument(
        "--pattern",
        default="*.xlsx",
        help='Glob pattern under folder (default: "*.xlsx")',
    )
    p.add_argument(
        "--no-source-column",
        action="store_true",
        help="Do not add a Source_File column",
    )
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    merge_excel_files(
        args.folder,
        args.output,
        pattern=args.pattern,
        add_source_column=not args.no_source_column,
    )
