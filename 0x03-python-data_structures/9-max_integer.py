#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if not my_list:
        return None
    for i, x in enumerate(my_list):
        if i == 0:
            max = i
        if x >= max:
            max = x
    return max
