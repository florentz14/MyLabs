# ------------------------------------------------------------ #
# File: music_database.py
# Date: 2026-04-19
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Create a SQLite music database with Artists, Genres, and Albums (foreign keys + extra fields).
# Explanation: Demonstrates a clean relational schema using sqlite3 — each table uses an `id` primary key, Albums references Artists/Genres via foreign keys, and additional realistic fields are included (country, label, duration, etc.).
# ------------------------------------------------------------ #
# Requires: standard library (sqlite3 ships with Python)

import argparse
import sqlite3
from pathlib import Path

_DB_PATH = Path(__file__).resolve().parent / "data" / "music_database.db"


def create_music_database(db_path: Path = _DB_PATH) -> None:
    """Create music_database.db with Artists, Genres, and Albums tables."""
    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_path)
    try:
        cursor = connection.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        # Artists: who creates the music
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS artists (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT    NOT NULL UNIQUE,
                country     TEXT,
                formed_year INTEGER CHECK (formed_year BETWEEN 1800 AND 2100),
                bio         TEXT,
                created_at  TEXT    NOT NULL DEFAULT (CURRENT_TIMESTAMP)
            )
            """
        )

        # Genres: musical style; name is unique to avoid duplicates
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS genres (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT    NOT NULL UNIQUE,
                description TEXT,
                created_at  TEXT    NOT NULL DEFAULT (CURRENT_TIMESTAMP)
            )
            """
        )

        # Albums: belongs to exactly one artist and (optionally) one genre
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS albums (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                title            TEXT    NOT NULL,
                release_date     DATE,
                track_count      INTEGER CHECK (track_count >= 0),
                duration_minutes INTEGER CHECK (duration_minutes >= 0),
                label            TEXT,
                cover_url        TEXT,
                artist_id        INTEGER NOT NULL,
                genre_id         INTEGER,
                created_at       TEXT    NOT NULL DEFAULT (CURRENT_TIMESTAMP),
                UNIQUE (artist_id, title),
                FOREIGN KEY (artist_id) REFERENCES artists (id)
                    ON UPDATE CASCADE ON DELETE RESTRICT,
                FOREIGN KEY (genre_id)  REFERENCES genres  (id)
                    ON UPDATE CASCADE ON DELETE SET NULL
            )
            """
        )

        # Helpful indexes for common lookups
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_albums_artist  ON albums (artist_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_albums_genre   ON albums (genre_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_albums_release ON albums (release_date);")

        connection.commit()
        print("Database and tables created successfully based on the diagram.")
        print(f"Database file: {db_path}")
    finally:
        connection.close()


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=create_music_database.__doc__)
    p.add_argument(
        "--db",
        type=Path,
        default=_DB_PATH,
        help=f"SQLite database path (default: {_DB_PATH})",
    )
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    create_music_database(args.db)
