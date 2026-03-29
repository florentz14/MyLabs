from pathlib import Path

# Project root (directory containing this file)
BASE_PATH = Path(__file__).resolve().parent

# Data directories
DATA_PATH = BASE_PATH / "data"
CSV_PATH = DATA_PATH / "csv_files"
EXPORT_PATH = DATA_PATH / "export_files"
GEN_PATH = DATA_PATH / "gen_files"
JSON_PATH = DATA_PATH / "json_files"
PDF_PATH = DATA_PATH / "pdf_files"
SQL_PATH = DATA_PATH / "sql_files"
TEXT_PATH = DATA_PATH / "text_files"

# Built by labs/sql/init_school_db.py from school_schema.sql + school_seed.sql (SQLite database)
SCHOOL_DB_PATH = SQL_PATH / "school.db"

# Lab file examples (read/write in labs/files/)
FILES_PATH = TEXT_PATH

# Lab exercise directories (code under labs/)
LABS_PATH = BASE_PATH / "labs"
CLASSES_PATH = LABS_PATH / "classes"
MATPLOTLIB_PATH = LABS_PATH / "matplotlib"
PANDAS_PATH = LABS_PATH / "pandas"