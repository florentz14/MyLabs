# ------------------------------------------------------------ #
# File: basic_metrics.py
# Date: 2026-04-01
# Author: Florentino
# Description: Starter metrics — MAE / MSE for regression, accuracy for classification.
# ------------------------------------------------------------ #

from __future__ import annotations

from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error

# Regression
Y_TRUE = [3.0, 4.5, 5.0]
Y_PRED = [2.5, 4.0, 5.5]

# Classification (binary labels)
Y_TRUE_C = [0, 1, 1, 0]
Y_PRED_C = [0, 1, 0, 0]


def main() -> None:
    mae = mean_absolute_error(Y_TRUE, Y_PRED)
    mse = mean_squared_error(Y_TRUE, Y_PRED)
    acc = accuracy_score(Y_TRUE_C, Y_PRED_C)

    print("Regression — MAE:", round(mae, 4))
    print("Regression — MSE:", round(mse, 4))
    print("Classification — accuracy:", round(acc, 4))


if __name__ == "__main__":
    main()
