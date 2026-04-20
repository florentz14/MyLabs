# ------------------------------------------------------------ #
# File: query_music_database.py
# Date: 2026-04-19
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Run sample SELECT/JOIN queries on the SQLite music database.
# Explanation: Demonstrates JOINs, GROUP BY, aggregates, ORDER BY and filtering across artists, genres, and albums.
# ------------------------------------------------------------ #
# Requires: standard library (sqlite3)

import argparse
import sqlite3
from pathlib import Path

_DB_PATH = Path(__file__).resolve().parent / "data" / "music_database.db"


def _print_section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def _print_rows(headers: list[str], rows: list[tuple]) -> None:
    if not rows:
        print("(no rows)")
        return
    widths = [
        max(len(str(h)), max(len(str(r[i])) for r in rows))
        for i, h in enumerate(headers)
    ]
    line = "  ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    print(line)
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print("  ".join(str(v).ljust(widths[i]) for i, v in enumerate(r)))


def run_queries(db_path: Path = _DB_PATH) -> None:
    """Run a handful of demonstration queries against the music database."""
    if not db_path.exists():
        raise FileNotFoundError(
            f"Database not found at {db_path}. "
            "Run seed_music_database.py first."
        )

    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON;")
        cursor = connection.cursor()

        _print_section("1. All albums with artist and genre")
        rows = cursor.execute(
            """
            SELECT al.title, ar.name AS artist, g.name AS genre, al.release_date
            FROM albums  AS al
            JOIN artists AS ar ON ar.id = al.artist_id
            LEFT JOIN genres AS g ON g.id = al.genre_id
            ORDER BY al.release_date
            """
        ).fetchall()
        _print_rows(["title", "artist", "genre", "release_date"], rows)

        _print_section("2. Album count per artist")
        rows = cursor.execute(
            """
            SELECT ar.name, COUNT(al.id) AS album_count
            FROM artists AS ar
            LEFT JOIN albums AS al ON al.artist_id = ar.id
            GROUP BY ar.id
            ORDER BY album_count DESC, ar.name
            """
        ).fetchall()
        _print_rows(["artist", "album_count"], rows)

        _print_section("3. Total minutes per genre")
        rows = cursor.execute(
            """
            SELECT g.name AS genre,
                   COUNT(al.id) AS albums,
                   COALESCE(SUM(al.duration_minutes), 0) AS total_minutes
            FROM genres AS g
            LEFT JOIN albums AS al ON al.genre_id = g.id
            GROUP BY g.id
            ORDER BY total_minutes DESC
            """
        ).fetchall()
        _print_rows(["genre", "albums", "total_minutes"], rows)

        _print_section("4. Albums released after 2000 (most recent first)")
        rows = cursor.execute(
            """
            SELECT al.title, ar.name AS artist, al.release_date
            FROM albums AS al
            JOIN artists AS ar ON ar.id = al.artist_id
            WHERE al.release_date >= '2000-01-01'
            ORDER BY al.release_date DESC
            """
        ).fetchall()
        _print_rows(["title", "artist", "release_date"], rows)

        _print_section("5. Longest album per artist")
        rows = cursor.execute(
            """
            SELECT ar.name AS artist,
                   al.title,
                   al.duration_minutes
            FROM albums AS al
            JOIN artists AS ar ON ar.id = al.artist_id
            WHERE al.duration_minutes = (
                SELECT MAX(duration_minutes)
                FROM albums
                WHERE artist_id = al.artist_id
            )
            ORDER BY ar.name
            """
        ).fetchall()
        _print_rows(["artist", "title", "minutes"], rows)
    finally:
        connection.close()


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=run_queries.__doc__)
    p.add_argument(
        "--db",
        type=Path,
        default=_DB_PATH,
        help=f"SQLite database path (default: {_DB_PATH})",
    )
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    run_queries(args.db)
