# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
# test_dict = {"a": 43, "b": 1233, "c": 8, "d": 88}
min_ = min(test_dict.values())
max_ = max(test_dict.values())
# print(min_, max_)
for x, y in test_dict.items():
    if y == min_:
        min_ = x
    if y == max_:
        max_ = x
print('min:', min_)
print('max:', max_)