class Book:
    def __init__(self,title,author,isbn,availablity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availablity = availablity
    def details(self):
        print(f"The writer of the book is: {self.author}")
        print(f"The title of the book is: {self.title}")
        print(f"The international standard book number of the book is: {self.isbn}")
    def availablity_status(self):
        if self.availablity == True:
            print("The book is available") 
        else:
            print("Sorry, the book is not available")   

class User:
    def __init__(self, name, user_id,book_borrrowed, book_returned):
        self.name = name
        self.user_id = user_id
        self.book_borrrowed = book_borrrowed
        self.book_returned = book_returned
    def details(self):
        print(f"The users name is: {self.name}")
        print(f"The users id is: {self.user_id}")
    def book_borrrowed_status(self):
        print(f"This user borrowed this book: {self.book_borrrowed}")
    def book_returned_status(self):
        print(f"This user returned this books: {self.book_returned} ") 

class Library:
    def __init__(self):
        self.books = []
        self.registration1 = {}
        self.handling_book_borrowed1 = {}
        self.handling_book_returned1 = {}
    def display(self):
        print(f"Your name and id is: {self.registration1} ")
        print(f"The books you added to the library: {self.books}")
        print(f"The name you use to borrow the book and The book you borrowed is: {self.handling_book_borrowed1}")  
        print(f"The name you use to return the book and The book you returned is: {self.handling_book_returned1}")     
    def add_books(self,book):
        self.books.append(book)
    def registration(self,name, id):
        self.registration1[name] = id
    def handling_book_borrowed(self,name ,book_borrrowed):
        self.handling_book_borrowed1[name] = book_borrrowed
    def handling_book_returned(self, name, book_returned):
        self.handling_book_returned1[name] = book_returned   

class Transaction:
    def __init__(self):
        self.handling_book_borrowed1 = {}
        self.handling_book_returned1 = {}
    def display(self):
        print(f"The person that borrowed the books and the book that borrowed are: {self.handling_book_borrowed1}")  
        print(f"The person that returned the books and the book that returned are: {self.handling_book_returned1}")  
    def handling_book_borrowed(self,name ,book_borrrowed):
        self.handling_book_borrowed1[name] = book_borrrowed
    def handling_book_returned(self, name, book_returned):
        self.handling_book_returned1[name] = book_returned    


user = Library()
registration_name = input("Write your name to rigister to the library: ")
registration_id = input("and your ID: ")
user.registration(registration_name,registration_id)
add_book = input("Add any book you want to the library: ")
user.add_books(add_book)
book_borrow = input("Ask any any book you want to borrow: ")
if book_borrow in user.books:
    user.handling_book_borrowed(registration_name, book_borrow)
else:
    print("Sorry, but the book your looking for is not available")
book_return = input("What book do you want to return: ")
user.handling_book_returned(registration_name, book_return)
user.display()    




        