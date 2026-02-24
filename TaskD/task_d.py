"""
Task D - Weekly Electricity Consumption and Production (kWh)

Reads week42.csv, groups hourly data by day,
converts Wh -> kWh, and prints a formatted table.
"""

import csv
import os
from datetime import datetime, date
from typing import Dict, List


def read_data(filename: str) -> List[List[str]]:
    """
    Reads CSV file and returns all data rows (header skipped).
    File path is resolved relative to this script.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    rows: List[List[str]] = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)  # skip header
        for row in reader:
            if row:
                rows.append(row)
    return rows


def calculate_daily_totals(rows: List[List[str]]) -> Dict[date, Dict[str, List[float]]]:
    """
    Groups rows by date and calculates daily totals in kWh.
    """
    daily: Dict[date, Dict[str, List[float]]] = {}

    for row in rows:
        dt = datetime.fromisoformat(row[0])
        d = dt.date()

        cons = [int(row[1]), int(row[2]), int(row[3])]
        prod = [int(row[4]), int(row[5]), int(row[6])]

        if d not in daily:
            daily[d] = {
                "cons": [0.0, 0.0, 0.0],
                "prod": [0.0, 0.0, 0.0],
            }

        for i in range(3):
            daily[d]["cons"][i] += cons[i] / 1000
            daily[d]["prod"][i] += prod[i] / 1000

    return daily


def finnish_day_name(d: date) -> str:
    """Returns Finnish weekday name."""
    names = [
        "Maanantai",
        "Tiistai",
        "Keskiviikko",
        "Torstai",
        "Perjantai",
        "Lauantai",
        "Sunnuntai",
    ]
    return names[d.weekday()]


def fmt(value: float) -> str:
    """Formats kWh value with comma decimal separator."""
    return f"{value:.2f}".replace(".", ",")


def print_table(daily: Dict[date, Dict[str, List[float]]]) -> None:
    """
    Prints the results in a formatted table.
    """
    print("Week 42 electricity consumption and production (kWh, by phase)\n")
    print("Day        Date        Consumption [kWh]               Production [kWh]")
    print("           (dd.mm.yyyy)  v1      v2      v3             v1      v2      v3")
    print("-" * 75)

    for d in sorted(daily.keys()):
        day = finnish_day_name(d)
        date_str = d.strftime("%d.%m.%Y")

        c = daily[d]["cons"]
        p = daily[d]["prod"]

        print(
            f"{day:<10} {date_str:<10}  "
            f"{fmt(c[0]):>6}  {fmt(c[1]):>6}  {fmt(c[2]):>6}           "
            f"{fmt(p[0]):>6}  {fmt(p[1]):>6}  {fmt(p[2]):>6}"
        )


def main() -> None:
    """Main program execution."""
    rows = read_data("week42.csv")
    daily = calculate_daily_totals(rows)
    print_table(daily)


if __name__ == "__main__":
    main()
