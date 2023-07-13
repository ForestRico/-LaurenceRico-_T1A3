import csv

class Booking():
    def __init__(self, customer_name, customer_phone, date, time, service_types, cost):
        self.customer_name = customer_name 
        self.customer_phone = customer_phone
        self.date = date
        self.time = time
        self.service_types = service_types
        self.cost = cost

    def __str__(self):
        return f"Booking : {self.customer_name}, {self.customer_phone}, {self.date}, {self.time}, {self.service_types}"

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

def creating_booking(): 
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
    # if key and service_choice(user input) match, then the users choices will append on the chosen_services list 
            
    print("You have chosen the following services: ")
    for services in chosen_services:
        print(services)
        service_types = services

    print("Total Cost: " + "$" + str(price))
    service_types = ", ".join(chosen_services)

    cost = price

    booking = Booking(customer_name, customer_phone, date, time, service_types, cost)
    booking_storage[customer_name] = booking

def write_to_csv():
    with open('bookings.csv', mode='w') as csvfile:
        # fieldnames = booking_storage[customer_name].__dict__.keys()
        fieldnames = booking_storage[list(booking_storage.keys())[0]].__dict__.keys()
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for row in booking_storage.values():
            writer.writerow(row.__dict__)

def show_booking_list():
    for index, bookings in enumerate(booking_storage.values()):
        print("-----------------")
        print(f"Booking {index+1}: {bookings}")
        print("-----------------")
              
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
            creating_booking()
            write_to_csv()        
    
        elif choice == "2":
            name_input = input("Please enter name associated with Booking: ").lower() 
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
            show_booking_list()

        elif choice == "4":
            show_booking_list()
            editRow = int(input("\nChoose which boooking number you would like to edit. Enter 1 - " + str(len(booking_storage)) + " :"))
            if editRow in range(1, len(booking_storage) + 1):
                print("Please enter the new details for each of the following: ")
                new_booking = booking_storage[list(booking_storage.keys())[editRow - 1]]
                new_booking.customer_name = input("Enter new customer name: ")
                new_booking.customer_phone = input("Enter new customer phone: ")
                new_booking.date = input("Enter new date (DD-MM-YY): ")
                new_booking.time = input("Enter new time (HH-MM): ")
                service_choice = input("Enter new service type(s) separated by commas (1-5): ")
                service_choices = service_choice.split(",")
                new_booking.service_types = ", ".join(service_type_dict[choice] for choice in service_choices)
                new_booking.cost = sum(service_package[choice] for choice in service_choices)
                print("\nPlease see the details of the updated booking below: ")
                print(new_booking)
                changeCSV = input("\nWould you like to make the changes to the CSV file? (Y/N): ").lower()
                if changeCSV == "y":
                    with open('bookings.csv', mode='w') as csvfile:
                        fieldnames = booking_storage[list(booking_storage.keys())[0]].__dict__.keys()
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        for row in booking_storage.values():
                            writer.writerow(row.__dict__)


            # editRow = int(input("\nWhich row would you like to change? Enter 1 - " + str(len(booking_storage)-1) + " :" ))
            # print("Please enter the new details for each of the following: ")

            # for i in range(len(booking_storage[0])):
            #     newDetails = input("Enter new data for " + str(booking_storage[0][i] + " :"))
            #     booking_storage[editRow][i] = newDetails

            # print("\nPlease see the details of the new file below: ")
            # for i in range (len(booking_storage)):
            #     print("Row " + str(i) + " :" + str(booking_storage[i]))

            # changeCSV = input("\nWould you like to make the changes to the csv file? Y/N").lower()

            # # if changeCSV == "y":
            # #     with open("booking.csv", "w+") as csvfile:


        elif choice == "5":
            print("Thanks For Using Our Service!")
            return False
            
    
booking_menu()