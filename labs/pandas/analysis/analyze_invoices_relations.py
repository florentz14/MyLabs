"""Join ``invoices.csv``, ``customers.csv``, and ``employees.csv`` for a tiny relational view."""

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

INVOICES = EXCEL_PATH / "invoices.csv"
CUSTOMERS = EXCEL_PATH / "customers.csv"
EMPLOYEES = EXCEL_PATH / "employees.csv"


def main() -> None:
    inv = pd.read_csv(INVOICES)
    cust = pd.read_csv(CUSTOMERS)
    emp = pd.read_csv(EMPLOYEES)

    m = inv.merge(cust, left_on="customer_id", right_on="id", how="left", suffixes=("", "_cust"))
    m = m.merge(emp, left_on="employee_id", right_on="id", how="left", suffixes=("", "_emp"))

    print("=" * 60)
    print("INVOICES + CUSTOMERS + EMPLOYEES")
    print("=" * 60)
    cols = [
        "id",
        "date",
        "name",
        "email",
        "address",
        "first_name",
        "last_name",
        "role",
    ]
    cols = [c for c in cols if c in m.columns]
    print(m[cols].to_string(index=False))

    print("\n" + "=" * 60)
    print("Invoices per day")
    print("=" * 60)
    print(m.groupby("date").size().to_string())


if __name__ == "__main__":
    main()
