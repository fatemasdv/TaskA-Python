from datetime import datetime


def convert_reservation_data(reservation: list[str]) -> dict:
    reservation = [x.strip() for x in reservation]

    return {
        "reservationId": int(reservation[0]),
        "name": reservation[1],
        "email": reservation[2],
        "phone": reservation[3],
        "reservationDate": datetime.strptime(reservation[4], "%Y-%m-%d").date(),
        "reservationTime": datetime.strptime(reservation[5], "%H:%M").time(),
        "durationHours": int(reservation[6]),
        "price": float(reservation[7]),
        "confirmed": True if reservation[8] == "True" else False,
        "reservedResource": reservation[9],
        "createdAt": datetime.strptime(reservation[10], "%Y-%m-%d %H:%M:%S"),
    }


def fetch_reservations(reservation_file: str) -> list[dict]:
    reservations = []

    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            if len(line) > 1:
                fields = line.split("|")
                reservations.append(convert_reservation_data(fields))

    return reservations


def confirmed_reservations(reservations: list[dict]) -> None:
    for reservation in reservations:
        if reservation["confirmed"]:
            print(
                f'- {reservation["name"]}, '
                f'{reservation["reservedResource"]}, '
                f'{reservation["reservationDate"].strftime("%d.%m.%Y")} at '
                f'{reservation["reservationTime"].strftime("%H.%M")}'
            )


def long_reservations(reservations: list[dict]) -> None:
    for reservation in reservations:
        if reservation["durationHours"] > 3:
            print(
                f'- {reservation["name"]}, '
                f'{reservation["reservationDate"].strftime("%d.%m.%Y")} at '
                f'{reservation["reservationTime"].strftime("%H.%M")}, '
                f'duration {reservation["durationHours"]} h, '
                f'{reservation["reservedResource"]}'
            )


def confirmation_statuses(reservations: list[dict]) -> None:
    for reservation in reservations:
        print(
            f'{reservation["name"]} → '
            f'{"Confirmed" if reservation["confirmed"] else "NOT Confirmed"}'
        )


def confirmation_summary(reservations: list[dict]) -> None:
    confirmed = len([x for x in reservations if x["confirmed"]])
    print(
        f'- Confirmed reservations: {confirmed} pcs\n'
        f'- Not confirmed reservations: {len(reservations) - confirmed} pcs'
    )


def total_revenue(reservations: list[dict]) -> None:
    revenue = sum(
        x["durationHours"] * x["price"]
        for x in reservations
        if x["confirmed"]
    )
    print(
        f'Total revenue from confirmed reservations: {revenue:.2f} €'
        .replace(".", ",")
    )


def main():
    reservations = fetch_reservations("reservations.txt")

    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)

    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)

    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)

    print("4) Confirmation Summary")
    confirmation_summary(reservations)

    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)


if __name__ == "__main__":
    main()