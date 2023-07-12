class Booking():
    def __init__(self, customer_name, customer_phone, date, time, service_types, cost):
        self.customer_name = customer_name 
        self.customer_phone = customer_phone
        self.date = date
        self.time = time
        self.service_types = service_types
        self.cost = cost

    def __str__(self):
        return f"Booking : {self.customer_name}, {self.customer_phone}, {self.date}, {self.time}, {self.service_type}"
    
booking_storage = {}

service_package = {
    "1" : 300, 
    "2" : 500,
    "3" : 1000,
    "4" : 750,
    "5" : 1000
}

service_type_dict = {
    "1" : "Photography",
    "2" : "Videography",
    "3" : "Website Services",
    "4" : "Marketing Services",
    "5" : "Advertisements",
}


def booking_menu():
    while True:
        print("Welcome to elRico Motorsports")
        print("1. Create Booking")
        print("2. Find your Booking")
        print("3. Show All Bookings")
        print("4. Edit a Booking")
        print("5. Exit")
        choice = input("Enter Choice (1-5): ")
        if choice == "1":
            customer_name = input("Please enter your fullname: ")
            customer_phone = input("Please enter your phone number: ")
            date = input("Please enter the date DD-MM-YY: ")
            time = input("Please enter the time HH-MM: ")

            print("Please enter service type: \n1. Photography\n2. Videography\n3. Website Services\n4. Marketing Services\5. Advertisements")
            service_choice = input("Enter Choice(s) serparated by commas (1-5): ")
            service_choices = service_choice.split(",")

            price = 0 
            chosen_services = []

            for key in service_package:
                if key in service_choices:
                    price += service_package[key]
                    chosen_services.append(service_type_dict[key])
                    # if key and service_choice(user input) match, then the users choices will append on a list 
            
            print("You have chosen the following services: ")
            for services in chosen_services:
                print(services)

            print("Total Cost: " + str(price))
            service_types = ", ".join(chosen_services)
            # Combining the service types into a comma-separated string

            # if key in service_type_dict:
            #     print(key)

            # for service_no in service_choice:
            #     if service_no in service_type_dict:
            #         print("You have chosen the following services: ")
            #         for service_no in service_choice:
            #             service_types = (service_type_dict[service_no])
            #             print(service_types + "\nTotal Cost: " + str(price))
            #             return service_types

            # booking = Booking(customer_name, customer_phone, date, time, service_types, cost)
            # booking_storage[customer_name] = booking
 
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