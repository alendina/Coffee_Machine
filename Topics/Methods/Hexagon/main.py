import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return round(3 * math.sqrt(3) * (float(self.side_length) ** 2) / 2, 3)


# t = Hexagon(5.4)
# print(t.get_area())
