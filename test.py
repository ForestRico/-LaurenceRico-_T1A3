from testclass import Book

def menu():
    while True: 
        choice = input("Welcome to MK Motorsports!\nWould you like to book a service?\nType Y or N: ")
        if choice.lower() == "y":
            print("Thanks for choosing us")
            return True
        elif choice.lower() == "n":
            print("Thank you for visiting us!")
            return False
        else:
            print("Invalid Input")
         
booking_bank = []

while True:
    if not menu():
        break

    attribute1 = input("Enter attribute 1: ")
    attribute2 = input("Enter attribute 2: ")
    attribute3 = input("Enter attribute 3: ")

    p1 = Book(attribute1, attribute2, attribute3)
    booking_bank.append(p1)

# Show the user their bookings
if len(booking_bank) > 0:
    print("Your bookings:")
    for index, booking in enumerate(booking_bank):
        print(f"Booking {index+1}: {booking}")

















# from testclass import Book 

# data = []

# b1 = Book("name", "author", "genre")

# b1.user_input()

# data.append(b1)

# for element in data: 
#     print(element)

