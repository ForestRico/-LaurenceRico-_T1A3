import csv
import re
import functions
from classes import Booking

# booking_storage = {}

# service_package = {
#     "1" : 300, 
#     "2" : 500,
#     "3" : 1000,
#     "4" : 750,
#     "5" : 1000
# }

# service_type_dict = {
#     "1" : "Photography",
#     "2" : "Videography",
#     "3" : "Website Services",
#     "4" : "Marketing Services",
#     "5" : "Advertisements",
# }

# def create_booking(): 
#     print("\nTo Book with us we will need your details!\n")
#     customer_name = input("Please enter your full name: ")
    
#     while True:
#         customer_phone = input("Please enter your phone number: ")
#         if re.match(r'^\d{10}$', customer_phone):
#             break
#         else:
#             print("Invalid phone number format! Please enter a 10-digit number.")
    
#     while True:
#         date = input("Please enter the date (DD-MM-YY): ")
#         if re.match(r'^\d{2}-\d{2}-\d{2}$', date):
#             break
#         else:
#             print("Invalid date format! Please enter a valid date in the format DD-MM-YY.")
    
#     while True:
#         time = input("Please enter the time (HH:MM): ")
#         if re.match(r'^\d{2}:\d{2}$', time):
#             break
#         else:
#             print("Invalid time format! Please enter a valid time in the format HH:MM.")

#     print("\nPlease enter service type(s):\n1. Photography\n2. Videography\n3. Website Services\n4. Marketing Services\n5. Advertisements")
#     service_choice = input("\nEnter choice(s) separated by commas (1-5): ")
#     service_choices = [choice.strip() for choice in service_choice.split(",")]

#     while not all(choice.isdigit() and choice in service_package for choice in service_choices):
#         print("Invalid input. Service choice(s) should be comma-separated numbers (1-5).")
#         service_choice = input("Enter choice(s) separated by commas (1-5): ")
#         service_choices = [choice.strip() for choice in service_choice.split(",")]

#     price = 0 
#     chosen_services = []

#     for key in service_package:
#         if key in service_choices:
#             price += service_package[key]
#             chosen_services.append(service_type_dict[key])

#     print("\nYou have chosen the following services:")
#     for service in chosen_services:
#         print(service)

#     print("\nYour Total Cost is: $" + str(price))
#     service_types = ", ".join(chosen_services)

#     cost = price

#     booking = Booking(customer_name, customer_phone, date, time, service_types, cost)
#     booking_storage[customer_name] = booking

# def write_to_csv():
#     with open('bookings.csv', mode='w') as csvfile:
#         fieldnames = booking_storage[list(booking_storage.keys())[0]].__dict__.keys()
#         writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
#         writer.writeheader()
#         for row in booking_storage.values():
#             writer.writerow(row.__dict__)

# def find_booking():
#     name_input = input("Please enter name associated with Booking: ")
#     found_booking = False
#     with open('bookings.csv', mode='r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['customer_name'] == name_input:
#                 print("-----------------")
#                 print(f"Booking Found!")
#                 print(f"Customer Name: {row['customer_name']}")
#                 print(f"Customer Phone: {row['customer_phone']}")
#                 print(f"Date: {row['date']}")
#                 print(f"Time: {row['time']}")
#                 print(f"Service Types: {row['service_types']}")
#                 print(f"Cost: {row['cost']}")
#                 print("-----------------")
#                 found_booking = True
#                 break
#     if not found_booking:
#         print("\nName and booking not found")

# def show_booking_list():
#     with open('bookings.csv', mode='r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         bookings = list(reader)
#         if len(bookings) > 0:
#             for index, row in enumerate(bookings):
#                 print("-----------------")
#                 print(f"Booking {index+1}:")
#                 print(f"Customer Name: {row['customer_name']}")
#                 print(f"Customer Phone: {row['customer_phone']}")
#                 print(f"Date: {row['date']}")
#                 print(f"Time: {row['time']}")
#                 print(f"Service Types: {row['service_types']}")
#                 print(f"Cost: {row['cost']}")
#                 print("-----------------")
#         else: 
#             print("\nThere are currently no bookings to show")

# def edit_booking_list():
#     with open('bookings.csv', mode='r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         bookings = list(reader)

#         editRow = int(input("\nChoose which booking number you would like to edit. Enter 1 - " + str(len(bookings)) + " :"))
#         if editRow in range(1, len(bookings) + 1):
#             print("Please enter the new details for each of the following: ")
#             new_booking = bookings[editRow - 1]
            
