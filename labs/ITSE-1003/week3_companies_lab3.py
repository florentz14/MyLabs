# ------------------------------------------------------------ #
# File: week3_companies_lab3.py
# Date: 2026-04-19
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Lab 3 — Company directory data cleaning and analysis with Pandas (read_csv, missing values, duplicates, sort, groupby, export).
# Explanation: Loads companies_lab3.csv, cleans and analyzes the directory (missing Email, dedupe, sorts, industry counts, Technology filter, HasWebsite bonus), then exports a cleaned CSV.
# ------------------------------------------------------------ #

from pathlib import Path

import pandas as pd

_DATA_DIR = Path(__file__).resolve().parent / "data"
_INPUT_CSV = _DATA_DIR / "companies_lab3.csv"
_OUTPUT_CSV = _DATA_DIR / "companies_lab3_cleaned.csv"


def main() -> None:
    # -------------------------------------------------------------------------
    # 1. Load the dataset and show the first 5 rows
    # -------------------------------------------------------------------------
    df = pd.read_csv(_INPUT_CSV)

    print("1. First 5 rows:")
    print(df.head())
    print()

    # -------------------------------------------------------------------------
    # 2. Missing values in each column
    # -------------------------------------------------------------------------
    print("2. Missing values per column:")
    print(df.isnull().sum())
    print()

    # -------------------------------------------------------------------------
    # 3. Remove rows with missing Email
    # -------------------------------------------------------------------------
    df = df.dropna(subset=["Email"])
    print("3. After removing rows with missing Email, row count:", len(df))
    print()

    # -------------------------------------------------------------------------
    # 4. Remove duplicate rows (same company can appear twice with different Id)
    # -------------------------------------------------------------------------
    before_dedup = len(df)
    cols_for_dupes = [c for c in df.columns if c != "Id"]
    df = df.drop_duplicates(subset=cols_for_dupes, keep="first")
    print(
        "4. After removing duplicate rows:",
        len(df),
        "rows (removed",
        before_dedup - len(df),
        "duplicates)",
    )
    print()

    # -------------------------------------------------------------------------
    # 5. Sort alphabetically by CompanyName
    # -------------------------------------------------------------------------
    by_company = df.sort_values("CompanyName")
    print("5. Companies sorted by CompanyName:")
    print(by_company[["CompanyName", "Industry"]])
    print()

    # -------------------------------------------------------------------------
    # 6. Sort by Industry
    # -------------------------------------------------------------------------
    by_industry = df.sort_values("Industry")
    print("6. Companies sorted by Industry:")
    print(by_industry[["CompanyName", "Industry"]])
    print()

    # -------------------------------------------------------------------------
    # 7. Count companies per Industry (groupby)
    # -------------------------------------------------------------------------
    industry_counts = df.groupby("Industry", sort=True).size().rename("CompanyCount")
    print("7. Number of companies per industry:")
    print(industry_counts)
    print()

    # -------------------------------------------------------------------------
    # 8. All companies in the Technology industry
    # -------------------------------------------------------------------------
    technology = df[df["Industry"] == "Technology"]
    print("8. Technology companies:")
    print(technology)
    print()

    # -------------------------------------------------------------------------
    # Bonus: HasWebsite — Yes if Website is present, No otherwise
    # -------------------------------------------------------------------------
    website_present = df["Website"].notna() & (
        df["Website"].astype(str).str.strip() != ""
    )
    df["HasWebsite"] = website_present.map({True: "Yes", False: "No"})
    print("Bonus. HasWebsite column (sample):")
    print(df[["CompanyName", "Website", "HasWebsite"]])
    print()

    # -------------------------------------------------------------------------
    # Export cleaned dataset (after steps 3–4, with bonus column)
    # -------------------------------------------------------------------------
    df_out = df.sort_values("CompanyName")
    df_out.to_csv(_OUTPUT_CSV, index=False)
    print("Cleaned data exported to:", _OUTPUT_CSV)


if __name__ == "__main__":
    main()
