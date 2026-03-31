# File: ml_03_linear_regression.py
# Description: Basic linear regression with two numeric features.

from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from settings import EXCEL_PATH


def main() -> None:
    df = pd.read_csv(EXCEL_PATH / "students.csv")

    # Minimal cleaning for this beginner example.
    df["gpa"] = pd.to_numeric(df["gpa"], errors="coerce")
    df = df.dropna(subset=["gpa"])

    x = df[["age", "credits_completed"]]
    y = df["gpa"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)

    preds = model.predict(x_test)
    mae = mean_absolute_error(y_test, preds)

    print("MAE:", round(mae, 4))
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)


if __name__ == "__main__":
    main()
