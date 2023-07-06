class Book: 
    def __init__(self, title, author, pages):
        self.title = title 
        self.author = author
        self.pages = pages

    def book_result():
        print("The book you have purchased is called " + self.title + " by" + self.author + " with" + self.pages + " pages.")

b1 = Book("HarryPotter", "JK Rowling", "750p")


book_result()