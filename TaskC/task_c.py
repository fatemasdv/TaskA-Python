"""
Task C - Handling Reservation Data (PRINT ONLY PART B)

Windows-safe version:
- Uses ">= " instead of "≥"
- Uses "->" instead of "→"
- Uses "EUR" instead of "€" to avoid encoding problems
"""

from datetime import datetime


def convert_reservation_data(reservation: list) -> list:
    """
    Convert one reservation row (list of strings) into correct data types.

    Returns values in this order:
    reservationId | name | email | phone | reservationDate | reservationTime |
    durationHours | price | confirmed | reservedResource | createdAt
    """
    reservation = [x.strip() for x in reservation]

    reservation_id = int(reservation[0])
    name = reservation[1]
    email = reservation[2]
    phone = reservation[3]

    reservation_date = datetime.strptime(reservation[4], "%Y-%m-%d").date()
    reservation_time = datetime.strptime(reservation[5], "%H:%M").time()

    duration_hours = int(reservation[6])
    price = float(reservation[7])

    confirmed = reservation[8] == "True"
    reserved_resource = reservation[9]

    created_at = datetime.strptime(reservation[10], "%Y-%m-%d %H:%M:%S")

    return [
        reservation_id,      # int
        name,                # str
        email,               # str
        phone,               # str
        reservation_date,    # date
        reservation_time,    # time
        duration_hours,      # int
        price,               # float
        confirmed,           # bool
        reserved_resource,   # str
        created_at,          # datetime
    ]


def fetch_reservations(reservation_file: str) -> list:
    """
    Reads reservations from a file and returns converted reservations.
    """
    reservations = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.split("|")
            reservations.append(convert_reservation_data(fields))
    return reservations


def confirmed_reservations(reservations: list[list]) -> None:
    """
    1) Confirmed Reservations
    - Name, Reserved Resource, dd.mm.yyyy at hh.mm
    """
    for r in reservations:
        if r[8]:
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {r[9]}, {date_str} at {time_str}")


def long_reservations(reservations: list[list]) -> None:
    """
    2) Long Reservations (>= 3 h)
    - Name, dd.mm.yyyy at hh.mm, duration X h, Reserved Resource
    """
    for r in reservations:
        if r[6] >= 3:
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {date_str} at {time_str}, duration {r[6]} h, {r[9]}")


def confirmation_statuses(reservations: list[list]) -> None:
    """
    3) Reservation Confirmation Status
    Name -> Confirmed / NOT Confirmed
    """
    for r in reservations:
        status = "Confirmed" if r[8] else "NOT Confirmed"
        print(f"{r[1]} -> {status}")


def confirmation_summary(reservations: list[list]) -> None:
    """
    4) Confirmation Summary
    - Confirmed reservations: X pcs
    - Not confirmed reservations: Y pcs
    """
    confirmed_count = 0
    not_confirmed_count = 0

    for r in reservations:
        if r[8]:
            confirmed_count += 1
        else:
            not_confirmed_count += 1

    print(f"- Confirmed reservations: {confirmed_count} pcs")
    print(f"- Not confirmed reservations: {not_confirmed_count} pcs")


def total_revenue(reservations: list[list]) -> None:
    """
    5) Total Revenue from Confirmed Reservations (comma decimal)
    Total revenue from confirmed reservations: 243,50 EUR
    """
    total = 0.0
    for r in reservations:
        if r[8]:
            total += r[6] * r[7]

    total_str = f"{total:.2f}".replace(".", ",")
    print(f"Total revenue from confirmed reservations: {total_str} EUR")


def main():
    reservations = fetch_reservations("reservations.txt")

    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print()

    print("2) Long Reservations (>= 3 h)")
    long_reservations(reservations)
    print()

    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print()

    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print()

    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)


if __name__ == "__main__":
    main()
