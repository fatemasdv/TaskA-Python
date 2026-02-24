# Copyright (c) 2025 Fatema Akter
# License: MIT

"""
Task F - Annual Electricity Consumption Reporting

Interactive program that reads 2025.csv and generates:
- Daily summary for a date range
- Monthly summary
- Full year summary

Reports can also be written to report.txt.
"""

import csv
from datetime import datetime, date
from typing import List, Dict


# --------------------------------------------------
# Formatting Functions
# --------------------------------------------------

def format_date(d: date) -> str:
    """Formats a date as dd.mm.yyyy."""
    return f"{d.day}.{d.month}.{d.year}"


def format_decimal(value: float) -> str:
    """Formats float with two decimals and comma separator."""
    return f"{value:.2f}".replace(".", ",")


# --------------------------------------------------
# Reading Data
# --------------------------------------------------

def read_data(filename: str) -> List[Dict]:
    """Reads CSV file and returns list of measurement dictionaries."""
    data: List[Dict] = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)  # skip header

        for row in reader:
            dt = datetime.fromisoformat(row[0])

            data.append({
                "datetime": dt,
                "date": dt.date(),
                "consumption": float(row[1]),
                "production": float(row[2]),
                "temperature": float(row[3])
            })

    return data


# --------------------------------------------------
# Report Functions
# --------------------------------------------------

def create_daily_report(data: List[Dict]) -> List[str]:
    """Creates daily summary report for a date range."""
    start_input = input("Enter start date (dd.mm.yyyy): ")
    end_input = input("Enter end date (dd.mm.yyyy): ")

    start_date = datetime.strptime(start_input, "%d.%m.%Y").date()
    end_date = datetime.strptime(end_input, "%d.%m.%Y").date()

    total_cons = 0.0
    total_prod = 0.0
    temps: List[float] = []

    for row in data:
        if start_date <= row["date"] <= end_date:
            total_cons += row["consumption"]
            total_prod += row["production"]
            temps.append(row["temperature"])

    avg_temp = sum(temps) / len(temps) if temps else 0.0

    return [
        "-" * 50,
        f"Report for the period {format_date(start_date)}–{format_date(end_date)}",
        f"- Total consumption: {format_decimal(total_cons)} kWh",
        f"- Total production: {format_decimal(total_prod)} kWh",
        f"- Average temperature: {format_decimal(avg_temp)} °C",
    ]


def create_monthly_report(data: List[Dict]) -> List[str]:
    """Creates monthly summary report."""
    month_input = int(input("Enter month number (1–12): "))

    total_cons = 0.0
    total_prod = 0.0
    temps: List[float] = []

    for row in data:
        if row["date"].month == month_input:
            total_cons += row["consumption"]
            total_prod += row["production"]
            temps.append(row["temperature"])

    avg_temp = sum(temps) / len(temps) if temps else 0.0

    month_name = datetime(2025, month_input, 1).strftime("%B")

    return [
        "-" * 50,
        f"Report for the month: {month_name}",
        f"- Total consumption: {format_decimal(total_cons)} kWh",
        f"- Total production: {format_decimal(total_prod)} kWh",
        f"- Average temperature: {format_decimal(avg_temp)} °C",
    ]


def create_yearly_report(data: List[Dict]) -> List[str]:
    """Creates full-year 2025 summary report."""
    total_cons = sum(row["consumption"] for row in data)
    total_prod = sum(row["production"] for row in data)
    avg_temp = sum(row["temperature"] for row in data) / len(data)

    return [
        "-" * 50,
        "Report for the year: 2025",
        f"- Total consumption: {format_decimal(total_cons)} kWh",
        f"- Total production: {format_decimal(total_prod)} kWh",
        f"- Average temperature: {format_decimal(avg_temp)} °C",
    ]


# --------------------------------------------------
# Output Functions
# --------------------------------------------------

def print_report(lines: List[str]) -> None:
    """Prints report to console."""
    for line in lines:
        print(line)


def write_report(lines: List[str]) -> None:
    """Writes report to report.txt (overwrites file)."""
    with open("report.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print("Report written to report.txt")


# --------------------------------------------------
# Menus
# --------------------------------------------------

def show_main_menu() -> str:
    """Displays main menu."""
    print("\nChoose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary for one month")
    print("3) Full year 2025 summary")
    print("4) Exit")

    return input("Select option: ")


def show_after_menu() -> str:
    """Displays post-report menu."""
    print("\nWhat would you like to do next?")
    print("1) Write the report to report.txt")
    print("2) Create a new report")
    print("3) Exit")

    return input("Select option: ")


# --------------------------------------------------
# Main Program
# --------------------------------------------------

def main() -> None:
    """Main program loop."""
    data = read_data("2025.csv")

    while True:
        choice = show_main_menu()

        if choice == "1":
            report = create_daily_report(data)
        elif choice == "2":
            report = create_monthly_report(data)
        elif choice == "3":
            report = create_yearly_report(data)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
            continue

        print_report(report)

        while True:
            next_choice = show_after_menu()

            if next_choice == "1":
                write_report(report)
            elif next_choice == "2":
                break
            elif next_choice == "3":
                print("Exiting program.")
                return
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
