class Book: 
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def user_input(self):
        self.name = input("Please Enter Book Name: ")
        self.author = input("Please Enter Author: ")
        self.genre = input("Please Enter Genre: ")
    
    def __str__(self):
        return f"Booking: {self.name}, {self.author}, {self.genre}"