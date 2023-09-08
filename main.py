from library import Library, Book

def main():
    my_library = Library()

    # Add books
    book1 = Book("Atomic Habits", "J. Clear", "22334455")
    book2 = Book("Stories Grimm", "Grimm Brothers", "2233443322")
    book3 = Book("The Chronicles of Narnia", "C.S. Lewis", "33445566")
    book4 = Book("Moby Dick", "Herman Melville", "33445577")
    book5 = Book("The Odyssey", "Homer", "33445588")
    book6 = Book("Pride and Prejudice", "Jane Austen", "33445599")
    book7 = Book("To Kill a Mockingbird", "Harper Lee", "33445500")
    book8 = Book("The Catcher in the Rye", "J.D. Salinger", "44556611")
    book9 = Book("Brave New World", "Aldous Huxley", "44556622")
    book10 = Book("Lord of the Flies", "William Golding", "44556633")
    book11 = Book("War and Peace", "Leo Tolstoy", "44556644")
    book12 = Book("1984", "George Orwell", "55667755")

# Add the books to the mt_library list
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)
    my_library.add_book(book5)
    my_library.add_book(book6)
    my_library.add_book(book7)
    my_library.add_book(book8)
    my_library.add_book(book9)
    my_library.add_book(book10)
    my_library.add_book(book11)
    my_library.add_book(book12)

# Show available books
    print("Available books:", my_library.display_available_books())
    
# Check out a book
    print(my_library.check_out_book("1984"))  

 # Show available books again
    print("Available books:", my_library.display_available_books())

 # return the book
    print(my_library.return_book("1984"))

# Show available books again
    print("Available books:", my_library.display_available_books())

if __name__ == "__main__":
    main()
