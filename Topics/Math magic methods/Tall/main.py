class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __iadd__(self, h):
        self.height += h
        return self

    def __isub__(self, h):
        self.height -= h
        return self

# p = Person('uuu', 7.2)
# print(p.height)
# p += 5.5
# print(p.height)
# p -= 2
# print(p.height)
