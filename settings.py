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

# Lab file examples (read/write in labs/files/)
FILES_PATH = TEXT_PATH

# Lab exercise directories (code under labs/)
LABS_PATH = BASE_PATH / "labs"
CLASSES_PATH = LABS_PATH / "classes"
NUMPY_PATH = LABS_PATH / "numpy"
CLEANING_PATH = LABS_PATH / "cleaning"
VIZ_PATH = LABS_PATH / "viz"
STATS_PATH = LABS_PATH / "stats"
FEATURES_PATH = LABS_PATH / "features"
EVAL_PATH = LABS_PATH / "eval"
PROJECTS_PATH = LABS_PATH / "projects"
ML_PATH = LABS_PATH / "ml"
PANDAS_PATH = LABS_PATH / "pandas"