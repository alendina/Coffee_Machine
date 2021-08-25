class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"Object of the class Patient. name: {self.name}, last_name: {self.last_name}, age: {self.age}"

    def __str__(self):
        return f'{self.name} {self.last_name}. {self.age}'


# b = Book("George Orwell", "1984", 13.59, 1956789)
# print(b)
# print(repr(b))