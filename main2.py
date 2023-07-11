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
        print("Welcome to MK Motorsports")
        print("1. Create Booking")
        print("2. Show All Bookings")
        print("3. Exit")
        choice = input("Enter Choice (1-3): ")
        if choice == "1":
            booking_data = {}
            customer_name = input("Please enter your fullname: ")
            customer_phone = input("Please enter your phone number: ")
            date = input("Please enter the date DD-MM-YY: ")
            time = input("Please enter the time HH-MM: ")
            service_type = input("Please enter service type: ")

            booking_data["name"] = customer_name
            booking_data["phone"] = customer_phone
            booking_data["date_e"] = date
            booking_data["time_e"] = time
            booking_data["service"] = service_type

            booking_storage[customer_name] = booking_data
            print(booking_storage[customer_name])

            # booking_storage[customer_name] = booking_data
            # print(booking_data[customer_name])



            # c1 = Booking(customer_name, customer_phone, date, time, service_type)
            # booking_data.append(c1)

        elif choice == "2":
            for index, bookings in enumerate(booking_data):
                print("-----------------")
                print(f"Booking {index+1}: {bookings}")
                print("-----------------")
            # booking_data.show_bookings()
        
        elif choice == "3":
            print("Thanks For Using Our Service!")
            return False
            
    
booking_menu()