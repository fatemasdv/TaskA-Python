from datetime import datetime


class Reservation:
    def __init__(
        self,
        reservationId,
        name,
        email,
        phone,
        reservationDate,
        reservationTime,
        durationHours,
        price,
        confirmed,
        reservedResource,
        createdAt,
    ):
        self.reservationId = reservationId
        self.name = name
        self.email = email
        self.phone = phone
        self.reservationDate = reservationDate
        self.reservationTime = reservationTime
        self.durationHours = durationHours
        self.price = price
        self.confirmed = confirmed
        self.reservedResource = reservedResource
        self.createdAt = createdAt

    def is_confirmed(self):
        return self.confirmed

    def is_long(self):
        return self.durationHours > 3

    def total_price(self):
        return self.durationHours * self.price


def convert_reservation_data(reservation: list[str]) -> Reservation:
    reservation = [x.strip() for x in reservation]

    return Reservation(
        int(reservation[0]),
        reservation[1],
        reservation[2],
        reservation[3],
        datetime.strptime(reservation[4], "%Y-%m-%d").date(),
        datetime.strptime(reservation[5], "%H:%M").time(),
        int(reservation[6]),
        float(reservation[7]),
        True if reservation[8] == "True" else False,
        reservation[9],
        datetime.strptime(reservation[10], "%Y-%m-%d %H:%M:%S"),
    )


def fetch_reservations(reservation_file: str) -> list[Reservation]:
    reservations = []

    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            if len(line) > 1:
                fields = line.split("|")
                reservations.append(convert_reservation_data(fields))

    return reservations


def confirmed_reservations(reservations: list[Reservation]) -> None:
    for reservation in reservations:
        if reservation.is_confirmed():
            print(
                f'- {reservation.name}, '
                f'{reservation.reservedResource}, '
                f'{reservation.reservationDate.strftime("%d.%m.%Y")} at '
                f'{reservation.reservationTime.strftime("%H.%M")}'
            )


def long_reservations(reservations: list[Reservation]) -> None:
    for reservation in reservations:
        if reservation.is_long():
            print(
                f'- {reservation.name}, '
                f'{reservation.reservationDate.strftime("%d.%m.%Y")} at '
                f'{reservation.reservationTime.strftime("%H.%M")}, '
                f'duration {reservation.durationHours} h, '
                f'{reservation.reservedResource}'
            )


def confirmation_statuses(reservations: list[Reservation]) -> None:
    for reservation in reservations:
        print(
            f'{reservation.name} → '
            f'{"Confirmed" if reservation.is_confirmed() else "NOT Confirmed"}'
        )


def confirmation_summary(reservations: list[Reservation]) -> None:
    confirmed = len([x for x in reservations if x.is_confirmed()])
    print(
        f'- Confirmed reservations: {confirmed} pcs\n'
        f'- Not confirmed reservations: {len(reservations) - confirmed} pcs'
    )


def total_revenue(reservations: list[Reservation]) -> None:
    revenue = sum(x.total_price() for x in reservations if x.is_confirmed())
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