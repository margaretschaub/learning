#practice with books

class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def define_genre(self, genre):
        return f"{self.title} is considered to be {genre}"

    def book_length(self):
        return f"{self.title} is {self.page_count} pages long!"

#harry_potter = Book("Harry Potter", "J.K Rowling", 500)


class Fiction(Book):
    def define_genre(self, genre="fiction"):
        return f"{self.title} is considered to be {genre}"

harry_potter = Fiction("Harry Potter", "J.K Rowling", 500)

class Nonfiction(Book):
    def define_genre(self, genre="nonfiction"):
        return f"{self.title} is considered to be {genre}"

print(harry_potter.book_length())

#look in to super()