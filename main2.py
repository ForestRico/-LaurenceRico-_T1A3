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
        print("3. Edit a Booking")
        print("4. Exit")
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
            for index, bookings in enumerate(booking_storage.values()):
                print("-----------------")
                print(f"Booking {index+1}: {bookings}")
                print("-----------------")
           
        
        elif choice == "4":
            print("Thanks For Using Our Service!")
            return False
            
    
booking_menu()