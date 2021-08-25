input_list = input().lower().split()
our_dict = {key: input_list.count(key) for key in input_list}
for x, y in our_dict.items():
    print(x, y)