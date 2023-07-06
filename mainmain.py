import datetime

class Booking:
    def __init__(self, customer_name, date, time):
        self.customer_name = customer_name
        self.date = date
        self.time = time

class BookingSystem:
    def __init__(self):
        self.bookings = []

    def make_booking(self, customer_name, date, time):
        booking = Booking(customer_name, date, time)
        self.bookings.append(booking)
        print("Booking created successfully!")

    def show_bookings(self):
        if not self.bookings:
            print("No bookings found.")
        else:
            for booking in self.bookings:
                print(f"Customer: {booking.customer_name}, Date: {booking.date}, Time: {booking.time}")

# Example usage
booking_system = BookingSystem()

while True:
    print("\n1. Make Booking")
    print("2. Show Bookings")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        customer_name = input("Enter customer name: ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        time_str = input("Enter time (HH:MM): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            time = datetime.datetime.strptime(time_str, "%H:%M").time()
            booking_system.make_booking(customer_name, date, time)
        except ValueError:
            print("Invalid date or time format!")
    
    elif choice == "2":
        booking_system.show_bookings()

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")
