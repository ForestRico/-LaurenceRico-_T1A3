class Booking():
    def __init__(self, customer_name, customer_phone, date, time, service_type):
        self.customer_name = customer_name 
        self.customer_phone = customer_phone
        self.date = date
        self.time = time
        self.service_type = service_type

    def __str__(self):
        return f"Booking : {self.customer_name}, {self.customer_phone}, {self.date}, {self.time}, {self.service_type}"
    
booking_storage = {}

def booking_menu():
    while True:
        print("Welcome to elRico Motorsports")
        print("1. Create Booking")
        print("2. Find your Booking")
        print("3. Show All Bookings")
        print("4. Edit a Booking")
        print("5. Exit")
        choice = input("Enter Choice (1-3): ")
        if choice == "1":
            customer_name = input("Please enter your fullname: ")
            customer_phone = input("Please enter your phone number: ")
            date = input("Please enter the date DD-MM-YY: ")
            time = input("Please enter the time HH-MM: ")
            service_type = input("Please enter service type: ")

            booking = Booking(customer_name, customer_phone, date, time, service_type)
            booking_storage[customer_name] = booking
 
        elif choice == "2":
            name_input = input("Please enter name associated with Booking: ") 
            found_booking = False
            while not found_booking:
                for name_find in booking_storage:
                    if name_find == name_input:    
                        print(booking_storage[name_input])
                        found_booking = True
                        break 
                if not found_booking:
                    print("Name and booking not found")
                    name_input = input("Please enter a valid name associated with a booking")
            # add .lower() function to name_input so that the user doesnt have to worry about being case sensitive


        elif choice == "3":
            for index, bookings in enumerate(booking_storage.values()):
                print("-----------------")
                print(f"Booking {index+1}: {bookings}")
                print("-----------------")

        # elif choice == "4":
            
    
        elif choice == "5":
            print("Thanks For Using Our Service!")
            return False
            
    
booking_menu()