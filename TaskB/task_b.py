"""
Task B – Using Functions
Reads one reservation from reservations.txt and prints it in a formatted way.
"""

from datetime import datetime


def print_reservation_number(reservation: list) -> None:
    number = int(reservation[0])
    print(f"Reservation number: {number}")


def print_booker(reservation: list) -> None:
    print(f"Booker: {reservation[1]}")


def print_date(reservation: list) -> None:
    date_obj = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    print(f"Date: {date_obj.strftime('%d.%m.%Y')}")


def print_start_time(reservation: list) -> None:
    time_obj = datetime.strptime(reservation[3], "%H:%M").time()
    print(f"Start time: {time_obj.strftime('%H.%M')}")


def print_hours(reservation: list) -> None:
    hours = int(reservation[4])
    print(f"Number of hours: {hours}")


def print_hourly_rate(reservation: list) -> None:
    rate = float(reservation[5])
    rate_fi = f"{rate:.2f}".replace(".", ",")
    print(f"Hourly price: {rate_fi} €")


def print_total_price(reservation: list) -> None:
    hours = int(reservation[4])
    rate = float(reservation[5])
    total = hours * rate
    total_fi = f"{total:.2f}".replace(".", ",")
    print(f"Total price: {total_fi} €")


def print_paid(reservation: list) -> None:
    paid = reservation[6] == "True"
    print(f"Paid: {'Yes' if paid else 'No'}")


def print_venue(reservation: list) -> None:
    print(f"Location: {reservation[7]}")


def print_phone(reservation: list) -> None:
    print(f"Phone: {reservation[8]}")


def print_email(reservation: list) -> None:
    print(f"Email: {reservation[9]}")


def main() -> None:
    with open("reservations.txt", "r", encoding="utf-8") as file:
        reservation = file.read().strip().split("|")

    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_rate(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_venue(reservation)
    print_phone(reservation)
    print_email(reservation)


if __name__ == "__main__":
    main()
