# ------------------------------------------------------------ #
# File: stock.py
# Date: 2026-03-31
# Author: Florentino
# Description: Load Google stock Excel from data/excel, normalize columns, validate types.
# ------------------------------------------------------------ #

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

from settings import EXCEL_PATH

# Stock data file
DEFAULT_STOCK_FILE = "Google_Stock_Market_Data.xlsx"

REQUIRED = ("date", "open", "high", "low", "close", "volume", "adj_close")


def _normalize_column_name(name: str) -> str:
    return str(name).strip().lower().replace(" ", "_").replace("-", "_")


def load_stock_excel(file_path: Path, sheet_name: int | str = 0) -> pd.DataFrame:
    """Read Excel and return a DataFrame with canonical column names."""
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")
    df = df.rename(columns={c: _normalize_column_name(c) for c in df.columns})

    alias = {"adjclose": "adj_close", "adjusted_close": "adj_close"}
    df = df.rename(columns={k: v for k, v in alias.items() if k in df.columns})

    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(
            f"Missing columns after normalization: {missing}. "
            f"Found: {list(df.columns)}"
        )

    out = df[list(REQUIRED)].copy()
    out["date"] = pd.to_datetime(out["date"], errors="coerce")
    for col in ("open", "high", "low", "close", "adj_close"):
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out["volume"] = pd.to_numeric(out["volume"], errors="coerce").round().astype("Int64")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Load and inspect Google stock Excel data.")
    parser.add_argument(
        "--file",
        type=Path,
        default=EXCEL_PATH / DEFAULT_STOCK_FILE,
        help=f"Path to .xlsx (default: {EXCEL_PATH / DEFAULT_STOCK_FILE})",
    )
    parser.add_argument("--sheet", default=0, help="Sheet name or index (default: 0)")
    args = parser.parse_args()

    if not args.file.is_file():
        print(
            f"File not found: {args.file}\n"
            f"Copy {DEFAULT_STOCK_FILE} to:\n  {EXCEL_PATH / DEFAULT_STOCK_FILE}\n"
            "or pass --file /path/to/your.xlsx",
            file=sys.stderr,
        )
        sys.exit(1)

    df = load_stock_excel(args.file, sheet_name=args.sheet)

    before = len(df)
    df = df.dropna(subset=["date"])
    df = df.dropna(how="all", subset=["open", "high", "low", "close"])
    dropped = before - len(df)

    print(f"Rows: {len(df)}  (dropped {dropped} empty/invalid rows)")
    print("\nFirst row:")
    print(df.iloc[0].to_dict())
    print("\nNumeric summary (OHLC + Adj Close):")
    print(df[["open", "high", "low", "close", "adj_close"]].describe().round(4))
    print("\nHead:")
    print(df.head())


if __name__ == "__main__":
    main()
