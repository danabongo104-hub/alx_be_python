
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library collection if it isn't already present."""
        if book not in self._books:
            self._books.append(book)
        
    def check_out_book(self, title):
        """Checks out a book by title if it is available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return f"{title} has been checked out."
        return f"{title} not found in the library."

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book.return_book()
                    return f"{title} has been returned."
                return f"{title} was not checked out."
        return f"{title} not found in the library."
        
    def list_available_books(self):
       """Lists all available books in the library."""
       for book in self._books:
           if not book._is_checked_out:
               print(f"{book.title} by {book.author}")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if it is not already."""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False

