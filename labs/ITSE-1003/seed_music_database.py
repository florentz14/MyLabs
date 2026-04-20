# ------------------------------------------------------------ #
# File: seed_music_database.py
# Date: 2026-04-19
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Seed the SQLite music database (artists, genres, albums) with sample data.
# Explanation: Re-runs safely thanks to UNIQUE constraints (INSERT OR IGNORE) and resolves foreign keys by name lookup so seeds work regardless of insertion order.
# ------------------------------------------------------------ #
# Requires: standard library (sqlite3)

import argparse
import sqlite3
from pathlib import Path

from music_database import create_music_database

_DB_PATH = Path(__file__).resolve().parent / "data" / "music_database.db"


ARTISTS: list[tuple[str, str | None, int | None, str | None]] = [
    ("The Beatles",      "United Kingdom", 1960, "Iconic English rock band from Liverpool."),
    ("Pink Floyd",       "United Kingdom", 1965, "Progressive rock pioneers."),
    ("Daft Punk",        "France",         1993, "French electronic music duo."),
    ("Miles Davis",      "United States",  1944, "Influential jazz trumpeter and composer."),
    ("Radiohead",        "United Kingdom", 1985, "Alternative rock band from Oxfordshire."),
    ("Kendrick Lamar",   "United States",  2003, "Pulitzer-winning hip-hop artist."),
]

GENRES: list[tuple[str, str | None]] = [
    ("Rock",         "Guitar-driven popular music."),
    ("Progressive",  "Conceptual, extended-form rock."),
    ("Electronic",   "Music produced primarily with electronic instruments."),
    ("Jazz",         "Improvisational genre rooted in blues and swing."),
    ("Alternative",  "Non-mainstream rock styles."),
    ("Hip-Hop",      "Rhythmic music with rapped vocals."),
]

# (album_title, release_date, track_count, duration_minutes, label, cover_url, artist_name, genre_name)
ALBUMS: list[tuple[str, str, int, int, str | None, str | None, str, str]] = [
    ("Abbey Road",                   "1969-09-26", 17,  47, "Apple Records",       None, "The Beatles",    "Rock"),
    ("Sgt. Pepper's Lonely Hearts",  "1967-05-26", 13,  39, "Parlophone",          None, "The Beatles",    "Rock"),
    ("The Dark Side of the Moon",    "1973-03-01", 10,  43, "Harvest Records",     None, "Pink Floyd",     "Progressive"),
    ("Wish You Were Here",           "1975-09-12",  5,  44, "Harvest Records",     None, "Pink Floyd",     "Progressive"),
    ("Discovery",                    "2001-03-12", 14,  61, "Virgin Records",      None, "Daft Punk",      "Electronic"),
    ("Random Access Memories",       "2013-05-17", 13,  74, "Columbia Records",    None, "Daft Punk",      "Electronic"),
    ("Kind of Blue",                 "1959-08-17",  5,  46, "Columbia Records",    None, "Miles Davis",    "Jazz"),
    ("OK Computer",                  "1997-05-21", 12,  53, "Parlophone",          None, "Radiohead",      "Alternative"),
    ("In Rainbows",                  "2007-10-10", 10,  43, "XL Recordings",       None, "Radiohead",      "Alternative"),
    ("To Pimp a Butterfly",          "2015-03-15", 16,  79, "Top Dawg / Aftermath", None, "Kendrick Lamar", "Hip-Hop"),
    ("DAMN.",                        "2017-04-14", 14,  55, "Top Dawg / Aftermath", None, "Kendrick Lamar", "Hip-Hop"),
]


def seed(db_path: Path = _DB_PATH, *, reset: bool = False) -> None:
    """Insert sample artists, genres, and albums (idempotent).

    If ``reset`` is True, delete existing rows in albums/genres/artists first.
    """
    create_music_database(db_path)

    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON;")
        cursor = connection.cursor()

        if reset:
            # Delete in FK-safe order (albums first because it references the others)
            cursor.execute("DELETE FROM albums;")
            cursor.execute("DELETE FROM genres;")
            cursor.execute("DELETE FROM artists;")
            cursor.execute(
                "DELETE FROM sqlite_sequence WHERE name IN ('albums','genres','artists');"
            )
            print("Reset: cleared albums, genres, artists.")

        cursor.executemany(
            "INSERT OR IGNORE INTO artists (name, country, formed_year, bio) VALUES (?, ?, ?, ?)",
            ARTISTS,
        )

        cursor.executemany(
            "INSERT OR IGNORE INTO genres (name, description) VALUES (?, ?)",
            GENRES,
        )

        # Resolve names to ids so insertion order does not matter
        artist_ids = {name: aid for aid, name in cursor.execute("SELECT id, name FROM artists")}
        genre_ids = {name: gid for gid, name in cursor.execute("SELECT id, name FROM genres")}

        album_rows: list[tuple[str, str, int, int, str | None, str | None, int, int]] = []
        for (title, release_date, tracks, minutes, label, cover, artist, genre) in ALBUMS:
            if artist not in artist_ids:
                print(f"  Skipping album '{title}': unknown artist '{artist}'.")
                continue
            if genre not in genre_ids:
                print(f"  Skipping album '{title}': unknown genre '{genre}'.")
                continue
            album_rows.append(
                (
                    title,
                    release_date,
                    tracks,
                    minutes,
                    label,
                    cover,
                    artist_ids[artist],
                    genre_ids[genre],
                )
            )

        cursor.executemany(
            """
            INSERT OR IGNORE INTO albums
                (title, release_date, track_count, duration_minutes,
                 label, cover_url, artist_id, genre_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            album_rows,
        )

        connection.commit()

        counts = {
            "artists": cursor.execute("SELECT COUNT(*) FROM artists").fetchone()[0],
            "genres":  cursor.execute("SELECT COUNT(*) FROM genres").fetchone()[0],
            "albums":  cursor.execute("SELECT COUNT(*) FROM albums").fetchone()[0],
        }
        print("Seed complete. Row counts:")
        for table, n in counts.items():
            print(f"  {table:>8}: {n}")

        print("\nAlbums per artist:")
        rows = cursor.execute(
            """
            SELECT ar.name, g.name, COUNT(al.id) AS album_count
            FROM artists  AS ar
            LEFT JOIN albums AS al ON al.artist_id = ar.id
            LEFT JOIN genres AS g  ON g.id        = al.genre_id
            GROUP BY ar.id
            ORDER BY ar.name
            """
        ).fetchall()
        for name, genre, count in rows:
            genre_label = genre or "—"
            print(f"  {name:<16} ({genre_label:<12}): {count}")
    finally:
        connection.close()


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=seed.__doc__)
    p.add_argument(
        "--db",
        type=Path,
        default=_DB_PATH,
        help=f"SQLite database path (default: {_DB_PATH})",
    )
    p.add_argument(
        "--reset",
        action="store_true",
        help="Delete existing rows from albums, genres, and artists before seeding.",
    )
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    seed(args.db, reset=args.reset)
