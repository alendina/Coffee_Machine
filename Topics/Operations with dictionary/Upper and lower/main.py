# the list with words from string
# please, do not modify it
some_iterable = input().split()
new_dict = {x.upper(): x.lower() for x in some_iterable}
print(new_dict)
# use dictionary comprehension to create a new dictionary