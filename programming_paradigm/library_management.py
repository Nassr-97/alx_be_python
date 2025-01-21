

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout_book(self):
        if (not self._is_checked_out):
            self._is_checked_out = True
        else:
            Print(f"{self.title} is already checked out")
        return self._is_checked_out

    def return_book(self):
        if (self._is_checked_out):
            self._is_checked_out = False
        else:
            Print(f"{self.title} is already returned")
        return not self._is_checked_out

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        self._books.append(book(title, author))

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.checkout_book():
                    return f"{title} has been succesfully checked out"
        return f"{title} is either not available or not in the library"


    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    return f"{title} has been succesfully returned"
        return f"{title} is either not checked out or not in the library"

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")



