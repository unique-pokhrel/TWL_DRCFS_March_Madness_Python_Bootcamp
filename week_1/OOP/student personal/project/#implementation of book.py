#implementation of book
class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available_copies = available_copies

    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        self.__available_copies += 1

    @property
    def available_copies(self):
        return self.__available_copies

    @property
    def percent_available(self):
        return self.__available_copies / (self.__available_copies + self.borrowed_copies) * 100

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn}, {self.available_copies})"
    
    #implementation of library class

    class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def register_member(self, member):
        self.members.append(member)

    def unregister_member(self, member):
        self.members.remove(member)

    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

    def __str__(self):
        return f"Library with {len(self.books)} books and {len(self.members)} members"

    def __repr__(self):
        return f"Library()"

#implementation of member class

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Member({self.name}, {self.email})"

