# ------------------------------------------------------------ #
# File: phone_directory.py
# Date: 2026-04-01
# Author: Florentino
# Description: Phone directory — create file, look up, add, delete (CSV lines: name,phone).
# ------------------------------------------------------------ #

from __future__ import annotations

from pathlib import Path

from settings import FILES_PATH

PHONE_FILE: Path = FILES_PATH / "phone_directory.txt"


def ensure_phone_file_exists() -> None:
    """Create phone_directory.txt if it does not exist."""
    if not PHONE_FILE.is_file():
        PHONE_FILE.write_text("", encoding="utf-8")
        print(f"Created '{PHONE_FILE}'.")


def load_directory() -> dict[str, str]:
    """Load name -> phone from the directory file."""
    ensure_phone_file_exists()
    result: dict[str, str] = {}
    with open(PHONE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "," in line:
                name, phone = line.split(",", 1)
                result[name.strip()] = phone.strip()
    return result


def save_directory(d: dict[str, str]) -> None:
    """Write directory to disk (sorted by name)."""
    with open(PHONE_FILE, "w", encoding="utf-8") as f:
        for name, phone in sorted(d.items()):
            f.write(f"{name},{phone}\n")


def consult_phone(name: str) -> str | None:
    """Return phone for name, or None if missing."""
    return load_directory().get(name)


def add_client(name: str, phone: str) -> None:
    """Add or update a client."""
    d = load_directory()
    d[name] = phone
    save_directory(d)
    print(f"Added/updated: {name} -> {phone}")


def delete_client(name: str) -> bool:
    """Remove client. Returns True if the name existed."""
    d = load_directory()
    if name not in d:
        return False
    del d[name]
    save_directory(d)
    return True


def menu() -> None:
    ensure_phone_file_exists()
    while True:
        print("\n1. Look up phone | 2. Add client | 3. Delete client | 4. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            phone = consult_phone(name)
            print(phone if phone else "Not found.")
        elif choice == "2":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                add_client(name, phone)
        elif choice == "3":
            name = input("Name: ").strip()
            if delete_client(name):
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == "4":
            break


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
