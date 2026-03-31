# File: ml_02_train_test_split.py
# Description: Basic train/test split using one target column.

from __future__ import annotations

import pandas as pd
from sklearn.model_selection import train_test_split

from settings import EXCEL_PATH


def main() -> None:
    df = pd.read_csv(EXCEL_PATH / "students.csv")

    # Keep this very simple: fill missing GPA with median.
    df["gpa"] = pd.to_numeric(df["gpa"], errors="coerce")
    df["gpa"] = df["gpa"].fillna(df["gpa"].median())

    # Features and target (predict GPA from age and credits).
    x = df[["age", "credits_completed"]]
    y = df["gpa"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42
    )

    print("Train shape:", x_train.shape)
    print("Test shape:", x_test.shape)
    print("Train target size:", y_train.shape)
    print("Test target size:", y_test.shape)


if __name__ == "__main__":
    main()
