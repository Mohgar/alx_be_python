class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"Checked out: {self.title} by {self.author}")
        else:
            print(f"{self.title} by {self.author} is already checked out")
    def return_book(self):
        if self._is_checked_out:
            return f"{self.title} is returned"
        else:
            return f"{self.title} is not returned"
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)


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




