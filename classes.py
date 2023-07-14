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