# ------------------------------------------------------------ #
# File: dic_countries.py
# Date: 2026-04-15
# Author: Florentino
# Description: Write/read countries CSV using DictReader.
# Explanation: It explains countries CSV write/read and validation flow for basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import csv
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent / "data"

# Countries with explicit id/code to support richer CSV exercises.
country_rows = [
    {"country_id": 1, "country_code": "USA", "country_key": "USA", "value": "United States"},
    {"country_id": 2, "country_code": "CAN", "country_key": "Canada", "value": "Canada"},
    {"country_id": 3, "country_code": "MEX", "country_key": "Mexico", "value": "Mexico"},
    {"country_id": 4, "country_code": "BRA", "country_key": "Brazil", "value": "Brazil"},
    {"country_id": 5, "country_code": "ARG", "country_key": "Argentina", "value": "Buenos Aires"},
    {"country_id": 6, "country_code": "CHL", "country_key": "Chile", "value": "Santiago"},
    {"country_id": 7, "country_code": "PER", "country_key": "Peru", "value": "Lima"},
    {"country_id": 8, "country_code": "COL", "country_key": "Colombia", "value": "Bogota"},
    {"country_id": 9, "country_code": "DOM", "country_key": "Republica Dominicana", "value": "Santo Domingo"},
    {"country_id": 10, "country_code": "ECU", "country_key": "Ecuador", "value": "Quito"},
    {"country_id": 11, "country_code": "URY", "country_key": "Uruguay", "value": "Montevideo"},
    {"country_id": 12, "country_code": "PRY", "country_key": "Paraguay", "value": "Asuncion"},
    {"country_id": 13, "country_code": "BOL", "country_key": "Bolivia", "value": "Sucre"},
    {"country_id": 14, "country_code": "VEN", "country_key": "Venezuela", "value": "Caracas"},
    {"country_id": 15, "country_code": "CRI", "country_key": "Costa Rica", "value": "San Jose"},
    {"country_id": 16, "country_code": "PAN", "country_key": "Panama", "value": "Panama City"},
    {"country_id": 17, "country_code": "GTM", "country_key": "Guatemala", "value": "Guatemala City"},
    {"country_id": 18, "country_code": "HND", "country_key": "Honduras", "value": "Tegucigalpa"},
    {"country_id": 19, "country_code": "SLV", "country_key": "El Salvador", "value": "San Salvador"},
    {"country_id": 20, "country_code": "NIC", "country_key": "Nicaragua", "value": "Managua"},
]


def validate_country_rows(data: list[dict[str, object]]) -> None:
    """Validate country rows before writing to CSV."""
    if not data:
        raise ValueError("country_rows is empty")

    normalized_keys: set[str] = set()
    used_ids: set[int] = set()
    used_codes: set[str] = set()
    for row in data:
        raw_id = row.get("country_id")
        key = str(row.get("country_key", "")).strip()
        value = str(row.get("value", "")).strip()
        code = str(row.get("country_code", "")).strip().upper()

        if not isinstance(raw_id, int):
            raise ValueError(f"country_id must be int, got: {raw_id!r}")
        if raw_id in used_ids:
            raise ValueError(f"Duplicate country_id: {raw_id}")
        used_ids.add(raw_id)

        if not key:
            raise ValueError("country_rows contains an empty country_key")
        if not value:
            raise ValueError(f"country_rows contains an empty value for '{key}'")
        if not code:
            raise ValueError(f"country_rows contains an empty country_code for '{key}'")
        if code in used_codes:
            raise ValueError(f"Duplicate country_code: {code}")
        used_codes.add(code)

        normalized = key.casefold()
        if normalized in normalized_keys:
            raise ValueError(f"country_rows has duplicate normalized key: '{key}'")
        normalized_keys.add(normalized)


def write_countries_csv(path: Path) -> None:
    validate_country_rows(country_rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["country_id", "country_code", "country_key", "value"]
        )
        w.writeheader()
        w.writerows(country_rows)


def read_countries_csv(path: Path) -> dict[str, str]:
    """Each DictReader row -> one entry country_key -> value."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expected = {"country_id", "country_code", "country_key", "value"}
        fieldnames = set(reader.fieldnames or [])
        missing = expected - fieldnames
        if missing:
            missing_list = ", ".join(sorted(missing))
            raise ValueError(
                f"Countries CSV missing required columns ({missing_list}): {path}"
            )

        out: dict[str, str] = {}
        for idx, row in enumerate(reader, start=2):
            key = (row.get("country_key") or "").strip()
            value = (row.get("value") or "").strip()
            if not key:
                raise ValueError(f"Empty country_key at line {idx} in {path}")
            if not value:
                raise ValueError(f"Empty value at line {idx} in {path}")
            out[key] = value
        return out


def main() -> None:
    c_path = _DATA_DIR / "dic_countries.csv"
    write_countries_csv(c_path)
    print("Wrote:", c_path)

    countries_from_csv = read_countries_csv(c_path)
    print("Countries from DictReader:", countries_from_csv)


if __name__ == "__main__":
    main()
