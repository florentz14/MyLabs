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

# Built by labs/sql/init_school_db.py from school_schema.sql + school_seed.sql (SQLite database)
SCHOOL_DB_PATH = SQL_PATH / "school.db"

# Lab file examples (read/write in labs/files/)
FILES_PATH = TEXT_PATH

# Lab exercise directories (code under labs/)
LABS_PATH = BASE_PATH / "labs"
CLASSES_PATH = LABS_PATH / "classes"
MATPLOTLIB_PATH = LABS_PATH / "matplotlib"
PANDAS_PATH = LABS_PATH / "pandas"