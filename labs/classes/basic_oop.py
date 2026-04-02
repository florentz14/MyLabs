# ------------------------------------------------------------ #
# File: basic_oop.py
# Date: 2026-04-01
# Author: Florentino
# Description: Minimal class — attributes, method, string representation.
# ------------------------------------------------------------ #

from __future__ import annotations


class Person:
    """Tiny example type for lab exercises."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name}."

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age})"


def main() -> None:
    p = Person("Ada", 30)
    print(p.greet())
    print(p)


if __name__ == "__main__":
    main()
