#-*-coding:utf8;-*-
#qpy:console

print "This is console module"
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = True

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
        status = "Available" if self.available else "Not Available"
        print("Status:", status)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            for book in self.books:
                book.display_info()

# Create library object
library = Library()

# Add books to the library
book1 = Book("Book 1", "Author 1", 2000)
book2 = Book("Book 2", "Author 2", 2005)
book3 = Book("Book 3", "Author 3", 2010)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books in the library
library.display_books()

# Search a book by title
search_title = "Book 2"
found_book = library.search_book(search_title)
if found_book:
    print("Book found:")
    found_book.display_info()
else:
    print("Book not found.")

# Remove a book from the library
library.remove_book(book3)
print("Book 3 removed from the library.")

# Display updated books list
library.display_books()