#!/usr/bin/python3
def max_integer(my_list=[]):
    max_n = 0
    if not my_list:
        return None
    for i, x in enumerate(my_list):
        if i == 0:
            max_n = i
        if x >= max_n:
            max_n = x
    return max_n

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
max_value = max_integer()
print("Max: {}".format(max_value))

