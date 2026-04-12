from pathlib import Path

# Project root (directory containing this file)
BASE_PATH = Path(__file__).resolve().parent

# Data directories
DATA_PATH = BASE_PATH / "data"
EXCEL_PATH = DATA_PATH / "excel"
# Backward-compatible alias used by existing labs.
CSV_PATH = EXCEL_PATH
EXPORT_PATH = DATA_PATH / "export"
GEN_PATH = DATA_PATH / "gen"
JSON_PATH = DATA_PATH / "json"
PDF_PATH = DATA_PATH / "pdf"
SQL_PATH = DATA_PATH / "sql"
TEXT_PATH = DATA_PATH / "text"

# Built by labs/db/init_school_db.py from school_schema.sql + school_seed.sql (SQLite database)
SCHOOL_DB_PATH = SQL_PATH / "school.db"

# Lab file examples (read/write in labs/files/; scripts named 01_*.py … 16_*.py)
FILES_PATH = TEXT_PATH

# Lab exercise directories (code under labs/)
LABS_PATH = BASE_PATH / "labs"
CLASSES_PATH = LABS_PATH / "classes"
NUMPY_PATH = LABS_PATH / "numpy"
PANDAS_PATH = LABS_PATH / "pandas"
CLEANING_PATH = PANDAS_PATH / "cleaning"
VIZ_PATH = PANDAS_PATH / "viz"
STATS_PATH = LABS_PATH / "stats"
FEATURES_PATH = PANDAS_PATH / "features"
EVAL_PATH = LABS_PATH / "eval"
PROJECTS_PATH = PANDAS_PATH / "projects"
ML_PATH = LABS_PATH / "ml"
ANALYSIS_PATH = PANDAS_PATH / "analysis"
ITSE_1003_PATH = LABS_PATH / "ITSE-1003"
ITSE_1003_DATA_PATH = ITSE_1003_PATH / "data"
ITSE_STUDENTS_CSV = ITSE_1003_DATA_PATH / "students.csv"
ITSE_STUDENTS_UPDATED_CSV = ITSE_1003_DATA_PATH / "students_updated.csv"


def load_students():
    """Load ITSE-1003 ``students.csv`` with stripped column names."""
    import pandas as pd

    df = pd.read_csv(ITSE_STUDENTS_CSV)
    df.columns = df.columns.str.strip()
    return df
