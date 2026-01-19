from datetime import datetime

def main():
    # Read the reservation line from the file
    with open("reservations.txt", "r", encoding="utf-8") as f:
        reservation = f.read().strip()

    # Split the line into parts
    parts = reservation.split("|")

    # Convert data types
    reservation_number = int(parts[0])
    hours = int(parts[4])
    hourly_price = float(parts[5])
    paid = parts[6] == "True"

    # Convert date and time to Finnish format
    date_fi = datetime.strptime(parts[2], "%Y-%m-%d").date().strftime("%d.%m.%Y")
    time_fi = datetime.strptime(parts[3], "%H:%M").time().strftime("%H.%M")

    # Calculate total price
    total_price = hours * hourly_price

    # Format prices (comma instead of dot)
    hourly_fi = f"{hourly_price:.2f}".replace(".", ",")
    total_fi = f"{total_price:.2f}".replace(".", ",")

    # Print required output
    print(f"Reservation number: {reservation_number}")
    print(f"Booker: {parts[1]}")
    print(f"Date: {date_fi}")
    print(f"Start time: {time_fi}")
    print(f"Number of hours: {hours}")
    print(f"Hourly price: {hourly_fi} €")
    print(f"Total price: {total_fi} €")
    print(f"Paid: {'Yes' if paid else 'No'}")
    print(f"Location: {parts[7]}")
    print(f"Phone: {parts[8]}")
    print(f"Email: {parts[9]}")

if __name__ == "__main__":
    main()

