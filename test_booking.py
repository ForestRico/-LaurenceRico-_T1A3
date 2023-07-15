import unittest
import main
import csv
import re
from classes import Booking

def test_create_booking():
    # Simulate user input for creating a booking
    input_values = ['John Doe', '1234567890', '01-01-23', '10:00', '1, 2', '']
    def mock_input(prompt):
        return input_values.pop(0)
    
    # Patch the 'input' function to use our mock_input
    original_input = __builtins__.input
    __builtins__.input = mock_input
    
    # Call the create_booking function
    create_booking()
    write_to_csv()
    
    # Read the CSV file and check if the booking is stored correctly
    with open('bookings.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        bookings = list(reader)
        assert len(bookings) == 1
        booking = bookings[0]
        assert booking['customer_name'] == 'John Doe'
        assert booking['customer_phone'] == '1234567890'
        assert booking['date'] == '01-01-23'
        assert booking['time'] == '10:00'
        assert booking['service_types'] == 'Photography, Videography'
        assert booking['cost'] == '800'
    
    # Restore the original input function
    __builtins__.input = original_input

# Run the test
test_create_booking()

def test_find_booking():
    # Create a booking in the CSV file
    with open('bookings.csv', mode='w') as csvfile:
        fieldnames = ['customer_name', 'customer_phone', 'date', 'time', 'service_types', 'cost']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'customer_name': 'John Doe', 'customer_phone': '1234567890', 'date': '01-01-23', 'time': '10:00', 'service_types': 'Photography', 'cost': '300'})
    
    # Simulate user input for finding a booking
    input_values = ['John Doe']
    def mock_input(prompt):
        return input_values.pop(0)
    
    # Patch the 'input' function to use our mock_input
    original_input = __builtins__.input
    __builtins__.input = mock_input
    
    # Call the find_booking function
    find_booking()
    
    # Restore the original input function
    __builtins__.input = original_input

# Run the test
test_find_booking()















# # class TestBooking(unittest.TestCase):
    
# #     def test_add(self):
# #         result = calc.add(10, 5)


# def test_create_booking_and_write_to_csv():
#     # Simulate user input
#     customer_name = "John Doe"
#     customer_phone = "1234567890"
#     date = "01-01-23"
#     time = "10:30"
#     service_choices = ["1", "3"]
    
#     # Set up expected output
#     expected_booking = Booking(
#         customer_name,
#         customer_phone,
#         date,
#         time,
#         "Photography, Website Services",
#         1300
#     )
    
#     # Call the function being tested
#     create_booking()
#     write_to_csv()
    
#     # Check if the booking is stored correctly
#     assert booking_storage[customer_name] == expected_booking
    
#     # Check if the booking is written to the CSV file
#     with open('bookings.csv', mode='r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         bookings = list(reader)
        
#         assert len(bookings) == 1
#         assert bookings[0]['customer_name'] == customer_name
#         assert bookings[0]['customer_phone'] == customer_phone
#         assert bookings[0]['date'] == date
#         assert bookings[0]['time'] == time
#         assert bookings[0]['service_types'] == "Photography, Website Services"
#         assert bookings[0]['cost'] == "1300"
