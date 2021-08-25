import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


# p1 = Point(1.5, 1)
# p2 = Point(1.5, 2)
#
# print(p1.dist(p2))