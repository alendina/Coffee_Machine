class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    def __repr__(self):
        # return "Book({}, {}, {}, {})".format(self.author, self.title, self.price, self.book_id)
        return f'{self.title} by {self.author}. ${self.price}. [{self.book_id}]'

    def __str__(self):
        return f'{self.title} by {self.author}. ${self.price}. [{self.book_id}]'


# b = Book("George Orwell", "1984", 13.59, 1956789)
# print(b)
# print(repr(b))