#             new_booking['customer_name'] = input("Enter new customer name: ")
           
#             while True:
#                 customer_phone = input("Enter new customer phone number: ")
#                 if re.match(r'^\d{10}$', customer_phone):
#                     new_booking['customer_phone'] = customer_phone
#                     break
#                 else:
#                     print("Invalid phone number format! Please enter a 10-digit number.")

            
#             while True:
#                 date = input("Please enter the date (DD-MM-YY): ")
#                 if re.match(r'^\d{2}-\d{2}-\d{2}$', date):
#                     new_booking['date'] = date
#                     break
#                 else:
#                     print("Invalid date format! Please enter a valid date in the format DD-MM-YY.")

            
#             while True:
#                 time = input("Please enter the time (HH:MM): ")
#                 if re.match(r'^\d{2}:\d{2}$', time):
#                     new_booking['time'] = time
#                     break
#                 else:
#                     print("Invalid time format! Please enter a valid time in the format HH:MM.")

#             service_choice = input("\nPlease enter new service type(s):\n1. Photography\n2. Videography\n3. Website Services\n4. Marketing Services\n5. Advertisements\nEnter choice separated by commas (1-5): ")
#             service_choices = service_choice.split(",")
#             new_booking['service_types'] = ", ".join(service_type_dict[choice] for choice in service_choices)
#             new_booking['cost'] = str(sum(service_package[choice] for choice in service_choices))

#             print("\nPlease see the details of the updated booking below: ")
#             print(f"Booking {editRow}:")
#             print(f"Customer Name: {new_booking['customer_name']}")
#             print(f"Customer Phone: {new_booking['customer_phone']}")
#             print(f"Date: {new_booking['date']}")
#             print(f"Time: {new_booking['time']}")
#             print(f"Service Types: {new_booking['service_types']}")
#             print(f"Cost: {new_booking['cost']}")
            
#             changeCSV = input("\nWould you like to make the changes to the CSV file? (Y/N): ").lower()
#             if changeCSV == "y":
#                 with open('bookings.csv', mode='w', newline='') as csvfile:
#                     fieldnames = reader.fieldnames
#                     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                     writer.writeheader()
#                     writer.writerows(bookings)

# def load_booking_list():
#     with open("bookings.csv", mode = "r") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             booking = Booking(row['customer_name'], row['customer_phone'], row['date'], row['time'], row['service_types'], row['cost'])
#             booking_storage[row['customer_name']] = booking

# def delete_booking():
#     with open('bookings.csv', mode='r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         bookings = list(reader)

#         delete_no = int(input("\nChoose which booking number you would like to delete. Enter 1 - " + str(len(bookings)) + " :"))

#         if delete_no in range(1, len(bookings) + 1):
#             bookings.pop(delete_no - 1)
#             with open('bookings.csv', mode='w', newline='') as csvfile:
#                 fieldnames = reader.fieldnames
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 writer.writerows(bookings)
#             print("\nBooking successfully deleted.")
#         else:
#             print("Invalid booking number.")

# def end_menu():
#     choice = input("\n-----Would you like to return to the menu?-----\nEnter (Y/N): ").lower()
#     if choice == ("y"):
#         return True
#     elif choice == ("n"):
#         print("Thanks for using our service!!")
#         return False
#     else: 
#         print("\n--Invalid Input please enter either (Y/N)--")
#         return end_menu()
        
# def booking_menu():
    # while True:
    #     print("\nWelcome to Rico's Media & Marketing Services!\n1. Create a Booking\n2. Find your Booking Details\n3. Show all Bookings\n4. Edit a Booking\n5. Delete a Booking\n6. Exit")
    #     choice = input("\nEnter a choice (1-5): ")
    #     if choice == "1":
    #         create_booking()
    #         write_to_csv()
    #         if not end_menu():
    #             return False        
    
    #     elif choice == "2":
    #         find_booking()
    #         if not end_menu():
    #             return False

    #     elif choice == "3":
    #         show_booking_list()
    #         # load_booking_list()
    #         if not end_menu():
    #             return False

    #     elif choice == "4":
    #         show_booking_list()
    #         edit_booking_list()
    #         if not end_menu():
    #             return False

    #     elif choice =="5":
    #         show_booking_list()
    #         delete_booking()
    #         if not end_menu():
    #             return False

    #     elif choice == "6":
    #         print("Thanks For Using Our Service!")
    #         return False

functions.booking_menu()

