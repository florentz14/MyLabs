# ------------------------------------------------------------ #
# File: read_json.py
# Date: 2026-04-12
# Author: Florentino
# Description: Basic track — load JSON records into a DataFrame.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import JSON_PATH

IN_JSON = JSON_PATH / "students_records.json"


def main() -> None:
    if not IN_JSON.is_file():
        raise FileNotFoundError(IN_JSON)
    df = pd.read_json(IN_JSON, encoding="utf-8")
    print(f"Loaded: {IN_JSON}")
    print(df.head())
    print("Shape:", df.shape)

if __name__ == "__main__":
    main()
