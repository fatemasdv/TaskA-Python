# Copyright (c) 2026 Fatema Akter
# License: MIT

"""
Task E - Three Weeks of Electricity Consumption and Production

Reads weekly CSV files, calculates daily summaries,
converts Wh to kWh, formats values using Finnish conventions,
and writes the results to summary.txt.
"""

from datetime import datetime, date
from collections import defaultdict
from typing import List, Dict


def read_data(filename: str) -> List[List[str]]:
    """
    Reads a semicolon-separated CSV file and returns rows as list of lists.
    """
    rows: List[List[str]] = []
    with open(filename, "r", encoding="utf-8") as file:
        next(file)  # skip header
        for line in file:
            if line.strip():
                rows.append(line.strip().split(";"))  # IMPORTANT: semicolon
    return rows


def calculate_daily_summary(rows: List[List[str]]) -> Dict[date, Dict[str, List[float]]]:
    """
    Calculates daily consumption and production totals (in kWh).
    Returns dictionary grouped by date.
    """
    daily_data: Dict[date, Dict[str, List[float]]] = defaultdict(
        lambda: {
            "consumption": [0.0, 0.0, 0.0],
            "production": [0.0, 0.0, 0.0]
        }
    )

    for row in rows:
        dt: datetime = datetime.fromisoformat(row[0])
        day: date = dt.date()

        # Convert Wh → kWh
        for i in range(3):
            daily_data[day]["consumption"][i] += float(row[1 + i]) / 1000
            daily_data[day]["production"][i] += float(row[4 + i]) / 1000

    return daily_data


def format_number(value: float) -> str:
    """
    Formats number to Finnish style (2 decimals, comma separator).
    """
    return f"{value:.2f}".replace(".", ",")


def write_week_summary(file, week_number: int, daily_data: Dict[date, Dict[str, List[float]]]) -> None:
    """
    Writes one week's summary to file.
    """
    file.write(f"Week {week_number} electricity consumption and production (kWh, by phase)\n")
    file.write("Day      Date           Consumption [kWh]            Production [kWh]\n")
    file.write("                        v1      v2      v3           v1      v2      v3\n")
    file.write("---------------------------------------------------------------------------\n")

    for day in sorted(daily_data.keys()):
        weekday: str = day.strftime("%A")
        date_str: str = day.strftime("%d.%m.%Y")

        cons = daily_data[day]["consumption"]
        prod = daily_data[day]["production"]

        file.write(
            f"{weekday:<9} {date_str:<14} "
            f"{format_number(cons[0]):<7} {format_number(cons[1]):<7} {format_number(cons[2]):<7} "
            f"{format_number(prod[0]):<7} {format_number(prod[1]):<7} {format_number(prod[2]):<7}\n"
        )

    file.write("\n")


def write_report() -> None:
    """
    Reads all weeks and writes summary.txt.
    """
    weeks = {
        41: "week41.csv",
        42: "week42.csv",
        43: "week43.csv"
    }

    with open("summary.txt", "w", encoding="utf-8") as file:
        for week_number, filename in weeks.items():
            rows = read_data(filename)
            daily_data = calculate_daily_summary(rows)
            write_week_summary(file, week_number, daily_data)


def main() -> None:
    """
    Main function: reads data and writes report.
    """
    write_report()
    print("Summary file created successfully.")


if __name__ == "__main__":
    main()