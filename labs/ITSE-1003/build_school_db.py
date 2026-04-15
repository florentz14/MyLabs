# ------------------------------------------------------------ #
# File: build_school_db.py
# Date: 2026-04-15
# Author: Florentino
# Description: Build school.db from exam_data.csv (users + exam_scores).
# Explanation: It explains build school.db from exam_data.csv (users + exam_scores) and why it is useful in basic data analysis.
# ------------------------------------------------------------ #
# Run from repo root: python3 labs/ITSE-1003/build_school_db.py

from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent
DATA_DIR = _LAB_DIR / "data"
GENERATED_DIR = _LAB_DIR / "generated"
DB_PATH = GENERATED_DIR / "school.db"
EXAM_CSV = DATA_DIR / "exam_data.csv"


def build_database() -> None:
    """Recreate SQLite DB with users and exam_scores loaded from exam_data.csv."""
    if not EXAM_CSV.is_file():
        raise FileNotFoundError(f"Missing exam CSV: {EXAM_CSV}")

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    DB_PATH.unlink(missing_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE exam_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            student_name TEXT NOT NULL,
            exam_id INTEGER NOT NULL,
            exam_name TEXT,
            subject TEXT,
            score REAL,
            grade TEXT,
            exam_date TEXT,
            teacher TEXT,
            FOREIGN KEY (student_id) REFERENCES users(id)
        )
        """
    )

    with EXAM_CSV.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    seen: dict[int, str] = {}
    for row in rows:
        sid = int(row["Student_ID"])
        if sid not in seen:
            seen[sid] = row["Student_Name"]

    cur.executemany(
        "INSERT INTO users (id, name) VALUES (?, ?)",
        sorted(seen.items(), key=lambda x: x[0]),
    )

    cur.executemany(
        """
        INSERT INTO exam_scores (
            student_id, student_name, exam_id, exam_name,
            subject, score, grade, exam_date, teacher
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                int(r["Student_ID"]),
                r["Student_Name"],
                int(r["Exam_ID"]),
                r["Exam_Name"],
                r["Subject"],
                float(r["Score"]),
                r["Grade"],
                r["Exam_Date"],
                r["Teacher"],
            )
            for r in rows
        ],
    )

    conn.commit()
    conn.close()


def main() -> None:
    build_database()
    conn = sqlite3.connect(DB_PATH)
    nu = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    ne = conn.execute("SELECT COUNT(*) FROM exam_scores").fetchone()[0]
    conn.close()
    print(f"Created {DB_PATH}")
    print(f"  users: {nu} rows, exam_scores: {ne} rows")


if __name__ == "__main__":
    main()
