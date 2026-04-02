# ------------------------------------------------------------ #
# File: basic_ml.py
# Date: 2026-04-01
# Author: Florentino
# Description: Minimal sklearn fit — synthetic regression, no CSV required.
# ------------------------------------------------------------ #

from __future__ import annotations

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def main() -> None:
    x, y = make_regression(
        n_samples=200, n_features=1, noise=15.0, random_state=42
    )
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    preds = model.predict(x_test)
    mae = mean_absolute_error(y_test, preds)

    print("MAE (test):", round(mae, 4))
    print("Coefficient:", round(float(model.coef_[0]), 4))
    print("Intercept:", round(float(model.intercept_), 4))


if __name__ == "__main__":
    main()
