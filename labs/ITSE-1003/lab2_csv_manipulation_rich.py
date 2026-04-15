# ------------------------------------------------------------ #
# File: lab2_csv_manipulation_rich.py
# Date: 2026-04-15
# Author: Florentino
# Description: Lab 2 — same logic as lab2_csv_manipulation.py with Rich tables/panels.
# Explanation: It explains lab 2 — same logic as lab2_csv_manipulation.py with rich tables/panels and why it is useful in basic data analysis.
# ------------------------------------------------------------ #
# Requires: pip install rich

from __future__ import annotations

import csv
from pathlib import Path

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

_LAB_DIR = Path(__file__).resolve().parent
_DATA_DIR = _LAB_DIR / "data"
_GENERATED_DIR = _LAB_DIR / "generated"
CSV_PATH = _DATA_DIR / "lab2_students.csv"
SUMMARY_PATH = _GENERATED_DIR / "lab2_summary_rich.txt"

console = Console()


def load_students() -> list[dict[str, str]]:
    with CSV_PATH.open(mode="r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main() -> None:
    _GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    students = load_students()

    console.print(
        Panel.fit(
            "[bold cyan]Lab 2 — CSV report[/bold cyan]\n"
            f"[dim]{CSV_PATH.name}[/dim]",
            border_style="cyan",
        )
    )

    # --- Task 2: all students ---
    t_all = Table(
        title="Task 2 — All students",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
    )
    t_all.add_column("Name", style="cyan")
    t_all.add_column("Last_Name", style="dim")
    t_all.add_column("Email", overflow="ellipsis", max_width=36)
    t_all.add_column("Age", justify="right")
    t_all.add_column("Major")
    t_all.add_column("GPA", justify="right")
    for s in students:
        email = (s.get("Email") or "").strip() or "—"
        t_all.add_row(
            s["Name"],
            s.get("Last_Name", ""),
            email,
            s["Age"],
            s["Major"],
            s["GPA"],
        )
    console.print(t_all)

    total_age = sum(int(s["Age"]) for s in students)
    num_students = len(students)
    average_age = total_age / num_students

    console.print(
        f"\n[bold green]Average age:[/bold green] [yellow]{average_age:.1f}[/yellow]"
    )

    oldest = max(students, key=lambda s: int(s["Age"]))
    console.print(
        f"[bold green]Oldest student:[/bold green] "
        f"[yellow]{oldest['Name']} {oldest.get('Last_Name', '')}[/yellow] "
        f"([cyan]{oldest['Age']}[/cyan] years)"
    )

    # --- Task 5: Computer Sci ---
    cs = [s for s in students if s["Major"] == "Computer Sci"]
    t_cs = Table(title="Task 5 — Computer Sci", box=box.SIMPLE_HEAVY)
    t_cs.add_column("Name", style="cyan")
    t_cs.add_column("Last_Name", style="dim")
    for s in cs:
        t_cs.add_row(s["Name"], s.get("Last_Name", ""))
    console.print()
    console.print(t_cs)

    # --- Task 6: majors ---
    major_count: dict[str, int] = {}
    for s in students:
        m = s["Major"]
        major_count[m] = major_count.get(m, 0) + 1
    t_maj = Table(title="Task 6 — Students per major", box=box.MINIMAL_DOUBLE_HEAD)
    t_maj.add_column("Major", style="bold")
    t_maj.add_column("Count", justify="right", style="green")
    for major, count in sorted(major_count.items()):
        t_maj.add_row(major, str(count))
    console.print()
    console.print(t_maj)

    # --- Task 7: GPA >= 3.5 ---
    high = [s for s in students if float(s["GPA"]) >= 3.5]
    t_hi = Table(title="Task 7 — GPA ≥ 3.5", box=box.HEAVY_EDGE)
    t_hi.add_column("Name")
    t_hi.add_column("GPA", justify="right")
    for s in high:
        t_hi.add_row(s["Name"], f"{float(s['GPA']):.2f}")
    console.print()
    console.print(t_hi)

    total_gpa = sum(float(s["GPA"]) for s in students)
    average_gpa = total_gpa / num_students
    console.print(
        f"\n[bold green]Average GPA:[/bold green] [yellow]{average_gpa:.2f}[/yellow]"
    )

    over_21 = [s for s in students if int(s["Age"]) > 21]
    t_21 = Table(title="Stretch — Students older than 21 years", box=box.SIMPLE)
    t_21.add_column("Name")
    t_21.add_column("Age", justify="right")
    for s in over_21:
        t_21.add_row(s["Name"], s["Age"])
    console.print()
    console.print(t_21)

    with SUMMARY_PATH.open(mode="w", encoding="utf-8") as f:
        f.write("Lab 2 Summary (rich run)\n")
        f.write("-----------------\n")
        f.write(f"Average Age: {average_age:.1f}\n")
        f.write(f"Average GPA: {average_gpa:.2f}\n")
        f.write("Students older than 21:\n")
        for s in students:
            if int(s["Age"]) > 21:
                f.write(f"- {s['Name']}\n")

    console.print(
        f"\n[dim]Summary written to[/dim] [bold]{SUMMARY_PATH.name}[/bold]"
    )


if __name__ == "__main__":
    main()
