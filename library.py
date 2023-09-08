class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_checked_out= False

    def check_out(self):   
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):  
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
          self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.check_out():
                return f"{title} has been checked out."
        return f"{title} is not available."

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return f"{title} has been returned."
        return f"{title} was not checked out."

    def display_available_books(self):
        available_books = [book.title for book in self.books if not book.is_checked_out]
        return available_books if available_books else "No books available."
