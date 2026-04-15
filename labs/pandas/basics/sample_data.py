# ------------------------------------------------------------ #
# File: sample_data.py
# Date: 2026-04-01
# Author: Florentino
# Description: Shared tiny DataFrame for pandas basics scripts.
# Explanation: It explains shared tiny DataFrame for pandas basics scripts and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np
import pandas as pd


def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Name": [
                "Ana",
                "Luis",
                "Maria",
                "Juan",
                "Elena",
                "Pedro",
                "Lucia",
                "Diego",
                "Sofia",
                "Carlos",
            ],
            "Age": [23, 30, 23, 45, 30, 27, 29, 35, 22, 41],
            "City": [
                "Madrid",
                "Barcelona",
                "Madrid",
                "Valencia",
                "Barcelona",
                "Sevilla",
                "Bilbao",
                "Valencia",
                "Sevilla",
                "Madrid",
            ],
            "Score": [85, 90, np.nan, 70, 95, 88, 76, 82, np.nan, 91],
        }
    )


def sample_df_large() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Name": [
                "Ana",
                "Luis",
                "Maria",
                "Juan",
                "Elena",
                "Pedro",
                "Lucia",
                "Diego",
                "Sofia",
                "Carlos",
                "Irene",
                "Tomas",
                "Paula",
                "Andres",
                "Marta",
                "Raul",
                "Nuria",
                "Javier",
                "Claudia",
                "Alberto",
            ],
            "Age": [23, 30, 23, 45, 30, 27, 29, 35, 22, 41, 26, 38, 24, 33, 28, 36, 31, 40, 25, 34],
            "City": [
                "Madrid",
                "Barcelona",
                "Madrid",
                "Valencia",
                "Barcelona",
                "Sevilla",
                "Bilbao",
                "Valencia",
                "Sevilla",
                "Madrid",
                "Bilbao",
                "Malaga",
                "Sevilla",
                "Madrid",
                "Valencia",
                "Barcelona",
                "Zaragoza",
                "Malaga",
                "Bilbao",
                "Zaragoza",
            ],
            "Score": [85, 90, np.nan, 70, 95, 88, 76, 82, np.nan, 91, 79, 84, 87, 93, 68, 74, 89, np.nan, 77, 86],
        }
    )
