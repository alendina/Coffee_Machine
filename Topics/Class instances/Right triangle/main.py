class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

if input_c ** 2 == (input_a ** 2 + input_b ** 2):
    right_t = RightTriangle(input_c, input_a, input_b)
    print(round(0.5 * right_t.a * right_t.b, 1))
else:
    print('Not right')
