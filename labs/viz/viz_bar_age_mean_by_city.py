# ------------------------------------------------------------ #
# File: viz_bar_age_mean_by_city.py
# Date: 2026-04-02
# Author: Florentino
# Description: DataFrame desde CSV en memoria; edad media por ciudad; barra horizontal; PNG en data/gen/.
# ------------------------------------------------------------ #

"""Muestra embebida → pandas → agrupación por ciudad → gráfico y CSV auxiliar (no pisa people.csv)."""

from __future__ import annotations

import io

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

from settings import EXCEL_PATH, GEN_PATH

CSV_PEOPLE = """id,person_code,first_name,last_name,age,city,email,occupation
1,PER-101,Alice,Johnson,22,Austin,alice.j@example.com,Student
2,PER-102,Bob,Smith,30,Boston,bob.smith@example.com,Engineer
3,PER-103,Carol,Williams,27,Chicago,carol.w@example.com,Designer
4,PER-104,David,Brown,35,Denver,david.b@example.com,Manager
5,PER-105,Eve,Jones,29,Austin,eve.j@example.com,Developer
6,PER-106,Frank,Miller,40,Chicago,frank.m@example.com,Architect
7,PER-107,Grace,Davis,24,Boston,grace.d@example.com,Intern
8,PER-108,Henry,Garcia,33,Denver,henry.g@example.com,Analyst
9,PER-109,Ivy,Rodriguez,26,Austin,ivy.r@example.com,Designer
10,PER-110,Jack,Wilson,31,Chicago,jack.w@example.com,Engineer"""


def main() -> None:
    df_people = pd.read_csv(io.StringIO(CSV_PEOPLE))
    age_by_city = df_people.groupby("city", observed=True)["age"].mean().sort_values()

    out_csv = EXCEL_PATH / "people_city_sample.csv"
    out_png = GEN_PATH / "viz_age_mean_by_city.png"
    EXCEL_PATH.mkdir(parents=True, exist_ok=True)
    GEN_PATH.mkdir(parents=True, exist_ok=True)

    df_people.to_csv(out_csv, index=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    age_by_city.plot(kind="barh", color="salmon", ax=ax)
    ax.set_title("Edad Promedio por Ciudad", fontsize=14)
    ax.set_xlabel("Edad Promedio", fontsize=12)
    ax.set_ylabel("Ciudad", fontsize=12)
    ax.grid(axis="x", linestyle="--", alpha=0.6)
    fig.tight_layout()
    fig.savefig(out_png, dpi=120, bbox_inches="tight")
    print(f"CSV guardado: {out_csv}")
    print(f"Gráfico guardado: {out_png}")
    if mpl.get_backend().lower() == "agg":
        print("(Backend Agg: sin ventana. Usa otro backend o abre el PNG.)")
    else:
        plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
