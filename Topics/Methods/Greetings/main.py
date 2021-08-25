class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, I am {self.name}!'


p = Person(input())
print(p.greet())
