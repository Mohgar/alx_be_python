class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        _is_checked_out = False
class Library:
    def __init__(self):
        self._books = list()
        self._books = _books
    def add_book(self):
        self._books.append(self)

    def check_out_book(self, title):
        if title in self._books:
            return "this book is already exist"
        else:
            return "this book is not exist"

    def return_book(self, title):
        self._books.append(title)

    def list_available_books(self):
        for book in self._books:
            return book




